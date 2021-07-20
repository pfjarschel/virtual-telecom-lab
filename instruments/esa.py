# Simple virtual ESA class
# Default time unit: 1 s
# Default frequency unit = 1 MHz
# Default voltage unit: V
# By pfjarschel, 2021

# Imports
import os, time
import PyQt5
import numpy as np
from scipy.fft import fft
from scipy.signal import windows
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.ticker import (AutoLocator, AutoMinorLocator)
from PyQt5 import uic, QtCore
from PyQt5.QtCore import QTimer, QDir
from PyQt5.QtWidgets import QFileDialog

# File paths
main_path = os.path.dirname(os.path.realpath(__file__))
thisfile = os.path.basename(__file__)

# Load ui file
FormUI, WindowUI = uic.loadUiType(f"{main_path}/esa.ui")

# Main instrument class
class ESA(FormUI, WindowUI):

    # Main parameters
    fstart = 0.0
    fstop = 10.0
    fcenter = (fstop + fstart)/2.0
    fspan = fstop - fstart
    fdiv = fspan/10.0
    dBm = True
    dbdiv = 10.0
    reflevel = 10.0
    npoints = 1000
    averages = 1
    rbw = fspan/npoints
    peakdet = False
    windowfilt = False
    window_beta = 0.0
    npoints_inc = 1
    sync_start = False
    
    # Input objects
    input_objs = [None]  

    # Internal parameters
    busy = False
    ui_busy = False
    running = False
    loop_timer = None
    sampletime = 1/rbw
    x_axis = np.linspace(fstart, fstop, npoints)
    y_axis = np.zeros([npoints])
    sg_x = []
    sg_y = np.linspace(fstart, fstop, npoints)
    sg_z = np.zeros([1, npoints])
    avg_buffer = np.zeros([2, npoints])
    peak_buffer = np.zeros([npoints])
    sg_buffer = np.zeros([1, npoints])
    avg_counter = 0
    sg_counter = 0
    sg_t0 = time.time()
    
    
    # Default functions
    def __init__(self):
        super(ESA, self).__init__()

        print("Initializing ESA")

        self.setupUi(self)
        self.setupOtherUi()
        self.setupActions()
        self.show()
        

    def __del__(self):
        print("Deleting ESA object")


    # UI functions
    def setupOtherUi(self):
        self.sgn = self.sgNSpin.value()
        self.sg_buffer = np.ones([self.sgn, self.npoints])
        self.setup_graph()

    def setupActions(self):
        # Connect UI signals to functions
        self.startBut.clicked.connect(self.runAcquisition)
        self.stopBut.clicked.connect(self.stopAcquisition)
        self.singleBut.clicked.connect(self.singleAcquisition)
        self.saveBut.clicked.connect(self.saveData)
        self.peakCheck.clicked.connect(self.setAcquisition)
        self.windowCheck.clicked.connect(self.setAcquisition)
        self.pointsSpin.valueChanged.connect(self.setAcquisition)
        self.avgSpin.valueChanged.connect(self.setAcquisition)
        self.rbwSpin.valueChanged.connect(self.setAcquisition)
        self.windowSpin.valueChanged.connect(self.setAcquisition)
        self.startSpin.valueChanged.connect(self.setAcquisition)
        self.stopSpin.valueChanged.connect(self.setAcquisition)
        self.centerSpin.valueChanged.connect(self.setAcquisition)
        self.spanSpin.valueChanged.connect(self.setAcquisition)
        self.dbdivSpin.valueChanged.connect(self.setAcquisition)
        self.reflevelSpin.valueChanged.connect(self.setAcquisition)
        self.linRadio.clicked.connect(self.setAcquisition)
        self.dbmRadio.clicked.connect(self.setAcquisition)
        self.sgNSpin.valueChanged.connect(self.setAcquisition)
        self.tabWidget.currentChanged.connect(self.setAcquisition)
        self.srturboSpin.valueChanged.connect(self.setAcquisition)
        self.syncCheck.clicked.connect(self.setAcquisition)
        
        # Timers
        self.loop_timer = QTimer()
        self.loop_timer.timeout.connect(self.measLoop)
        self.loop_timer.setInterval(10)
        
    def setup_graph(self):
        # Main
        self.figure = plt.figure()
        self.graph = FigureCanvas(self.figure)
        self.graphToolbar = NavigationToolbar(self.graph, self)
        self.graphToolbar.locLabel.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.graphHolder.addWidget(self.graphToolbar)
        self.graphHolder.addWidget(self.graph)
        self.graph_ax = self.figure.add_subplot()
        (self.graph_line,) = self.graph_ax.plot([],[])
        
        self.graph_ax.set_xlim([self.fstart, self.fstop])
        self.graph_ax.xaxis.set_ticks(np.linspace(self.fstart, self.fstop, 11))
        self.graph_ax.xaxis.set_minor_locator(AutoMinorLocator())
        self.graph_ax.set_xlabel("Frequency (MHz)")

        if self.dBm:
            ymin = (self.reflevel - 10*self.dbdiv)
            ymax = self.reflevel
            self.graph_ax.set_ylim([ymin, ymax])
            self.graph_ax.yaxis.set_ticks(np.linspace(ymin, ymax, 11))
            self.graph_ax.set_ylabel("Magnitude (dBm)")
        else:
            ymin = 0.0
            ymax = 1.0
            self.graph_ax.set_ylim([ymin, ymax])
            self.graph_ax.yaxis.set_major_locator(AutoLocator())
            self.graph_ax.set_ylabel("Magnitude (V)")
        self.graph_ax.yaxis.set_minor_locator(AutoMinorLocator())
        
        self.graph_ax.grid(True, which='minor', color='gainsboro')
        self.graph_ax.grid(True, which='major', color='gray')
        self.graph.draw()

        # Spectrogram
        self.sgfigure = plt.figure()
        self.sggraph = FigureCanvas(self.sgfigure)
        self.sggraphToolbar = NavigationToolbar(self.sggraph, self)
        self.sggraphToolbar.locLabel.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.sggraphHolder.addWidget(self.sggraphToolbar)
        self.sggraphHolder.addWidget(self.sggraph)
        self.sggraph_ax = self.sgfigure.add_subplot()
        
        self.sggraph_ax.set_xlabel("Time (s)")
        self.sggraph_ax.set_ylabel("Frequency (MHz)")
        
        self.sggraph.draw()

    # Start/stop Acquisition
    def runAcquisition(self):
        if not self.running:
            self.running = True
            self.loop_timer.start()

    def stopAcquisition(self):
        if self.running:
            self.running = False
            self.loop_timer.stop()

    def singleAcquisition(self):
        self.measLoop()

    # Set acquisition stuff
    def setAcquisition(self):
        if not self.ui_busy:
            self.ui_busy = True
            was_running = False
            if self.running:
                self.stopAcquisition()
                was_running = True

            sname = self.sender().objectName()

            self.dBm = self.dbmRadio.isChecked()
            self.dbdiv = self.dbdivSpin.value()
            self.reflevel = self.reflevelSpin.value()
            self.peakdet = self.peakCheck.isChecked()
            self.windowfilt = self.windowCheck.isChecked()
            self.window_beta = self.windowSpin.value()
            self.npoints_inc = self.srturboSpin.value()
            self.sync_start = self.syncCheck.isChecked()
            
            changed_f = False
            if sname == "startSpin" or sname == "stopSpin":
                changed_f = True
                if sname == "startSpin":
                    if self.startSpin.value() >= self.stopSpin.value():
                        self.startSpin.setValue(self.stopSpin.value() - 1e-3)
                elif sname == "stopSpin":
                    if self.stopSpin.value() <= self.startSpin.value():
                        self.stopSpin.setValue(self.startSpin.value() + 1e-3)
                self.fstart = self.startSpin.value()
                self.fstop = self.stopSpin.value()
                self.fcenter = (self.fstop + self.fstart)/2.0
                self.fspan = self.fstop - self.fstart
                self.centerSpin.setValue(self.fcenter)
                self.spanSpin.setValue(self.fspan)
            elif sname == "spanSpin" or sname == "centerSpin":
                changed_f = True
                self.fspan = self.spanSpin.value()
                self.fcenter = self.centerSpin.value()
                self.fstart = max(self.fcenter - self.fspan/2.0, 0.0)
                self.fstop = min(self.fcenter + self.fspan/2.0, 20000.0)
                self.fcenter = (self.fstop + self.fstart)/2.0
                self.fspan = self.fstop - self.fstart
                self.startSpin.setValue(self.fstart)
                self.stopSpin.setValue(self.fstop)
                self.centerSpin.setValue(self.fcenter)
                self.spanSpin.setValue(self.fspan)
            
            if sname == "rbwSpin" or changed_f:
                self.rbw = min(max(self.rbwSpin.value(), self.fspan/1000000), self.fspan/10)
                self.npoints = int(self.fspan/self.rbw)
                self.rbwSpin.setValue(self.rbw)
                self.pointsSpin.setValue(self.npoints)
            elif sname == "pointsSpin":
                self.npoints = int(min(max(self.pointsSpin.value(), self.fspan/2000.0), self.fspan/0.0001))
                self.rbw = self.fspan/self.npoints
                self.rbwSpin.setValue(self.rbw)
                self.pointsSpin.setValue(self.npoints)

            self.sampletime = 1/self.rbw
            self.sgn = self.sgNSpin.value()
            self.x_axis = np.linspace(self.fstart, self.fstop, self.npoints)
            self.y_axis = np.zeros([self.npoints])
            self.peak_buffer = np.zeros([self.npoints])
            self.avg_buffer = np.zeros([self.avgSpin.value(), self.npoints])
            self.sg_buffer = 1e-30*np.ones([self.sgn, self.npoints])
            self.sg_y = np.linspace(self.fstart, self.fstop, self.npoints)  
            self.sg_x = np.zeros([self.sgn])
            self.avg_counter = 0
            self.sg_counter = 0
            self.sg_t0 = time.time()

            # Get rid of empty average buffer
            data = self.input_signal()
            self.avg_buffer = np.tile(data, (self.avgSpin.value(), 1))
            
            if was_running:
                self.runAcquisition()

            self.ui_busy = False


    # Internal functions   
    # Acquisition loop
    def measLoop(self):
        if not self.busy:
            # Set soft lock
            self.busy = True

            if self.tabWidget.currentIndex() == 0:
                # Create arrays
                self.x_axis = np.linspace(self.fstart, self.fstop, self.npoints)  
                
                # Get signal
                if self.input_objs[0]:                    
                    # Get data
                    new_data = self.input_signal()

                    # If peak detect is enabled, hold maxima
                    if self.peakCheck.isChecked():
                        mask = (new_data > self.peak_buffer)
                        self.peak_buffer[mask] = new_data[mask]
                        self.y_axis = self.peak_buffer
                    # If not, perform averaging
                    elif self.avgSpin.value() > 1:
                        self.avg_buffer = np.concatenate(([new_data], self.avg_buffer[0:-1]))
                        self.y_axis = self.avg_buffer[0:self.avg_counter + 1].mean(axis=0)
                    else:
                        self.y_axis = new_data

                    if self.dBm:
                        self.y_axis = 20*np.log10(self.y_axis)
                
                    # Update plot
                    self.graph_line.set_ydata(self.y_axis)
                    self.graph_line.set_xdata(self.x_axis)
                    self.graph_line.set_visible(True)

                self.graph_ax.set_xlim([self.fstart, self.fstop])
                self.graph_ax.xaxis.set_ticks(np.linspace(self.fstart, self.fstop, 11))
                self.graph_ax.set_xlabel("Frequency (MHz)")

                if self.dBm:
                    self.graph_ax.set_autoscaley_on(False)
                    self.graph_ax.set_autoscalex_on(False)
                    ymin = (self.reflevel - 10*self.dbdiv)
                    ymax = self.reflevel
                    self.graph_ax.set_ylim([ymin, ymax])
                    self.graph_ax.yaxis.set_ticks(np.linspace(ymin, ymax, 11))
                    self.graph_ax.set_ylabel("Magnitude (dBm)")
                else:
                    self.graph_ax.set_autoscaley_on(True)
                    self.graph_ax.set_autoscalex_on(False)
                    self.graph_ax.relim()
                    self.graph_ax.yaxis.set_major_locator(AutoLocator())
                    self.graph_ax.autoscale_view()
                    self.graph_ax.set_ylabel("Magnitude (V)")
                
                self.graph.draw()
                self.graph.flush_events()

                # Update counters
                if self.avgSpin.value() > 1:
                    self.avg_counter += 1
                    if self.avg_counter >= self.avgSpin.value():
                        self.avg_counter = self.avgSpin.value() - 1
            else:                
                # Get signal
                if self.input_objs[0]:
                    # Clear image
                    self.sggraph_ax.clear()

                    # Get data
                    new_data = np.abs(self.input_signal())
                    if self.dBm:
                        new_data = 20*np.log10(new_data)

                    # Join data
                    if self.sg_counter < self.sgn:
                        self.sg_buffer[self.sg_counter] = new_data
                        t = time.time() - self.sg_t0
                        dt = t/(self.sg_counter + 1)
                        self.sg_x[self.sg_counter] = t
                        self.sg_x[-1] = dt*self.sgn
                    else:
                        self.sg_buffer = np.roll(self.sg_buffer, -1, axis=0)
                        self.sg_buffer[-1] = new_data
                        self.sg_x = np.roll(self.sg_x, -1, axis=0)
                        self.sg_x[-1] = time.time() - self.sg_t0

                    # Update plot
                    self.sggraph_ax.imshow(self.sg_buffer.T, aspect='auto', origin='lower',
                                           extent=[self.sg_x[0], self.sg_x[-1], self.sg_y[0], self.sg_y[-1]])

                self.sggraph_ax.set_xlabel("Time (s)")
                self.sggraph_ax.set_ylabel("Frequency (MHz)")
                
                self.sggraph.draw()
                self.sggraph.flush_events()

                # Update counters
                self.sg_counter += 1
                if self.sg_counter > self.sgn:
                    self.sg_counter = self.sgn - 1

            # Release soft lock
            self.busy = False

    # Save data
    def saveData(self):
        was_running = False
        if self.running:
            self.stopAcquisition()
            was_running = True
        
        file = QFileDialog.getSaveFileName(self, "Save file", QDir.homePath() , "Text files (*.txt)")
        filename = file[0]
        if filename != "":
            if filename[-4:] != ".txt" and filename[-4:] != ".TXT":
                filename = filename + ".txt"   

            with open(filename, "w") as file:
                if self.tabWidget.currentIndex() == 0:
                    vertname = "Magnitude (V)"
                    if self.dBm:
                        vertname = "Magnitude (dBm)"
                    file.write(f"Frequency (MHz)\t{vertname}\n")
                    for i in range(len(self.y_axis)):
                        file.write(f"{self.x_axis[i]}\t")
                        file.write(f"{self.y_axis[i]}")
                        file.write("\n")
                else:
                    vertname = "Mag. (V)"
                    if self.dBm:
                        vertname = "Mag. (dBm)"
                    file.write(f"Frequency (MHz)\t")
                    for j in range(0, len(self.sg_x)):
                        file.write(f"{vertname} t={self.sg_x[j]:.02f}\t")
                    file.write("\n")
                    for i in range(len(self.sg_buffer[0])):
                        file.write(f"{self.sg_y[i]}\t")
                        for j in range(0, len(self.sg_buffer)):
                            file.write(f"{self.sg_buffer[j][i]}")
                            if j < len(self.sg_buffer) - 1:
                                file.write("\t")
                        file.write("\n")
                file.close()

        if was_running:
            self.runAcquisition()


    # I/O functions
    # Set inputs: to connect the in functions to other instruments
    def set_inputs(self, sig=None):    
        self.input_objs = [sig]

    # Input functions: all parameters and instrument inputs are processed here. These are active (calls the output from other instruments)
    # Total time of the output wave
    def input_signal(self):
        if self.input_objs[0]:
            # Sync
            if self.sync_start:
                self.input_objs[0].t0 = 0.0
            else:
                self.input_objs[0].t0 = self.input_objs[0].tref
            
            data = 2*self.input_objs[0].output_signal()  # 2*: Consider Vpp
        else:
            data = np.zeros([int(self.npoints_inc*2*self.npoints)])

        N = int(2*self.fstop/self.rbw)
        inc_N = int(N*self.npoints_inc)
        skip = N//2 - self.npoints

        yf = []
        if self.windowfilt:
            w = windows.kaiser(inc_N, self.window_beta)
            if skip >= 0:  # This value can sometimes be < 0, leading to errors. If it happens, we just take some more points
                yf = fft(data*w)[skip:N//2]
            else:
                yf = fft(data*w)[:(N//2 - skip)]
        else:
            if skip >= 0:
                yf = fft(data)[skip:N//2] 
            else:   
                yf = fft(data)[:(N//2 - skip)]

        return (2.0/inc_N)*np.abs(yf)

    # Output functions: all instrument outputs are processed here. These are passive (called from other instruments)
    # Output sample time 
    def output_sampletime(self):
        return self.sampletime/1e6

    # Output npoints
    def output_npoints(self):
        return int(self.npoints_inc*2*self.fstop/self.rbw)
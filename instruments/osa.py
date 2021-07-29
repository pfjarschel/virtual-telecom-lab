# Simple virtual OSA class
# Default wavelength unit: nm
# Default power unit: W
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
FormUI, WindowUI = uic.loadUiType(f"{main_path}/osa.ui")

# Main instrument class
class OSA(FormUI, WindowUI):

    # Main parameters
    wlstart = 700.0
    wlstop = 1700.0
    wlcenter = (wlstop + wlstart)/2.0
    wlspan = wlstop - wlstart
    wldiv = wlspan/10.0
    dBm = True
    dbdiv = 10.0
    reflevel = 10.0
    npoints = 1000
    averages = 1
    rbw = wlspan/npoints
    peakdet = False
    
    # Input objects
    input_objs = [None]  

    # Internal parameters
    busy = False
    ui_busy = False
    running = False
    loop_timer = None
    x_axis = np.linspace(wlstart, wlstop, npoints)
    y_axis = np.zeros([npoints])
    sg_x = []
    sg_y = np.linspace(wlstart, wlstop, npoints)
    sg_z = np.zeros([1, npoints])
    avg_buffer = np.zeros([2, npoints])
    peak_buffer = np.zeros([npoints])
    sg_buffer = np.zeros([1, npoints])
    avg_counter = 0
    sg_counter = 0
    sg_t0 = time.time()
    
    
    # Default functions
    def __init__(self):
        super(OSA, self).__init__()

        print("Initializing OSA")

        self.setupUi(self)
        self.setupOtherUi()
        self.setupActions()
        self.show()
        

    def __del__(self):
        print("Deleting OSA object")


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
        self.pointsSpin.valueChanged.connect(self.setAcquisition)
        self.avgSpin.valueChanged.connect(self.setAcquisition)
        self.rbwSpin.valueChanged.connect(self.setAcquisition)
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
        
        self.graph_ax.set_xlim([self.wlstart, self.wlstop])
        self.graph_ax.xaxis.set_ticks(np.linspace(self.wlstart, self.wlstop, 11))
        self.graph_ax.xaxis.set_minor_locator(AutoMinorLocator())
        self.graph_ax.set_xlabel("Wavelength (nm)")

        if self.dBm:
            ymin = (self.reflevel - 10*self.dbdiv)
            ymax = self.reflevel
            self.graph_ax.set_ylim([ymin, ymax])
            self.graph_ax.yaxis.set_ticks(np.linspace(ymin, ymax, 11))
            self.graph_ax.set_ylabel("Power (dBm)")
        else:
            ymin = 0.0
            ymax = 1.0
            self.graph_ax.set_ylim([ymin, ymax])
            self.graph_ax.yaxis.set_major_locator(AutoLocator())
            self.graph_ax.set_ylabel("Power (mW)")
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
        self.sggraph_ax.set_ylabel("Wavelength (nm)")
        
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
            
            changed_f = False
            if sname == "startSpin" or sname == "stopSpin":
                changed_f = True
                if sname == "startSpin":
                    if self.startSpin.value() >= self.stopSpin.value():
                        self.startSpin.setValue(self.stopSpin.value() - 1e-2)
                elif sname == "stopSpin":
                    if self.stopSpin.value() <= self.startSpin.value():
                        self.stopSpin.setValue(self.startSpin.value() + 1e-2)
                self.wlstart = self.startSpin.value()
                self.wlstop = self.stopSpin.value()
                self.wlcenter = (self.wlstop + self.wlstart)/2.0
                self.wlspan = self.wlstop - self.wlstart
                self.centerSpin.setValue(self.wlcenter)
                self.spanSpin.setValue(self.wlspan)
            elif sname == "spanSpin" or sname == "centerSpin":
                changed_f = True
                self.wlspan = self.spanSpin.value()
                self.wlcenter = self.centerSpin.value()
                self.wlstart = max(self.wlcenter - self.wlspan/2.0, 700.0)
                self.wlstop = min(self.wlcenter + self.wlspan/2.0, 1700.0)
                self.wlcenter = (self.wlstop + self.wlstart)/2.0
                self.wlspan = self.wlstop - self.wlstart
                self.startSpin.setValue(self.wlstart)
                self.stopSpin.setValue(self.wlstop)
                self.centerSpin.setValue(self.wlcenter)
                self.spanSpin.setValue(self.wlspan)
            
            if sname == "rbwSpin" or changed_f:
                self.rbw = min(max(self.rbwSpin.value(), 0.01), 2.0)
                self.npoints = int(self.wlspan/self.rbw)
                self.rbwSpin.setValue(self.rbw)
                self.pointsSpin.setValue(self.npoints)
            elif sname == "pointsSpin":
                self.npoints = int(min(max(self.pointsSpin.value(), self.wlspan/2.0), self.wlspan/0.01))
                self.rbw = self.wlspan/self.npoints
                self.rbwSpin.setValue(self.rbw)
                self.pointsSpin.setValue(self.npoints)

            self.sgn = self.sgNSpin.value()
            self.x_axis = np.linspace(self.wlstart, self.wlstop, self.npoints)
            self.y_axis = np.zeros([self.npoints])
            self.peak_buffer = np.zeros([self.npoints])
            self.avg_buffer = np.zeros([self.avgSpin.value(), self.npoints])
            self.sg_buffer = 1e-30*np.ones([self.sgn, self.npoints])
            self.sg_y = np.linspace(self.wlstart, self.wlstop, self.npoints)  
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
                self.x_axis = np.linspace(self.wlstart, self.wlstop, self.npoints)  
                
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
                        self.y_axis = 10*np.log10(self.y_axis)
                
                    # Update plot
                    self.graph_line.set_ydata(self.y_axis)
                    self.graph_line.set_xdata(self.x_axis)
                    self.graph_line.set_visible(True)

                self.graph_ax.set_xlim([self.wlstart, self.wlstop])
                self.graph_ax.xaxis.set_ticks(np.linspace(self.wlstart, self.wlstop, 11))
                self.graph_ax.set_xlabel("Wavelength (nm)")

                if self.dBm:
                    self.graph_ax.set_autoscaley_on(False)
                    self.graph_ax.set_autoscalex_on(False)
                    ymin = (self.reflevel - 10*self.dbdiv)
                    ymax = self.reflevel
                    self.graph_ax.set_ylim([ymin, ymax])
                    self.graph_ax.yaxis.set_ticks(np.linspace(ymin, ymax, 11))
                    self.graph_ax.set_ylabel("Power (dBm)")
                else:
                    self.graph_ax.set_autoscaley_on(True)
                    self.graph_ax.set_autoscalex_on(False)
                    self.graph_ax.relim()
                    self.graph_ax.yaxis.set_major_locator(AutoLocator())
                    self.graph_ax.autoscale_view()
                    self.graph_ax.set_ylabel("Power (mW)")
                
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
                        new_data = 10*np.log10(new_data)

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
                self.sggraph_ax.set_ylabel("Wavelength (nm)")
                
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
                    vertname = "Power (mW)"
                    if self.dBm:
                        vertname = "Power (dBm)"
                    file.write(f"Wavelength (nm)\t{vertname}\n")
                    for i in range(len(self.y_axis)):
                        file.write(f"{self.x_axis[i]}\t")
                        file.write(f"{self.y_axis[i]}")
                        file.write("\n")
                else:
                    vertname = "P (mW)"
                    if self.dBm:
                        vertname = "P (dBm)"
                    file.write(f"WL (nm)\t")
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
            spec, wf = self.input_objs[0].output_opt_signal()
            data = 1000*np.interp(self.x_axis, spec[0], spec[1])
        else:
            data = np.zeros([int(self.npoints)])

        noise_min = 10**(-70/10)
        noise_max = 10**(-60/10)
        data = data + np.random.uniform(noise_min, noise_max, len(data))
        return data
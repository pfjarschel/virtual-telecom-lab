# Simple virtual oscilloscope class
# Default time unit: 1 s
# Default frequency unit = 1 Hz
# Default voltage unit: V
# By pfjarschel, 2021

# Imports
import os, time
import PyQt5
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from PyQt5 import uic, QtCore
from PyQt5.QtCore import QTimer, QDir
from PyQt5.QtWidgets import QFileDialog

# File paths
main_path = os.path.dirname(os.path.realpath(__file__))
thisfile = os.path.basename(__file__)

# Load ui file
FormUI, WindowUI = uic.loadUiType(f"{main_path}/oscilloscope.ui")

# Main instrument class
class Oscilloscope(FormUI, WindowUI):

    # Main parameters
    npoints = 1000
    timediv = 100e-9
    timeoffs = 0.0
    voltdivs = np.array([0.5, 0.5, 0.5, 0.5])
    voltscales = voltdivs*10
    voffsets = np.array([0.0, 0.0, 0.0, 0.0])
    channels = [True, False, False, False]
    averages = 1
    hold = False
    holdn = 2
    
    # Input objects
    input_objs = [None, None, None, None]  

    # Internal parameters
    busy = False
    running = False
    loop_timer = None
    mastervscale = [-5.0, 5.0]
    sampletime = timediv*10
    x_axis = np.linspace(timeoffs, timeoffs + sampletime, npoints)
    y_axis = np.zeros([4, npoints])
    avg_buffer = np.zeros([4, 2, npoints])
    hold_buffer = np.zeros([4, 2, npoints])
    avg_counter = 0
    hold_counter = 0
    xymode = False
    xy_x = 1
    
    
    # Default functions
    def __init__(self):
        super(Oscilloscope, self).__init__()

        print("Initializing oscilloscope")

        self.setupUi(self)
        self.setupOtherUi()
        self.setupActions()
        self.show()
        

    def __del__(self):
        print("Deleting oscilloscope object")


    # UI functions
    def setupOtherUi(self):
        self.setup_graph()
        self.channelsChecks = [self.ch1Check, self.ch2Check, self.ch3Check, self.ch4Check]
        self.xyChecks = [self.ch1XCheck, self.ch2XCheck, self.ch3XCheck, self.ch4XCheck]

    def setupActions(self):
        # Connect UI signals to functions
        self.startBut.clicked.connect(self.runAcquisition)
        self.stopBut.clicked.connect(self.stopAcquisition)
        self.saveBut.clicked.connect(self.saveData)
        self.holdCheck.clicked.connect(self.setAcquisition)
        self.ch1XCheck.clicked.connect(self.change_xy)
        self.ch2XCheck.clicked.connect(self.change_xy)
        self.ch3XCheck.clicked.connect(self.change_xy)
        self.ch4XCheck.clicked.connect(self.change_xy)
        self.hoffsetSpin.valueChanged.connect(self.setScales)
        self.pointsSpin.valueChanged.connect(self.setAcquisition)
        self.avgSpin.valueChanged.connect(self.setAcquisition)
        self.holdSpin.valueChanged.connect(self.setAcquisition)
        self.ch1offsSpin.valueChanged.connect(self.setScales)
        self.ch2offsSpin.valueChanged.connect(self.setScales)
        self.ch3offsSpin.valueChanged.connect(self.setScales)
        self.ch4offsSpin.valueChanged.connect(self.setScales)
        self.hscaleDial.valueChanged.connect(self.syncDialsSpins)
        self.hoffsetDial.valueChanged.connect(self.syncDialsSpins)
        self.ch1scaleDial.valueChanged.connect(self.syncDialsSpins)
        self.ch2scaleDial.valueChanged.connect(self.syncDialsSpins)
        self.ch3scaleDial.valueChanged.connect(self.syncDialsSpins)
        self.ch4scaleDial.valueChanged.connect(self.syncDialsSpins)
        self.ch1offsDial.valueChanged.connect(self.syncDialsSpins)
        self.ch2offsDial.valueChanged.connect(self.syncDialsSpins)
        self.ch3offsDial.valueChanged.connect(self.syncDialsSpins)
        self.ch4offsDial.valueChanged.connect(self.syncDialsSpins)
        
        # Timers
        self.loop_timer = QTimer()
        self.loop_timer.timeout.connect(self.measLoop)
        self.loop_timer.setInterval(10)
        
    def setup_graph(self):
        self.figure = plt.figure()
        self.graph = FigureCanvas(self.figure)
        self.graphToolbar = NavigationToolbar(self.graph, self)
        self.graphToolbar.locLabel.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.graphHolder.addWidget(self.graphToolbar)
        self.graphHolder.addWidget(self.graph)
        self.graph_ax = self.figure.add_subplot()
        self.graph_lines = [None, None, None, None]
        (self.graph_lines[0],) = self.graph_ax.plot([],[], 'o', markersize=1)
        (self.graph_lines[1],) = self.graph_ax.plot([],[], 'o', markersize=1)
        (self.graph_lines[2],) = self.graph_ax.plot([],[], 'o', markersize=1)
        (self.graph_lines[3],) = self.graph_ax.plot([],[], 'o', markersize=1)
        for line in self.graph_lines:
            line.set_visible(False)
        self.graph_ax.set_xlim([self.timeoffs, self.timediv*10 + self.timeoffs])
        self.graph_ax.set_ylim([self.mastervscale[0], self.mastervscale[1]])
        self.graph_ax.xaxis.set_ticks(np.linspace(self.timeoffs, self.timediv*10 + self.timeoffs, 11))
        self.graph_ax.yaxis.set_ticks(np.linspace(self.mastervscale[0], self.mastervscale[1], 11))
        self.graph_ax.xaxis.set_minor_locator(AutoMinorLocator())
        self.graph_ax.yaxis.set_minor_locator(AutoMinorLocator())
        self.graph_ax.set_xlabel("Time (s)")
        self.graph_ax.set_ylabel("Voltage (Div)")
        self.graph_ax.grid(True, which='minor', color='gainsboro')
        self.graph_ax.grid(True, which='major', color='gray')
        self.graph.draw()

    # Enable/disable vertical numbers in graph
    def change_vdivs(self):
        if self.showvdivCheck.isChecked():
            self.graph_ax.set_yticklabels(np.linspace(-5, 5, 11))
        else:
            self.graph_ax.set_yticklabels([])

        # self.graphHolder.removeWidget(self.graphToolbar)
        # self.graphToolbar = NavigationToolbar(self.graph, self)
        # self.graphToolbar.locLabel.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        # self.graphHolder.addWidget(self.graphToolbar)

    # Change XY mode
    def change_xy(self):
        ch = int(self.sender().objectName()[2])
        enable = self.sender().isChecked()
        self.ch1XCheck.setChecked(False)
        self.ch2XCheck.setChecked(False)
        self.ch3XCheck.setChecked(False)
        self.ch4XCheck.setChecked(False)
        self.sender().setChecked(enable)
        self.xymode = enable
        self.xy_x = ch
        if enable:
            self.channelsChecks[ch - 1].setChecked(True)

        self.setAcquisition()

    # Start/stop Acquisition
    def runAcquisition(self):
        if not self.running:
            self.running = True
            self.loop_timer.start()

    def stopAcquisition(self):
        if self.running:
            self.running = False
            self.loop_timer.stop()

    # Set acquisition stuff
    def setAcquisition(self):
        was_running = False
        if self.running:
            self.stopAcquisition()
            was_running = True

        self.npoints = self.pointsSpin.value()
        self.x_axis = np.linspace(self.timeoffs, self.timeoffs + self.sampletime, self.npoints)
        self.y_axis = np.zeros([4, self.npoints])
        self.avg_buffer = np.zeros([4, self.avgSpin.value(), self.npoints])
        self.hold_buffer = np.zeros([4, self.holdSpin.value(), self.npoints])
        self.avg_counter = 0
        self.hold_counter = 0

        # Get rid of empty average buffer
        for i in range(0, 4):
            data = self.input_channels(i)
            self.avg_buffer[i] = np.tile(data, (self.avgSpin.value(), 1))
        
        if was_running:
            self.runAcquisition()
            
    # Set oscilloscope scales
    def setScales(self):
        # Horizontal
        self.timeoffs = 0.01*self.hoffsetSpin.value()*self.sampletime
        
        # Vertical
        self.voffsets[0] = self.ch1offsSpin.value()                             
        self.voffsets[1] = self.ch2offsSpin.value()
        self.voffsets[2] = self.ch3offsSpin.value()
        self.voffsets[3] = self.ch4offsSpin.value()
        
        # Adjust dials positions
        self.hoffsetDial.setValue(self.hoffsetSpin.value()*10.0)
        self.ch1offsDial.setValue(self.ch1offsSpin.value()*10.0)
        self.ch2offsDial.setValue(self.ch2offsSpin.value()*10.0)
        self.ch3offsDial.setValue(self.ch3offsSpin.value()*10.0)
        self.ch4offsDial.setValue(self.ch4offsSpin.value()*10.0)
    
    # Sync spin boxes values to dials and sliders values
    def syncDialsSpins(self):
        # Horizontal
        horiz_list = [1e-12, 2e-12, 5e-12]
        hmultiplier = 10**(np.floor(self.hscaleDial.value()/3))
        hvalue = horiz_list[int(self.hscaleDial.value() % 3)]
        self.timediv = hvalue*hmultiplier
        self.sampletime = 10*self.timediv
        self.hscaleInd.setText(f"{self.float2SI(self.timediv)}s")
        self.hoffsetSpin.setValue(self.hoffsetDial.value()/10.0)
        
        # Vertical
        vert_list = [1e-4, 2e-4, 5e-4]
        
        # CH1
        vmultiplier = 10**(np.floor(self.ch1scaleDial.value()/3))
        vvalue = vert_list[int(self.ch1scaleDial.value() % 3)]
        vdiv = vvalue*vmultiplier
        self.ch1scaleInd.setText(f"{self.float2SI(vdiv)}V")
        self.ch1offsSpin.setValue(self.ch1offsDial.value()/10.0)
        self.voltdivs[0] = vdiv
        
        # CH2
        multiplier = 10**(np.floor(self.ch2scaleDial.value()/3))
        value = vert_list[int(self.ch2scaleDial.value() % 3)]
        vdiv = value*multiplier
        self.ch2scaleInd.setText(f"{self.float2SI(vdiv)}V")
        self.ch2offsSpin.setValue(self.ch2offsDial.value()/10.0)
        self.voltdivs[1] = vdiv
        
        # CH3
        multiplier = 10**(np.floor(self.ch3scaleDial.value()/3))
        value = vert_list[int(self.ch3scaleDial.value() % 3)]
        vdiv = value*multiplier
        self.ch3scaleInd.setText(f"{self.float2SI(vdiv)}V")
        self.ch3offsSpin.setValue(self.ch3offsDial.value()/10.0)
        self.voltdivs[2] = vdiv
        
        # CH4
        multiplier = 10**(np.floor(self.ch4scaleDial.value()/3))
        value = vert_list[int(self.ch4scaleDial.value() % 3)]
        vdiv = value*multiplier
        self.ch4scaleInd.setText(f"{self.float2SI(vdiv)}V")
        self.ch4offsSpin.setValue(self.ch4offsDial.value()/10.0)
        self.voltdivs[3] = vdiv
        
        self.voltscales = self.voltdivs*10


    # Internal functions
    # Helper to convert scientific notation to readable number with appropriate unit
    def float2SI(self, number):
        units = {  0:' ',
           1:'K',  2:'M',  3:'G',  4:'T',  5:'P',  6:'E',  7:'Z',  8:'Y',  9:'R',  10:'Q',
          -1:'m', -2:'u', -3:'n', -4:'p', -5:'f', -6:'a', -7:'z', -8:'y', -9:'r', -10:'q'
        }
         
        mantissa,exponent = f"{number:e}".split("e")
        unitRange         = int(exponent)//3                        
        unit              = units.get(unitRange,None)
        unitValue         = float(mantissa)*10**(int(exponent)%3)
        return f"{unitValue:.0f} {unit}" if unit else f"{number:.5e}"
    
    # Acquisition loop
    def measLoop(self):
        if not self.busy:
            # Set soft lock
            self.busy = True
            
            # Create arrays
            self.x_axis = np.linspace(self.timeoffs, self.timeoffs + self.sampletime, self.npoints)  
            if self.holdCheck.isChecked():
                self.x_axis = np.tile(self.x_axis, self.hold_counter + 1)
                self.y_axis = np.zeros([4, self.npoints*(self.hold_counter + 1)])
            
            # Sweep channels
            for i in range(0, len(self.input_objs)):
                if self.channelsChecks[i].isChecked() and self.input_objs[i]:
                    # Adjust phase to simulate trigger (and time offset)
                    if self.triggerautoRadio.isChecked():
                        freq = self.input_objs[i].freq
                        argument = 2*np.pi*freq*self.timeoffs
                        self.input_objs[i].t0 = argument
                    else:
                        self.input_objs[i].t0 = np.random.uniform(0.0, 2*np.pi)
                        
                    # Get data
                    new_data = self.input_channels(i)

                    # If hold is enabled, hold data
                    if self.holdCheck.isChecked():
                        self.hold_buffer[i] = np.concatenate(([new_data], self.hold_buffer[i][0:-1]))
                        self.y_axis[i] = np.concatenate(self.hold_buffer[i][0:self.hold_counter + 1])
                    # If not, perform averaging
                    elif self.avgSpin.value() > 1:
                        self.avg_buffer[i] = np.concatenate(([new_data], self.avg_buffer[i][0:-1]))
                        self.y_axis[i] = self.avg_buffer[i][0:self.avg_counter + 1].mean(axis=0)
                    else:
                        self.y_axis[i] = new_data
                
                    # Update plot
                    self.graph_lines[i].set_ydata((self.y_axis[i] + self.voffsets[i])/self.voltdivs[i])
                    self.graph_lines[i].set_xdata(self.x_axis)
                    self.graph_lines[i].set_visible(True)
                else:
                    self.graph_lines[i].set_visible(False)

            self.graph_ax.set_xlim([self.timeoffs, self.timediv*10 + self.timeoffs])
            self.graph_ax.set_ylim([self.mastervscale[0], self.mastervscale[1]])
            self.graph_ax.xaxis.set_ticks(np.linspace(self.timeoffs, self.timediv*10 + self.timeoffs, 11))
            self.graph_ax.yaxis.set_ticks(np.linspace(self.mastervscale[0], self.mastervscale[1], 11))
            self.graph_ax.set_xlabel("Time (s)")
            self.graph_ax.set_ylabel("Voltage (Div)")

            # After getting all data, change plots to XY mode if enabled
            ch = self.xy_x - 1
            if self.xymode and self.channelsChecks[ch].isChecked() and self.input_objs[ch]:
                for i in range(0, len(self.input_objs)):
                    if self.channelsChecks[i].isChecked() and self.input_objs[i] and i != ch:
                        new_x = (self.y_axis[ch] + self.voffsets[ch])/self.voltdivs[ch]
                        self.graph_lines[i].set_xdata(new_x)
                        self.graph_lines[i].set_visible(True)
                        self.graph_ax.set_xlim([self.mastervscale[0], self.mastervscale[1]])
                        self.graph_ax.xaxis.set_ticks(np.linspace(self.mastervscale[0], self.mastervscale[1], 11))
                    elif self.channelsChecks[i].isChecked() and self.input_objs[i] and i == ch:
                        self.graph_lines[i].set_visible(False)
                
                self.graph_ax.set_xlabel(f"CH{ch + 1} Voltage (Div)")
                self.graph_ax.set_ylabel("Voltage (Div)")
            
            self.graph.draw()
            self.graph.flush_events()

            # Update counters
            if self.holdCheck.isChecked():
                self.hold_counter += 1
                if self.hold_counter >= self.holdSpin.value():
                    self.hold_counter = self.holdSpin.value() - 1
            elif self.avgSpin.value() > 1:
                self.avg_counter += 1
                if self.avg_counter >= self.avgSpin.value():
                    self.avg_counter = self.avgSpin.value() - 1
            
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
                file.write("Time(s)\t")
                for j in range(0, len(self.input_objs)):
                    if self.channelsChecks[j].isChecked():
                        file.write(f"CH{j + 1}(V)\t")
                file.write("\n")

                for i in range(len(self.y_axis[0])):
                    file.write(f"{self.x_axis[i]}\t")
                    for j in range(0, len(self.input_objs)):
                        if self.channelsChecks[j].isChecked():
                            file.write(f"{self.y_axis[j][i]}")
                            if j < len(self.input_objs) - 1:
                                file.write("\t")
                    file.write("\n")
                file.close()

        if was_running:
            self.runAcquisition()


    # I/O functions
    # Set inputs: to connect the in functions to other instruments
    def set_inputs(self, ch1=None, ch2=None, ch3=None, ch4=None):    
        self.input_objs = [ch1, ch2, ch3, ch4]

    # Input functions: all parameters and instrument inputs are processed here. These are active (calls the output from other instruments)
    # Total time of the output wave
    def input_channels(self, channel):
        if self.input_objs[channel] and self.channelsChecks[channel].isChecked():
            data = self.input_objs[channel].output_signal()
        else:
            data = np.zeros([self.npoints])
        return data

    # Output functions: all instrument outputs are processed here. These are passive (called from other instruments)
    # Output sample time 
    def output_sampletime(self):
        return self.sampletime*1

    # Output npoints
    def output_npoints(self):
        return self.npoints*1
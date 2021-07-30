# Simple virtual OTDR class
# Default time unit: 1 ns
# Default wavelength unit: nm
# Default power unit: W
# By pfjarschel, 2021

# Imports
import os, time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from PyQt5 import uic, QtCore
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QFileDialog

# File paths
main_path = os.path.dirname(os.path.realpath(__file__))
thisfile = os.path.basename(__file__)

# Load ui file
FormUI, WindowUI = uic.loadUiType(f"{main_path}/otdr.ui")


# Main instrument class
class OTDR(FormUI, WindowUI):

    # Main parameters
    powerdbm = 0.0
    fiber_n = 1.45
    pulsew = 1.0
    stopkm = 100.0

    # Internal parameters
    resln = (3e8/fiber_n)*pulsew*1e-9
    npoints = int(stopkm*1000.0/resln)
    real_length = 0.0
    real_loss = 0.0
    noise_level_top = -100.0
    noise_level_bot = -120.0

    # Data holders
    fiber_z = np.linspace(0, stopkm, npoints)
    refl_pwr = np.zeros([npoints])
    events = []


    # Input objs
    input_fiber = None
    
    # Default functions
    def __init__(self):
        super(OTDR, self).__init__()
        
        print("Initializing OTDR object")

        self.setupUi(self)
        self.setupOtherUi()
        self.setupActions()

        self.show()

    def __del__(self):
        print("Deleting OTDR object")

    
    # UI functions
    def setupOtherUi(self):
        self.figure = plt.figure()
        self.graph = FigureCanvas(self.figure)
        self.graphToolbar = NavigationToolbar(self.graph, self)
        self.graphToolbar.locLabel.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.graphHolder.addWidget(self.graphToolbar)
        self.graphHolder.addWidget(self.graph)
        self.graph_ax = self.figure.add_subplot()
        self.graph_line = None
        self.graph_line, = self.graph_ax.plot([],[])
        self.graph_ax.set_xlim([0, self.stopkm])
        self.graph_ax.set_ylim([-100, 0])
        self.graph_ax.set_xlabel("Length (km)")
        self.graph_ax.set_ylabel("Rel. reflected power (dB)")
        self.graph_ax.grid(True, which='minor', color='gainsboro')
        self.graph_ax.grid(True, which='major', color='gray')
        self.graph.draw()
    
    def setupActions(self):
        # Connect UI signals to functions
        self.pwrSpin.valueChanged.connect(self.setParameters)
        self.fibernSpin.valueChanged.connect(self.setParameters)
        self.pwSpin.valueChanged.connect(self.setParameters)
        self.stopSpin.valueChanged.connect(self.setParameters)

        self. startBut.clicked.connect(self.create_measmnt)
        self.saveBut.clicked.connect(self.saveData)

    def setParameters(self):
        self.powerdbm = self.pwrSpin.value()
        self.fiber_n = self.fibernSpin.value()
        self.pulsew = self.pwSpin.value()
        self.stopkm = self.stopSpin.value()

        self.resln = (3e8/self.fiber_n)*self.pulsew*1e-9
        self.npoints = int(self.stopkm*1000.0/self.resln)
        if self.npoints < 20:
            self.npoints = 20

        # Data holders
        self.fiber_z = np.linspace(0, self.stopkm, self.npoints)
        self.refl_pwr = np.zeros([self.npoints])


    # Internal functions    
    # Create measuremetnt
    def create_measmnt(self):
        # Get stuff from fiber
        self.input_fiber_params()

        # Pure attenuation measurement
        end_i = -1
        loss = self.real_loss
        for i in range(self.npoints):
            z = self.fiber_z[i]
            rp = 0
            if z <= self.real_length:
                # Add tiny variations to loss
                if i % int(self.npoints/10) == 0:
                    loss = self.real_loss + np.random.uniform(-0.005, 0.005)

                rp = self.powerdbm - z*loss
                if rp <= self.noise_level_top:
                    rp = np.random.uniform(self.noise_level_bot, self.noise_level_top)
            else:
                if end_i < 0:
                    end_i = i - 1
                rp = np.random.uniform(self.noise_level_bot, self.noise_level_top)
            
            self.refl_pwr[i] = rp

        # Add tiny noise
        self.refl_pwr = self.refl_pwr + np.random.uniform(-0.03, 0.03, self.npoints)

        # Add random events
        if len(self.events) < 1:
            print("asdfsdf")
            n = np.random.randint(1, 20)
            self.events = np.zeros([2, n])
            for i in range(n):
                amp = np.random.uniform(-5, 3)
                loc_z = np.random.uniform(0.1, self.real_length)
                self.events[0][i] = loc_z
                self.events[1][i] = amp
            
        for i in range(len(self.events[0])):
            loc_z = self.events[0][i]
            amp = self.events[1][i]
            loc = np.abs(self.fiber_z - loc_z).argmin()
            if amp < 0 and loc < end_i:
                    self.refl_pwr[loc:] = self.refl_pwr[loc:] + amp
            else:
                self.refl_pwr[loc] += amp
                self.refl_pwr[loc + 1] = self.refl_pwr[loc - 1]

        # Reset noise floor
        for i in range(end_i):
            if self.refl_pwr[i] < self.noise_level_top:
                self.refl_pwr[i] = np.random.uniform(self.noise_level_bot, self.noise_level_top)
        self.refl_pwr[end_i:] = np.random.uniform(self.noise_level_bot, self.noise_level_top, len(self.refl_pwr[end_i:]))

        # Add start/end events
        self.refl_pwr[0:10] += 1.0
        self.refl_pwr[1] += 1.0
        if end_i > 0:   
            self.refl_pwr[end_i] += 2.0
            self.refl_pwr[end_i + 1] = self.refl_pwr[end_i - 1]

        # Normalize
        self.refl_pwr = self.refl_pwr - self.refl_pwr.max()

        # Plot
        self.graph_line.set_ydata(self.refl_pwr)
        self.graph_line.set_xdata(self.fiber_z)
        self.graph_ax.set_xlim([0.0, self.stopkm])
        self.graph_ax.set_xlabel("Length (km)")
        self.graph_ax.set_ylabel("Rel. reflected power (dB)")
        self.graph_ax.set_autoscaley_on(True)
        self.graph_ax.set_autoscalex_on(False)
        self.graph_ax.relim()
        self.graph_ax.autoscale_view()
        self.graph.draw()
        self.graph.flush_events()


    # Set inputs: to connect the in functions to other instruments
    def set_input_fiber(self, fiber=None):    
        self.input_fiber = fiber

    # Input functions: all parameters and instrument inputs are processed here. These are active (calls the output from other instruments)
    # Total time of the output wave
    def input_fiber_params(self):
        if self.input_fiber:
            self.real_length = self.input_fiber.length
            self.real_loss = self.input_fiber.att

    # Save data
    def saveData(self):        
        file = QFileDialog.getSaveFileName(self, "Save file", QDir.homePath() , "Text files (*.txt)")
        filename = file[0]
        if filename != "":
            if filename[-4:] != ".txt" and filename[-4:] != ".TXT":
                filename = filename + ".txt"   

            with open(filename, "w") as file:
                file.write(f"Length (km)\tRel. reflected power (dB)\n")
                for i in range(len(self.refl_pwr)):
                    file.write(f"{self.fiber_z[i]}\t")
                    file.write(f"{self.refl_pwr[i]}")
                    file.write("\n")
                file.close()
# Simple virtual tunable laser class
# Default time unit: 1 s
# Default frequency unit = 1 THz
# Default wavelength unit: nm
# Default power unit: W
# By pfjarschel, 2021

# Imports
import os, time
import numpy as np
from PyQt5 import uic

# File paths
main_path = os.path.dirname(os.path.realpath(__file__))
thisfile = os.path.basename(__file__)

# Load ui file
FormUI, WindowUI = uic.loadUiType(f"{main_path}/laser.ui")


# Main instrument class
class Laser(FormUI, WindowUI):

    # Main parameters
    wavelength = 1550.0
    frequency = 193.548
    powermw = 1.0
    powerdbm = 0.0

    # Internal parameters
    linewidth = 0.01
    start_wl = 700
    stop_wl = 1700
    npoints = 1000000
    ui_busy = False

    # Spec and wf holders
    spec = np.zeros([2, npoints])
    wf = np.zeros([2, 100])
    
    # Default functions
    def __init__(self):
        super(Laser, self).__init__()
        
        print("Initializing Tunable Laser object")

        self.setupUi(self)
        self.setupOtherUi()
        self.setupActions()
        self.create_spec()
        self.create_wf()
        self.show()

    def __del__(self):
        print("Deleting Tunable Laser object")

    
    # UI functions
    def setupOtherUi(self):
        # No need for this class, but is standard on my scripts (see oscilloscope for an example)
        pass  
    
    def setupActions(self):
        # Connect UI signals to functions
        self.wlSpin.valueChanged.connect(self.setParameters)
        self.freqSpin.valueChanged.connect(self.setParameters)
        self.dbpwrSpin.valueChanged.connect(self.setParameters)
        self.mwpwrSpin.valueChanged.connect(self.setParameters)

    def setParameters(self):
        if not self.ui_busy:
            self.ui_busy = True

            sname = self.sender().objectName()

            # Set WL/Frequency
            if sname == "wlSpin":
                self.wavelength = self.wlSpin.value()
                self.frequency = 3e5/self.wavelength
                self.freqSpin.setValue(self.frequency)
            elif sname == "freqSpin":
                self.frequency = self.freqSpin.value()
                self.wavelength = 3e5/self.frequency
                self.wlSpin.setValue(self.wavelength)

            # Set Power
            if sname == "dbpwrSpin":
                self.powerdbm = self.dbpwrSpin.value()
                self.powermw = 10**(self.powerdbm/10)
                self.mwpwrSpin.setValue(self.powermw)
            elif sname == "mwpwrSpin":
                self.powermw = self.mwpwrSpin.value()
                self.powerdbm = 10*np.log10(self.powermw)
                self.dbpwrSpin.setValue(self.powerdbm)

            self.create_spec()

            self.ui_busy = False


    # Internal functions    
    # Create full spectrum
    def create_spec(self):
        self.spec = np.zeros([2, self.npoints])
        self.spec[0] = np.linspace(self.start_wl, self.stop_wl, self.npoints)

        # Gaussian with linewidth
        self.spec[1] = 1e-3*self.powermw*np.exp(-((self.spec[0] - self.wavelength)**2)/(2*(self.linewidth**2)))

    # Create constant waveform
    def create_wf(self):
        self.wf = np.ones([2, 100])
        self.wf[0] = np.linspace(0.0, 1.0, 100)
        self.wf[1] = 1e-3*self.powermw*self.wf[1]

    # I/O functions

    # Output functions: all instrument outputs are processed here. These are passive (called from other instruments)
    # Output optical signal: The instrument output (the laser spectrum) 
    def output_opt_signal(self):
        return np.copy(self.spec), np.copy(self.wf)
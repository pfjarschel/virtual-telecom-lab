# Simple virtual prbs generator class
# Default time unit: 1 s
# Default frequency unit = 1 Hz
# Default voltage unit: V
# By pfjarschel, 2021

# Imports
import os, time
import numpy as np
from PyQt5 import uic

# File paths
main_path = os.path.dirname(os.path.realpath(__file__))
thisfile = os.path.basename(__file__)

# Load ui file
FormUI, WindowUI = uic.loadUiType(f"{main_path}/prbs_gen.ui")


# Main instrument class
class PRBSGenerator(FormUI, WindowUI):

    # Main parameters
    freq = 1e6
    amplitude = 1.0
    dutycycle = 0.5
    offset = 0.0
    sampletime = 2e-6
    npoints = 1000

    # Input objects
    input_sampletime_obj = None
    input_npoints_obj = None

    # Independent limits
    max_freq = 10e9
    min_freq= 100e3
    max_amplitude = 1e2
    min_amplitude = 1e-3
    max_offset = 1e2
    min_offset = -1e2

    # Internal parameters
    risetime = 0.4*(1/max_freq)
    falltime = risetime
    noiselevel = 5*min_amplitude
    jitter = 20e-12
    phase = 0.0
    output_enabled = False
    timemult = 1.0

    # Waveform holder
    wf = []
    
    # Default functions
    def __init__(self):
        super(PRBSGenerator, self).__init__()
        
        print("Initializing PRBS generator")
        self.t0 = time.time()  # Will be the phase of the output wave
        self.refresh_params()  # Recalculate some parameters

        self.setupUi(self)
        self.setupOtherUi()
        self.setupActions()
        self.show()

    def __del__(self):
        print("Deleting PRBS generator object")

    
    # UI functions
    def setupOtherUi(self):
        # No need for this class, but is standard on my scripts (see oscilloscope for an example)
        pass  
    
    def setupActions(self):
        # Connect UI signals to functions
        self.f1mhzCheck.clicked.connect(self.setParameters)
        self.f100mhzCheck.clicked.connect(self.setParameters)
        self.f1ghzCheck.clicked.connect(self.setParameters)
        self.a1mvCheck.clicked.connect(self.setParameters)
        self.a10mvCheck.clicked.connect(self.setParameters)
        self.a100mvCheck.clicked.connect(self.setParameters)
        self.a1vCheck.clicked.connect(self.setParameters)
        self.a10vCheck.clicked.connect(self.setParameters)
        self.fmultSpin.valueChanged.connect(self.setParameters)
        self.amultSpin.valueChanged.connect(self.setParameters)
        self.offsetSpin.valueChanged.connect(self.setParameters)
        self.fmultDial.valueChanged.connect(self.syncDialsSpins)
        self.amultDial.valueChanged.connect(self.syncDialsSpins)
        self.offsetSlider.valueChanged.connect(self.syncDialsSpins)
        

    def toggleOutput(self):
        if self.output_enabled:
            self.output_enabled = False
            self.onoffBut.setText("Output is OFF")
        else:
            self.output_enabled = True
            self.onoffBut.setText("Output is ON")

    def syncDialsSpins(self):
        # Sync spin boxes values to dials and sliders values
        self.fmultSpin.setValue(self.fmultDial.value()/100.0)
        self.amultSpin.setValue(self.amultDial.value()/10.0)
        self.offsetSpin.setValue(self.offsetSlider.value()/10.0)

    def setParameters(self):
        # Set Frequency
        frange = 1.0
        if self.f1mhzCheck.isChecked():
            frange = 1e6
        elif self.f100mhzCheck.isChecked():
            frange = 100e6
        elif self.f1ghzCheck.isChecked():
            frange = 1e9
        freq = frange*self.fmultSpin.value()
        self.freq = max(min(self.max_freq, freq), self.min_freq)

        # Set Amplitude
        arange = 1.0
        if self.a1mvCheck.isChecked():
            arange = 1e-3
        elif self.a10mvCheck.isChecked():
            arange = 10e-3
        elif self.a100mvCheck.isChecked():
            arange = 0.1
        elif self.a1vCheck.isChecked():
            arange = 1.0
        elif self.a10vCheck.isChecked():
            arange = 10.0
        amplitude = arange*self.amultSpin.value()
        offset = self.offsetSpin.value()
        self.amplitude = max(min(self.max_amplitude, amplitude), self.min_amplitude)
        self.offset = max(min(self.max_offset, offset), self.min_offset)

        # Recalculate some stuff
        self.refresh_params()

        # Adjust dials/sliders positions and limited values
        self.fmultDial.setValue(self.fmultSpin.value()*100.0)
        self.amultDial.setValue(self.amultSpin.value()*10.0)
        self.offsetSlider.setValue(self.offsetSpin.value()*10.0)


    # Internal functions    
    # Create full waveform
    def get_waveform(self):
        wf = np.zeros([self.totnpoints])
        phase = self.t0 % (2*np.pi)

        # Add some jitter
        jitter = np.random.uniform(-self.jitter/2, self.jitter/2)
        argument = 2*np.pi*self.freq*(self.exttimearray + jitter) + phase

        # Create bits
        multiplier_array = np.zeros([self.totnpoints])
        bit = int(np.round(np.random.random()))
        bit_n = np.floor(argument[0]/(2*np.pi))
        for i in range(self.totnpoints):
            if np.floor(argument[i]/(2*np.pi)) > bit_n:
                bit_n = np.floor(argument[i]/(2*np.pi))
                bit = int(np.round(np.random.random()))
            multiplier_array[i] = bit
        wf = self.amplitude*(multiplier_array - 0.5)
            
        # Filter (simulate risetime)
        filt_wl = min(max(int(self.risetime/self.delta), 3), self.totnpoints)
        if not (filt_wl % 2): filt_wl -= 1
        w = np.blackman(filt_wl)
        wf = np.convolve(wf, w, 'same')/np.sum(w)
        
        # Get only the numper of points wanted
        wf = wf[self.addpoints:-self.addpoints]

        # Add some noise
        noise = np.random.uniform(-self.noiselevel/2, self.noiselevel/2, size=self.npoints)
        wf = wf + noise + self.offset

        self.wf = np.clip(wf, self.min_offset, self.max_offset)
    
    # Recalculate some parameters
    def refresh_params(self):  
        self.delta = self.sampletime/self.npoints  # Time step
        
        # Points to add (will be cut off later, increases filter precision)
        self.npoints = int(self.npoints*self.timemult)
        self.addpoints = int(self.npoints*0.1)
        self.totnpoints = self.npoints + 2*self.addpoints

        # Added time due to the added points
        self.sampletime = self.sampletime*self.timemult
        self.addtime = self.delta*self.addpoints
        self.tottime = self.sampletime + self.addtime

        # Time arrays
        self.exttimearray = np.linspace(-self.addtime, self.tottime, self.totnpoints)
        self.timearray = np.linspace(0, self.sampletime, self.npoints)


    # I/O functions
    # Set inputs: to connect the in functions to other instruments
    def set_inputs(self, sampletime_obj, npoints_obj):    
        self.input_sampletime_obj = sampletime_obj
        self.input_npoints_obj = npoints_obj

    # Input functions: all parameters and instrument inputs are processed here. These are active (calls the output from other instruments)
    # Total time of the output wave
    def input_sampletime(self):
        if self.input_sampletime_obj:
            sampletime = self.input_sampletime_obj.output_sampletime()
        else:
            sampletime = self.sampletime
        if self.sampletime != sampletime:
            self.sampletime = sampletime

    # Number of points of the output wave
    def input_npoints(self):
        if self.input_npoints_obj:
            npoints = self.input_npoints_obj.output_npoints()
        else:
            npoints = self.npoints
        if npoints != self.npoints:
            self.npoints = npoints

    # Output functions: all instrument outputs are processed here. These are passive (called from other instruments)
    # Output signal: The instrument oputput (a time-dependent signal)   
    def output_signal(self):
        # Get sampletime and npoints
        self.input_sampletime()
        self.input_npoints()
        self.refresh_params()
        self.wf = np.zeros([self.npoints])

        # Get data
        self.get_waveform()

        return self.wf

    # Output time array: outputs the instrument time array on which the signal is based
    def output_timearray(self):
        return self.timearray

    # Output frequency: outputs the signal frequency
    def output_freq(self):
        return self.freq
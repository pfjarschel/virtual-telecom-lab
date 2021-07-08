# Simple virtual QAM generator class
# Default time unit: 1 s
# Default frequency unit = 1 Hz
# Default voltage unit: V
# By pfjarschel, 2021

# Imports
import os, time
import numpy as np
from PyQt5 import uic
from instruments.qam_i_signal import QAMISignal
from instruments.qam_q_signal import QAMQSignal

# File paths
main_path = os.path.dirname(os.path.realpath(__file__))
thisfile = os.path.basename(__file__)

# Load ui file
FormUI, WindowUI = uic.loadUiType(f"{main_path}/qam_gen.ui")


# Main instrument class
class QAMGenerator(FormUI, WindowUI):

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
    max_freq = 50e9
    min_freq= 100e3
    max_amplitude = 1e2
    min_amplitude = 1e-3
    max_offset = 1e2
    min_offset = -1e2

    # Internal parameters
    risetime = 0.4*(5/max_freq)
    falltime = risetime
    noiselevel = 5*min_amplitude
    jitter = 20e-12
    phasei = 0.0
    phaseq = 0.0
    output_enabled = False
    timemult = 1.0
    outp_count = 0

    # Waveform holder
    wf = []

    # I and Q signal outputs
    signal_i = QAMISignal()
    signal_q = QAMQSignal()
    
    # Default functions
    def __init__(self):
        super(QAMGenerator, self).__init__()
        
        print("Initializing QAM generator")
        self.t0 = time.time()  # Will be the phase of the output wave
        self.refresh_params()  # Recalculate some parameters

        # Connect internal gens to mainframe
        self.signal_i.set_inputs(self)
        self.signal_q.set_inputs(self)

        # UI init
        self.setupUi(self)
        self.setupOtherUi()
        self.setupActions()
        self.show()

    def __del__(self):
        print("Deleting QAM generator object")

    
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
        self.phaseiSpin.valueChanged.connect(self.setParameters)
        self.phaseqSpin.valueChanged.connect(self.setParameters)
        self.levelsSpin.valueChanged.connect(self.setBitLevels)
        self.fmultDial.valueChanged.connect(self.syncDialsSpins)
        self.amultDial.valueChanged.connect(self.syncDialsSpins)
        self.offsetSlider.valueChanged.connect(self.syncDialsSpins)
        self.phaseiSlider.valueChanged.connect(self.syncDialsSpins)
        self.phaseqSlider.valueChanged.connect(self.syncDialsSpins)
        

    def syncDialsSpins(self):
        # Sync spin boxes values to dials and sliders values
        self.fmultSpin.setValue(self.fmultDial.value()/100.0)
        self.amultSpin.setValue(self.amultDial.value()/10.0)
        self.offsetSpin.setValue(self.offsetSlider.value()/10.0)
        self.phaseiSpin.setValue(self.phaseiSlider.value()/10.0)
        self.phaseqSpin.setValue(self.phaseqSlider.value()/10.0)

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

        # Set phase
        self.phasei = self.phaseiSpin.value()*np.pi/180.0
        self.phaseq = self.phaseqSpin.value()*np.pi/180.0

        # Adjust dials/sliders positions and limited values
        self.fmultDial.setValue(self.fmultSpin.value()*100.0)
        self.amultDial.setValue(self.amultSpin.value()*10.0)
        self.offsetSlider.setValue(self.offsetSpin.value()*10.0)
        self.phaseiSlider.setValue(self.phaseiSpin.value()*10.0)
        self.phaseqSlider.setValue(self.phaseqSpin.value()*10.0)

    def setBitLevels(self):
        if self.levelsSpin.value() % 2:
            self.levelsSpin.setValue(self.levelsSpin.value() + 1)


    # Internal functions    
    # Create full waveform
    def get_waveform(self):
        wf = np.zeros([self.totnpoints])
        phasei = self.t0 % (2*np.pi) + self.phasei
        phaseq = self.t0 % (2*np.pi) + self.phaseq

        # Create signals
        pts_per_symb = int(max((1/self.freq)/self.delta, 1))
        num_symbols = int(np.floor(self.totnpoints/pts_per_symb))
        rem_points = int(self.totnpoints % pts_per_symb)

        nphases = 4
        ph_int = np.random.randint(0, nphases, num_symbols)
        ph_degrees = (360/nphases)*(ph_int + 0.5)
        ph_radians = np.repeat(ph_degrees*np.pi/180.0, pts_per_symb)
        extra_ph = (360/nphases)*(np.random.randint(0, nphases) + 0.5)
        extra_rad = extra_ph*np.pi/180.0
        ph_radians = np.concatenate([ph_radians, np.array(rem_points*[extra_rad])])

        sig1 = np.cos(ph_radians)
        sig2 = np.sin(ph_radians)

        nlevels = self.levelsSpin.value()
        amps = np.arange(-(nlevels - 1), nlevels, 2)/max(nlevels - 1, 1)
        amp1 = amps[np.random.randint(1, nlevels + 1, int(num_symbols)) - 1]
        amp2 = amps[np.random.randint(1, nlevels + 1, int(num_symbols)) - 1]
        extra_amp1 = amps[np.random.randint(1, nlevels + 1) - 1]
        extra_amp2 = amps[np.random.randint(1, nlevels + 1) - 1]
        amp1_array = np.concatenate([np.repeat(amp1, pts_per_symb), np.array(rem_points*[extra_amp1])])
        amp2_array = np.concatenate([np.repeat(amp2, pts_per_symb), np.array(rem_points*[extra_amp2])])
        sig1 = sig1*amp1_array
        sig2 = sig2*amp2_array

        sig = sig1 + 1j*sig2

        # Phase imbalance
        o = 1j * (sig.imag * np.cos(self.phaseq) + sig.real * np.sin(self.phasei))
        o += sig.real * np.cos(self.phasei) + sig.imag *  np.sin(self.phaseq)
        sig = o
        
        # Phase noise
        jitter = np.random.uniform(-self.jitter/2, self.jitter/2, self.totnpoints)
        phase_noise = 2*np.pi*self.freq*(jitter)
        sig = sig * np.exp(1j*phase_noise)

        # Non-linear
        # nlf = 0.0
        # sig = sig*np.exp(1j*np.abs(sig)*2*nlf)

        # Filter (simulate risetime)
        filt_wl = min(max(int(self.risetime/self.delta), 3), self.totnpoints)
        if not (filt_wl % 2): filt_wl -= 1
        w = np.blackman(filt_wl)
        sig = np.convolve(sig, w, 'same')/np.sum(w)
        
        # Get only the numper of points wanted
        sig = sig[self.addpoints:-self.addpoints]

        # Add some noise
        n1 = (np.random.randn(self.npoints) + 1j*np.random.randn(self.npoints))/np.sqrt(2) # AWGN with unity power
        n2 = (np.random.randn(self.npoints) + 1j*np.random.randn(self.npoints))/np.sqrt(2) # AWGN with unity power
        noise_power = self.noiselevel/5000
        sig = self.amplitude*sig + n1*np.sqrt(noise_power) + 1j*n2*np.sqrt(noise_power)


        self.wf = np.clip(sig, self.min_offset, self.max_offset)
    
    # Recalculate some parameters
    def refresh_params(self):  
        self.delta = self.sampletime/self.npoints  # Time step
        self.outp_count = 0
        
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
        if not self.outp_count % 2:
            # Get sampletime and npoints
            self.input_sampletime()
            self.input_npoints()
            self.refresh_params()
            self.wf = np.zeros([self.npoints])

            # Get data
            self.get_waveform()

            self.outp_count += 1

        elif self.outp_count == 1:
            self.outp_count += 1

        return self.wf

    # Output time array: outputs the instrument time array on which the signal is based
    def output_timearray(self):
        return self.timearray

    # Output frequency: outputs the signal frequency
    def output_freq(self):
        return self.freq
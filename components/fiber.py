# Simple optical fiber class
# Default wavelength unit = 1 nm
# Default power unit: W
# By pfjarschel, 2021

# Imports
import os, time
import numpy as np

# File paths
main_path = os.path.dirname(os.path.realpath(__file__))
thisfile = os.path.basename(__file__)


# Main component class
class Fiber():
    # Main parameters
    att = 0.35  # dB/km
    freq = 1e6
    
    # Input objects
    input_opt_signal_obj = None


    # Default functions
    def __init__(self, length=1.0):    
        print("Initializing fiber")
        self.t0 = time.time()
        self.tref = self.t0
        self.length = length

    def __del__(self):
        print("Deleting fiber object")

    # I/O functions
    # Set inputs: to connect the in functions to other instruments
    def set_inputs(self, opt_signal_obj):    
        self.input_opt_signal_obj = opt_signal_obj

    # Waveform to propagate
    def input_opt_signal(self):
        spec, wf = self.input_opt_signal_obj.output_opt_signal()
        return spec, wf

    # Output functions: all instrument outputs are processed here. These are passive (called from other instruments)
    # Output signal: The instrument oputput (a time-dependent signal)   
    def output_opt_signal(self):
        # Get stuff from signal
        self.freq = self.input_opt_signal_obj.freq

        # Calculate exponential attenuation
        exp_att = self.att/4.343
        total_att = np.exp(-exp_att*self.length)

        # Get waveform, and time array
        spec, wf = self.input_opt_signal()
        
        # Attenuate
        wf[1] = total_att*wf[1]
        spec[1] = total_att*spec[1]
        
        return spec, wf
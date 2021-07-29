# Simple photodetector class
# Default wavelength unit = 1 nm
# Default power unit: W
# By pfjarschel, 2021

# Imports
import os, time
import numpy as np

# File paths
main_path = os.path.dirname(os.path.realpath(__file__))
thisfile = os.path.basename(__file__)


# Responsivity parameters [zero, half, max, zero, max_resp]
INGAAS = [850.0, 950.0, 1550.0, 1700.0, 0.95]
GE = [550.0, 1000.0, 1450.0, 1650.0, 0.55]
SI = [200.0, 550.0, 900.0, 1100.0, 0.6]


# Main component class
class Photodetector():
    # Main parameters
    amp = 10e3  # V/A
    bw = 1e12  # Hz
    freq = 1e6

    # Input objects
    input_opt_signal_obj = None


    # Default functions
    def __init__(self, material=INGAAS):    
        print("Initializing photodetector")
        self.t0 = time.time()
        self.tref = self.t0
        self.material = material

    def __del__(self):
        print("Deleting photodetector object")

    # Create resp function
    def create_resp_function(self, wl_array):
        material = self.material
        max_resp = material[-1]
        half_resp = max_resp/2.0

        rough_x = [material[0] - 100.0, material[0], material[1], material[2], material[3], material[3] + 100.0]
        rough_y = [0, 0, half_resp, max_resp, 0, 0]

        resp = np.interp(wl_array, rough_x, rough_y)
        return resp

    # I/O functions
    # Set inputs: to connect the in functions to other instruments
    def set_inputs(self, opt_signal_obj):    
        self.input_opt_signal_obj = opt_signal_obj

    # Signal to detect
    def input_opt_signal(self):
        spec, wf = self.input_opt_signal_obj.output_opt_signal()
        return spec, wf

    # Output functions: all instrument outputs are processed here. These are passive (called from other instruments)
    # Output signal: The instrument oputput (a time-dependent signal)   
    def output_signal(self):      
        # Get stuff from signal
        self.freq = self.input_opt_signal_obj.freq

        # Get spectrum and waveform
        spec, wf = self.input_opt_signal()
        
        # Create responsivity function
        resp_function = self.create_resp_function(spec[0])

        # Get detected power
        detected_spec = spec[1]*resp_function
        detected_power = np.sum(detected_spec)*(spec[0][1] - spec[0][0])

        # Normalize waveform with detected power
        max_v = detected_power*self.amp

        signal = max_v*wf[1]/wf[1].max()
        
        return signal
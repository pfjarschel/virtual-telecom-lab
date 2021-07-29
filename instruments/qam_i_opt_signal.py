# Simple QAM signal output class
# Default time unit: 1 s
# Default frequency unit = 1 Hz
# Default voltage unit: V
# By pfjarschel, 2021

# Imports
import os, time
import numpy as np
import matplotlib.pyplot as plt

# File paths
main_path = os.path.dirname(os.path.realpath(__file__))
thisfile = os.path.basename(__file__)


# Main component class
class QAMIOSignal():

    # Input objects
    input_signal_obj = None
    
    # Default functions
    def __init__(self):    
        pass

    def __del__(self):
        pass


    # I/O functions
    # Set inputs: to connect the in functions to other instruments
    def set_inputs(self, signal_obj):    
        self.input_signal_obj = signal_obj
        self.freq = signal_obj.freq

    # Input functions: all parameters and instrument inputs are processed here. These are active (calls the output from other instruments)
    def input_opt_signal(self):
        spec, wf = self.input_signal_obj.output_opt_signal()
        return spec, np.real(wf)

    # Output functions: all instrument outputs are processed here. These are passive (called from other instruments)
    # Output signal: The instrument oputput (a time-dependent signal)   
    def output_opt_signal(self):
        # Get signal
        spec, wf = self.input_opt_signal()
        return spec, wf
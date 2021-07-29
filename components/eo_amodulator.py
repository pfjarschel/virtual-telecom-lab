# Simple electro-optic amplitude modulator class
# Default wavelength unit = 1 nm
# Default power unit: W
# By pfjarschel, 2021

# Imports
import os, time
import numpy as np
from scipy.fft import fft, fftfreq

# File paths
main_path = os.path.dirname(os.path.realpath(__file__))
thisfile = os.path.basename(__file__)


# Main component class
class EOAM():
    # Main parameters
    v_pi = 5.7  # V
    v_offs = -2.4  # V
    ins_loss = 6.0  # dB
    freq = 1e6

    # Input objects
    input_opt_signal_obj = None
    input_mod_signal_obj = None

    # Spec and wf holders
    spec = np.zeros([2, 100])
    wf = np.zeros([2, 100])
    mod_wf = []

    # Default functions
    def __init__(self):    
        print("Initializing EO Amplitude Modulator object")
        self.t0 = time.time()
        self.tref = self.t0

    def __del__(self):
        print("Deleting EO Amplitude Modulator object")

    # Modulate signal
    def modulate(self):
        in_spec = self.spec
        in_wf = self.wf
        m_wf = self.mod_wf
        max_pwr = in_wf[1].max()

        # Time domain
        # Get params from input obj
        time_array = self.input_mod_signal_obj.output_timearray()     

        # Create unmodulated output waveform
        out_wf_y = np.interp(time_array, in_wf[0], in_wf[1])

        # Modulate
        out_wf_y = (10**(-self.ins_loss/10.0))*out_wf_y*np.abs(np.sin(np.pi*(m_wf + self.v_offs)/self.v_pi))
        att = out_wf_y.max()/max_pwr


        # WL domain
        # Convert to freq
        out_spec_x = np.flip(3e5/in_spec[0])
        out_spec_y = np.flip(in_spec[1])

        peak_freq = out_spec_x[np.abs(out_spec_y - out_spec_y.max()).argmin()]
        r_span = out_spec_x[-1] - peak_freq
        l_span = out_spec_x[0] - peak_freq

        # Signal FFT
        nfft = 20000
        hnfft = int(nfft/2)
        interp_time = np.linspace(0, time_array[-1], nfft)
        interp_signal = np.interp(interp_time, time_array, out_wf_y)
        yf_full = (2/nfft)*np.abs(fft(interp_signal))
        yf0 = yf_full[hnfft:]
        yf0[-1] = 0
        yf1 = yf_full[:hnfft]
        yf1[0] = 0
        yf = np.concatenate([yf0, yf1])
        xf_full = fftfreq(nfft, interp_time[1] - interp_time[0]) + peak_freq*1e12
        xf0 = xf_full[hnfft:]
        xf1 = xf_full[:hnfft]
        xf = np.concatenate([xf0, xf1])

        # Get interpolated array with same values as spectrum
        yf_interp = np.interp(out_spec_x*1e12, xf, yf)

        # Add to spectrum
        out_spec_y = out_spec_y + yf_interp

        # Go back to wavelength and renormalize
        out_spec_x = np.flip(3e5/out_spec_x)
        out_spec_y = att*np.flip(out_spec_y)

        return np.array([out_spec_x, out_spec_y]), np.array([time_array, out_wf_y])


    # I/O functions
    # Set inputs: to connect the in functions to other instruments
    def set_inputs(self, opt_signal_obj, mod_signal_obj):    
        self.input_opt_signal_obj = opt_signal_obj
        self.input_mod_signal_obj = mod_signal_obj

    # Signal to modulate
    def input_opt_signal(self):
        spec, wf = self.input_opt_signal_obj.output_opt_signal()
        return spec, wf

    # Modulation signal
    def input_mod_signal(self):
        mod_wf = self.input_mod_signal_obj.output_signal()
        return mod_wf

    # Output functions: all instrument outputs are processed here. These are passive (called from other instruments)
    # Output signal: The instrument oputput (a time-dependent signal)   
    def output_opt_signal(self):
        # Get stuff from signal
        self.freq = self.input_mod_signal_obj.freq
  
        # Get spectrum, waveform and modulation signal
        self.spec, self.wf = self.input_opt_signal()
        self.mod_wf = self.input_mod_signal()
        
        out_spec, out_wf = self.modulate()
        
        return out_spec, out_wf
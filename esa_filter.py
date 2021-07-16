from instruments import signal_gen, esa
from components import filter
import sys, time
from PyQt5.QtWidgets import QApplication


# Construct application
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create instruments
    esa = esa.ESA()
    sg1 = signal_gen.SignalGenerator()
    filt = filter.Filter()
    
    # Connect parameters and instruments 
    # The ESA gets the signal generator direct output (channel 1), and the filter output (channel 2)
    esa.set_inputs(filt)
    
    # The signal generator gets the sample time and npoints when needed
    sg1.set_inputs(sampletime_obj=esa, npoints_obj=esa)

    # The filter gets the signal generator waveform, and other parameters to optimize simulation speed
    filt.set_inputs(sg1, sg1, sg1)

    # Run application
    app.exec_()

    # Exit when done
    sys.exit()
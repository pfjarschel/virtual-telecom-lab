from instruments import signal_gen, oscilloscope
import sys, time
from PyQt5.QtWidgets import QApplication


# Construct application
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create instruments
    osc = oscilloscope.Oscilloscope()
    sg1 = signal_gen.SignalGenerator()
    
    # Connect parameters and instruments 
    # The oscilloscope gets the signal generator output (1 channel)
    osc.set_inputs(sg1)
    
    # The signal generator gets the sample time and npoints when needed
    sg1.set_inputs(sampletime_obj=osc, npoints_obj=osc)

    # Run application
    app.exec_()

    # Exit when done
    sys.exit()
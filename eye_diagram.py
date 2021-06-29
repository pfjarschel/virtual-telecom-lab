from instruments import prbs_gen, oscilloscope
import sys, time
from PyQt5.QtWidgets import QApplication


# Construct application
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create instruments
    osc = oscilloscope.Oscilloscope()
    bitg1 = prbs_gen.PRBSGenerator()
    
    # Connect parameters and instruments 
    # The oscilloscope gets the signal generator direct output (channel 1), and the filter output (channel 2)
    osc.set_inputs(bitg1)
    
    # The signal generator gets the sample time and npoints when needed
    bitg1.set_inputs(sampletime_obj=osc, npoints_obj=osc)

    # Run application
    app.exec_()

    # Exit when done
    sys.exit()
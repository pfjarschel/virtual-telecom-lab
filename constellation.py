from instruments import qam_gen, oscilloscope
import sys, time
from PyQt5.QtWidgets import QApplication


# Construct application
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create instruments
    osc = oscilloscope.Oscilloscope()
    qamg = qam_gen.QAMGenerator()
    
    # Connect parameters and instruments 
    # The oscilloscope gets the prbs generator output (2 channels)
    osc.set_inputs(qamg.signal_i, qamg.signal_q)
    
    # The qam generator get the sample time and npoints when needed
    qamg.set_inputs(sampletime_obj=osc, npoints_obj=osc)

    # Run application
    app.exec_()

    # Exit when done
    sys.exit()
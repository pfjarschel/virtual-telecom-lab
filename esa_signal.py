from instruments import signal_gen, esa
import sys, time
from PyQt5.QtWidgets import QApplication


# Construct application
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create instruments
    esa1 = esa.ESA()
    sg1 = signal_gen.SignalGenerator()
    
    # Connect parameters and instruments 
    # The ESA gets the signal generator output (1 channel)
    esa1.set_inputs(sg1)
    
    # The signal generator gets the sample time and npoints when needed
    sg1.set_inputs(sampletime_obj=esa1, npoints_obj=esa1)

    # Run application
    app.exec_()

    # Exit when done
    sys.exit()
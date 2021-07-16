from instruments import prbs_gen, esa
import sys, time
from PyQt5.QtWidgets import QApplication


# Construct application
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create instruments
    esa = esa.ESA()
    bitg1 = prbs_gen.PRBSGenerator()
    
    # Connect parameters and instruments 
    # The ESA gets the prbs generator output (1 channel)
    esa.set_inputs(bitg1)
    
    # The prbs generator gets the sample time and npoints when needed
    bitg1.set_inputs(sampletime_obj=esa, npoints_obj=esa)

    # Run application
    app.exec_()

    # Exit when done
    sys.exit()
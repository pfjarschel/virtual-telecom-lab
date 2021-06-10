from instruments import signal_gen, oscilloscope
import sys, time
from PyQt5.QtWidgets import QApplication


# Construct application
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create instruments
    osc = oscilloscope.Oscilloscope()
    sg4 = signal_gen.SignalGenerator()
    sg3 = signal_gen.SignalGenerator()
    sg2 = signal_gen.SignalGenerator()
    sg1 = signal_gen.SignalGenerator()
    
    # Connect parameters and instruments 
    # The oscilloscope gets the signal generator output (4 channels)
    osc.set_inputs(sg1, sg2, sg3, sg4)
    
    # The signal generators get the sample time and npoints when needed
    sg1.set_inputs(sampletime_obj=osc, npoints_obj=osc)
    sg2.set_inputs(sampletime_obj=osc, npoints_obj=osc)
    sg3.set_inputs(sampletime_obj=osc, npoints_obj=osc)
    sg4.set_inputs(sampletime_obj=osc, npoints_obj=osc)

    # Identify each of the generators with a better window title
    sg1.setWindowTitle(f"{sg1.windowTitle()} #1")
    sg2.setWindowTitle(f"{sg2.windowTitle()} #2")
    sg3.setWindowTitle(f"{sg3.windowTitle()} #3")
    sg4.setWindowTitle(f"{sg4.windowTitle()} #4")

    # Run application
    app.exec_()

    # Exit when done
    sys.exit()
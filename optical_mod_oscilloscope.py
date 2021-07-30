from instruments import laser, signal_gen, oscilloscope
from components import photodetector, fiber, eo_amodulator
import sys, time
from PyQt5.QtWidgets import QApplication


# Construct application
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create instruments
    laser1 = laser.Laser()
    sg1 = signal_gen.SignalGenerator()
    osc = oscilloscope.Oscilloscope()
    
    # Create components
    eo_am = eo_amodulator.EOAM()
    fiber1 = fiber.Fiber(length=10.0)  # km
    pd1 = photodetector.Photodetector(material=photodetector.GE)  # GE, INGAAS, SI

    # Connect parameters, instruments, and components
    # The modulator gets the laser and signal generator outputs
    eo_am.set_inputs(laser1, sg1)

    # The fiber is between the modulator and detector
    fiber1.set_inputs(eo_am)

    # The photodetector detects the signal from the fiber
    pd1.set_inputs(fiber1)

    # The oscilloscope gets the signal from the photodetector (ch1)
    osc.set_inputs(pd1)
    
    # The signal generator gets the sample time and npoints when needed
    sg1.set_inputs(sampletime_obj=osc, npoints_obj=osc)

    # Run application
    app.exec_()

    # Exit when done
    sys.exit()
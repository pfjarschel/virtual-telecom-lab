from instruments import laser, qam_gen, oscilloscope
from components import photodetector, fiber, eo_qamodulator
import sys, time
from PyQt5.QtWidgets import QApplication


# Construct application
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create instruments
    laser1 = laser.Laser()
    qam1 = qam_gen.QAMGenerator()
    osc = oscilloscope.Oscilloscope()
    
    # Create components
    eo_qam = eo_qamodulator.EOQAM()
    fiber1 = fiber.Fiber(length=10.0)
    fiber2 = fiber.Fiber(length=10.0)  # Actually the same fiber, but we need two inputs/outputs
    pd1 = photodetector.Photodetector(material=photodetector.GE)
    pd2 = photodetector.Photodetector(material=photodetector.GE)

    # Connect parameters, instruments, and components
    # The modulator gets the laser and signal generator outputs
    eo_qam.set_inputs(laser1, qam1.signal_i, qam1.signal_q)

    # The fiber is between the modulator and detector
    fiber1.set_inputs(eo_qam.signal_i)
    fiber2.set_inputs(eo_qam.signal_q)

    # The photodetector detects the signal from the fiber
    pd1.set_inputs(fiber1)
    pd2.set_inputs(fiber2)

    # The oscilloscope gets the signal from the photodetectors (ch1, ch2)
    osc.set_inputs(pd1, pd2)
    
    # The signal generator gets the sample time and npoints when needed
    qam1.set_inputs(sampletime_obj=osc, npoints_obj=osc)

    # Run application
    app.exec_()

    # Exit when done
    sys.exit()
from instruments import laser, signal_gen, osa
from components import fiber, eo_amodulator
import sys, time
from PyQt5.QtWidgets import QApplication


# Construct application
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create instruments
    laser1 = laser.Laser()
    sg1 = signal_gen.SignalGenerator()
    osa = osa.OSA()
    
    # Create components
    eo_am = eo_amodulator.EOAM()
    fiber1 = fiber.Fiber(length=10.0)
    
    # Connect parameters, instruments, and components
    # The modulator gets the laser and signal generator outputs
    eo_am.set_inputs(laser1, sg1)

    # The fiber is between the modulator and detector
    fiber1.set_inputs(eo_am)

    # The OSA gets the signal from the fiber
    osa.set_inputs(fiber1)

    # Run application
    app.exec_()

    # Exit when done
    sys.exit()
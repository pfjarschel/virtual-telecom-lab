from instruments import otdr
from components import fiber
import numpy as np
import sys, time
from PyQt5.QtWidgets import QApplication


# Construct application
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create instruments
    otdr1 = otdr.OTDR()
    
    # Create components
    # To make things more interesting, create a fiber with random length and loss
    length = np.random.uniform(1.0, 300.0)  # km
    loss = np.random.uniform(0.1, 1.0)  # dB/km
    fiber1 = fiber.Fiber(length=length, loss=loss)
    
    # Connect parameters, instruments, and components
    # The OTDR is connected to the fiber
    otdr1.set_input_fiber(fiber1)

    # Run application
    app.exec_()

    # Exit when done
    sys.exit()
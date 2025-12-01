"""
"""

# Import modules
from core.meta import DEVELOPMENT_BUILD
from PySide6.QtWidgets import QApplication
from core.utility.run_counter import increment_counter
import sys

# Import ui objects
from core.ui.object.main_window import MainWindow


if __name__ == "__main__":
    # Create application
    application = QApplication()
    application.setStyle("Fusion")

    # Increment run counter
    if DEVELOPMENT_BUILD:
        increment_counter()

    # Create loading window
    loading_window = MainWindow()
    loading_window.show()

    # Run application
    sys.exit(application.exec())

"""
"""

# Import modules
from core.meta import DEVELOPMENT_BUILD
from PySide6.QtWidgets import QApplication
from core.utility.run_counter import increment_counter
from core.style.font_loader import load_fonts_from_directory
import sys

# Import ui objects
from core.ui.object.main_window import MainWindow

# Import resouurces
import resources.qresources.fonts
import resources.qresources.images


if __name__ == "__main__":
    # Increment run counter
    if DEVELOPMENT_BUILD:
        increment_counter()

    # Create application
    application = QApplication()
    application.setStyle("Fusion")

    # Load fonts
    load_fonts_from_directory(":/fonts")

    # Create loading window
    loading_window = MainWindow()
    loading_window.show()

    # Run application
    sys.exit(application.exec())

"""
"""

# Import modules
from typing import Optional
from PySide6.QtCore import QSize
from PySide6.QtGui import QPalette
from PySide6.QtWidgets import QWidget
from core.meta import get_full_version
from qframelesswindow import FramelessMainWindow
from core.utility.label_tools import insert_data
from core.style.style_manager import load_coloured_icon, load_stylesheet_from_file

# Import ui layouts
from core.ui.layout.main_window import Ui_main_window

# Import ui elements
from core.ui.element.widget import HidingWidget

# Import ui objects
from core.ui.object.title_bar import TitleBar


class MainWindow(FramelessMainWindow):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        self._ui = Ui_main_window()
        self._ui.setupUi(self)

        self.setTitleBar(TitleBar(self))

        self.__setup_ui()
        self.__style_ui()

        self.titleBar.raise_()
    

    def __setup_ui(self) -> None:

        # Reassign hiding class
        old_bottom_widget = self._ui.bottom_widget
        new_bottom_widget = HidingWidget(self._ui.bottom_widget.parent())

        new_bottom_widget.setObjectName(old_bottom_widget.objectName())
        new_bottom_widget.setSizePolicy(old_bottom_widget.sizePolicy())
        new_bottom_widget.setMinimumSize(old_bottom_widget.minimumSize())
        new_bottom_widget.setMaximumSize(old_bottom_widget.maximumSize())
        new_bottom_widget.setLayout(old_bottom_widget.layout())

        for child in old_bottom_widget.findChildren(QWidget):
            child.setParent(new_bottom_widget)

        self._ui.main_layout.replaceWidget(old_bottom_widget, new_bottom_widget)
        self._ui.bottom_widget = new_bottom_widget
        old_bottom_widget.deleteLater()

        # Connect close button on hide hiding widget
        self._ui.close_button.clicked.connect(self._ui.bottom_widget.hide)


        # Set version text
        insert_data(self._ui.version_label, get_full_version())

    def __style_ui(self) -> None:
        # Set stylesheet
        load_stylesheet_from_file(self, "resources/styles/dark/main_window.qss")

        # Set close button icon
        self._ui.close_button.setIconSize(QSize(25, 25))
        close_button_icon_color = self._ui.close_button.palette().color(QPalette.ColorRole.Text)
        close_button_icon = load_coloured_icon(":/images/icons/close_small.svg", close_button_icon_color)
        self._ui.close_button.setIcon(close_button_icon)

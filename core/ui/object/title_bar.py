"""
"""

# Import modules
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPalette, QIcon
from qframelesswindow import TitleBarBase
from core.style.style_manager import load_coloured_icon, load_stylesheet_from_file

# Import ui layouts
from core.ui.layout.title_bar_widget import Ui_title_bar_widget


class TitleBar(TitleBarBase):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)

        self._ui = Ui_title_bar_widget()
        self._ui.setupUi(self)

        self.__setup_ui()
        self.__style_ui()

    def __setup_ui(self) -> None:
        # Hide base title bar buttons
        self.minBtn.hide()
        self.maxBtn.hide()
        self.closeBtn.hide()

        # Connect control buttons
        self._ui.minimize_button.clicked.connect(self.window().showMinimized)
        self._ui.close_button.clicked.connect(self.window().close)

        self._ui.current_score_label.setText("0000")
        self._ui.high_score_label.setText("0000")

    def __style_ui(self) -> None:
        # Style ui
        load_stylesheet_from_file(self, "resources/styles/dark/title_bar.qss")

        # Set close button icon
        self._ui.close_button.setIconSize(QSize(30, 30))
        close_button_icon_color = self._ui.close_button.palette().color(QPalette.ColorRole.Text)
        close_button_icon = load_coloured_icon(":/images/icons/close.svg", close_button_icon_color)
        self._ui.close_button.setIcon(close_button_icon)

        # Set minimize button icon
        self._ui.minimize_button.setIconSize(QSize(30, 30))
        minimize_button_icon_color = self._ui.close_button.palette().color(QPalette.ColorRole.Text)
        minimize_button_icon = load_coloured_icon(":/images/icons/minimize.svg", minimize_button_icon_color)
        self._ui.minimize_button.setIcon(minimize_button_icon)

        # Set menu button icon
        self._ui.menu_button.setIconSize(QSize(25, 25))
        menu_button_icon_color = self._ui.close_button.palette().color(QPalette.ColorRole.Text)
        menu_button_icon = load_coloured_icon(":/images/icons/menu.svg", menu_button_icon_color)
        self._ui.menu_button.setIcon(menu_button_icon)

        # Set home button icon
        self._ui.home_button.setIconSize(self._ui.home_button.size())
        home_button_icon = QIcon(":/images/icons/icon.png")
        self._ui.home_button.setIcon(home_button_icon)


"""
"""

# Import modules
from PySide6.QtWidgets import QWidget
from qframelesswindow import TitleBarBase


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

    def __style_ui(self) -> None:
        pass


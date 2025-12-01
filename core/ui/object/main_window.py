"""
"""

# Import modules
from typing import Optional
from PySide6.QtWidgets import QWidget
from core.meta import get_full_version
from qframelesswindow import FramelessMainWindow

# Import ui layouts
from core.ui.layout.main_window import Ui_main_window

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
        self._ui.version_label.setText(get_full_version())

    def __style_ui(self) -> None:
        pass

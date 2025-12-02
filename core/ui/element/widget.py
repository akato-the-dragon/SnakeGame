""""""

# Import modules
from typing import Optional
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QPoint, Property, QPropertyAnimation, QEasingCurve, QPoint, QEvent


class HidingWidget(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        # Animation properties
        self._animation_start_value = QPoint()
        self._animation_end_value = QPoint()
        self._animation_duration = 500

        self._position_changed = False

        # Init animation
        self.__init_animation()

    def __init_animation(self) -> None:
        self._animation = QPropertyAnimation(self, b"pos")
        self._animation.setStartValue(self._animation_start_value)
        self._animation.setEndValue(self._animation_end_value)
        self._animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        self._animation.setDuration(self._animation_duration)
        self._animation.valueChanged.connect(self.update)

    def moveEvent(self, event: QEvent) -> None:
        if not self._position_changed:
            self._animation_start_value = self.pos()
            self._animation_end_value = QPoint(self.x(), self.y() + self.height())
            self.__init_animation()

            self._position_changed = True

        super().moveEvent(event)

    def hide(self) -> None:
        self._animation.finished.connect(super(HidingWidget, self).hide)
        self._animation.setDirection(QPropertyAnimation.Direction.Forward)
        self._animation.start()

    def show(self) -> None:
        self._animation.finished.disconnect(super(HidingWidget, self).hide)
        super(HidingWidget, self).show()
        self._animation.setDirection(QPropertyAnimation.Direction.Backward)
        self._animation.start()

    @Property(QPoint)
    def animation_start_value(self) -> QPoint:
        return self._animation_start_value
    
    @animation_start_value.setter
    def animation_start_value(self, value: QPoint) -> None:
        self._animation_start_value = value
    
    @Property(QPoint)
    def animation_end_value(self) -> QPoint:
        return self._animation_end_value
    
    @animation_end_value.setter
    def animation_end_value(self, value: QPoint) -> None:
        self._animation_end_value = value
    
    @Property(int)
    def animation_duration(self) -> int:
        return self._animation_duration
    
    @animation_duration.setter
    def animation_duration(self, value: int) -> None:
        self._animation_duration = value

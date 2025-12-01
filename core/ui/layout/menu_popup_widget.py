# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_popup_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_menu_popup_widget(object):
    def setupUi(self, menu_popup_widget):
        if not menu_popup_widget.objectName():
            menu_popup_widget.setObjectName(u"menu_popup_widget")
        menu_popup_widget.resize(400, 500)
        menu_popup_widget.setStyleSheet(u"")
        self.menu_popup_layout = QVBoxLayout(menu_popup_widget)
        self.menu_popup_layout.setSpacing(0)
        self.menu_popup_layout.setObjectName(u"menu_popup_layout")
        self.menu_popup_layout.setContentsMargins(0, 15, 0, 30)
        self.stackedWidget = QStackedWidget(menu_popup_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QSize(300, 0))

        self.menu_popup_layout.addWidget(self.stackedWidget, 0, Qt.AlignHCenter)


        self.retranslateUi(menu_popup_widget)

        QMetaObject.connectSlotsByName(menu_popup_widget)
    # setupUi

    def retranslateUi(self, menu_popup_widget):
        menu_popup_widget.setWindowTitle(QCoreApplication.translate("menu_popup_widget", u"Form", None))
    # retranslateUi


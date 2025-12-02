# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'map_choose_page_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_map_choose_page_widget(object):
    def setupUi(self, map_choose_page_widget):
        if not map_choose_page_widget.objectName():
            map_choose_page_widget.setObjectName(u"map_choose_page_widget")
        map_choose_page_widget.resize(300, 455)
        self.map_choose_page_layout = QVBoxLayout(map_choose_page_widget)
        self.map_choose_page_layout.setSpacing(30)
        self.map_choose_page_layout.setObjectName(u"map_choose_page_layout")
        self.map_choose_page_layout.setContentsMargins(0, 0, 0, 0)
        self.title_layout = QVBoxLayout()
        self.title_layout.setSpacing(5)
        self.title_layout.setObjectName(u"title_layout")
        self.title_label = QLabel(map_choose_page_widget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.title_layout.addWidget(self.title_label)

        self.separator_line = QFrame(map_choose_page_widget)
        self.separator_line.setObjectName(u"separator_line")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.separator_line.sizePolicy().hasHeightForWidth())
        self.separator_line.setSizePolicy(sizePolicy)
        self.separator_line.setMinimumSize(QSize(250, 0))
        self.separator_line.setFrameShape(QFrame.Shape.HLine)
        self.separator_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.title_layout.addWidget(self.separator_line, 0, Qt.AlignHCenter)


        self.map_choose_page_layout.addLayout(self.title_layout)

        self.map_list_widget = QListWidget(map_choose_page_widget)
        self.map_list_widget.setObjectName(u"map_list_widget")

        self.map_choose_page_layout.addWidget(self.map_list_widget)

        self.choosing_layout = QHBoxLayout()
        self.choosing_layout.setSpacing(10)
        self.choosing_layout.setObjectName(u"choosing_layout")
        self.choose_button = QPushButton(map_choose_page_widget)
        self.choose_button.setObjectName(u"choose_button")
        self.choose_button.setMinimumSize(QSize(0, 40))

        self.choosing_layout.addWidget(self.choose_button)

        self.back_button = QPushButton(map_choose_page_widget)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setMinimumSize(QSize(0, 40))

        self.choosing_layout.addWidget(self.back_button)

        self.choosing_layout.setStretch(0, 3)
        self.choosing_layout.setStretch(1, 2)

        self.map_choose_page_layout.addLayout(self.choosing_layout)

        self.map_choose_page_layout.setStretch(0, 1)
        self.map_choose_page_layout.setStretch(1, 3)

        self.retranslateUi(map_choose_page_widget)

        QMetaObject.connectSlotsByName(map_choose_page_widget)
    # setupUi

    def retranslateUi(self, map_choose_page_widget):
        map_choose_page_widget.setWindowTitle(QCoreApplication.translate("map_choose_page_widget", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("map_choose_page_widget", u"\u0412\u044b\u0431\u043e\u0440 \u043a\u0430\u0440\u0442\u044b", None))
        self.choose_button.setText(QCoreApplication.translate("map_choose_page_widget", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.back_button.setText(QCoreApplication.translate("map_choose_page_widget", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi


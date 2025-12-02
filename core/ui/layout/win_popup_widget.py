# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'win_popup_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_win_popup_widget(object):
    def setupUi(self, win_popup_widget):
        if not win_popup_widget.objectName():
            win_popup_widget.setObjectName(u"win_popup_widget")
        win_popup_widget.resize(450, 250)
        self.verticalLayout_2 = QVBoxLayout(win_popup_widget)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 15, 15, 30)
        self.title_layout = QVBoxLayout()
        self.title_layout.setSpacing(5)
        self.title_layout.setObjectName(u"title_layout")
        self.title_label = QLabel(win_popup_widget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.title_layout.addWidget(self.title_label)

        self.separator_line = QFrame(win_popup_widget)
        self.separator_line.setObjectName(u"separator_line")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.separator_line.sizePolicy().hasHeightForWidth())
        self.separator_line.setSizePolicy(sizePolicy)
        self.separator_line.setMinimumSize(QSize(300, 0))
        self.separator_line.setFrameShape(QFrame.Shape.HLine)
        self.separator_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.title_layout.addWidget(self.separator_line, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addLayout(self.title_layout)

        self.beat_highscore_label = QLabel(win_popup_widget)
        self.beat_highscore_label.setObjectName(u"beat_highscore_label")
        self.beat_highscore_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.beat_highscore_label)

        self.score_label = QLabel(win_popup_widget)
        self.score_label.setObjectName(u"score_label")
        self.score_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.score_label)

        self.time_label = QLabel(win_popup_widget)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.time_label)


        self.retranslateUi(win_popup_widget)

        QMetaObject.connectSlotsByName(win_popup_widget)
    # setupUi

    def retranslateUi(self, win_popup_widget):
        win_popup_widget.setWindowTitle(QCoreApplication.translate("win_popup_widget", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("win_popup_widget", u"\u0412\u044b \u0432\u044b\u0438\u0433\u0440\u0430\u043b\u0438!", None))
        self.beat_highscore_label.setText(QCoreApplication.translate("win_popup_widget", u"\u0412\u044b \u043f\u043e\u0441\u0442\u0430\u0432\u0438\u043b\u0438 \u043d\u043e\u0432\u044b\u0439 \u0440\u0435\u043a\u043e\u0440\u0434!", None))
        self.score_label.setText(QCoreApplication.translate("win_popup_widget", u"\u0421\u0447\u0451\u0442:", None))
        self.time_label.setText(QCoreApplication.translate("win_popup_widget", u"\u0412\u0440\u0435\u043c\u044f:", None))
    # retranslateUi


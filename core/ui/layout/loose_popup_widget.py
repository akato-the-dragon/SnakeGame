# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loose_popup_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_loose_popup_widget(object):
    def setupUi(self, loose_popup_widget):
        if not loose_popup_widget.objectName():
            loose_popup_widget.setObjectName(u"loose_popup_widget")
        loose_popup_widget.resize(450, 250)
        loose_popup_widget.setBaseSize(QSize(0, 0))
        self.loose_popup_layout = QVBoxLayout(loose_popup_widget)
        self.loose_popup_layout.setSpacing(5)
        self.loose_popup_layout.setObjectName(u"loose_popup_layout")
        self.loose_popup_layout.setContentsMargins(10, 15, 15, 30)
        self.title_layout = QVBoxLayout()
        self.title_layout.setSpacing(5)
        self.title_layout.setObjectName(u"title_layout")
        self.title_label = QLabel(loose_popup_widget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.title_layout.addWidget(self.title_label)

        self.separator_line = QFrame(loose_popup_widget)
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


        self.loose_popup_layout.addLayout(self.title_layout)

        self.beat_highscore_label = QLabel(loose_popup_widget)
        self.beat_highscore_label.setObjectName(u"beat_highscore_label")
        self.beat_highscore_label.setAlignment(Qt.AlignCenter)

        self.loose_popup_layout.addWidget(self.beat_highscore_label)

        self.score_label = QLabel(loose_popup_widget)
        self.score_label.setObjectName(u"score_label")
        self.score_label.setAlignment(Qt.AlignCenter)

        self.loose_popup_layout.addWidget(self.score_label)

        self.time_label = QLabel(loose_popup_widget)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setAlignment(Qt.AlignCenter)

        self.loose_popup_layout.addWidget(self.time_label)


        self.retranslateUi(loose_popup_widget)

        QMetaObject.connectSlotsByName(loose_popup_widget)
    # setupUi

    def retranslateUi(self, loose_popup_widget):
        loose_popup_widget.setWindowTitle(QCoreApplication.translate("loose_popup_widget", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("loose_popup_widget", u"\u0412\u044b \u043f\u0440\u043e\u0438\u0433\u0440\u0430\u043b\u0438!", None))
        self.beat_highscore_label.setText(QCoreApplication.translate("loose_popup_widget", u"\u0412\u044b \u043c\u043e\u0433\u043b\u0438 \u043f\u043e\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u0440\u0435\u043a\u043e\u0440\u0434!", None))
        self.score_label.setText(QCoreApplication.translate("loose_popup_widget", u"\u0421\u0447\u0451\u0442:", None))
        self.time_label.setText(QCoreApplication.translate("loose_popup_widget", u"\u0412\u0440\u0435\u043c\u044f:", None))
    # retranslateUi


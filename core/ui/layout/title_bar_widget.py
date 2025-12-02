# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'title_bar_widget.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_title_bar_widget(object):
    def setupUi(self, title_bar_widget):
        if not title_bar_widget.objectName():
            title_bar_widget.setObjectName(u"title_bar_widget")
        title_bar_widget.resize(720, 50)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(title_bar_widget.sizePolicy().hasHeightForWidth())
        title_bar_widget.setSizePolicy(sizePolicy)
        title_bar_widget.setMinimumSize(QSize(0, 50))
        title_bar_widget.setMaximumSize(QSize(16777215, 50))
        self.title_bar_layout = QHBoxLayout(title_bar_widget)
        self.title_bar_layout.setSpacing(10)
        self.title_bar_layout.setObjectName(u"title_bar_layout")
        self.title_bar_layout.setContentsMargins(0, 0, 0, 0)
        self.shadow_widget = QWidget(title_bar_widget)
        self.shadow_widget.setObjectName(u"shadow_widget")
        self.shadow_layout = QHBoxLayout(self.shadow_widget)
        self.shadow_layout.setSpacing(10)
        self.shadow_layout.setObjectName(u"shadow_layout")
        self.shadow_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout = QHBoxLayout()
        self.main_layout.setSpacing(5)
        self.main_layout.setObjectName(u"main_layout")
        self.home_button = QPushButton(self.shadow_widget)
        self.home_button.setObjectName(u"home_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.home_button.sizePolicy().hasHeightForWidth())
        self.home_button.setSizePolicy(sizePolicy1)
        self.home_button.setMinimumSize(QSize(50, 50))
        self.home_button.setMaximumSize(QSize(50, 50))

        self.main_layout.addWidget(self.home_button)

        self.score_layout = QVBoxLayout()
        self.score_layout.setSpacing(0)
        self.score_layout.setObjectName(u"score_layout")
        self.score_layout.setContentsMargins(-1, 5, -1, -1)
        self.current_score_label = QLabel(self.shadow_widget)
        self.current_score_label.setObjectName(u"current_score_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.current_score_label.sizePolicy().hasHeightForWidth())
        self.current_score_label.setSizePolicy(sizePolicy2)
        self.current_score_label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.score_layout.addWidget(self.current_score_label)

        self.high_score_label = QLabel(self.shadow_widget)
        self.high_score_label.setObjectName(u"high_score_label")
        sizePolicy2.setHeightForWidth(self.high_score_label.sizePolicy().hasHeightForWidth())
        self.high_score_label.setSizePolicy(sizePolicy2)
        self.high_score_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.score_layout.addWidget(self.high_score_label)


        self.main_layout.addLayout(self.score_layout)


        self.shadow_layout.addLayout(self.main_layout)

        self.menu_button = QPushButton(self.shadow_widget)
        self.menu_button.setObjectName(u"menu_button")
        sizePolicy1.setHeightForWidth(self.menu_button.sizePolicy().hasHeightForWidth())
        self.menu_button.setSizePolicy(sizePolicy1)
        self.menu_button.setMinimumSize(QSize(35, 35))
        self.menu_button.setMaximumSize(QSize(35, 35))

        self.shadow_layout.addWidget(self.menu_button)

        self.separator_line = QFrame(self.shadow_widget)
        self.separator_line.setObjectName(u"separator_line")
        sizePolicy1.setHeightForWidth(self.separator_line.sizePolicy().hasHeightForWidth())
        self.separator_line.setSizePolicy(sizePolicy1)
        self.separator_line.setMinimumSize(QSize(0, 40))
        self.separator_line.setMaximumSize(QSize(16777215, 40))
        self.separator_line.setFrameShape(QFrame.Shape.VLine)
        self.separator_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.shadow_layout.addWidget(self.separator_line)

        self.control_layout = QHBoxLayout()
        self.control_layout.setSpacing(0)
        self.control_layout.setObjectName(u"control_layout")
        self.minimize_button = QPushButton(self.shadow_widget)
        self.minimize_button.setObjectName(u"minimize_button")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.minimize_button.sizePolicy().hasHeightForWidth())
        self.minimize_button.setSizePolicy(sizePolicy3)
        self.minimize_button.setMinimumSize(QSize(40, 0))
        self.minimize_button.setMaximumSize(QSize(40, 16777215))

        self.control_layout.addWidget(self.minimize_button)

        self.close_button = QPushButton(self.shadow_widget)
        self.close_button.setObjectName(u"close_button")
        sizePolicy3.setHeightForWidth(self.close_button.sizePolicy().hasHeightForWidth())
        self.close_button.setSizePolicy(sizePolicy3)
        self.close_button.setMinimumSize(QSize(40, 0))
        self.close_button.setMaximumSize(QSize(40, 16777215))

        self.control_layout.addWidget(self.close_button)


        self.shadow_layout.addLayout(self.control_layout)


        self.title_bar_layout.addWidget(self.shadow_widget)


        self.retranslateUi(title_bar_widget)

        QMetaObject.connectSlotsByName(title_bar_widget)
    # setupUi

    def retranslateUi(self, title_bar_widget):
        title_bar_widget.setWindowTitle(QCoreApplication.translate("title_bar_widget", u"Form", None))
        self.home_button.setText("")
        self.current_score_label.setText("")
        self.high_score_label.setText("")
        self.menu_button.setText("")
        self.minimize_button.setText("")
        self.close_button.setText("")
    # retranslateUi


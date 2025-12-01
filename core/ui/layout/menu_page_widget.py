# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_page_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_menu_page_widget(object):
    def setupUi(self, menu_page_widget):
        if not menu_page_widget.objectName():
            menu_page_widget.setObjectName(u"menu_page_widget")
        menu_page_widget.resize(300, 455)
        self.menu_page_layout = QVBoxLayout(menu_page_widget)
        self.menu_page_layout.setSpacing(45)
        self.menu_page_layout.setObjectName(u"menu_page_layout")
        self.menu_page_layout.setContentsMargins(0, 0, 0, 0)
        self.title_layout = QVBoxLayout()
        self.title_layout.setSpacing(5)
        self.title_layout.setObjectName(u"title_layout")
        self.title_label = QLabel(menu_page_widget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.title_layout.addWidget(self.title_label)

        self.separator_line = QFrame(menu_page_widget)
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


        self.menu_page_layout.addLayout(self.title_layout)

        self.buttons_layout = QVBoxLayout()
        self.buttons_layout.setSpacing(10)
        self.buttons_layout.setObjectName(u"buttons_layout")
        self.buttons_layout.setContentsMargins(30, -1, 30, -1)
        self.continue_button = QPushButton(menu_page_widget)
        self.continue_button.setObjectName(u"continue_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.continue_button.sizePolicy().hasHeightForWidth())
        self.continue_button.setSizePolicy(sizePolicy1)

        self.buttons_layout.addWidget(self.continue_button)

        self.restart_button = QPushButton(menu_page_widget)
        self.restart_button.setObjectName(u"restart_button")
        sizePolicy1.setHeightForWidth(self.restart_button.sizePolicy().hasHeightForWidth())
        self.restart_button.setSizePolicy(sizePolicy1)

        self.buttons_layout.addWidget(self.restart_button)

        self.choose_map_button = QPushButton(menu_page_widget)
        self.choose_map_button.setObjectName(u"choose_map_button")
        sizePolicy1.setHeightForWidth(self.choose_map_button.sizePolicy().hasHeightForWidth())
        self.choose_map_button.setSizePolicy(sizePolicy1)

        self.buttons_layout.addWidget(self.choose_map_button)

        self.settings_button = QPushButton(menu_page_widget)
        self.settings_button.setObjectName(u"settings_button")
        sizePolicy1.setHeightForWidth(self.settings_button.sizePolicy().hasHeightForWidth())
        self.settings_button.setSizePolicy(sizePolicy1)

        self.buttons_layout.addWidget(self.settings_button)

        self.exit_buitton = QPushButton(menu_page_widget)
        self.exit_buitton.setObjectName(u"exit_buitton")
        sizePolicy1.setHeightForWidth(self.exit_buitton.sizePolicy().hasHeightForWidth())
        self.exit_buitton.setSizePolicy(sizePolicy1)

        self.buttons_layout.addWidget(self.exit_buitton)


        self.menu_page_layout.addLayout(self.buttons_layout)

        self.menu_page_layout.setStretch(0, 1)
        self.menu_page_layout.setStretch(1, 4)

        self.retranslateUi(menu_page_widget)

        QMetaObject.connectSlotsByName(menu_page_widget)
    # setupUi

    def retranslateUi(self, menu_page_widget):
        menu_page_widget.setWindowTitle(QCoreApplication.translate("menu_page_widget", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("menu_page_widget", u"\u041c\u0435\u043d\u044e", None))
        self.continue_button.setText(QCoreApplication.translate("menu_page_widget", u"\u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u044c", None))
        self.restart_button.setText(QCoreApplication.translate("menu_page_widget", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0437\u0430\u043d\u043e\u0432\u043e", None))
        self.choose_map_button.setText(QCoreApplication.translate("menu_page_widget", u"\u0412\u044b\u0431\u043e\u0440 \u043a\u0430\u0440\u0442\u044b", None))
        self.settings_button.setText(QCoreApplication.translate("menu_page_widget", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.exit_buitton.setText(QCoreApplication.translate("menu_page_widget", u"\u0412\u044b\u0445\u043e\u0434", None))
    # retranslateUi


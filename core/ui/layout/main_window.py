# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(720, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(sizePolicy)
        main_window.setMinimumSize(QSize(720, 800))
        main_window.setMaximumSize(QSize(720, 800))
        self.main_widget = QWidget(main_window)
        self.main_widget.setObjectName(u"main_widget")
        self.main_layout = QVBoxLayout(self.main_widget)
        self.main_layout.setSpacing(0)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.game_widget = QWidget(self.main_widget)
        self.game_widget.setObjectName(u"game_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.game_widget.sizePolicy().hasHeightForWidth())
        self.game_widget.setSizePolicy(sizePolicy1)
        self.game_layout = QVBoxLayout(self.game_widget)
        self.game_layout.setSpacing(0)
        self.game_layout.setObjectName(u"game_layout")
        self.game_layout.setContentsMargins(0, 0, 0, 0)

        self.main_layout.addWidget(self.game_widget)

        self.bottom_widget = QWidget(self.main_widget)
        self.bottom_widget.setObjectName(u"bottom_widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.bottom_widget.sizePolicy().hasHeightForWidth())
        self.bottom_widget.setSizePolicy(sizePolicy2)
        self.bottom_widget.setMinimumSize(QSize(0, 30))
        self.bottom_widget.setMaximumSize(QSize(16777215, 30))
        self.bottom_layout = QHBoxLayout(self.bottom_widget)
        self.bottom_layout.setSpacing(10)
        self.bottom_layout.setObjectName(u"bottom_layout")
        self.bottom_layout.setContentsMargins(5, 0, 0, 0)
        self.version_label = QLabel(self.bottom_widget)
        self.version_label.setObjectName(u"version_label")

        self.bottom_layout.addWidget(self.version_label)

        self.update_widget = QWidget(self.bottom_widget)
        self.update_widget.setObjectName(u"update_widget")
        self.update_layout = QHBoxLayout(self.update_widget)
        self.update_layout.setSpacing(5)
        self.update_layout.setObjectName(u"update_layout")
        self.update_layout.setContentsMargins(5, 0, 0, 0)
        self.update_label = QLabel(self.update_widget)
        self.update_label.setObjectName(u"update_label")

        self.update_layout.addWidget(self.update_label)

        self.update_button = QPushButton(self.update_widget)
        self.update_button.setObjectName(u"update_button")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.update_button.sizePolicy().hasHeightForWidth())
        self.update_button.setSizePolicy(sizePolicy3)

        self.update_layout.addWidget(self.update_button)

        self.close_layout = QHBoxLayout()
        self.close_layout.setSpacing(0)
        self.close_layout.setObjectName(u"close_layout")
        self.close_layout.setContentsMargins(15, -1, 5, -1)
        self.dont_show_again_check_box = QCheckBox(self.update_widget)
        self.dont_show_again_check_box.setObjectName(u"dont_show_again_check_box")

        self.close_layout.addWidget(self.dont_show_again_check_box)

        self.close_button = QPushButton(self.update_widget)
        self.close_button.setObjectName(u"close_button")
        sizePolicy.setHeightForWidth(self.close_button.sizePolicy().hasHeightForWidth())
        self.close_button.setSizePolicy(sizePolicy)
        self.close_button.setMinimumSize(QSize(25, 25))
        self.close_button.setMaximumSize(QSize(25, 25))

        self.close_layout.addWidget(self.close_button)


        self.update_layout.addLayout(self.close_layout)


        self.bottom_layout.addWidget(self.update_widget)


        self.main_layout.addWidget(self.bottom_widget)

        main_window.setCentralWidget(self.main_widget)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"MainWindow", None))
        self.version_label.setText(QCoreApplication.translate("main_window", u"<version>", None))
        self.update_label.setText(QCoreApplication.translate("main_window", u"\u0414\u043e\u0441\u0442\u0443\u043f\u043d\u043e \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435!", None))
        self.update_button.setText(QCoreApplication.translate("main_window", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.dont_show_again_check_box.setText(QCoreApplication.translate("main_window", u"\u041d\u0435 \u043f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u0441\u043d\u043e\u0432\u0430", None))
        self.close_button.setText("")
    # retranslateUi


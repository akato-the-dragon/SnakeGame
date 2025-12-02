# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_page_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSlider, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_settings_page_widget(object):
    def setupUi(self, settings_page_widget):
        if not settings_page_widget.objectName():
            settings_page_widget.setObjectName(u"settings_page_widget")
        settings_page_widget.resize(300, 455)
        self.settings_page_layout = QVBoxLayout(settings_page_widget)
        self.settings_page_layout.setSpacing(15)
        self.settings_page_layout.setObjectName(u"settings_page_layout")
        self.settings_page_layout.setContentsMargins(0, 0, 0, 0)
        self.title_layout = QVBoxLayout()
        self.title_layout.setSpacing(5)
        self.title_layout.setObjectName(u"title_layout")
        self.title_label = QLabel(settings_page_widget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.title_layout.addWidget(self.title_label)

        self.separator_line = QFrame(settings_page_widget)
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


        self.settings_page_layout.addLayout(self.title_layout)

        self.scroll_area = QScrollArea(settings_page_widget)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area_content = QWidget()
        self.scroll_area_content.setObjectName(u"scroll_area_content")
        self.scroll_area_content.setGeometry(QRect(0, 0, 283, 670))
        self.scroll_area_content_layout = QVBoxLayout(self.scroll_area_content)
        self.scroll_area_content_layout.setSpacing(15)
        self.scroll_area_content_layout.setObjectName(u"scroll_area_content_layout")
        self.scroll_area_content_layout.setContentsMargins(10, 10, 10, 10)
        self.general_group_box = QGroupBox(self.scroll_area_content)
        self.general_group_box.setObjectName(u"general_group_box")
        self.general_combo_box_layout = QGridLayout(self.general_group_box)
        self.general_combo_box_layout.setObjectName(u"general_combo_box_layout")
        self.general_combo_box_layout.setHorizontalSpacing(5)
        self.general_combo_box_layout.setVerticalSpacing(10)
        self.general_combo_box_layout.setContentsMargins(5, 5, 5, 5)
        self.sounds_label = QLabel(self.general_group_box)
        self.sounds_label.setObjectName(u"sounds_label")

        self.general_combo_box_layout.addWidget(self.sounds_label, 3, 0, 1, 1)

        self.theme_label = QLabel(self.general_group_box)
        self.theme_label.setObjectName(u"theme_label")

        self.general_combo_box_layout.addWidget(self.theme_label, 0, 0, 1, 1)

        self.language_combo_box = QComboBox(self.general_group_box)
        self.language_combo_box.setObjectName(u"language_combo_box")

        self.general_combo_box_layout.addWidget(self.language_combo_box, 1, 1, 1, 1)

        self.theme_combo_box = QComboBox(self.general_group_box)
        self.theme_combo_box.setObjectName(u"theme_combo_box")

        self.general_combo_box_layout.addWidget(self.theme_combo_box, 0, 1, 1, 1)

        self.music_label = QLabel(self.general_group_box)
        self.music_label.setObjectName(u"music_label")

        self.general_combo_box_layout.addWidget(self.music_label, 2, 0, 1, 1)

        self.music_slider = QSlider(self.general_group_box)
        self.music_slider.setObjectName(u"music_slider")
        self.music_slider.setMaximum(100)
        self.music_slider.setSingleStep(1)
        self.music_slider.setOrientation(Qt.Horizontal)

        self.general_combo_box_layout.addWidget(self.music_slider, 2, 1, 1, 1)

        self.sounds_slider = QSlider(self.general_group_box)
        self.sounds_slider.setObjectName(u"sounds_slider")
        self.sounds_slider.setMaximum(100)
        self.sounds_slider.setOrientation(Qt.Horizontal)

        self.general_combo_box_layout.addWidget(self.sounds_slider, 3, 1, 1, 1)

        self.language_label = QLabel(self.general_group_box)
        self.language_label.setObjectName(u"language_label")

        self.general_combo_box_layout.addWidget(self.language_label, 1, 0, 1, 1)

        self.general_combo_box_layout.setColumnStretch(0, 1)
        self.general_combo_box_layout.setColumnStretch(1, 2)

        self.scroll_area_content_layout.addWidget(self.general_group_box)

        self.gameplay_group_box = QGroupBox(self.scroll_area_content)
        self.gameplay_group_box.setObjectName(u"gameplay_group_box")
        self.gameplay_group_box_layout = QGridLayout(self.gameplay_group_box)
        self.gameplay_group_box_layout.setObjectName(u"gameplay_group_box_layout")
        self.gameplay_group_box_layout.setHorizontalSpacing(5)
        self.gameplay_group_box_layout.setVerticalSpacing(10)
        self.gameplay_group_box_layout.setContentsMargins(5, 5, 5, 5)
        self.deadly_borders_label = QLabel(self.gameplay_group_box)
        self.deadly_borders_label.setObjectName(u"deadly_borders_label")

        self.gameplay_group_box_layout.addWidget(self.deadly_borders_label, 12, 0, 1, 1)

        self.score_multiplier_label = QLabel(self.gameplay_group_box)
        self.score_multiplier_label.setObjectName(u"score_multiplier_label")

        self.gameplay_group_box_layout.addWidget(self.score_multiplier_label, 1, 0, 1, 1)

        self.score_multiplier_line_edit = QLineEdit(self.gameplay_group_box)
        self.score_multiplier_line_edit.setObjectName(u"score_multiplier_line_edit")
        self.score_multiplier_line_edit.setReadOnly(True)

        self.gameplay_group_box_layout.addWidget(self.score_multiplier_line_edit, 1, 1, 1, 1)

        self.deadly_borders_check_box = QCheckBox(self.gameplay_group_box)
        self.deadly_borders_check_box.setObjectName(u"deadly_borders_check_box")

        self.gameplay_group_box_layout.addWidget(self.deadly_borders_check_box, 12, 1, 1, 1)

        self.invert_x_check_box = QCheckBox(self.gameplay_group_box)
        self.invert_x_check_box.setObjectName(u"invert_x_check_box")

        self.gameplay_group_box_layout.addWidget(self.invert_x_check_box, 13, 1, 1, 1)

        self.speed_label = QLabel(self.gameplay_group_box)
        self.speed_label.setObjectName(u"speed_label")

        self.gameplay_group_box_layout.addWidget(self.speed_label, 3, 0, 1, 1)

        self.speed_spin_box = QSpinBox(self.gameplay_group_box)
        self.speed_spin_box.setObjectName(u"speed_spin_box")

        self.gameplay_group_box_layout.addWidget(self.speed_spin_box, 3, 1, 1, 1)

        self.invert_y_label = QLabel(self.gameplay_group_box)
        self.invert_y_label.setObjectName(u"invert_y_label")

        self.gameplay_group_box_layout.addWidget(self.invert_y_label, 14, 0, 1, 1)

        self.invert_y_check_box = QCheckBox(self.gameplay_group_box)
        self.invert_y_check_box.setObjectName(u"invert_y_check_box")

        self.gameplay_group_box_layout.addWidget(self.invert_y_check_box, 14, 1, 1, 1)

        self.speed_up_multiplier_spin_box = QDoubleSpinBox(self.gameplay_group_box)
        self.speed_up_multiplier_spin_box.setObjectName(u"speed_up_multiplier_spin_box")

        self.gameplay_group_box_layout.addWidget(self.speed_up_multiplier_spin_box, 10, 1, 1, 1)

        self.invert_x_label = QLabel(self.gameplay_group_box)
        self.invert_x_label.setObjectName(u"invert_x_label")

        self.gameplay_group_box_layout.addWidget(self.invert_x_label, 13, 0, 1, 1)

        self.food_duration_spin_box = QDoubleSpinBox(self.gameplay_group_box)
        self.food_duration_spin_box.setObjectName(u"food_duration_spin_box")

        self.gameplay_group_box_layout.addWidget(self.food_duration_spin_box, 5, 1, 1, 1)

        self.super_food_duration_label = QLabel(self.gameplay_group_box)
        self.super_food_duration_label.setObjectName(u"super_food_duration_label")

        self.gameplay_group_box_layout.addWidget(self.super_food_duration_label, 8, 0, 1, 1)

        self.super_food_strenght_spin_box = QSpinBox(self.gameplay_group_box)
        self.super_food_strenght_spin_box.setObjectName(u"super_food_strenght_spin_box")

        self.gameplay_group_box_layout.addWidget(self.super_food_strenght_spin_box, 6, 1, 1, 1)

        self.food_strenght_label = QLabel(self.gameplay_group_box)
        self.food_strenght_label.setObjectName(u"food_strenght_label")

        self.gameplay_group_box_layout.addWidget(self.food_strenght_label, 4, 0, 1, 1)

        self.food_duration_label = QLabel(self.gameplay_group_box)
        self.food_duration_label.setObjectName(u"food_duration_label")

        self.gameplay_group_box_layout.addWidget(self.food_duration_label, 5, 0, 1, 1)

        self.start_lenght_label = QLabel(self.gameplay_group_box)
        self.start_lenght_label.setObjectName(u"start_lenght_label")

        self.gameplay_group_box_layout.addWidget(self.start_lenght_label, 2, 0, 1, 1)

        self.start_lenght_spin_box = QSpinBox(self.gameplay_group_box)
        self.start_lenght_spin_box.setObjectName(u"start_lenght_spin_box")

        self.gameplay_group_box_layout.addWidget(self.start_lenght_spin_box, 2, 1, 1, 1)

        self.super_food_strenght_label = QLabel(self.gameplay_group_box)
        self.super_food_strenght_label.setObjectName(u"super_food_strenght_label")

        self.gameplay_group_box_layout.addWidget(self.super_food_strenght_label, 6, 0, 1, 1)

        self.food_strenght_spin_box = QSpinBox(self.gameplay_group_box)
        self.food_strenght_spin_box.setObjectName(u"food_strenght_spin_box")

        self.gameplay_group_box_layout.addWidget(self.food_strenght_spin_box, 4, 1, 1, 1)

        self.speed_up_label = QLabel(self.gameplay_group_box)
        self.speed_up_label.setObjectName(u"speed_up_label")

        self.gameplay_group_box_layout.addWidget(self.speed_up_label, 9, 0, 1, 1)

        self.speed_up_multiplier_label = QLabel(self.gameplay_group_box)
        self.speed_up_multiplier_label.setObjectName(u"speed_up_multiplier_label")

        self.gameplay_group_box_layout.addWidget(self.speed_up_multiplier_label, 10, 0, 1, 1)

        self.speed_up_check_box = QCheckBox(self.gameplay_group_box)
        self.speed_up_check_box.setObjectName(u"speed_up_check_box")

        self.gameplay_group_box_layout.addWidget(self.speed_up_check_box, 9, 1, 1, 1)

        self.super_food_frequency_spin_box = QSpinBox(self.gameplay_group_box)
        self.super_food_frequency_spin_box.setObjectName(u"super_food_frequency_spin_box")

        self.gameplay_group_box_layout.addWidget(self.super_food_frequency_spin_box, 7, 1, 1, 1)

        self.super_food_duration_spin_box = QDoubleSpinBox(self.gameplay_group_box)
        self.super_food_duration_spin_box.setObjectName(u"super_food_duration_spin_box")

        self.gameplay_group_box_layout.addWidget(self.super_food_duration_spin_box, 8, 1, 1, 1)

        self.super_food_frequency_label = QLabel(self.gameplay_group_box)
        self.super_food_frequency_label.setObjectName(u"super_food_frequency_label")

        self.gameplay_group_box_layout.addWidget(self.super_food_frequency_label, 7, 0, 1, 1)

        self.safe_mode_label = QLabel(self.gameplay_group_box)
        self.safe_mode_label.setObjectName(u"safe_mode_label")

        self.gameplay_group_box_layout.addWidget(self.safe_mode_label, 11, 0, 1, 1)

        self.safe_mode_check_box = QCheckBox(self.gameplay_group_box)
        self.safe_mode_check_box.setObjectName(u"safe_mode_check_box")

        self.gameplay_group_box_layout.addWidget(self.safe_mode_check_box, 11, 1, 1, 1)


        self.scroll_area_content_layout.addWidget(self.gameplay_group_box)

        self.other_group_box = QGroupBox(self.scroll_area_content)
        self.other_group_box.setObjectName(u"other_group_box")
        self.other_group_box_layout = QGridLayout(self.other_group_box)
        self.other_group_box_layout.setObjectName(u"other_group_box_layout")
        self.other_group_box_layout.setHorizontalSpacing(5)
        self.other_group_box_layout.setVerticalSpacing(10)
        self.other_group_box_layout.setContentsMargins(5, 5, 5, 5)
        self.reset_score_label = QLabel(self.other_group_box)
        self.reset_score_label.setObjectName(u"reset_score_label")
        self.reset_score_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.other_group_box_layout.addWidget(self.reset_score_label, 1, 0, 1, 1)

        self.reset_settings_button = QPushButton(self.other_group_box)
        self.reset_settings_button.setObjectName(u"reset_settings_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.reset_settings_button.sizePolicy().hasHeightForWidth())
        self.reset_settings_button.setSizePolicy(sizePolicy1)

        self.other_group_box_layout.addWidget(self.reset_settings_button, 0, 1, 1, 1)

        self.reset_settings_label = QLabel(self.other_group_box)
        self.reset_settings_label.setObjectName(u"reset_settings_label")
        self.reset_settings_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.other_group_box_layout.addWidget(self.reset_settings_label, 0, 0, 1, 1)

        self.reset_score_button = QPushButton(self.other_group_box)
        self.reset_score_button.setObjectName(u"reset_score_button")
        sizePolicy1.setHeightForWidth(self.reset_score_button.sizePolicy().hasHeightForWidth())
        self.reset_score_button.setSizePolicy(sizePolicy1)

        self.other_group_box_layout.addWidget(self.reset_score_button, 1, 1, 1, 1)

        self.other_group_box_layout.setColumnStretch(0, 1)
        self.other_group_box_layout.setColumnStretch(1, 2)

        self.scroll_area_content_layout.addWidget(self.other_group_box)

        self.scroll_area.setWidget(self.scroll_area_content)

        self.settings_page_layout.addWidget(self.scroll_area)

        self.choosing_layout = QHBoxLayout()
        self.choosing_layout.setSpacing(10)
        self.choosing_layout.setObjectName(u"choosing_layout")
        self.apply_button = QPushButton(settings_page_widget)
        self.apply_button.setObjectName(u"apply_button")
        self.apply_button.setMinimumSize(QSize(0, 40))

        self.choosing_layout.addWidget(self.apply_button)

        self.back_button = QPushButton(settings_page_widget)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setMinimumSize(QSize(0, 40))

        self.choosing_layout.addWidget(self.back_button)

        self.choosing_layout.setStretch(0, 3)
        self.choosing_layout.setStretch(1, 2)

        self.settings_page_layout.addLayout(self.choosing_layout)

        self.settings_page_layout.setStretch(0, 1)
        self.settings_page_layout.setStretch(1, 4)

        self.retranslateUi(settings_page_widget)

        QMetaObject.connectSlotsByName(settings_page_widget)
    # setupUi

    def retranslateUi(self, settings_page_widget):
        settings_page_widget.setWindowTitle(QCoreApplication.translate("settings_page_widget", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("settings_page_widget", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.general_group_box.setTitle(QCoreApplication.translate("settings_page_widget", u"\u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435", None))
        self.sounds_label.setText(QCoreApplication.translate("settings_page_widget", u"\u0417\u0432\u0443\u043a\u0438:", None))
        self.theme_label.setText(QCoreApplication.translate("settings_page_widget", u"\u0422\u0435\u043c\u0430:", None))
        self.music_label.setText(QCoreApplication.translate("settings_page_widget", u"\u041c\u0443\u0437\u044b\u043a\u0430:", None))
        self.language_label.setText(QCoreApplication.translate("settings_page_widget", u"\u042f\u0437\u044b\u043a:", None))
        self.gameplay_group_box.setTitle(QCoreApplication.translate("settings_page_widget", u"\u0413\u0435\u0439\u043c\u043f\u043b\u0435\u0439", None))
        self.deadly_borders_label.setText(QCoreApplication.translate("settings_page_widget", u"\u0421\u043c\u0435\u0440\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u0433\u0440\u0430\u043d\u0438\u0446\u044b:", None))
        self.score_multiplier_label.setText(QCoreApplication.translate("settings_page_widget", u"\u041c\u043d\u043e\u0436\u0438\u0442\u0435\u043b\u044c \u043e\u0447\u043a\u043e\u0432:", None))
        self.deadly_borders_check_box.setText("")
        self.invert_x_check_box.setText("")
        self.speed_label.setText(QCoreApplication.translate("settings_page_widget", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c:", None))
        self.invert_y_label.setText(QCoreApplication.translate("settings_page_widget", u"\u0418\u043d\u0432\u0435\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u043e \u043e\u0441\u0438 y:", None))
        self.invert_y_check_box.setText("")
        self.invert_x_label.setText(QCoreApplication.translate("settings_page_widget", u"\u0418\u043d\u0432\u0435\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u043e \u043e\u0441\u0438 x:", None))
        self.super_food_duration_label.setText(QCoreApplication.translate("settings_page_widget", u"\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0441\u0443\u043f\u0435\u0440 \u0435\u0434\u044b:", None))
        self.food_strenght_label.setText(QCoreApplication.translate("settings_page_widget", u"\u0421\u0438\u043b\u0430 \u0435\u0434\u044b:", None))
        self.food_duration_label.setText(QCoreApplication.translate("settings_page_widget", u"\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0435\u0434\u044b:", None))
        self.start_lenght_label.setText(QCoreApplication.translate("settings_page_widget", u"\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u0430\u044f \u0434\u043b\u0438\u043d\u0430:", None))
        self.super_food_strenght_label.setText(QCoreApplication.translate("settings_page_widget", u"\u0421\u0438\u043b\u0430 \u0441\u0443\u043f\u0435\u0440 \u0435\u0434\u044b:", None))
        self.speed_up_label.setText(QCoreApplication.translate("settings_page_widget", u"\u0423\u0432\u0438\u043b\u0435\u0447\u0435\u043d\u0438\u0435 \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u0438:", None))
        self.speed_up_multiplier_label.setText(QCoreApplication.translate("settings_page_widget", u"\u041c\u043d\u043e\u0436\u0438\u0442\u0435\u043b\u044c \u0443\u0441\u043a\u043e\u0440\u0435\u043d\u0438\u044f:", None))
        self.speed_up_check_box.setText("")
        self.super_food_frequency_label.setText(QCoreApplication.translate("settings_page_widget", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430 \u0441\u0443\u043f\u0435\u0440 \u0435\u0434\u044b:", None))
        self.safe_mode_label.setText(QCoreApplication.translate("settings_page_widget", u"\u0411\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u044b\u0439 \u0440\u0435\u0436\u0438\u043c:", None))
        self.safe_mode_check_box.setText("")
        self.other_group_box.setTitle(QCoreApplication.translate("settings_page_widget", u"\u041e\u0441\u0442\u0430\u043b\u044c\u043d\u043e\u0435", None))
        self.reset_score_label.setText(QCoreApplication.translate("settings_page_widget", u"\u0421\u0431\u0440\u043e\u0441 \u0441\u0447\u0451\u0442\u0430:", None))
        self.reset_settings_button.setText(QCoreApplication.translate("settings_page_widget", u"\u0421\u0431\u0440\u043e\u0441", None))
        self.reset_settings_label.setText(QCoreApplication.translate("settings_page_widget", u"\u0421\u0431\u0440\u043e\u0441 \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043a:", None))
        self.reset_score_button.setText(QCoreApplication.translate("settings_page_widget", u"\u0421\u0431\u0440\u043e\u0441", None))
        self.apply_button.setText(QCoreApplication.translate("settings_page_widget", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.back_button.setText(QCoreApplication.translate("settings_page_widget", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi


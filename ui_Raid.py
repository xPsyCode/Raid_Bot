# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_RaidKhcGEe.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(739, 500)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setStyleSheet(u"QPushButton{\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"	font: 9pt \"Comic Sans MS\";\n"
"}\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.level_Btn = QPushButton(self.frame)
        self.level_Btn.setObjectName(u"level_Btn")
        self.level_Btn.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.level_Btn)

        self.dungeon_Btn = QPushButton(self.frame)
        self.dungeon_Btn.setObjectName(u"dungeon_Btn")
        self.dungeon_Btn.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.dungeon_Btn)

        self.auto_Btn = QPushButton(self.frame)
        self.auto_Btn.setObjectName(u"auto_Btn")
        self.auto_Btn.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.auto_Btn)

        self.cal_Btn = QPushButton(self.frame)
        self.cal_Btn.setObjectName(u"cal_Btn")
        self.cal_Btn.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.cal_Btn)

        self.info_Btn = QPushButton(self.frame)
        self.info_Btn.setObjectName(u"info_Btn")
        self.info_Btn.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.info_Btn)


        self.verticalLayout.addWidget(self.frame)

        self.main_Stack = QStackedWidget(self.centralwidget)
        self.main_Stack.setObjectName(u"main_Stack")
        self.start_Page = QWidget()
        self.start_Page.setObjectName(u"start_Page")
        self.horizontalLayout_6 = QHBoxLayout(self.start_Page)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.start_Page)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"font: 32pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_4)


        self.horizontalLayout_6.addWidget(self.frame_7)

        self.main_Stack.addWidget(self.start_Page)
        self.level_Page = QWidget()
        self.level_Page.setObjectName(u"level_Page")
        self.verticalLayout_5 = QVBoxLayout(self.level_Page)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.level_Page)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 80))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_8)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 28pt \"Comic Sans MS\";")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_5)


        self.verticalLayout_5.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.level_Page)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_10)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.frame_18)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_22)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_34 = QFrame(self.frame_22)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(45, 0, 0, 0)
        self.label_35 = QLabel(self.frame_34)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFrameShadow(QFrame.Plain)
        self.label_35.setPixmap(QPixmap(u":/star/star.png"))

        self.horizontalLayout_22.addWidget(self.label_35)


        self.verticalLayout_12.addWidget(self.frame_34, 0, Qt.AlignLeft)

        self.frame_33 = QFrame(self.frame_22)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(45, 0, 0, 0)
        self.label_31 = QLabel(self.frame_33)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFrameShadow(QFrame.Plain)
        self.label_31.setPixmap(QPixmap(u":/star/star.png"))

        self.horizontalLayout_19.addWidget(self.label_31)

        self.label_32 = QLabel(self.frame_33)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFrameShadow(QFrame.Plain)
        self.label_32.setPixmap(QPixmap(u":/star/star.png"))

        self.horizontalLayout_19.addWidget(self.label_32)


        self.verticalLayout_12.addWidget(self.frame_33, 0, Qt.AlignLeft)

        self.frame_29 = QFrame(self.frame_22)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(45, 0, 0, 0)
        self.label_27 = QLabel(self.frame_29)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFrameShadow(QFrame.Plain)
        self.label_27.setPixmap(QPixmap(u":/star/star.png"))

        self.horizontalLayout_18.addWidget(self.label_27)

        self.label_28 = QLabel(self.frame_29)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFrameShadow(QFrame.Plain)
        self.label_28.setPixmap(QPixmap(u":/star/star.png"))

        self.horizontalLayout_18.addWidget(self.label_28)

        self.label_29 = QLabel(self.frame_29)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFrameShadow(QFrame.Plain)
        self.label_29.setPixmap(QPixmap(u":/star/star.png"))

        self.horizontalLayout_18.addWidget(self.label_29)


        self.verticalLayout_12.addWidget(self.frame_29, 0, Qt.AlignLeft)

        self.frame_35 = QFrame(self.frame_22)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(45, 0, 0, 0)
        self.label_43 = QLabel(self.frame_35)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFrameShadow(QFrame.Plain)
        self.label_43.setPixmap(QPixmap(u":/star/star.png"))

        self.horizontalLayout_24.addWidget(self.label_43)

        self.label_44 = QLabel(self.frame_35)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFrameShadow(QFrame.Plain)
        self.label_44.setPixmap(QPixmap(u":/star/star.png"))

        self.horizontalLayout_24.addWidget(self.label_44)

        self.label_45 = QLabel(self.frame_35)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFrameShadow(QFrame.Plain)
        self.label_45.setPixmap(QPixmap(u":/star/star.png"))

        self.horizontalLayout_24.addWidget(self.label_45)

        self.label_46 = QLabel(self.frame_35)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFrameShadow(QFrame.Plain)
        self.label_46.setPixmap(QPixmap(u":/star/star.png"))

        self.horizontalLayout_24.addWidget(self.label_46)


        self.verticalLayout_12.addWidget(self.frame_35, 0, Qt.AlignLeft)


        self.horizontalLayout_14.addWidget(self.frame_22)

        self.frame_25 = QFrame(self.frame_18)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_25)
        self.verticalLayout_13.setSpacing(35)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(60, 0, 0, 0)
        self.level1_Radio = QRadioButton(self.frame_25)
        self.level1_Radio.setObjectName(u"level1_Radio")
        self.level1_Radio.setChecked(True)

        self.verticalLayout_13.addWidget(self.level1_Radio)

        self.level2_Radio = QRadioButton(self.frame_25)
        self.level2_Radio.setObjectName(u"level2_Radio")

        self.verticalLayout_13.addWidget(self.level2_Radio)

        self.level3_Radio = QRadioButton(self.frame_25)
        self.level3_Radio.setObjectName(u"level3_Radio")

        self.verticalLayout_13.addWidget(self.level3_Radio)

        self.level4_Radio = QRadioButton(self.frame_25)
        self.level4_Radio.setObjectName(u"level4_Radio")

        self.verticalLayout_13.addWidget(self.level4_Radio)


        self.horizontalLayout_14.addWidget(self.frame_25)


        self.horizontalLayout_12.addWidget(self.frame_18)

        self.frame_24 = QFrame(self.frame_10)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_24)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_30 = QFrame(self.frame_24)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(10, 0, 100, 0)
        self.label_19 = QLabel(self.frame_30)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Comic Sans MS\";")

        self.horizontalLayout_20.addWidget(self.label_19)

        self.status_level_lbl = QLabel(self.frame_30)
        self.status_level_lbl.setObjectName(u"status_level_lbl")
        self.status_level_lbl.setStyleSheet(u"font: 14pt \"Comic Sans MS\";")

        self.horizontalLayout_20.addWidget(self.status_level_lbl)


        self.verticalLayout_14.addWidget(self.frame_30)

        self.frame_31 = QFrame(self.frame_24)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(10, 0, 75, 0)
        self.label_21 = QLabel(self.frame_31)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Comic Sans MS\";")

        self.horizontalLayout_21.addWidget(self.label_21)

        self.counter_level_lbl = QLabel(self.frame_31)
        self.counter_level_lbl.setObjectName(u"counter_level_lbl")
        self.counter_level_lbl.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Comic Sans MS\";")

        self.horizontalLayout_21.addWidget(self.counter_level_lbl)


        self.verticalLayout_14.addWidget(self.frame_31)

        self.frame_32 = QFrame(self.frame_24)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)

        self.verticalLayout_14.addWidget(self.frame_32)


        self.horizontalLayout_12.addWidget(self.frame_24)


        self.verticalLayout_4.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 100))
        self.frame_11.setStyleSheet(u"QPushButton{\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"	font: 9pt \"Comic Sans MS\";\n"
"}\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }\n"
"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setSpacing(220)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(100, 0, 100, 0)
        self.start_level = QPushButton(self.frame_11)
        self.start_level.setObjectName(u"start_level")
        self.start_level.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.start_level)

        self.stop_level = QPushButton(self.frame_11)
        self.stop_level.setObjectName(u"stop_level")
        self.stop_level.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.stop_level)


        self.verticalLayout_4.addWidget(self.frame_11)


        self.verticalLayout_5.addWidget(self.frame_9)

        self.main_Stack.addWidget(self.level_Page)
        self.dungeon_Page = QWidget()
        self.dungeon_Page.setObjectName(u"dungeon_Page")
        self.verticalLayout_7 = QVBoxLayout(self.dungeon_Page)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.dungeon_Page)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 78))
        self.frame_15.setMaximumSize(QSize(16777215, 80))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_15)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 28pt \"Comic Sans MS\";")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_6)


        self.verticalLayout_7.addWidget(self.frame_15)

        self.frame_12 = QFrame(self.dungeon_Page)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_12)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(100, 0))
        self.frame_14.setStyleSheet(u"QPushButton{\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"	font: 9pt \"Comic Sans MS\";\n"
"}\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }\n"
"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_14)
        self.verticalLayout_15.setSpacing(50)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(5, 15, 5, 0)
        self.dragon_Btn = QPushButton(self.frame_14)
        self.dragon_Btn.setObjectName(u"dragon_Btn")
        self.dragon_Btn.setStyleSheet(u"")

        self.verticalLayout_15.addWidget(self.dragon_Btn)

        self.golem_Btn = QPushButton(self.frame_14)
        self.golem_Btn.setObjectName(u"golem_Btn")
        self.golem_Btn.setStyleSheet(u"")

        self.verticalLayout_15.addWidget(self.golem_Btn)

        self.knight_Btn = QPushButton(self.frame_14)
        self.knight_Btn.setObjectName(u"knight_Btn")
        self.knight_Btn.setStyleSheet(u"")

        self.verticalLayout_15.addWidget(self.knight_Btn)

        self.minotaurus_Btn = QPushButton(self.frame_14)
        self.minotaurus_Btn.setObjectName(u"minotaurus_Btn")

        self.verticalLayout_15.addWidget(self.minotaurus_Btn)


        self.horizontalLayout_10.addWidget(self.frame_14, 0, Qt.AlignTop)

        self.dungeon_Stack = QStackedWidget(self.frame_13)
        self.dungeon_Stack.setObjectName(u"dungeon_Stack")
        self.dragon_Page = QWidget()
        self.dragon_Page.setObjectName(u"dragon_Page")
        self.horizontalLayout_16 = QHBoxLayout(self.dragon_Page)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QFrame(self.dragon_Page)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_26)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_28 = QFrame(self.frame_26)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_36 = QFrame(self.frame_28)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_36)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_38 = QFrame(self.frame_36)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.pushButton_2 = QPushButton(self.frame_38)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(40, 40))
        self.pushButton_2.setMaximumSize(QSize(40, 40))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	image: url(:/dragon/gen.png);\n"
"}\n"
"QPushButton:checked{\n"
"	border: 4px solid;\n"
"	border-color: rgb(17, 255, 0);\n"
"}")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setChecked(True)

        self.horizontalLayout_17.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.frame_38)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(40, 40))
        self.pushButton.setMaximumSize(QSize(40, 40))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	image: url(:/dragon/gew.png);\n"
"}\n"
"QPushButton:checked{\n"
"	border: 4px solid;\n"
"	border-color: rgb(17, 255, 0);\n"
"}")
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(True)

        self.horizontalLayout_17.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.frame_38)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(40, 40))
        self.pushButton_3.setMaximumSize(QSize(40, 40))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	image: url(:/dragon/leb.png);\n"
"}\n"
"QPushButton:checked{\n"
"	border: 4px solid;\n"
"	border-color: rgb(17, 255, 0);\n"
"}")
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setChecked(True)

        self.horizontalLayout_17.addWidget(self.pushButton_3)


        self.verticalLayout_17.addWidget(self.frame_38)

        self.frame_40 = QFrame(self.frame_36)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.pushButton_4 = QPushButton(self.frame_40)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(40, 40))
        self.pushButton_4.setMaximumSize(QSize(40, 40))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	image: url(:/dragon/ver.png);\n"
"}\n"
"QPushButton:checked{\n"
"	border: 4px solid;\n"
"	border-color: rgb(17, 255, 0);\n"
"}")
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setChecked(False)

        self.horizontalLayout_23.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_40)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(40, 40))
        self.pushButton_5.setMaximumSize(QSize(40, 40))
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"	image: url(:/dragon/gif.png);\n"
"}\n"
"QPushButton:checked{\n"
"	border: 4px solid;\n"
"	border-color: rgb(17, 255, 0);\n"
"}")
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setChecked(False)

        self.horizontalLayout_23.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_40)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(40, 40))
        self.pushButton_6.setMaximumSize(QSize(40, 40))
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"	image: url(:/dragon/fro.png);\n"
"}\n"
"QPushButton:checked{\n"
"	border: 4px solid;\n"
"	border-color: rgb(17, 255, 0);\n"
"}")
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setChecked(False)

        self.horizontalLayout_23.addWidget(self.pushButton_6)


        self.verticalLayout_17.addWidget(self.frame_40)

        self.frame_39 = QFrame(self.frame_36)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.pushButton_7 = QPushButton(self.frame_39)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(40, 40))
        self.pushButton_7.setMaximumSize(QSize(40, 40))
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
"	image: url(:/dragon/bet.png);\n"
"}\n"
"QPushButton:checked{\n"
"	border: 4px solid;\n"
"	border-color: rgb(17, 255, 0);\n"
"}")
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setChecked(False)

        self.horizontalLayout_27.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.frame_39)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(40, 40))
        self.pushButton_8.setMaximumSize(QSize(40, 40))
        self.pushButton_8.setStyleSheet(u"QPushButton{\n"
"	image: url(:/dragon/rac.png);\n"
"}\n"
"QPushButton:checked{\n"
"	border: 4px solid;\n"
"	border-color: rgb(17, 255, 0);\n"
"}")
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setChecked(False)

        self.horizontalLayout_27.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.frame_39)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(40, 40))
        self.pushButton_9.setMaximumSize(QSize(40, 40))
        self.pushButton_9.setStyleSheet(u"QPushButton{\n"
"	image: url(:/dragon/une.png);\n"
"}\n"
"QPushButton:checked{\n"
"	border: 4px solid;\n"
"	border-color: rgb(17, 255, 0);\n"
"}")
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setChecked(False)

        self.horizontalLayout_27.addWidget(self.pushButton_9)


        self.verticalLayout_17.addWidget(self.frame_39)


        self.horizontalLayout_26.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.frame_28)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_37)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_41 = QFrame(self.frame_37)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_24 = QLabel(self.frame_41)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Comic Sans MS\";")

        self.horizontalLayout_28.addWidget(self.label_24)

        self.label_23 = QLabel(self.frame_41)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"font: 14pt \"Comic Sans MS\";")

        self.horizontalLayout_28.addWidget(self.label_23)


        self.verticalLayout_18.addWidget(self.frame_41)

        self.frame_43 = QFrame(self.frame_37)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_29.setSpacing(60)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(35, 0, 85, 0)
        self.spinBox = QSpinBox(self.frame_43)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setStyleSheet(u"font: 12pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_29.addWidget(self.spinBox)

        self.level_Btn_5 = QPushButton(self.frame_43)
        self.level_Btn_5.setObjectName(u"level_Btn_5")
        self.level_Btn_5.setStyleSheet(u"QPushButton{\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"	font: 9pt \"Comic Sans MS\";\n"
"}\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }\n"
"QPushButton:checked{\n"
" 	border: 3px solid;\n"
"	border-color: rgb(5, 193, 5);\n"
"}")
        self.level_Btn_5.setCheckable(True)
        self.level_Btn_5.setChecked(False)

        self.horizontalLayout_29.addWidget(self.level_Btn_5)


        self.verticalLayout_18.addWidget(self.frame_43)

        self.frame_42 = QFrame(self.frame_37)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(21, -1, -1, -1)
        self.label_26 = QLabel(self.frame_42)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Comic Sans MS\";")

        self.horizontalLayout_30.addWidget(self.label_26)

        self.label_25 = QLabel(self.frame_42)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Comic Sans MS\";")

        self.horizontalLayout_30.addWidget(self.label_25)


        self.verticalLayout_18.addWidget(self.frame_42)


        self.horizontalLayout_26.addWidget(self.frame_37)


        self.verticalLayout_16.addWidget(self.frame_28)

        self.frame_27 = QFrame(self.frame_26)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMaximumSize(QSize(16777215, 80))
        self.frame_27.setStyleSheet(u"QPushButton{\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"	font: 9pt \"Comic Sans MS\";\n"
"}\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }\n"
"")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_25.setSpacing(250)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 10, 60, 0)
        self.info_Btn_4 = QPushButton(self.frame_27)
        self.info_Btn_4.setObjectName(u"info_Btn_4")
        self.info_Btn_4.setStyleSheet(u"")

        self.horizontalLayout_25.addWidget(self.info_Btn_4)

        self.info_Btn_5 = QPushButton(self.frame_27)
        self.info_Btn_5.setObjectName(u"info_Btn_5")
        self.info_Btn_5.setStyleSheet(u"")

        self.horizontalLayout_25.addWidget(self.info_Btn_5)


        self.verticalLayout_16.addWidget(self.frame_27)


        self.horizontalLayout_16.addWidget(self.frame_26)

        self.dungeon_Stack.addWidget(self.dragon_Page)
        self.golem_Page = QWidget()
        self.golem_Page.setObjectName(u"golem_Page")
        self.verticalLayout_22 = QVBoxLayout(self.golem_Page)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_44 = QFrame(self.golem_Page)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_44)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_45 = QFrame(self.frame_44)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_46 = QFrame(self.frame_45)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_46)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_47 = QFrame(self.frame_46)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.pushButton_10 = QPushButton(self.frame_47)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(40, 40))
        self.pushButton_10.setMaximumSize(QSize(40, 40))
        self.pushButton_10.setStyleSheet(u"QPushButton{\n"
"	image: url(:/golem/leben.png);\n"
"}\n"
"QPushButton:checked{\n"
"	border: 4px solid;\n"
"	border-color: rgb(17, 255, 0);\n"
"}")
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setChecked(False)

        self.horizontalLayout_32.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.frame_47)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(40, 40))
        self.pushButton_11.setMaximumSize(QSize(40, 40))
        self.pushButton_11.setStyleSheet(u"QPushButton{\n"
"	\n"
"	image: url(:/golem/off.png);\n"
"}\n"
"QPushButton:checked{\n"
"	border: 4px solid;\n"
"	border-color: rgb(17, 255, 0);\n"
"}")
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setChecked(False)

        self.horizontalLayout_32.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.frame_47)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(40, 40))
        self.pushButton_12.setMaximumSize(QSize(40, 40))
        self.pushButton_12.setStyleSheet(u"QPushButton{\n"
"	image: url(:/golem/def.png);\n"
"}\n"
"QPushButton:checked{\n"
"	border: 4px solid;\n"
"	border-color: rgb(17, 255, 0);\n"
"}")
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setChecked(False)

        self.horizontalLayout_32.addWidget(self.pushButton_12)


        self.verticalLayout_20.addWidget(self.frame_47)

        self.frame_48 = QFrame(self.frame_46)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.pushButton_13 = QPushButton(self.frame_48)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(40, 40))
        self.pushButton_13.setMaximumSize(QSize(40, 40))
        self.pushButton_13.setStyleSheet(u"QPushButton{\n"
"	image: url(:/golem/kritQ.png);\n"
"}\n"
"QPushButton:checked{\n"
"	border: 4px solid;\n"
"	border-color: rgb(17, 255, 0);\n"
"}")
        self.pushButton_13.setCheckable(True)
        self.pushButton_13.setChecked(False)

        self.horizontalLayout_33.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.frame_48)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(40, 40))
        self.pushButton_14.setMaximumSize(QSize(40, 40))
        self.pushButton_14.setStyleSheet(u"QPushButton{\n"
"	\n"
"	image: url(:/golem/wid.png);\n"
"}\n"
"QPushButton:checked{\n"
"	border: 4px solid;\n"
"	border-color: rgb(17, 255, 0);\n"
"}")
        self.pushButton_14.setCheckable(True)
        self.pushButton_14.setChecked(False)

        self.horizontalLayout_33.addWidget(self.pushButton_14)

        self.pushButton_15 = QPushButton(self.frame_48)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(40, 40))
        self.pushButton_15.setMaximumSize(QSize(40, 40))
        self.pushButton_15.setStyleSheet(u"QPushButton{\n"
"	\n"
"	image: url(:/golem/verg.png);\n"
"}\n"
"QPushButton:checked{\n"
"	border: 4px solid;\n"
"	border-color: rgb(17, 255, 0);\n"
"}")
        self.pushButton_15.setCheckable(True)
        self.pushButton_15.setChecked(False)

        self.horizontalLayout_33.addWidget(self.pushButton_15)


        self.verticalLayout_20.addWidget(self.frame_48)

        self.frame_49 = QFrame(self.frame_46)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.pushButton_16 = QPushButton(self.frame_49)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(40, 40))
        self.pushButton_16.setMaximumSize(QSize(40, 40))
        self.pushButton_16.setStyleSheet(u"QPushButton{\n"
"	image: url(:/golem/ref.png);\n"
"}\n"
"QPushButton:checked{\n"
"	border: 4px solid;\n"
"	border-color: rgb(17, 255, 0);\n"
"}")
        self.pushButton_16.setCheckable(True)
        self.pushButton_16.setChecked(False)

        self.horizontalLayout_34.addWidget(self.pushButton_16)

        self.pushButton_17 = QPushButton(self.frame_49)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMinimumSize(QSize(40, 40))
        self.pushButton_17.setMaximumSize(QSize(40, 40))
        self.pushButton_17.setStyleSheet(u"QPushButton{\n"
"	image: url(:/golem/verf.png);\n"
"}\n"
"QPushButton:checked{\n"
"	border: 4px solid;\n"
"	border-color: rgb(17, 255, 0);\n"
"}")
        self.pushButton_17.setCheckable(True)
        self.pushButton_17.setChecked(False)

        self.horizontalLayout_34.addWidget(self.pushButton_17)

        self.pushButton_18 = QPushButton(self.frame_49)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMinimumSize(QSize(40, 40))
        self.pushButton_18.setMaximumSize(QSize(40, 40))
        self.pushButton_18.setStyleSheet(u"QPushButton{\n"
"	image: url(:/golem/verh.png);\n"
"}\n"
"QPushButton:checked{\n"
"	border: 4px solid;\n"
"	border-color: rgb(17, 255, 0);\n"
"}")
        self.pushButton_18.setCheckable(True)
        self.pushButton_18.setChecked(False)

        self.horizontalLayout_34.addWidget(self.pushButton_18)


        self.verticalLayout_20.addWidget(self.frame_49)


        self.horizontalLayout_31.addWidget(self.frame_46)

        self.frame_50 = QFrame(self.frame_45)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_50)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_51 = QFrame(self.frame_50)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_30 = QLabel(self.frame_51)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Comic Sans MS\";")

        self.horizontalLayout_35.addWidget(self.label_30)

        self.label_33 = QLabel(self.frame_51)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"font: 14pt \"Comic Sans MS\";")

        self.horizontalLayout_35.addWidget(self.label_33)


        self.verticalLayout_21.addWidget(self.frame_51)

        self.frame_52 = QFrame(self.frame_50)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_36.setSpacing(60)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(35, 0, 85, 0)
        self.spinBox_2 = QSpinBox(self.frame_52)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setStyleSheet(u"font: 12pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_36.addWidget(self.spinBox_2)

        self.level_Btn_6 = QPushButton(self.frame_52)
        self.level_Btn_6.setObjectName(u"level_Btn_6")
        self.level_Btn_6.setStyleSheet(u"QPushButton{\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"	font: 9pt \"Comic Sans MS\";\n"
"}\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }\n"
"QPushButton:checked{\n"
" 	border: 3px solid;\n"
"	border-color: rgb(5, 193, 5);\n"
"}")
        self.level_Btn_6.setCheckable(True)
        self.level_Btn_6.setChecked(False)

        self.horizontalLayout_36.addWidget(self.level_Btn_6)


        self.verticalLayout_21.addWidget(self.frame_52)

        self.frame_53 = QFrame(self.frame_50)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(21, -1, -1, -1)
        self.label_34 = QLabel(self.frame_53)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Comic Sans MS\";")

        self.horizontalLayout_37.addWidget(self.label_34)

        self.label_36 = QLabel(self.frame_53)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Comic Sans MS\";")

        self.horizontalLayout_37.addWidget(self.label_36)


        self.verticalLayout_21.addWidget(self.frame_53)


        self.horizontalLayout_31.addWidget(self.frame_50)


        self.verticalLayout_19.addWidget(self.frame_45)

        self.frame_54 = QFrame(self.frame_44)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMaximumSize(QSize(16777215, 80))
        self.frame_54.setStyleSheet(u"QPushButton{\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"	font: 9pt \"Comic Sans MS\";\n"
"}\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }\n"
"")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_38.setSpacing(250)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 10, 60, 0)
        self.info_Btn_6 = QPushButton(self.frame_54)
        self.info_Btn_6.setObjectName(u"info_Btn_6")
        self.info_Btn_6.setStyleSheet(u"")

        self.horizontalLayout_38.addWidget(self.info_Btn_6)

        self.info_Btn_7 = QPushButton(self.frame_54)
        self.info_Btn_7.setObjectName(u"info_Btn_7")
        self.info_Btn_7.setStyleSheet(u"")

        self.horizontalLayout_38.addWidget(self.info_Btn_7)


        self.verticalLayout_19.addWidget(self.frame_54)


        self.verticalLayout_22.addWidget(self.frame_44)

        self.dungeon_Stack.addWidget(self.golem_Page)
        self.knight_Page = QWidget()
        self.knight_Page.setObjectName(u"knight_Page")
        self.verticalLayout_26 = QVBoxLayout(self.knight_Page)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_55 = QFrame(self.knight_Page)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_55)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_56 = QFrame(self.frame_55)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.frame_57 = QFrame(self.frame_56)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_57)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_58 = QFrame(self.frame_57)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.pushButton_19 = QPushButton(self.frame_58)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMinimumSize(QSize(40, 40))
        self.pushButton_19.setMaximumSize(QSize(40, 40))
        self.pushButton_19.setStyleSheet(u"QPushButton{\n"
"	image: url(:/knight/wut.png);\n"
"}\n"
"QPushButton:checked{\n"
"	border: 4px solid;\n"
"	border-color: rgb(17, 255, 0);\n"
"}")
        self.pushButton_19.setCheckable(True)
        self.pushButton_19.setChecked(False)

        self.horizontalLayout_40.addWidget(self.pushButton_19)

        self.pushButton_20 = QPushButton(self.frame_58)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setMinimumSize(QSize(40, 40))
        self.pushButton_20.setMaximumSize(QSize(40, 40))
        self.pushButton_20.setStyleSheet(u"QPushButton{\n"
"	image: url(:/knight/hei.png);\n"
"}\n"
"QPushButton:checked{\n"
"	border: 4px solid;\n"
"	border-color: rgb(17, 255, 0);\n"
"}")
        self.pushButton_20.setCheckable(True)
        self.pushButton_20.setChecked(False)

        self.horizontalLayout_40.addWidget(self.pushButton_20)

        self.pushButton_21 = QPushButton(self.frame_58)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMinimumSize(QSize(40, 40))
        self.pushButton_21.setMaximumSize(QSize(40, 40))
        self.pushButton_21.setStyleSheet(u"QPushButton{\n"
"	image: url(:/knight/imm.png);\n"
"}\n"
"QPushButton:checked{\n"
"	border: 4px solid;\n"
"	border-color: rgb(17, 255, 0);\n"
"}")
        self.pushButton_21.setCheckable(True)
        self.pushButton_21.setChecked(False)

        self.horizontalLayout_40.addWidget(self.pushButton_21)


        self.verticalLayout_24.addWidget(self.frame_58)

        self.frame_59 = QFrame(self.frame_57)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.pushButton_22 = QPushButton(self.frame_59)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMinimumSize(QSize(40, 40))
        self.pushButton_22.setMaximumSize(QSize(40, 40))
        self.pushButton_22.setStyleSheet(u"QPushButton{\n"
"	image: url(:/knight/sch.png);\n"
"}\n"
"QPushButton:checked{\n"
"	border: 4px solid;\n"
"	border-color: rgb(17, 255, 0);\n"
"}")
        self.pushButton_22.setCheckable(True)
        self.pushButton_22.setChecked(False)

        self.horizontalLayout_41.addWidget(self.pushButton_22)

        self.pushButton_23 = QPushButton(self.frame_59)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setMinimumSize(QSize(40, 40))
        self.pushButton_23.setMaximumSize(QSize(40, 40))
        self.pushButton_23.setStyleSheet(u"QPushButton{\n"
"	image: url(:/knight/kritD.png);\n"
"}\n"
"QPushButton:checked{\n"
"	border: 4px solid;\n"
"	border-color: rgb(17, 255, 0);\n"
"}")
        self.pushButton_23.setCheckable(True)
        self.pushButton_23.setChecked(False)

        self.horizontalLayout_41.addWidget(self.pushButton_23)

        self.pushButton_24 = QPushButton(self.frame_59)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setMinimumSize(QSize(40, 40))
        self.pushButton_24.setMaximumSize(QSize(40, 40))
        self.pushButton_24.setStyleSheet(u"QPushButton{\n"
"	image: url(:/knight/wah.png);\n"
"}\n"
"QPushButton:checked{\n"
"	border: 4px solid;\n"
"	border-color: rgb(17, 255, 0);\n"
"}")
        self.pushButton_24.setCheckable(True)
        self.pushButton_24.setChecked(False)

        self.horizontalLayout_41.addWidget(self.pushButton_24)


        self.verticalLayout_24.addWidget(self.frame_59)

        self.frame_60 = QFrame(self.frame_57)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.pushButton_25 = QPushButton(self.frame_60)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setMinimumSize(QSize(40, 40))
        self.pushButton_25.setMaximumSize(QSize(40, 40))
        self.pushButton_25.setStyleSheet(u"QPushButton{\n"
"	image: url(:/knight/reg.png);\n"
"}\n"
"QPushButton:checked{\n"
"	border: 4px solid;\n"
"	border-color: rgb(17, 255, 0);\n"
"}")
        self.pushButton_25.setCheckable(True)
        self.pushButton_25.setChecked(False)

        self.horizontalLayout_42.addWidget(self.pushButton_25)

        self.pushButton_26 = QPushButton(self.frame_60)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setMinimumSize(QSize(40, 40))
        self.pushButton_26.setMaximumSize(QSize(40, 40))
        self.pushButton_26.setStyleSheet(u"QPushButton{\n"
"	image: url(:/knight/stu.png);\n"
"}\n"
"QPushButton:checked{\n"
"	border: 4px solid;\n"
"	border-color: rgb(17, 255, 0);\n"
"}")
        self.pushButton_26.setCheckable(True)
        self.pushButton_26.setChecked(False)

        self.horizontalLayout_42.addWidget(self.pushButton_26)

        self.pushButton_27 = QPushButton(self.frame_60)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setMinimumSize(QSize(40, 40))
        self.pushButton_27.setMaximumSize(QSize(40, 40))
        self.pushButton_27.setStyleSheet(u"QPushButton{\n"
"	\n"
"	image: url(:/knight/wild.png);\n"
"}\n"
"QPushButton:checked{\n"
"	border: 4px solid;\n"
"	border-color: rgb(17, 255, 0);\n"
"}")
        self.pushButton_27.setCheckable(True)
        self.pushButton_27.setChecked(False)

        self.horizontalLayout_42.addWidget(self.pushButton_27)


        self.verticalLayout_24.addWidget(self.frame_60)


        self.horizontalLayout_39.addWidget(self.frame_57)

        self.frame_61 = QFrame(self.frame_56)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_61)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frame_62 = QFrame(self.frame_61)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_62)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_37 = QLabel(self.frame_62)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Comic Sans MS\";")

        self.horizontalLayout_43.addWidget(self.label_37)

        self.label_38 = QLabel(self.frame_62)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setStyleSheet(u"font: 14pt \"Comic Sans MS\";")

        self.horizontalLayout_43.addWidget(self.label_38)


        self.verticalLayout_25.addWidget(self.frame_62)

        self.frame_63 = QFrame(self.frame_61)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_63)
        self.horizontalLayout_44.setSpacing(60)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(35, 0, 85, 0)
        self.spinBox_3 = QSpinBox(self.frame_63)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setStyleSheet(u"font: 12pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_44.addWidget(self.spinBox_3)

        self.level_Btn_7 = QPushButton(self.frame_63)
        self.level_Btn_7.setObjectName(u"level_Btn_7")
        self.level_Btn_7.setStyleSheet(u"QPushButton{\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"	font: 9pt \"Comic Sans MS\";\n"
"}\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }\n"
"QPushButton:checked{\n"
" 	border: 3px solid;\n"
"	border-color: rgb(5, 193, 5);\n"
"}")
        self.level_Btn_7.setCheckable(True)
        self.level_Btn_7.setChecked(False)

        self.horizontalLayout_44.addWidget(self.level_Btn_7)


        self.verticalLayout_25.addWidget(self.frame_63)

        self.frame_64 = QFrame(self.frame_61)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_64)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(21, -1, -1, -1)
        self.label_39 = QLabel(self.frame_64)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Comic Sans MS\";")

        self.horizontalLayout_45.addWidget(self.label_39)

        self.label_40 = QLabel(self.frame_64)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Comic Sans MS\";")

        self.horizontalLayout_45.addWidget(self.label_40)


        self.verticalLayout_25.addWidget(self.frame_64)


        self.horizontalLayout_39.addWidget(self.frame_61)


        self.verticalLayout_23.addWidget(self.frame_56)

        self.frame_65 = QFrame(self.frame_55)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setMaximumSize(QSize(16777215, 80))
        self.frame_65.setStyleSheet(u"QPushButton{\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"	font: 9pt \"Comic Sans MS\";\n"
"}\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }\n"
"")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_65)
        self.horizontalLayout_46.setSpacing(250)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 10, 60, 0)
        self.info_Btn_8 = QPushButton(self.frame_65)
        self.info_Btn_8.setObjectName(u"info_Btn_8")
        self.info_Btn_8.setStyleSheet(u"")

        self.horizontalLayout_46.addWidget(self.info_Btn_8)

        self.info_Btn_9 = QPushButton(self.frame_65)
        self.info_Btn_9.setObjectName(u"info_Btn_9")
        self.info_Btn_9.setStyleSheet(u"")

        self.horizontalLayout_46.addWidget(self.info_Btn_9)


        self.verticalLayout_23.addWidget(self.frame_65)


        self.verticalLayout_26.addWidget(self.frame_55)

        self.dungeon_Stack.addWidget(self.knight_Page)
        self.minotaurus_Page = QWidget()
        self.minotaurus_Page.setObjectName(u"minotaurus_Page")
        self.horizontalLayout_55 = QHBoxLayout(self.minotaurus_Page)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.frame_77 = QFrame(self.minotaurus_Page)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_77)
        self.verticalLayout_31.setSpacing(6)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(9, 9, 9, 9)
        self.frame_79 = QFrame(self.frame_77)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_79)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.frame_80 = QFrame(self.frame_79)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_80)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.frame_82 = QFrame(self.frame_80)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_82)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.label_9 = QLabel(self.frame_82)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Comic Sans MS\";")

        self.horizontalLayout_58.addWidget(self.label_9)

        self.min_status_lbl = QLabel(self.frame_82)
        self.min_status_lbl.setObjectName(u"min_status_lbl")
        self.min_status_lbl.setStyleSheet(u"font: 14pt \"Comic Sans MS\";")

        self.horizontalLayout_58.addWidget(self.min_status_lbl)


        self.verticalLayout_32.addWidget(self.frame_82)

        self.frame_83 = QFrame(self.frame_80)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_83)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.label_14 = QLabel(self.frame_83)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Comic Sans MS\";")

        self.horizontalLayout_59.addWidget(self.label_14)

        self.min_refill_lbl = QLabel(self.frame_83)
        self.min_refill_lbl.setObjectName(u"min_refill_lbl")
        self.min_refill_lbl.setStyleSheet(u"font: 14pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_59.addWidget(self.min_refill_lbl)


        self.verticalLayout_32.addWidget(self.frame_83)


        self.horizontalLayout_57.addWidget(self.frame_80)

        self.frame_81 = QFrame(self.frame_79)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_81)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.frame_84 = QFrame(self.frame_81)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_84)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(80, -1, 80, 9)
        self.min_refill_Btn = QPushButton(self.frame_84)
        self.min_refill_Btn.setObjectName(u"min_refill_Btn")
        self.min_refill_Btn.setStyleSheet(u"QPushButton{\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"	font: 9pt \"Comic Sans MS\";\n"
"}\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }\n"
"QPushButton:checked{\n"
"	border: 4px solid;\n"
"	border-color: rgb(26, 255, 0);\n"
"}\n"
"")
        self.min_refill_Btn.setCheckable(True)
        self.min_refill_Btn.setChecked(False)

        self.verticalLayout_34.addWidget(self.min_refill_Btn)


        self.verticalLayout_33.addWidget(self.frame_84)

        self.frame_85 = QFrame(self.frame_81)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_85)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(100, -1, 110, -1)
        self.min_refill_Spin = QSpinBox(self.frame_85)
        self.min_refill_Spin.setObjectName(u"min_refill_Spin")
        self.min_refill_Spin.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Comic Sans MS\";")

        self.verticalLayout_35.addWidget(self.min_refill_Spin)


        self.verticalLayout_33.addWidget(self.frame_85)


        self.horizontalLayout_57.addWidget(self.frame_81)


        self.verticalLayout_31.addWidget(self.frame_79)

        self.frame_78 = QFrame(self.frame_77)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setMaximumSize(QSize(16777215, 80))
        self.frame_78.setStyleSheet(u"QPushButton{\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"	font: 9pt \"Comic Sans MS\";\n"
"}\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }\n"
"")
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_78)
        self.horizontalLayout_56.setSpacing(250)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 10, 60, 0)
        self.start_min_Btn = QPushButton(self.frame_78)
        self.start_min_Btn.setObjectName(u"start_min_Btn")
        self.start_min_Btn.setStyleSheet(u"")

        self.horizontalLayout_56.addWidget(self.start_min_Btn)

        self.stop_min_Btn = QPushButton(self.frame_78)
        self.stop_min_Btn.setObjectName(u"stop_min_Btn")
        self.stop_min_Btn.setStyleSheet(u"")

        self.horizontalLayout_56.addWidget(self.stop_min_Btn)


        self.verticalLayout_31.addWidget(self.frame_78)


        self.horizontalLayout_55.addWidget(self.frame_77)

        self.dungeon_Stack.addWidget(self.minotaurus_Page)

        self.horizontalLayout_10.addWidget(self.dungeon_Stack)


        self.verticalLayout_6.addWidget(self.frame_13)


        self.verticalLayout_7.addWidget(self.frame_12)

        self.main_Stack.addWidget(self.dungeon_Page)
        self.other_Page = QWidget()
        self.other_Page.setObjectName(u"other_Page")
        self.verticalLayout_9 = QVBoxLayout(self.other_Page)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.other_Page)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(16777215, 80))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_19)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 28pt \"Comic Sans MS\";")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_7)


        self.verticalLayout_9.addWidget(self.frame_19)

        self.frame_16 = QFrame(self.other_Page)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_16)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_17)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_66 = QFrame(self.frame_17)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_66)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.frame_68 = QFrame(self.frame_66)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_68)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.frame_71 = QFrame(self.frame_68)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_71)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.autoclicker_lbl = QLabel(self.frame_71)
        self.autoclicker_lbl.setObjectName(u"autoclicker_lbl")
        self.autoclicker_lbl.setStyleSheet(u"font: 16pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);")
        self.autoclicker_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_48.addWidget(self.autoclicker_lbl)


        self.verticalLayout_28.addWidget(self.frame_71)

        self.frame_72 = QFrame(self.frame_68)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setStyleSheet(u"QPushButton{\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"	font: 9pt \"Comic Sans MS\";\n"
"}\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }\n"
"")
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_72)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.start_autoclicker = QPushButton(self.frame_72)
        self.start_autoclicker.setObjectName(u"start_autoclicker")
        self.start_autoclicker.setStyleSheet(u"")

        self.horizontalLayout_49.addWidget(self.start_autoclicker)

        self.stop_autoclicker = QPushButton(self.frame_72)
        self.stop_autoclicker.setObjectName(u"stop_autoclicker")
        self.stop_autoclicker.setStyleSheet(u"")

        self.horizontalLayout_49.addWidget(self.stop_autoclicker)


        self.verticalLayout_28.addWidget(self.frame_72)


        self.horizontalLayout_47.addWidget(self.frame_68)

        self.frame_69 = QFrame(self.frame_66)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_69)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.frame_73 = QFrame(self.frame_69)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_73)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_10 = QLabel(self.frame_73)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font: 16pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_50.addWidget(self.label_10)


        self.verticalLayout_29.addWidget(self.frame_73)

        self.frame_74 = QFrame(self.frame_69)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setStyleSheet(u"QPushButton{\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"	font: 9pt \"Comic Sans MS\";\n"
"}\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }\n"
"")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_74)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(50, -1, 50, -1)
        self.start_autoseller = QPushButton(self.frame_74)
        self.start_autoseller.setObjectName(u"start_autoseller")
        self.start_autoseller.setStyleSheet(u"")

        self.horizontalLayout_51.addWidget(self.start_autoseller)


        self.verticalLayout_29.addWidget(self.frame_74)


        self.horizontalLayout_47.addWidget(self.frame_69)

        self.frame_70 = QFrame(self.frame_66)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_70)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.frame_75 = QFrame(self.frame_70)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_75)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.label_11 = QLabel(self.frame_75)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font: 16pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_52.addWidget(self.label_11)


        self.verticalLayout_30.addWidget(self.frame_75)

        self.frame_76 = QFrame(self.frame_70)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setStyleSheet(u"QPushButton{\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"	font: 9pt \"Comic Sans MS\";\n"
"}\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }\n"
"")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_76)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(50, 9, 50, -1)
        self.resize_Btn = QPushButton(self.frame_76)
        self.resize_Btn.setObjectName(u"resize_Btn")
        self.resize_Btn.setStyleSheet(u"")

        self.horizontalLayout_53.addWidget(self.resize_Btn)


        self.verticalLayout_30.addWidget(self.frame_76)


        self.horizontalLayout_47.addWidget(self.frame_70)


        self.verticalLayout_27.addWidget(self.frame_66)

        self.frame_67 = QFrame(self.frame_17)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setMaximumSize(QSize(16777215, 80))
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)

        self.verticalLayout_27.addWidget(self.frame_67)


        self.verticalLayout_8.addWidget(self.frame_17)


        self.verticalLayout_9.addWidget(self.frame_16)

        self.main_Stack.addWidget(self.other_Page)
        self.cal_Page = QWidget()
        self.cal_Page.setObjectName(u"cal_Page")
        self.verticalLayout_11 = QVBoxLayout(self.cal_Page)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.cal_Page)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMaximumSize(QSize(16777215, 80))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_23)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 28pt \"Comic Sans MS\";")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_8)


        self.verticalLayout_11.addWidget(self.frame_23)

        self.frame_20 = QFrame(self.cal_Page)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_20)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, -1, 0, 0)
        self.frame_87 = QFrame(self.frame_21)
        self.frame_87.setObjectName(u"frame_87")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_87.sizePolicy().hasHeightForWidth())
        self.frame_87.setSizePolicy(sizePolicy)
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_87)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.frame_89 = QFrame(self.frame_87)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setMaximumSize(QSize(16777215, 40))
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_89)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(9, -1, -1, -1)
        self.label_12 = QLabel(self.frame_89)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Comic Sans MS\";")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.label_12)


        self.verticalLayout_36.addWidget(self.frame_89)

        self.frame_90 = QFrame(self.frame_87)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_90)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.frame_91 = QFrame(self.frame_90)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_91)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(20, 30, 0, 0)
        self.frame_88 = QFrame(self.frame_91)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_88)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.acc_lbl = QLabel(self.frame_88)
        self.acc_lbl.setObjectName(u"acc_lbl")
        self.acc_lbl.setAutoFillBackground(False)
        self.acc_lbl.setStyleSheet(u"font: 10pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_39.addWidget(self.acc_lbl)

        self.acc_input = QLineEdit(self.frame_88)
        self.acc_input.setObjectName(u"acc_input")
        self.acc_input.setMaximumSize(QSize(115, 16777215))
        self.acc_input.setStyleSheet(u"font: 10pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);")
        self.acc_input.setMaxLength(3)

        self.verticalLayout_39.addWidget(self.acc_input)


        self.horizontalLayout_60.addWidget(self.frame_88, 0, Qt.AlignTop)

        self.frame_93 = QFrame(self.frame_91)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_93)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_40.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_60.addWidget(self.frame_93)

        self.frame_94 = QFrame(self.frame_91)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_94)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.res_lbl = QLabel(self.frame_94)
        self.res_lbl.setObjectName(u"res_lbl")
        self.res_lbl.setStyleSheet(u"font: 10pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_41.addWidget(self.res_lbl)

        self.res_input = QLineEdit(self.frame_94)
        self.res_input.setObjectName(u"res_input")
        self.res_input.setMaximumSize(QSize(115, 16777215))
        self.res_input.setStyleSheet(u"font: 10pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);")
        self.res_input.setMaxLength(3)

        self.verticalLayout_41.addWidget(self.res_input)


        self.horizontalLayout_60.addWidget(self.frame_94, 0, Qt.AlignTop)


        self.verticalLayout_38.addWidget(self.frame_91)

        self.frame_92 = QFrame(self.frame_90)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setStyleSheet(u"font: 14pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);")
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_92)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.chance_lbl = QLabel(self.frame_92)
        self.chance_lbl.setObjectName(u"chance_lbl")

        self.horizontalLayout_61.addWidget(self.chance_lbl)

        self.res_acc_chance_lbl = QLabel(self.frame_92)
        self.res_acc_chance_lbl.setObjectName(u"res_acc_chance_lbl")
        self.res_acc_chance_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_61.addWidget(self.res_acc_chance_lbl)


        self.verticalLayout_38.addWidget(self.frame_92)


        self.verticalLayout_36.addWidget(self.frame_90)


        self.horizontalLayout_54.addWidget(self.frame_87)

        self.frame_95 = QFrame(self.frame_21)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_95)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.frame_96 = QFrame(self.frame_95)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setMaximumSize(QSize(16777215, 40))
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_96)
        self.verticalLayout_43.setSpacing(6)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(9, 9, 9, 9)
        self.label_13 = QLabel(self.frame_96)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 40))
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Comic Sans MS\";")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_43.addWidget(self.label_13)


        self.verticalLayout_42.addWidget(self.frame_96)

        self.frame_97 = QFrame(self.frame_95)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_97)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(24, 0, 0, 0)
        self.frame_98 = QFrame(self.frame_97)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setStyleSheet(u"\n"
"font: 10pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);")
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.frame_98)
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_98)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(100, 0))
        self.label_15.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_62.addWidget(self.label_15)

        self.label_17 = QLabel(self.frame_98)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_62.addWidget(self.label_17)

        self.label_16 = QLabel(self.frame_98)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_62.addWidget(self.label_16)

        self.label_60 = QLabel(self.frame_98)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_62.addWidget(self.label_60)


        self.verticalLayout_44.addWidget(self.frame_98)

        self.frame_105 = QFrame(self.frame_97)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setStyleSheet(u"font: 10pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);")
        self.frame_105.setFrameShape(QFrame.StyledPanel)
        self.frame_105.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_105)
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.label_63 = QLabel(self.frame_105)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMinimumSize(QSize(100, 0))
        self.label_63.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_63.addWidget(self.label_63)

        self.label_65 = QLabel(self.frame_105)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_63.addWidget(self.label_65)

        self.label_64 = QLabel(self.frame_105)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_63.addWidget(self.label_64)

        self.label_61 = QLabel(self.frame_105)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_63.addWidget(self.label_61)


        self.verticalLayout_44.addWidget(self.frame_105)

        self.frame_103 = QFrame(self.frame_97)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setStyleSheet(u"font: 10pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);")
        self.frame_103.setFrameShape(QFrame.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_103)
        self.horizontalLayout_64.setSpacing(0)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.label_57 = QLabel(self.frame_103)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(100, 0))
        self.label_57.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_64.addWidget(self.label_57)

        self.label_59 = QLabel(self.frame_103)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_64.addWidget(self.label_59)

        self.label_58 = QLabel(self.frame_103)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_64.addWidget(self.label_58)

        self.label_62 = QLabel(self.frame_103)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_64.addWidget(self.label_62)


        self.verticalLayout_44.addWidget(self.frame_103)

        self.frame_101 = QFrame(self.frame_97)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setStyleSheet(u"font: 10pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);")
        self.frame_101.setFrameShape(QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.frame_101)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.label_51 = QLabel(self.frame_101)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMinimumSize(QSize(100, 0))
        self.label_51.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_65.addWidget(self.label_51)

        self.label_53 = QLabel(self.frame_101)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_65.addWidget(self.label_53)

        self.label_52 = QLabel(self.frame_101)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_65.addWidget(self.label_52)

        self.label_66 = QLabel(self.frame_101)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_65.addWidget(self.label_66)


        self.verticalLayout_44.addWidget(self.frame_101)

        self.frame_99 = QFrame(self.frame_97)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setStyleSheet(u"font: 10pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);")
        self.frame_99.setFrameShape(QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_99)
        self.horizontalLayout_66.setSpacing(0)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frame_99)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(100, 0))
        self.label_18.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_66.addWidget(self.label_18)

        self.label_22 = QLabel(self.frame_99)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_66.addWidget(self.label_22)

        self.label_20 = QLabel(self.frame_99)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_66.addWidget(self.label_20)

        self.label_67 = QLabel(self.frame_99)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_66.addWidget(self.label_67)


        self.verticalLayout_44.addWidget(self.frame_99)

        self.frame_100 = QFrame(self.frame_97)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setStyleSheet(u"font: 10pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);")
        self.frame_100.setFrameShape(QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.frame_100)
        self.horizontalLayout_68.setSpacing(0)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.label_48 = QLabel(self.frame_100)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMinimumSize(QSize(100, 0))
        self.label_48.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_68.addWidget(self.label_48)

        self.label_50 = QLabel(self.frame_100)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_68.addWidget(self.label_50)

        self.label_49 = QLabel(self.frame_100)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_68.addWidget(self.label_49)

        self.label_68 = QLabel(self.frame_100)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_68.addWidget(self.label_68)


        self.verticalLayout_44.addWidget(self.frame_100)

        self.frame_102 = QFrame(self.frame_97)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setStyleSheet(u"font: 10pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);")
        self.frame_102.setFrameShape(QFrame.StyledPanel)
        self.frame_102.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_102)
        self.horizontalLayout_67.setSpacing(0)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.label_54 = QLabel(self.frame_102)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMinimumSize(QSize(100, 0))
        self.label_54.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_67.addWidget(self.label_54)

        self.label_56 = QLabel(self.frame_102)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_67.addWidget(self.label_56)

        self.label_55 = QLabel(self.frame_102)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_67.addWidget(self.label_55)

        self.label_69 = QLabel(self.frame_102)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_67.addWidget(self.label_69)


        self.verticalLayout_44.addWidget(self.frame_102)


        self.verticalLayout_42.addWidget(self.frame_97)


        self.horizontalLayout_54.addWidget(self.frame_95)


        self.verticalLayout_10.addWidget(self.frame_21)

        self.frame_86 = QFrame(self.frame_20)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setMaximumSize(QSize(16777215, 80))
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.frame_86)


        self.verticalLayout_11.addWidget(self.frame_20)

        self.main_Stack.addWidget(self.cal_Page)
        self.info_Page = QWidget()
        self.info_Page.setObjectName(u"info_Page")
        self.verticalLayout_2 = QVBoxLayout(self.info_Page)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.info_Page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 80))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 28pt \"Comic Sans MS\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.info_Page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"font: 18pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(250, 0, 100, 0)
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.prank_Btn = QPushButton(self.frame_5)
        self.prank_Btn.setObjectName(u"prank_Btn")
        self.prank_Btn.setMaximumSize(QSize(160, 16777215))
        self.prank_Btn.setStyleSheet(u"QPushButton{\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"	font: 9pt \"Comic Sans MS\";\n"
"}\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }\n"
"")

        self.horizontalLayout_4.addWidget(self.prank_Btn)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"font: 14pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.prank_lbl = QLabel(self.frame_6)
        self.prank_lbl.setObjectName(u"prank_lbl")
        self.prank_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.prank_lbl)


        self.verticalLayout_3.addWidget(self.frame_6)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.main_Stack.addWidget(self.info_Page)

        self.verticalLayout.addWidget(self.main_Stack)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.main_Stack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Raid Bot", None))
        self.level_Btn.setText(QCoreApplication.translate("MainWindow", u"Level Bot", None))
        self.dungeon_Btn.setText(QCoreApplication.translate("MainWindow", u"Dungeon Bot", None))
        self.auto_Btn.setText(QCoreApplication.translate("MainWindow", u"Stuff", None))
        self.cal_Btn.setText(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.info_Btn.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Raid: Shadow Legends Bot", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Level Bot", None))
        self.label_35.setText("")
        self.label_31.setText("")
        self.label_32.setText("")
        self.label_27.setText("")
        self.label_28.setText("")
        self.label_29.setText("")
        self.label_43.setText("")
        self.label_44.setText("")
        self.label_45.setText("")
        self.label_46.setText("")
        self.level1_Radio.setText("")
        self.level2_Radio.setText("")
        self.level3_Radio.setText("")
        self.level4_Radio.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Bot Status:", None))
        self.status_level_lbl.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Round:", None))
        self.counter_level_lbl.setText("")
        self.start_level.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.stop_level.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Dungeon Bot", None))
        self.dragon_Btn.setText(QCoreApplication.translate("MainWindow", u"Dragon", None))
        self.golem_Btn.setText(QCoreApplication.translate("MainWindow", u"Golem", None))
        self.knight_Btn.setText(QCoreApplication.translate("MainWindow", u"Fireknight", None))
        self.minotaurus_Btn.setText(QCoreApplication.translate("MainWindow", u"Minotaurus", None))
        self.pushButton_2.setText("")
        self.pushButton.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.pushButton_6.setText("")
        self.pushButton_7.setText("")
        self.pushButton_8.setText("")
        self.pushButton_9.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Bot Status:", None))
        self.label_23.setText("")
        self.level_Btn_5.setText(QCoreApplication.translate("MainWindow", u"Inf.", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Round:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"48", None))
        self.info_Btn_4.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.info_Btn_5.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.pushButton_10.setText("")
        self.pushButton_11.setText("")
        self.pushButton_12.setText("")
        self.pushButton_13.setText("")
        self.pushButton_14.setText("")
        self.pushButton_15.setText("")
        self.pushButton_16.setText("")
        self.pushButton_17.setText("")
        self.pushButton_18.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Bot Status:", None))
        self.label_33.setText("")
        self.level_Btn_6.setText(QCoreApplication.translate("MainWindow", u"Inf.", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Round:", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"48", None))
        self.info_Btn_6.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.info_Btn_7.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.pushButton_19.setText("")
        self.pushButton_20.setText("")
        self.pushButton_21.setText("")
        self.pushButton_22.setText("")
        self.pushButton_23.setText("")
        self.pushButton_24.setText("")
        self.pushButton_25.setText("")
        self.pushButton_26.setText("")
        self.pushButton_27.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Bot Status:", None))
        self.label_38.setText("")
        self.level_Btn_7.setText(QCoreApplication.translate("MainWindow", u"Inf.", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Round:", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"48", None))
        self.info_Btn_8.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.info_Btn_9.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Bot Status:", None))
        self.min_status_lbl.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Refill left:", None))
        self.min_refill_lbl.setText("")
        self.min_refill_Btn.setText(QCoreApplication.translate("MainWindow", u"Refill", None))
        self.start_min_Btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.stop_min_Btn.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Stuff", None))
        self.autoclicker_lbl.setText(QCoreApplication.translate("MainWindow", u"Simple Auto Clicker", None))
        self.start_autoclicker.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.stop_autoclicker.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Auto Seller", None))
        self.start_autoseller.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Resize to 1280 x 720", None))
        self.resize_Btn.setText(QCoreApplication.translate("MainWindow", u"Resize", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Accuracy vs. Resistance Calculator", None))
        self.acc_lbl.setText(QCoreApplication.translate("MainWindow", u"Your Accuracy ", None))
        self.acc_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.res_lbl.setText(QCoreApplication.translate("MainWindow", u"Target Resistance ", None))
        self.res_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.chance_lbl.setText(QCoreApplication.translate("MainWindow", u" Chance to place a debuff:", None))
        self.res_acc_chance_lbl.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Clan Boss States", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Clan Boss Level", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"SPD", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"RES", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"ACC", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Easy", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"90", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"120", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Hard", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"140", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"75", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"40", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Brutal", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"160", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"75", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Nightmare", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"170", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"150", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"150", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Ulti-Nightmare", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"190", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"225", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"225", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Version:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"1.2", None))
        self.prank_Btn.setText(QCoreApplication.translate("MainWindow", u"Try Me", None))
        self.prank_lbl.setText("")
    # retranslateUi


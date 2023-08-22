# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1050, 685)
        MainWindow.setStyleSheet(u"*{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: none;\n"
"	color: #fff;\n"
"}\n"
"#sidebarWidget{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border-radius: 5px;\n"
"}\n"
"#mainFrame{\n"
"	background-color: rgb(55,55,55);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: #040f13;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: red;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_header = QFrame(self.centralwidget)
        self.frame_header.setObjectName(u"frame_header")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_header.sizePolicy().hasHeightForWidth())
        self.frame_header.setSizePolicy(sizePolicy)
        self.frame_header.setMinimumSize(QSize(0, 50))
        self.frame_header.setMaximumSize(QSize(16777215, 50))
        self.frame_header.setFrameShape(QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_header)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_toggle)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle = QPushButton(self.frame_toggle)
        self.btn_toggle.setObjectName(u"btn_toggle")
        font = QFont()
        font.setPointSize(15)
        self.btn_toggle.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/Resources/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.btn_toggle)


        self.horizontalLayout_2.addWidget(self.frame_toggle, 0, Qt.AlignLeft)

        self.frame_title = QFrame(self.frame_header)
        self.frame_title.setObjectName(u"frame_title")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_title.sizePolicy().hasHeightForWidth())
        self.frame_title.setSizePolicy(sizePolicy1)
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_title)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_title = QLabel(self.frame_title)
        self.lbl_title.setObjectName(u"lbl_title")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.lbl_title.setFont(font1)

        self.horizontalLayout_3.addWidget(self.lbl_title, 0, Qt.AlignLeft)


        self.horizontalLayout_2.addWidget(self.frame_title, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.frame_header, 0, Qt.AlignLeft)

        self.frame_body = QFrame(self.centralwidget)
        self.frame_body.setObjectName(u"frame_body")
        sizePolicy.setHeightForWidth(self.frame_body.sizePolicy().hasHeightForWidth())
        self.frame_body.setSizePolicy(sizePolicy)
        self.frame_body.setFrameShape(QFrame.StyledPanel)
        self.frame_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_body)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_sidebar = QWidget(self.frame_body)
        self.widget_sidebar.setObjectName(u"widget_sidebar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_sidebar.sizePolicy().hasHeightForWidth())
        self.widget_sidebar.setSizePolicy(sizePolicy2)
        self.verticalLayout_2 = QVBoxLayout(self.widget_sidebar)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_sidebar = QFrame(self.widget_sidebar)
        self.frame_sidebar.setObjectName(u"frame_sidebar")
        self.frame_sidebar.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.frame_sidebar.sizePolicy().hasHeightForWidth())
        self.frame_sidebar.setSizePolicy(sizePolicy2)
        self.frame_sidebar.setMinimumSize(QSize(150, 0))
        self.frame_sidebar.setMaximumSize(QSize(150, 16777215))
        self.frame_sidebar.setFrameShape(QFrame.StyledPanel)
        self.frame_sidebar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_sidebar)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 1)
        self.btn_home = QPushButton(self.frame_sidebar)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/icons/Resources/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon1)

        self.verticalLayout_3.addWidget(self.btn_home)

        self.btn_about = QPushButton(self.frame_sidebar)
        self.btn_about.setObjectName(u"btn_about")
        self.btn_about.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/icons/Resources/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_about.setIcon(icon2)

        self.verticalLayout_3.addWidget(self.btn_about)

        self.btn_quit = QPushButton(self.frame_sidebar)
        self.btn_quit.setObjectName(u"btn_quit")
        self.btn_quit.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/icons/Resources/icons/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_quit.setIcon(icon3)

        self.verticalLayout_3.addWidget(self.btn_quit)


        self.verticalLayout_2.addWidget(self.frame_sidebar, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout.addWidget(self.widget_sidebar)

        self.frame_main = QFrame(self.frame_body)
        self.frame_main.setObjectName(u"frame_main")
        sizePolicy1.setHeightForWidth(self.frame_main.sizePolicy().hasHeightForWidth())
        self.frame_main.setSizePolicy(sizePolicy1)
        self.frame_main.setAutoFillBackground(False)
        self.frame_main.setStyleSheet(u"background-color: rgb(58, 58, 58);\n"
"")
        self.frame_main.setFrameShape(QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_main)
#ifndef Q_OS_MAC
        self.verticalLayout_4.setSpacing(-1)
#endif
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(12, -1, -1, 12)
        self.widget_stacked = QStackedWidget(self.frame_main)
        self.widget_stacked.setObjectName(u"widget_stacked")
        self.widget_stacked.setAutoFillBackground(False)
        self.widget_stacked.setStyleSheet(u"")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_5 = QVBoxLayout(self.page_home)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_loadVideo = QFrame(self.page_home)
        self.frame_loadVideo.setObjectName(u"frame_loadVideo")
        self.frame_loadVideo.setFrameShape(QFrame.StyledPanel)
        self.frame_loadVideo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_loadVideo)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.edit_pathDir = QLineEdit(self.frame_loadVideo)
        self.edit_pathDir.setObjectName(u"edit_pathDir")
        self.edit_pathDir.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(196, 196, 196);\n"
"border-color: rgb(33, 33, 33);\n"
"border-radius: 2px;\n"
"padding: 7px 7px 7px 7px; ")

        self.horizontalLayout_7.addWidget(self.edit_pathDir)

        self.btn_loadVideo = QPushButton(self.frame_loadVideo)
        self.btn_loadVideo.setObjectName(u"btn_loadVideo")
        self.btn_loadVideo.setStyleSheet(u"background-color: #040f13;")

        self.horizontalLayout_7.addWidget(self.btn_loadVideo)


        self.verticalLayout_5.addWidget(self.frame_loadVideo)

        self.frame_videoList = QFrame(self.page_home)
        self.frame_videoList.setObjectName(u"frame_videoList")
        self.frame_videoList.setFrameShape(QFrame.StyledPanel)
        self.frame_videoList.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_videoList)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.video_list = QListWidget(self.frame_videoList)
        self.video_list.setObjectName(u"video_list")
        self.video_list.setStyleSheet(u"background-color: rgb(75, 75, 75);")

        self.verticalLayout_6.addWidget(self.video_list)


        self.verticalLayout_5.addWidget(self.frame_videoList)

        self.widget_stacked.addWidget(self.page_home)
        self.page_about = QWidget()
        self.page_about.setObjectName(u"page_about")
        self.verticalLayout_8 = QVBoxLayout(self.page_about)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_about = QFrame(self.page_about)
        self.frame_about.setObjectName(u"frame_about")
        self.frame_about.setFrameShape(QFrame.StyledPanel)
        self.frame_about.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_about)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lbl_about = QLabel(self.frame_about)
        self.lbl_about.setObjectName(u"lbl_about")
        self.lbl_about.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.lbl_about)


        self.verticalLayout_8.addWidget(self.frame_about)

        self.widget_stacked.addWidget(self.page_about)

        self.verticalLayout_4.addWidget(self.widget_stacked)


        self.horizontalLayout.addWidget(self.frame_main)


        self.verticalLayout.addWidget(self.frame_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"IFE Application", None))
        self.btn_toggle.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.lbl_title.setText(QCoreApplication.translate("MainWindow", u"IFE Application", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.btn_quit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.edit_pathDir.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Load video path directory...", None))
        self.btn_loadVideo.setText(QCoreApplication.translate("MainWindow", u"Load Videos", None))
        self.lbl_about.setText(QCoreApplication.translate("MainWindow", u"About Page", None))
    # retranslateUi


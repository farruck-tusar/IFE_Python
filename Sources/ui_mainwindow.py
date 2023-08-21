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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
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
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.headerFrame = QFrame(self.centralwidget)
        self.headerFrame.setObjectName(u"headerFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.headerFrame.sizePolicy().hasHeightForWidth())
        self.headerFrame.setSizePolicy(sizePolicy)
        self.headerFrame.setMinimumSize(QSize(0, 50))
        self.headerFrame.setMaximumSize(QSize(16777215, 50))
        self.headerFrame.setFrameShape(QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.headerFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuFrame = QFrame(self.headerFrame)
        self.menuFrame.setObjectName(u"menuFrame")
        self.menuFrame.setFrameShape(QFrame.StyledPanel)
        self.menuFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.menuFrame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_menu = QPushButton(self.menuFrame)
        self.btn_menu.setObjectName(u"btn_menu")
        font = QFont()
        font.setPointSize(15)
        self.btn_menu.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/Resources/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.btn_menu)


        self.horizontalLayout_2.addWidget(self.menuFrame, 0, Qt.AlignLeft)

        self.appNameFrame = QFrame(self.headerFrame)
        self.appNameFrame.setObjectName(u"appNameFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.appNameFrame.sizePolicy().hasHeightForWidth())
        self.appNameFrame.setSizePolicy(sizePolicy1)
        self.appNameFrame.setFrameShape(QFrame.StyledPanel)
        self.appNameFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.appNameFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.appName = QLabel(self.appNameFrame)
        self.appName.setObjectName(u"appName")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.appName.setFont(font1)

        self.horizontalLayout_3.addWidget(self.appName, 0, Qt.AlignLeft)


        self.horizontalLayout_2.addWidget(self.appNameFrame, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.headerFrame, 0, Qt.AlignLeft)

        self.bodyFrame = QFrame(self.centralwidget)
        self.bodyFrame.setObjectName(u"bodyFrame")
        sizePolicy.setHeightForWidth(self.bodyFrame.sizePolicy().hasHeightForWidth())
        self.bodyFrame.setSizePolicy(sizePolicy)
        self.bodyFrame.setFrameShape(QFrame.StyledPanel)
        self.bodyFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.bodyFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebarWidget = QWidget(self.bodyFrame)
        self.sidebarWidget.setObjectName(u"sidebarWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.sidebarWidget.sizePolicy().hasHeightForWidth())
        self.sidebarWidget.setSizePolicy(sizePolicy2)
        self.verticalLayout_2 = QVBoxLayout(self.sidebarWidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sidebarFrame = QFrame(self.sidebarWidget)
        self.sidebarFrame.setObjectName(u"sidebarFrame")
        self.sidebarFrame.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.sidebarFrame.sizePolicy().hasHeightForWidth())
        self.sidebarFrame.setSizePolicy(sizePolicy2)
        self.sidebarFrame.setMinimumSize(QSize(150, 0))
        self.sidebarFrame.setMaximumSize(QSize(150, 16777215))
        self.sidebarFrame.setFrameShape(QFrame.StyledPanel)
        self.sidebarFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.sidebarFrame)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 1)
        self.btn_home = QPushButton(self.sidebarFrame)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/icons/Resources/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon1)

        self.verticalLayout_3.addWidget(self.btn_home)

        self.btn_about = QPushButton(self.sidebarFrame)
        self.btn_about.setObjectName(u"btn_about")
        self.btn_about.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/icons/Resources/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_about.setIcon(icon2)

        self.verticalLayout_3.addWidget(self.btn_about)

        self.btn_quit = QPushButton(self.sidebarFrame)
        self.btn_quit.setObjectName(u"btn_quit")
        self.btn_quit.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/icons/Resources/icons/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_quit.setIcon(icon3)

        self.verticalLayout_3.addWidget(self.btn_quit)


        self.verticalLayout_2.addWidget(self.sidebarFrame, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout.addWidget(self.sidebarWidget)

        self.mainFrame = QFrame(self.bodyFrame)
        self.mainFrame.setObjectName(u"mainFrame")
        sizePolicy1.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy1)
        self.mainFrame.setAutoFillBackground(False)
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.mainFrame)
#ifndef Q_OS_MAC
        self.verticalLayout_4.setSpacing(-1)
#endif
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(12, -1, -1, 12)
        self.loadVideoFrame = QFrame(self.mainFrame)
        self.loadVideoFrame.setObjectName(u"loadVideoFrame")
        self.loadVideoFrame.setMinimumSize(QSize(0, 100))
        self.loadVideoFrame.setMaximumSize(QSize(16777215, 100))
        self.loadVideoFrame.setAutoFillBackground(False)
        self.loadVideoFrame.setStyleSheet(u"background-color: transparent;")
        self.loadVideoFrame.setFrameShape(QFrame.StyledPanel)
        self.loadVideoFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.loadVideoFrame)
#ifndef Q_OS_MAC
        self.horizontalLayout_5.setSpacing(-1)
#endif
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 12)
        self.edit_pathDir = QLineEdit(self.loadVideoFrame)
        self.edit_pathDir.setObjectName(u"edit_pathDir")
        font2 = QFont()
        font2.setPointSize(13)
        self.edit_pathDir.setFont(font2)
        self.edit_pathDir.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(196, 196, 196);\n"
"border-color: rgb(33, 33, 33);\n"
"border-radius: 2px;\n"
"padding: 7px 7px 7px 7px; ")
        self.edit_pathDir.setDragEnabled(True)
        self.edit_pathDir.setReadOnly(False)
        self.edit_pathDir.setClearButtonEnabled(False)

        self.horizontalLayout_5.addWidget(self.edit_pathDir)

        self.btn_loadVideo = QPushButton(self.loadVideoFrame)
        self.btn_loadVideo.setObjectName(u"btn_loadVideo")
        self.btn_loadVideo.setFont(font)
        self.btn_loadVideo.setStyleSheet(u"background-color: #040f13;")

        self.horizontalLayout_5.addWidget(self.btn_loadVideo)


        self.verticalLayout_4.addWidget(self.loadVideoFrame)

        self.videoPreviewFrame = QFrame(self.mainFrame)
        self.videoPreviewFrame.setObjectName(u"videoPreviewFrame")
        self.videoPreviewFrame.setAutoFillBackground(False)
        self.videoPreviewFrame.setStyleSheet(u"background-color: rgb(60, 60, 60);")
        self.videoPreviewFrame.setFrameShape(QFrame.StyledPanel)
        self.videoPreviewFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.videoPreviewFrame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.videoListPreview = QListWidget(self.videoPreviewFrame)
        self.videoListPreview.setObjectName(u"videoListPreview")

        self.horizontalLayout_6.addWidget(self.videoListPreview)


        self.verticalLayout_4.addWidget(self.videoPreviewFrame)


        self.horizontalLayout.addWidget(self.mainFrame)


        self.verticalLayout.addWidget(self.bodyFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"IFE Application", None))
        self.btn_menu.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.appName.setText(QCoreApplication.translate("MainWindow", u"IFE Application", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.btn_quit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.edit_pathDir.setText("")
        self.edit_pathDir.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Load video path directory...", None))
        self.btn_loadVideo.setText(QCoreApplication.translate("MainWindow", u"Load Videos", None))
    # retranslateUi


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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QHBoxLayout, QMainWindow,
    QMenu, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QStatusBar, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1258, 726)
        MainWindow.setMinimumSize(QSize(1024, 726))
        MainWindow.setStyleSheet(u"background:rgb(59,56,56);color:rgb(160, 160, 160);")
        self.actionVideo_Player = QAction(MainWindow)
        self.actionVideo_Player.setObjectName(u"actionVideo_Player")
        self.actionLoad_Directory = QAction(MainWindow)
        self.actionLoad_Directory.setObjectName(u"actionLoad_Directory")
        self.actionLoad_Directory.setIconVisibleInMenu(True)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionEnglish = QAction(MainWindow)
        self.actionEnglish.setObjectName(u"actionEnglish")
        self.actionEnglish.setCheckable(False)
        icon = QIcon()
        icon.addFile(u":/Resources/ICON/united-kingdom-flag-round-icon-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionEnglish.setIcon(icon)
        self.actionMongolia = QAction(MainWindow)
        self.actionMongolia.setObjectName(u"actionMongolia")
        self.actionMongolia.setCheckable(False)
        icon1 = QIcon()
        icon1.addFile(u":/Resources/ICON/mongolia-flag-round-icon-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionMongolia.setIcon(icon1)
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionRefresh_Directory = QAction(MainWindow)
        self.actionRefresh_Directory.setObjectName(u"actionRefresh_Directory")
        self.actionProcess_Images = QAction(MainWindow)
        self.actionProcess_Images.setObjectName(u"actionProcess_Images")
        self.actionAdvanced_Processing = QAction(MainWindow)
        self.actionAdvanced_Processing.setObjectName(u"actionAdvanced_Processing")
        self.actionProcess_All_2 = QAction(MainWindow)
        self.actionProcess_All_2.setObjectName(u"actionProcess_All_2")
        self.actionProcess_Images_2 = QAction(MainWindow)
        self.actionProcess_Images_2.setObjectName(u"actionProcess_Images_2")
        self.actionAdvanced_Processing_2 = QAction(MainWindow)
        self.actionAdvanced_Processing_2.setObjectName(u"actionAdvanced_Processing_2")
        self.actionAdvanced_Processing_2.setEnabled(False)
        self.actionAdvanced_Processing_2.setVisible(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget = QWidget(self.centralwidget)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, -1, -1, 0)
        self.widget_Middle = QWidget(self.horizontalWidget)
        self.widget_Middle.setObjectName(u"widget_Middle")
        self.verticalLayout_4 = QVBoxLayout(self.widget_Middle)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_DirectoryPath = QWidget(self.widget_Middle)
        self.widget_DirectoryPath.setObjectName(u"widget_DirectoryPath")
        self.widget_DirectoryPath.setMaximumSize(QSize(16777215, 25))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_DirectoryPath)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.btn_View = QPushButton(self.widget_DirectoryPath)
        self.btn_View.setObjectName(u"btn_View")
        self.btn_View.setMinimumSize(QSize(0, 23))
        self.btn_View.setMaximumSize(QSize(23, 23))
        self.btn_View.setStyleSheet(u"background:rgb(240, 240, 240);color:rgb(44,44,44);padding:5;")

        self.horizontalLayout_2.addWidget(self.btn_View)

        self.txtbrw_DirectoryPath = QTextBrowser(self.widget_DirectoryPath)
        self.txtbrw_DirectoryPath.setObjectName(u"txtbrw_DirectoryPath")
        self.txtbrw_DirectoryPath.setMaximumSize(QSize(16777215, 25))
        font = QFont()
        font.setBold(False)
        font.setKerning(True)
        self.txtbrw_DirectoryPath.setFont(font)
        self.txtbrw_DirectoryPath.setToolTipDuration(-1)
        self.txtbrw_DirectoryPath.setStyleSheet(u"background:rgb(44,44,44);border:none;")
        self.txtbrw_DirectoryPath.setMarkdown(u"Please load the directory with source videos ...\n"
"\n"
"")

        self.horizontalLayout_2.addWidget(self.txtbrw_DirectoryPath)

        self.btn_LoadDirectory = QPushButton(self.widget_DirectoryPath)
        self.btn_LoadDirectory.setObjectName(u"btn_LoadDirectory")
        self.btn_LoadDirectory.setMinimumSize(QSize(0, 23))
        self.btn_LoadDirectory.setMaximumSize(QSize(16777215, 23))
        font1 = QFont()
        font1.setBold(False)
        self.btn_LoadDirectory.setFont(font1)
        self.btn_LoadDirectory.setStyleSheet(u"color:rgb(44,44,44);background:rgb(100, 100, 100);")

        self.horizontalLayout_2.addWidget(self.btn_LoadDirectory)


        self.verticalLayout_4.addWidget(self.widget_DirectoryPath)

        self.widget_Main = QWidget(self.widget_Middle)
        self.widget_Main.setObjectName(u"widget_Main")
        self.widget_Main.setStyleSheet(u"background:rgb(44,44,44);")
        self.verticalLayout_6 = QVBoxLayout(self.widget_Main)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_Player = QWidget(self.widget_Main)
        self.widget_Player.setObjectName(u"widget_Player")
        self.widget_Player.setStyleSheet(u"background:rgb(44,44,44);")
        self.verticalLayout_7 = QVBoxLayout(self.widget_Player)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.layout_Player = QVBoxLayout()
        self.layout_Player.setSpacing(0)
        self.layout_Player.setObjectName(u"layout_Player")
        self.layout_Player.setContentsMargins(9, 9, 9, 9)

        self.verticalLayout_7.addLayout(self.layout_Player)


        self.verticalLayout_6.addWidget(self.widget_Player)

        self.scrollArea = QScrollArea(self.widget_Main)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setStyleSheet(u"background-color: red;")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 875, 312))
        self.scrollAreaWidgetContents.setStyleSheet(u"background:rgb(44,44,44);")
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_6.addWidget(self.scrollArea)


        self.verticalLayout_4.addWidget(self.widget_Main)


        self.horizontalLayout.addWidget(self.widget_Middle)

        self.scrollArea_SideBar = QScrollArea(self.horizontalWidget)
        self.scrollArea_SideBar.setObjectName(u"scrollArea_SideBar")
        self.scrollArea_SideBar.setMaximumSize(QSize(350, 16777215))
        self.scrollArea_SideBar.setStyleSheet(u"background:rgb(44,44,44); border:1px solid #2c2c2c;")
        self.scrollArea_SideBar.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea_SideBar.setWidgetResizable(True)
        self.scrollArea_SideBar.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.widget_SideBar = QWidget()
        self.widget_SideBar.setObjectName(u"widget_SideBar")
        self.widget_SideBar.setGeometry(QRect(0, 0, 348, 661))
        self.scrollArea_SideBar.setWidget(self.widget_SideBar)

        self.horizontalLayout.addWidget(self.scrollArea_SideBar)


        self.horizontalLayout_4.addWidget(self.horizontalWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1258, 24))
        self.menubar.setStyleSheet(u"")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuProcess_All = QMenu(self.menuFile)
        self.menuProcess_All.setObjectName(u"menuProcess_All")
        self.menuMore = QMenu(self.menubar)
        self.menuMore.setObjectName(u"menuMore")
        self.menuLanguage = QMenu(self.menuMore)
        self.menuLanguage.setObjectName(u"menuLanguage")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuMore.menuAction())
        self.menuFile.addAction(self.actionLoad_Directory)
        self.menuFile.addAction(self.menuProcess_All.menuAction())
        self.menuFile.addAction(self.actionRefresh_Directory)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuProcess_All.addAction(self.actionProcess_All_2)
        self.menuProcess_All.addAction(self.actionProcess_Images_2)
        self.menuProcess_All.addAction(self.actionAdvanced_Processing_2)
        self.menuMore.addAction(self.menuLanguage.menuAction())
        self.menuMore.addAction(self.actionHelp)
        self.menuMore.addAction(self.actionAbout)
        self.menuLanguage.addAction(self.actionEnglish)
        self.menuLanguage.addAction(self.actionMongolia)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionVideo_Player.setText(QCoreApplication.translate("MainWindow", u"Video Player", None))
        self.actionLoad_Directory.setText(QCoreApplication.translate("MainWindow", u"Open Directory", None))
#if QT_CONFIG(shortcut)
        self.actionLoad_Directory.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
#if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionEnglish.setText(QCoreApplication.translate("MainWindow", u"English", None))
#if QT_CONFIG(shortcut)
        self.actionEnglish.setShortcut(QCoreApplication.translate("MainWindow", u"F3", None))
#endif // QT_CONFIG(shortcut)
        self.actionMongolia.setText(QCoreApplication.translate("MainWindow", u"Mongolia", None))
#if QT_CONFIG(shortcut)
        self.actionMongolia.setShortcut(QCoreApplication.translate("MainWindow", u"F4", None))
#endif // QT_CONFIG(shortcut)
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
#if QT_CONFIG(shortcut)
        self.actionHelp.setShortcut(QCoreApplication.translate("MainWindow", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionRefresh_Directory.setText(QCoreApplication.translate("MainWindow", u"Refresh Directory", None))
#if QT_CONFIG(shortcut)
        self.actionRefresh_Directory.setShortcut(QCoreApplication.translate("MainWindow", u"F5", None))
#endif // QT_CONFIG(shortcut)
        self.actionProcess_Images.setText(QCoreApplication.translate("MainWindow", u"Process Images", None))
#if QT_CONFIG(shortcut)
        self.actionProcess_Images.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.actionAdvanced_Processing.setText(QCoreApplication.translate("MainWindow", u"Advanced Processing", None))
        self.actionProcess_All_2.setText(QCoreApplication.translate("MainWindow", u"Process All Files", None))
        self.actionProcess_Images_2.setText(QCoreApplication.translate("MainWindow", u"Process Images", None))
        self.actionAdvanced_Processing_2.setText(QCoreApplication.translate("MainWindow", u"Advanced Processing", None))
        self.btn_View.setText("")
        self.txtbrw_DirectoryPath.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:5px; margin-bottom:5px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt;\">Please load the directory with source videos ...</span></p></body></html>", None))
        self.btn_LoadDirectory.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuProcess_All.setTitle(QCoreApplication.translate("MainWindow", u"Process", None))
        self.menuMore.setTitle(QCoreApplication.translate("MainWindow", u"More", None))
        self.menuLanguage.setTitle(QCoreApplication.translate("MainWindow", u"Language", None))
    # retranslateUi


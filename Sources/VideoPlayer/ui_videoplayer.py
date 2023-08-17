# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_videoplayer.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QDoubleSpinBox,
    QFormLayout, QFrame, QHBoxLayout, QLabel,
    QLayout, QPushButton, QScrollArea, QSizePolicy,
    QSlider, QVBoxLayout, QWidget)

class Ui_VP_VideoPlayer(object):
    def setupUi(self, VP_VideoPlayer):
        if not VP_VideoPlayer.objectName():
            VP_VideoPlayer.setObjectName(u"VP_VideoPlayer")
        VP_VideoPlayer.resize(507, 480)
        self.verticalLayout = QVBoxLayout(VP_VideoPlayer)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.layout_Top = QHBoxLayout()
        self.layout_Top.setSpacing(0)
        self.layout_Top.setObjectName(u"layout_Top")
        self.layout_Top.setContentsMargins(-1, -1, 0, -1)
        self.layout_test = QVBoxLayout()
        self.layout_test.setSpacing(0)
        self.layout_test.setObjectName(u"layout_test")

        self.layout_Top.addLayout(self.layout_test)

        self.layout_Zoom = QVBoxLayout()
        self.layout_Zoom.setObjectName(u"layout_Zoom")
        self.slider_zoom = QSlider(VP_VideoPlayer)
        self.slider_zoom.setObjectName(u"slider_zoom")
        self.slider_zoom.setSingleStep(1)
        self.slider_zoom.setOrientation(Qt.Vertical)

        self.layout_Zoom.addWidget(self.slider_zoom)

        self.lbl_zoom = QLabel(VP_VideoPlayer)
        self.lbl_zoom.setObjectName(u"lbl_zoom")
        self.lbl_zoom.setMinimumSize(QSize(30, 0))
        self.lbl_zoom.setMaximumSize(QSize(30, 16777215))
        self.lbl_zoom.setAlignment(Qt.AlignCenter)

        self.layout_Zoom.addWidget(self.lbl_zoom)


        self.layout_Top.addLayout(self.layout_Zoom)


        self.verticalLayout.addLayout(self.layout_Top)

        self.layout_Middle = QHBoxLayout()
        self.layout_Middle.setSpacing(6)
        self.layout_Middle.setObjectName(u"layout_Middle")
        self.layout_Middle.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")

        self.verticalLayout_5.addLayout(self.formLayout_2)

        self.Videosliderwidget = QWidget(VP_VideoPlayer)
        self.Videosliderwidget.setObjectName(u"Videosliderwidget")
        self.horizontalLayout = QHBoxLayout(self.Videosliderwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.slider_position = QSlider(self.Videosliderwidget)
        self.slider_position.setObjectName(u"slider_position")
        self.slider_position.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.slider_position)

        self.widget = QWidget(self.Videosliderwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 6, -1, -1)
        self.lbl_time = QLabel(self.widget)
        self.lbl_time.setObjectName(u"lbl_time")

        self.verticalLayout_3.addWidget(self.lbl_time)


        self.horizontalLayout.addWidget(self.widget)


        self.verticalLayout_5.addWidget(self.Videosliderwidget)

        self.horizontalWidget = QWidget(VP_VideoPlayer)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.scrollArea = QScrollArea(self.horizontalWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(316, 71))
        self.scrollArea.setMaximumSize(QSize(16777215, 71))
        self.scrollArea.setLayoutDirection(Qt.LeftToRight)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 314, 69))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(16777215, 300))
        self.scrollAreaWidgetContents.setCursor(QCursor(Qt.OpenHandCursor))
        self.scrollAreaWidgetContents.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.heat_Slider = QSlider(self.scrollAreaWidgetContents)
        self.heat_Slider.setObjectName(u"heat_Slider")
        self.heat_Slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_4.addWidget(self.heat_Slider)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.scrollArea)

        self.scrollArea_2 = QScrollArea(self.horizontalWidget)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 160, 73))
        self.scrollAreaWidgetContents_2.setStyleSheet(u"margin: 0")
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.scrollAreaWidgetContents_2)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_6.addWidget(self.label, 0, Qt.AlignVCenter)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_2.addWidget(self.scrollArea_2)


        self.verticalLayout_5.addWidget(self.horizontalWidget, 0, Qt.AlignTop)


        self.layout_Middle.addLayout(self.verticalLayout_5)


        self.verticalLayout.addLayout(self.layout_Middle)

        self.layout_Bottom = QHBoxLayout()
        self.layout_Bottom.setSpacing(6)
        self.layout_Bottom.setObjectName(u"layout_Bottom")
        self.pb_play = QPushButton(VP_VideoPlayer)
        self.pb_play.setObjectName(u"pb_play")

        self.layout_Bottom.addWidget(self.pb_play)

        self.pb_stop = QPushButton(VP_VideoPlayer)
        self.pb_stop.setObjectName(u"pb_stop")

        self.layout_Bottom.addWidget(self.pb_stop)

        self.spinBox_speed = QDoubleSpinBox(VP_VideoPlayer)
        self.spinBox_speed.setObjectName(u"spinBox_speed")
        self.spinBox_speed.setMinimumSize(QSize(60, 0))
        self.spinBox_speed.setMaximumSize(QSize(60, 16777215))
        self.spinBox_speed.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_speed.setDecimals(1)
        self.spinBox_speed.setMinimum(0.100000000000000)
        self.spinBox_speed.setMaximum(5.000000000000000)
        self.spinBox_speed.setSingleStep(0.100000000000000)
        self.spinBox_speed.setValue(1.000000000000000)

        self.layout_Bottom.addWidget(self.spinBox_speed)

        self.pb_repeat = QPushButton(VP_VideoPlayer)
        self.pb_repeat.setObjectName(u"pb_repeat")
        self.pb_repeat.setMinimumSize(QSize(25, 0))
        self.pb_repeat.setMaximumSize(QSize(25, 16777215))
        self.pb_repeat.setCheckable(True)

        self.layout_Bottom.addWidget(self.pb_repeat)

        self.line = QFrame(VP_VideoPlayer)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.layout_Bottom.addWidget(self.line)

        self.comboBox_filter = QComboBox(VP_VideoPlayer)
        self.comboBox_filter.setObjectName(u"comboBox_filter")

        self.layout_Bottom.addWidget(self.comboBox_filter)

        self.pb_process = QPushButton(VP_VideoPlayer)
        self.pb_process.setObjectName(u"pb_process")

        self.layout_Bottom.addWidget(self.pb_process)


        self.verticalLayout.addLayout(self.layout_Bottom)


        self.retranslateUi(VP_VideoPlayer)

        QMetaObject.connectSlotsByName(VP_VideoPlayer)
    # setupUi

    def retranslateUi(self, VP_VideoPlayer):
        VP_VideoPlayer.setWindowTitle(QCoreApplication.translate("VP_VideoPlayer", u"Form", None))
        self.lbl_zoom.setText(QCoreApplication.translate("VP_VideoPlayer", u"1.0x", None))
        self.lbl_time.setText(QCoreApplication.translate("VP_VideoPlayer", u"00:00:00.000/00:00:00.000", None))
        self.label.setText(QCoreApplication.translate("VP_VideoPlayer", u"Label", None))
        self.pb_play.setText("")
        self.pb_stop.setText("")
        self.pb_repeat.setText("")
        self.pb_process.setText(QCoreApplication.translate("VP_VideoPlayer", u"Process video", None))
    # retranslateUi


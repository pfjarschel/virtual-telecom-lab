# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Stuff\SideWorks\VirtualTelecomLab\instruments\oscilloscope.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Oscilloscope(object):
    def setupUi(self, Oscilloscope):
        Oscilloscope.setObjectName("Oscilloscope")
        Oscilloscope.resize(979, 502)
        self.gridLayout = QtWidgets.QGridLayout(Oscilloscope)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setSpacing(16)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_9.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.startBut = QtWidgets.QPushButton(Oscilloscope)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startBut.sizePolicy().hasHeightForWidth())
        self.startBut.setSizePolicy(sizePolicy)
        self.startBut.setMinimumSize(QtCore.QSize(0, 0))
        self.startBut.setMaximumSize(QtCore.QSize(72, 16777215))
        self.startBut.setObjectName("startBut")
        self.horizontalLayout_2.addWidget(self.startBut)
        self.stopBut = QtWidgets.QPushButton(Oscilloscope)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopBut.sizePolicy().hasHeightForWidth())
        self.stopBut.setSizePolicy(sizePolicy)
        self.stopBut.setMinimumSize(QtCore.QSize(0, 0))
        self.stopBut.setMaximumSize(QtCore.QSize(72, 16777215))
        self.stopBut.setObjectName("stopBut")
        self.horizontalLayout_2.addWidget(self.stopBut)
        self.verticalLayout_9.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem)
        self.groupBox = QtWidgets.QGroupBox(Oscilloscope)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setHorizontalSpacing(12)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.hscaleDial = QtWidgets.QDial(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hscaleDial.sizePolicy().hasHeightForWidth())
        self.hscaleDial.setSizePolicy(sizePolicy)
        self.hscaleDial.setMaximumSize(QtCore.QSize(64, 64))
        self.hscaleDial.setMaximum(39)
        self.hscaleDial.setProperty("value", 15)
        self.hscaleDial.setNotchTarget(1.0)
        self.hscaleDial.setNotchesVisible(True)
        self.hscaleDial.setObjectName("hscaleDial")
        self.gridLayout_2.addWidget(self.hscaleDial, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)
        self.hoffsetDial = QtWidgets.QDial(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hoffsetDial.sizePolicy().hasHeightForWidth())
        self.hoffsetDial.setSizePolicy(sizePolicy)
        self.hoffsetDial.setMaximumSize(QtCore.QSize(64, 64))
        self.hoffsetDial.setMinimum(-10000)
        self.hoffsetDial.setMaximum(10000)
        self.hoffsetDial.setSingleStep(100)
        self.hoffsetDial.setPageStep(1000)
        self.hoffsetDial.setNotchTarget(10.0)
        self.hoffsetDial.setNotchesVisible(True)
        self.hoffsetDial.setObjectName("hoffsetDial")
        self.gridLayout_2.addWidget(self.hoffsetDial, 1, 1, 1, 1)
        self.hscaleInd = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hscaleInd.sizePolicy().hasHeightForWidth())
        self.hscaleInd.setSizePolicy(sizePolicy)
        self.hscaleInd.setMaximumSize(QtCore.QSize(64, 16777215))
        self.hscaleInd.setReadOnly(True)
        self.hscaleInd.setObjectName("hscaleInd")
        self.gridLayout_2.addWidget(self.hscaleInd, 2, 0, 1, 1)
        self.hoffsetSpin = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.hoffsetSpin.setKeyboardTracking(False)
        self.hoffsetSpin.setMinimum(-100.0)
        self.hoffsetSpin.setMaximum(100.0)
        self.hoffsetSpin.setObjectName("hoffsetSpin")
        self.gridLayout_2.addWidget(self.hoffsetSpin, 2, 1, 1, 1)
        self.verticalLayout_9.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Oscilloscope)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.triggerfreeRadio = QtWidgets.QRadioButton(self.groupBox_2)
        self.triggerfreeRadio.setChecked(True)
        self.triggerfreeRadio.setObjectName("triggerfreeRadio")
        self.gridLayout_3.addWidget(self.triggerfreeRadio, 0, 0, 1, 1)
        self.triggerautoRadio = QtWidgets.QRadioButton(self.groupBox_2)
        self.triggerautoRadio.setObjectName("triggerautoRadio")
        self.gridLayout_3.addWidget(self.triggerautoRadio, 0, 1, 1, 1)
        self.verticalLayout_9.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(Oscilloscope)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setHorizontalSpacing(12)
        self.gridLayout_4.setVerticalSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.holdCheck = QtWidgets.QCheckBox(self.groupBox_3)
        self.holdCheck.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.holdCheck.setObjectName("holdCheck")
        self.gridLayout_4.addWidget(self.holdCheck, 2, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.label_16)
        self.avgSpin = QtWidgets.QSpinBox(self.groupBox_3)
        self.avgSpin.setMaximumSize(QtCore.QSize(64, 16777215))
        self.avgSpin.setKeyboardTracking(False)
        self.avgSpin.setMinimum(1)
        self.avgSpin.setMaximum(1024)
        self.avgSpin.setObjectName("avgSpin")
        self.verticalLayout.addWidget(self.avgSpin)
        self.gridLayout_4.addLayout(self.verticalLayout, 1, 2, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_2.addWidget(self.label_15)
        self.pointsSpin = QtWidgets.QSpinBox(self.groupBox_3)
        self.pointsSpin.setMaximumSize(QtCore.QSize(64, 16777215))
        self.pointsSpin.setKeyboardTracking(False)
        self.pointsSpin.setMinimum(100)
        self.pointsSpin.setMaximum(10000)
        self.pointsSpin.setProperty("value", 1000)
        self.pointsSpin.setObjectName("pointsSpin")
        self.verticalLayout_2.addWidget(self.pointsSpin)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_17 = QtWidgets.QLabel(self.groupBox_3)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_3.addWidget(self.label_17)
        self.holdSpin = QtWidgets.QSpinBox(self.groupBox_3)
        self.holdSpin.setKeyboardTracking(False)
        self.holdSpin.setMinimum(2)
        self.holdSpin.setMaximum(1024)
        self.holdSpin.setObjectName("holdSpin")
        self.verticalLayout_3.addWidget(self.holdSpin)
        self.gridLayout_4.addLayout(self.verticalLayout_3, 2, 2, 1, 1)
        self.verticalLayout_9.addWidget(self.groupBox_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem1)
        self.saveBut = QtWidgets.QPushButton(Oscilloscope)
        self.saveBut.setMaximumSize(QtCore.QSize(256, 16777215))
        self.saveBut.setObjectName("saveBut")
        self.verticalLayout_9.addWidget(self.saveBut)
        self.horizontalLayout.addLayout(self.verticalLayout_9)
        self.groupBox_5 = QtWidgets.QGroupBox(Oscilloscope)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem3, 5, 1, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setVerticalSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.ch2offsDial = QtWidgets.QDial(self.groupBox_5)
        self.ch2offsDial.setMaximumSize(QtCore.QSize(64, 64))
        self.ch2offsDial.setMinimum(-100000)
        self.ch2offsDial.setMaximum(100000)
        self.ch2offsDial.setSingleStep(10)
        self.ch2offsDial.setPageStep(100)
        self.ch2offsDial.setObjectName("ch2offsDial")
        self.gridLayout_7.addWidget(self.ch2offsDial, 1, 1, 1, 1)
        self.ch2scaleDial = QtWidgets.QDial(self.groupBox_5)
        self.ch2scaleDial.setMaximumSize(QtCore.QSize(64, 64))
        self.ch2scaleDial.setMaximum(15)
        self.ch2scaleDial.setProperty("value", 11)
        self.ch2scaleDial.setNotchTarget(1.0)
        self.ch2scaleDial.setNotchesVisible(True)
        self.ch2scaleDial.setObjectName("ch2scaleDial")
        self.gridLayout_7.addWidget(self.ch2scaleDial, 0, 1, 1, 1)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_10 = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMaximumSize(QtCore.QSize(76, 16777215))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_13.addWidget(self.label_10)
        self.ch2scaleInd = QtWidgets.QLineEdit(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ch2scaleInd.sizePolicy().hasHeightForWidth())
        self.ch2scaleInd.setSizePolicy(sizePolicy)
        self.ch2scaleInd.setMaximumSize(QtCore.QSize(76, 16777215))
        self.ch2scaleInd.setReadOnly(True)
        self.ch2scaleInd.setObjectName("ch2scaleInd")
        self.verticalLayout_13.addWidget(self.ch2scaleInd)
        self.gridLayout_7.addLayout(self.verticalLayout_13, 0, 0, 1, 1)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_9 = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMaximumSize(QtCore.QSize(76, 16777215))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_14.addWidget(self.label_9)
        self.ch2offsSpin = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        self.ch2offsSpin.setKeyboardTracking(False)
        self.ch2offsSpin.setDecimals(3)
        self.ch2offsSpin.setMinimum(-100.0)
        self.ch2offsSpin.setMaximum(100.0)
        self.ch2offsSpin.setSingleStep(0.01)
        self.ch2offsSpin.setObjectName("ch2offsSpin")
        self.verticalLayout_14.addWidget(self.ch2offsSpin)
        self.gridLayout_7.addLayout(self.verticalLayout_14, 1, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_7, 2, 1, 1, 1)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem4)
        self.label_6 = QtWidgets.QLabel(self.groupBox_5)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_10.addWidget(self.label_6)
        self.ch4Check = QtWidgets.QCheckBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ch4Check.sizePolicy().hasHeightForWidth())
        self.ch4Check.setSizePolicy(sizePolicy)
        self.ch4Check.setText("")
        self.ch4Check.setObjectName("ch4Check")
        self.verticalLayout_10.addWidget(self.ch4Check)
        self.ch4XCheck = QtWidgets.QCheckBox(self.groupBox_5)
        self.ch4XCheck.setObjectName("ch4XCheck")
        self.verticalLayout_10.addWidget(self.ch4XCheck)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem5)
        self.gridLayout_6.addLayout(self.verticalLayout_10, 4, 0, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setVerticalSpacing(0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.ch3scaleDial = QtWidgets.QDial(self.groupBox_5)
        self.ch3scaleDial.setMaximumSize(QtCore.QSize(64, 64))
        self.ch3scaleDial.setMaximum(15)
        self.ch3scaleDial.setProperty("value", 11)
        self.ch3scaleDial.setNotchTarget(1.0)
        self.ch3scaleDial.setNotchesVisible(True)
        self.ch3scaleDial.setObjectName("ch3scaleDial")
        self.gridLayout_8.addWidget(self.ch3scaleDial, 0, 1, 1, 1)
        self.ch3offsDial = QtWidgets.QDial(self.groupBox_5)
        self.ch3offsDial.setMaximumSize(QtCore.QSize(64, 64))
        self.ch3offsDial.setMinimum(-10000)
        self.ch3offsDial.setMaximum(10000)
        self.ch3offsDial.setSingleStep(10)
        self.ch3offsDial.setPageStep(100)
        self.ch3offsDial.setObjectName("ch3offsDial")
        self.gridLayout_8.addWidget(self.ch3offsDial, 1, 1, 1, 1)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_8 = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMaximumSize(QtCore.QSize(76, 16777215))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_15.addWidget(self.label_8)
        self.ch3scaleInd = QtWidgets.QLineEdit(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ch3scaleInd.sizePolicy().hasHeightForWidth())
        self.ch3scaleInd.setSizePolicy(sizePolicy)
        self.ch3scaleInd.setMaximumSize(QtCore.QSize(76, 16777215))
        self.ch3scaleInd.setReadOnly(True)
        self.ch3scaleInd.setObjectName("ch3scaleInd")
        self.verticalLayout_15.addWidget(self.ch3scaleInd)
        self.gridLayout_8.addLayout(self.verticalLayout_15, 0, 0, 1, 1)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_7 = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMaximumSize(QtCore.QSize(76, 16777215))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_16.addWidget(self.label_7)
        self.ch3offsSpin = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        self.ch3offsSpin.setKeyboardTracking(False)
        self.ch3offsSpin.setDecimals(3)
        self.ch3offsSpin.setMinimum(-100.0)
        self.ch3offsSpin.setMaximum(100.0)
        self.ch3offsSpin.setSingleStep(0.01)
        self.ch3offsSpin.setObjectName("ch3offsSpin")
        self.verticalLayout_16.addWidget(self.ch3offsSpin)
        self.gridLayout_8.addLayout(self.verticalLayout_16, 1, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_8, 3, 1, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setVerticalSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.ch1offsDial = QtWidgets.QDial(self.groupBox_5)
        self.ch1offsDial.setMaximumSize(QtCore.QSize(64, 64))
        self.ch1offsDial.setMinimum(-100000)
        self.ch1offsDial.setMaximum(100000)
        self.ch1offsDial.setSingleStep(10)
        self.ch1offsDial.setPageStep(100)
        self.ch1offsDial.setObjectName("ch1offsDial")
        self.gridLayout_5.addWidget(self.ch1offsDial, 2, 1, 1, 1)
        self.ch1scaleDial = QtWidgets.QDial(self.groupBox_5)
        self.ch1scaleDial.setMaximumSize(QtCore.QSize(64, 64))
        self.ch1scaleDial.setMaximum(15)
        self.ch1scaleDial.setProperty("value", 11)
        self.ch1scaleDial.setNotchTarget(1.0)
        self.ch1scaleDial.setNotchesVisible(True)
        self.ch1scaleDial.setObjectName("ch1scaleDial")
        self.gridLayout_5.addWidget(self.ch1scaleDial, 0, 1, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_14 = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMaximumSize(QtCore.QSize(76, 16777215))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_5.addWidget(self.label_14)
        self.ch1scaleInd = QtWidgets.QLineEdit(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ch1scaleInd.sizePolicy().hasHeightForWidth())
        self.ch1scaleInd.setSizePolicy(sizePolicy)
        self.ch1scaleInd.setMaximumSize(QtCore.QSize(76, 16777215))
        self.ch1scaleInd.setReadOnly(True)
        self.ch1scaleInd.setObjectName("ch1scaleInd")
        self.verticalLayout_5.addWidget(self.ch1scaleInd)
        self.gridLayout_5.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMaximumSize(QtCore.QSize(76, 16777215))
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_12.addWidget(self.label_13)
        self.ch1offsSpin = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        self.ch1offsSpin.setKeyboardTracking(False)
        self.ch1offsSpin.setDecimals(3)
        self.ch1offsSpin.setMinimum(-100.0)
        self.ch1offsSpin.setMaximum(100.0)
        self.ch1offsSpin.setSingleStep(0.01)
        self.ch1offsSpin.setProperty("value", 0.0)
        self.ch1offsSpin.setObjectName("ch1offsSpin")
        self.verticalLayout_12.addWidget(self.ch1offsSpin)
        self.gridLayout_5.addLayout(self.verticalLayout_12, 2, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 1, 1, 1, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem6)
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_8.addWidget(self.label_5)
        self.ch3Check = QtWidgets.QCheckBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ch3Check.sizePolicy().hasHeightForWidth())
        self.ch3Check.setSizePolicy(sizePolicy)
        self.ch3Check.setText("")
        self.ch3Check.setObjectName("ch3Check")
        self.verticalLayout_8.addWidget(self.ch3Check)
        self.ch3XCheck = QtWidgets.QCheckBox(self.groupBox_5)
        self.ch3XCheck.setObjectName("ch3XCheck")
        self.verticalLayout_8.addWidget(self.ch3XCheck)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem7)
        self.gridLayout_6.addLayout(self.verticalLayout_8, 3, 0, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setVerticalSpacing(0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.ch4offsDial = QtWidgets.QDial(self.groupBox_5)
        self.ch4offsDial.setMaximumSize(QtCore.QSize(64, 64))
        self.ch4offsDial.setMinimum(-10000)
        self.ch4offsDial.setMaximum(10000)
        self.ch4offsDial.setSingleStep(10)
        self.ch4offsDial.setPageStep(100)
        self.ch4offsDial.setNotchTarget(100.0)
        self.ch4offsDial.setNotchesVisible(False)
        self.ch4offsDial.setObjectName("ch4offsDial")
        self.gridLayout_9.addWidget(self.ch4offsDial, 1, 1, 1, 1)
        self.ch4scaleDial = QtWidgets.QDial(self.groupBox_5)
        self.ch4scaleDial.setMaximumSize(QtCore.QSize(64, 64))
        self.ch4scaleDial.setMaximum(15)
        self.ch4scaleDial.setProperty("value", 11)
        self.ch4scaleDial.setNotchTarget(1.0)
        self.ch4scaleDial.setNotchesVisible(True)
        self.ch4scaleDial.setObjectName("ch4scaleDial")
        self.gridLayout_9.addWidget(self.ch4scaleDial, 0, 1, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMaximumSize(QtCore.QSize(76, 16777215))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_4.addWidget(self.label_11)
        self.ch4scaleInd = QtWidgets.QLineEdit(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ch4scaleInd.sizePolicy().hasHeightForWidth())
        self.ch4scaleInd.setSizePolicy(sizePolicy)
        self.ch4scaleInd.setMaximumSize(QtCore.QSize(76, 16777215))
        self.ch4scaleInd.setReadOnly(True)
        self.ch4scaleInd.setObjectName("ch4scaleInd")
        self.verticalLayout_4.addWidget(self.ch4scaleInd)
        self.gridLayout_9.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_12 = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMaximumSize(QtCore.QSize(76, 16777215))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_6.addWidget(self.label_12)
        self.ch4offsSpin = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ch4offsSpin.sizePolicy().hasHeightForWidth())
        self.ch4offsSpin.setSizePolicy(sizePolicy)
        self.ch4offsSpin.setMaximumSize(QtCore.QSize(76, 16777215))
        self.ch4offsSpin.setKeyboardTracking(False)
        self.ch4offsSpin.setDecimals(3)
        self.ch4offsSpin.setMinimum(-100.0)
        self.ch4offsSpin.setMaximum(100.0)
        self.ch4offsSpin.setSingleStep(0.01)
        self.ch4offsSpin.setObjectName("ch4offsSpin")
        self.verticalLayout_6.addWidget(self.ch4offsSpin)
        self.gridLayout_9.addLayout(self.verticalLayout_6, 1, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_9, 4, 1, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem8)
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        self.label_4.setMinimumSize(QtCore.QSize(24, 0))
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.ch1Check = QtWidgets.QCheckBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ch1Check.sizePolicy().hasHeightForWidth())
        self.ch1Check.setSizePolicy(sizePolicy)
        self.ch1Check.setText("")
        self.ch1Check.setChecked(True)
        self.ch1Check.setObjectName("ch1Check")
        self.verticalLayout_7.addWidget(self.ch1Check)
        self.ch1XCheck = QtWidgets.QCheckBox(self.groupBox_5)
        self.ch1XCheck.setObjectName("ch1XCheck")
        self.verticalLayout_7.addWidget(self.ch1XCheck)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem9)
        self.gridLayout_6.addLayout(self.verticalLayout_7, 1, 0, 1, 1)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem10)
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_11.addWidget(self.label_3)
        self.ch2Check = QtWidgets.QCheckBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ch2Check.sizePolicy().hasHeightForWidth())
        self.ch2Check.setSizePolicy(sizePolicy)
        self.ch2Check.setText("")
        self.ch2Check.setObjectName("ch2Check")
        self.verticalLayout_11.addWidget(self.ch2Check)
        self.ch2XCheck = QtWidgets.QCheckBox(self.groupBox_5)
        self.ch2XCheck.setObjectName("ch2XCheck")
        self.verticalLayout_11.addWidget(self.ch2XCheck)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem11)
        self.gridLayout_6.addLayout(self.verticalLayout_11, 2, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_5)
        self.graphHolder = QtWidgets.QGridLayout()
        self.graphHolder.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.graphHolder.setObjectName("graphHolder")
        self.horizontalLayout.addLayout(self.graphHolder)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(Oscilloscope)
        QtCore.QMetaObject.connectSlotsByName(Oscilloscope)

    def retranslateUi(self, Oscilloscope):
        _translate = QtCore.QCoreApplication.translate
        Oscilloscope.setWindowTitle(_translate("Oscilloscope", "Oscilloscope - Virtual Telecom Lab"))
        self.startBut.setText(_translate("Oscilloscope", "Run"))
        self.stopBut.setText(_translate("Oscilloscope", "Stop"))
        self.groupBox.setTitle(_translate("Oscilloscope", "Horizontal Control"))
        self.label.setText(_translate("Oscilloscope", "Scale (s/div)"))
        self.label_2.setText(_translate("Oscilloscope", "Offset (%)"))
        self.hscaleInd.setText(_translate("Oscilloscope", "100 ns"))
        self.groupBox_2.setTitle(_translate("Oscilloscope", "Trigger Control"))
        self.triggerfreeRadio.setText(_translate("Oscilloscope", "Free run"))
        self.triggerautoRadio.setText(_translate("Oscilloscope", "Auto"))
        self.groupBox_3.setTitle(_translate("Oscilloscope", "Acquisition Control"))
        self.holdCheck.setText(_translate("Oscilloscope", "Hold"))
        self.label_16.setText(_translate("Oscilloscope", "Averages"))
        self.label_15.setText(_translate("Oscilloscope", "Points"))
        self.label_17.setText(_translate("Oscilloscope", "Hold number"))
        self.saveBut.setText(_translate("Oscilloscope", "Save"))
        self.groupBox_5.setTitle(_translate("Oscilloscope", "Vertical Control"))
        self.label_10.setText(_translate("Oscilloscope", "Scale (V/div)"))
        self.ch2scaleInd.setText(_translate("Oscilloscope", "500 mV"))
        self.label_9.setText(_translate("Oscilloscope", "Offset (V)"))
        self.label_6.setText(_translate("Oscilloscope", "CH4"))
        self.ch4XCheck.setText(_translate("Oscilloscope", "As X"))
        self.label_8.setText(_translate("Oscilloscope", "Scale (V/div)"))
        self.ch3scaleInd.setText(_translate("Oscilloscope", "500 mV"))
        self.label_7.setText(_translate("Oscilloscope", "Offset (V)"))
        self.label_14.setText(_translate("Oscilloscope", "Scale (V/div)"))
        self.ch1scaleInd.setText(_translate("Oscilloscope", "500 mV"))
        self.label_13.setText(_translate("Oscilloscope", "Offset (V)"))
        self.label_5.setText(_translate("Oscilloscope", "CH3"))
        self.ch3XCheck.setText(_translate("Oscilloscope", "As X"))
        self.label_11.setText(_translate("Oscilloscope", "Scale (V/div)"))
        self.ch4scaleInd.setText(_translate("Oscilloscope", "500 mV"))
        self.label_12.setText(_translate("Oscilloscope", "Offset (V)"))
        self.label_4.setText(_translate("Oscilloscope", "CH1"))
        self.ch1XCheck.setText(_translate("Oscilloscope", "As X"))
        self.label_3.setText(_translate("Oscilloscope", "CH2"))
        self.ch2XCheck.setText(_translate("Oscilloscope", "As X"))

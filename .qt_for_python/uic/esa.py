# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Stuff\SideWorks\VirtualTelecomLab\instruments\esa.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ESA(object):
    def setupUi(self, ESA):
        ESA.setObjectName("ESA")
        ESA.resize(926, 511)
        self.gridLayout = QtWidgets.QGridLayout(ESA)
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
        self.startBut = QtWidgets.QPushButton(ESA)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startBut.sizePolicy().hasHeightForWidth())
        self.startBut.setSizePolicy(sizePolicy)
        self.startBut.setMinimumSize(QtCore.QSize(0, 0))
        self.startBut.setMaximumSize(QtCore.QSize(72, 16777215))
        self.startBut.setObjectName("startBut")
        self.horizontalLayout_2.addWidget(self.startBut)
        self.stopBut = QtWidgets.QPushButton(ESA)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopBut.sizePolicy().hasHeightForWidth())
        self.stopBut.setSizePolicy(sizePolicy)
        self.stopBut.setMinimumSize(QtCore.QSize(0, 0))
        self.stopBut.setMaximumSize(QtCore.QSize(72, 16777215))
        self.stopBut.setObjectName("stopBut")
        self.horizontalLayout_2.addWidget(self.stopBut)
        self.singleBut = QtWidgets.QPushButton(ESA)
        self.singleBut.setMaximumSize(QtCore.QSize(72, 16777215))
        self.singleBut.setObjectName("singleBut")
        self.horizontalLayout_2.addWidget(self.singleBut)
        self.verticalLayout_9.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem)
        self.groupBox = QtWidgets.QGroupBox(ESA)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setHorizontalSpacing(12)
        self.gridLayout_2.setVerticalSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setMaximumSize(QtCore.QSize(128, 16777215))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_8.addWidget(self.label_2)
        self.stopSpin = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.stopSpin.setMaximumSize(QtCore.QSize(128, 16777215))
        self.stopSpin.setKeyboardTracking(False)
        self.stopSpin.setDecimals(4)
        self.stopSpin.setMaximum(20000.0)
        self.stopSpin.setProperty("value", 10.0)
        self.stopSpin.setObjectName("stopSpin")
        self.verticalLayout_8.addWidget(self.stopSpin)
        self.gridLayout_2.addLayout(self.verticalLayout_8, 0, 1, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setMaximumSize(QtCore.QSize(128, 16777215))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout_7.addWidget(self.label)
        self.startSpin = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.startSpin.setMaximumSize(QtCore.QSize(128, 16777215))
        self.startSpin.setKeyboardTracking(False)
        self.startSpin.setDecimals(4)
        self.startSpin.setMaximum(20000.0)
        self.startSpin.setObjectName("startSpin")
        self.verticalLayout_7.addWidget(self.startSpin)
        self.gridLayout_2.addLayout(self.verticalLayout_7, 0, 0, 1, 1)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setMaximumSize(QtCore.QSize(128, 16777215))
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_11.addWidget(self.label_4)
        self.spanSpin = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.spanSpin.setMaximumSize(QtCore.QSize(128, 16777215))
        self.spanSpin.setKeyboardTracking(False)
        self.spanSpin.setDecimals(4)
        self.spanSpin.setMinimum(0.001)
        self.spanSpin.setMaximum(20000.0)
        self.spanSpin.setProperty("value", 10.0)
        self.spanSpin.setObjectName("spanSpin")
        self.verticalLayout_11.addWidget(self.spanSpin)
        self.gridLayout_2.addLayout(self.verticalLayout_11, 3, 1, 1, 1)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setMaximumSize(QtCore.QSize(128, 16777215))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_10.addWidget(self.label_3)
        self.centerSpin = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.centerSpin.setMaximumSize(QtCore.QSize(128, 16777215))
        self.centerSpin.setKeyboardTracking(False)
        self.centerSpin.setDecimals(4)
        self.centerSpin.setMaximum(20000.0)
        self.centerSpin.setProperty("value", 5.0)
        self.centerSpin.setObjectName("centerSpin")
        self.verticalLayout_10.addWidget(self.centerSpin)
        self.gridLayout_2.addLayout(self.verticalLayout_10, 3, 0, 1, 1)
        self.verticalLayout_9.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(ESA)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.dbmRadio = QtWidgets.QRadioButton(self.groupBox_2)
        self.dbmRadio.setChecked(True)
        self.dbmRadio.setObjectName("dbmRadio")
        self.gridLayout_3.addWidget(self.dbmRadio, 0, 0, 1, 1)
        self.linRadio = QtWidgets.QRadioButton(self.groupBox_2)
        self.linRadio.setObjectName("linRadio")
        self.gridLayout_3.addWidget(self.linRadio, 0, 1, 1, 1)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_12.addWidget(self.label_7)
        self.dbdivSpin = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.dbdivSpin.setKeyboardTracking(False)
        self.dbdivSpin.setDecimals(1)
        self.dbdivSpin.setMinimum(0.1)
        self.dbdivSpin.setMaximum(30.0)
        self.dbdivSpin.setProperty("value", 10.0)
        self.dbdivSpin.setObjectName("dbdivSpin")
        self.verticalLayout_12.addWidget(self.dbdivSpin)
        self.gridLayout_3.addLayout(self.verticalLayout_12, 1, 0, 1, 1)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_13.addWidget(self.label_8)
        self.reflevelSpin = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.reflevelSpin.setKeyboardTracking(False)
        self.reflevelSpin.setMinimum(-300.0)
        self.reflevelSpin.setMaximum(100.0)
        self.reflevelSpin.setProperty("value", 10.0)
        self.reflevelSpin.setObjectName("reflevelSpin")
        self.verticalLayout_13.addWidget(self.reflevelSpin)
        self.gridLayout_3.addLayout(self.verticalLayout_13, 1, 1, 1, 1)
        self.verticalLayout_9.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(ESA)
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
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.sgNSpin = QtWidgets.QSpinBox(self.groupBox_3)
        self.sgNSpin.setKeyboardTracking(False)
        self.sgNSpin.setMinimum(1)
        self.sgNSpin.setMaximum(1024)
        self.sgNSpin.setProperty("value", 32)
        self.sgNSpin.setObjectName("sgNSpin")
        self.verticalLayout_3.addWidget(self.sgNSpin)
        self.gridLayout_4.addLayout(self.verticalLayout_3, 3, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.windowCheck = QtWidgets.QCheckBox(self.groupBox_3)
        self.windowCheck.setObjectName("windowCheck")
        self.verticalLayout.addWidget(self.windowCheck)
        self.windowSpin = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.windowSpin.setKeyboardTracking(False)
        self.windowSpin.setObjectName("windowSpin")
        self.verticalLayout.addWidget(self.windowSpin)
        self.gridLayout_4.addLayout(self.verticalLayout, 1, 2, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setMaximumSize(QtCore.QSize(128, 16777215))
        self.label_15.setObjectName("label_15")
        self.verticalLayout_2.addWidget(self.label_15)
        self.pointsSpin = QtWidgets.QSpinBox(self.groupBox_3)
        self.pointsSpin.setMaximumSize(QtCore.QSize(128, 16777215))
        self.pointsSpin.setKeyboardTracking(False)
        self.pointsSpin.setMinimum(10)
        self.pointsSpin.setMaximum(1000000)
        self.pointsSpin.setProperty("value", 1000)
        self.pointsSpin.setObjectName("pointsSpin")
        self.verticalLayout_2.addWidget(self.pointsSpin)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.srturboSpin = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.srturboSpin.setKeyboardTracking(False)
        self.srturboSpin.setMinimum(1.0)
        self.srturboSpin.setMaximum(100.0)
        self.srturboSpin.setObjectName("srturboSpin")
        self.verticalLayout_5.addWidget(self.srturboSpin)
        self.gridLayout_4.addLayout(self.verticalLayout_5, 3, 0, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setMaximumSize(QtCore.QSize(128, 16777215))
        self.label_16.setObjectName("label_16")
        self.verticalLayout_6.addWidget(self.label_16)
        self.avgSpin = QtWidgets.QSpinBox(self.groupBox_3)
        self.avgSpin.setMaximumSize(QtCore.QSize(128, 16777215))
        self.avgSpin.setKeyboardTracking(False)
        self.avgSpin.setMinimum(1)
        self.avgSpin.setMaximum(1024)
        self.avgSpin.setObjectName("avgSpin")
        self.verticalLayout_6.addWidget(self.avgSpin)
        self.gridLayout_4.addLayout(self.verticalLayout_6, 0, 2, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setMaximumSize(QtCore.QSize(128, 16777215))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.rbwSpin = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.rbwSpin.setMaximumSize(QtCore.QSize(128, 16777215))
        self.rbwSpin.setKeyboardTracking(False)
        self.rbwSpin.setDecimals(4)
        self.rbwSpin.setMinimum(0.0001)
        self.rbwSpin.setMaximum(2000.0)
        self.rbwSpin.setProperty("value", 0.01)
        self.rbwSpin.setObjectName("rbwSpin")
        self.verticalLayout_4.addWidget(self.rbwSpin)
        self.gridLayout_4.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.peakCheck = QtWidgets.QCheckBox(self.groupBox_3)
        self.peakCheck.setMaximumSize(QtCore.QSize(128, 16777215))
        self.peakCheck.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.peakCheck.setObjectName("peakCheck")
        self.gridLayout_4.addWidget(self.peakCheck, 4, 0, 1, 1)
        self.syncCheck = QtWidgets.QCheckBox(self.groupBox_3)
        self.syncCheck.setObjectName("syncCheck")
        self.gridLayout_4.addWidget(self.syncCheck, 4, 2, 1, 1)
        self.verticalLayout_9.addWidget(self.groupBox_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem1)
        self.saveBut = QtWidgets.QPushButton(ESA)
        self.saveBut.setMaximumSize(QtCore.QSize(2560, 16777215))
        self.saveBut.setObjectName("saveBut")
        self.verticalLayout_9.addWidget(self.saveBut)
        self.horizontalLayout.addLayout(self.verticalLayout_9)
        self.tabWidget = QtWidgets.QTabWidget(ESA)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.normal = QtWidgets.QWidget()
        self.normal.setObjectName("normal")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.normal)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.graphHolder = QtWidgets.QGridLayout()
        self.graphHolder.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.graphHolder.setObjectName("graphHolder")
        self.gridLayout_5.addLayout(self.graphHolder, 0, 0, 1, 1)
        self.tabWidget.addTab(self.normal, "")
        self.spectrogram = QtWidgets.QWidget()
        self.spectrogram.setObjectName("spectrogram")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.spectrogram)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.sggraphHolder = QtWidgets.QGridLayout()
        self.sggraphHolder.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.sggraphHolder.setObjectName("sggraphHolder")
        self.gridLayout_6.addLayout(self.sggraphHolder, 0, 0, 1, 1)
        self.tabWidget.addTab(self.spectrogram, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(ESA)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ESA)

    def retranslateUi(self, ESA):
        _translate = QtCore.QCoreApplication.translate
        ESA.setWindowTitle(_translate("ESA", "ESA - Virtual Telecom Lab"))
        self.startBut.setText(_translate("ESA", "Run"))
        self.stopBut.setText(_translate("ESA", "Stop"))
        self.singleBut.setText(_translate("ESA", "Single"))
        self.groupBox.setTitle(_translate("ESA", "Horizontal Control"))
        self.label_2.setText(_translate("ESA", "Stop (MHz)"))
        self.label.setText(_translate("ESA", "Start (MHz)"))
        self.label_4.setText(_translate("ESA", "Span (MHz)"))
        self.label_3.setText(_translate("ESA", "Center (MHz)"))
        self.groupBox_2.setTitle(_translate("ESA", "Vertical Control"))
        self.dbmRadio.setText(_translate("ESA", "dBm"))
        self.linRadio.setText(_translate("ESA", "Linear (Auto)"))
        self.label_7.setText(_translate("ESA", "dB/Div"))
        self.label_8.setText(_translate("ESA", "Ref level (dBm)"))
        self.groupBox_3.setTitle(_translate("ESA", "Acquisition Control"))
        self.label_6.setText(_translate("ESA", "Spectrogram N"))
        self.windowCheck.setText(_translate("ESA", "Kaiser Window"))
        self.label_15.setText(_translate("ESA", "Points"))
        self.label_9.setText(_translate("ESA", "Sample Rate Turbo"))
        self.label_16.setText(_translate("ESA", "Averages"))
        self.label_5.setText(_translate("ESA", "RBW (MHz)"))
        self.peakCheck.setText(_translate("ESA", "Peak detection"))
        self.syncCheck.setText(_translate("ESA", "Sync start"))
        self.saveBut.setText(_translate("ESA", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.normal), _translate("ESA", "Normal"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.spectrogram), _translate("ESA", "Spectrogram"))

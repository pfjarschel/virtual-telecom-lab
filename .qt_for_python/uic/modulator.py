# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Stuff\SideWorks\VirtualTelecomLab\components\modulator.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Laser(object):
    def setupUi(self, Laser):
        Laser.setObjectName("Laser")
        Laser.resize(367, 167)
        self.gridLayout = QtWidgets.QGridLayout(Laser)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(Laser)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)
        self.freqSpin = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.freqSpin.setReadOnly(False)
        self.freqSpin.setDecimals(3)
        self.freqSpin.setMinimum(176.471)
        self.freqSpin.setMaximum(428.571)
        self.freqSpin.setProperty("value", 193.548)
        self.freqSpin.setObjectName("freqSpin")
        self.gridLayout_2.addWidget(self.freqSpin, 5, 0, 1, 1)
        self.wlSpin = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.wlSpin.setKeyboardTracking(False)
        self.wlSpin.setDecimals(2)
        self.wlSpin.setMinimum(700.0)
        self.wlSpin.setMaximum(1700.0)
        self.wlSpin.setProperty("value", 1550.0)
        self.wlSpin.setObjectName("wlSpin")
        self.gridLayout_2.addWidget(self.wlSpin, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 3, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Laser)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 4, 0, 1, 1)
        self.mwpwrSpin = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.mwpwrSpin.setMinimum(0.01)
        self.mwpwrSpin.setMaximum(10.0)
        self.mwpwrSpin.setObjectName("mwpwrSpin")
        self.gridLayout_3.addWidget(self.mwpwrSpin, 5, 0, 1, 1)
        self.dbpwrSpin = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.dbpwrSpin.setKeyboardTracking(False)
        self.dbpwrSpin.setDecimals(2)
        self.dbpwrSpin.setMinimum(-20.0)
        self.dbpwrSpin.setMaximum(10.0)
        self.dbpwrSpin.setProperty("value", 0.0)
        self.dbpwrSpin.setObjectName("dbpwrSpin")
        self.gridLayout_3.addWidget(self.dbpwrSpin, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 3, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(Laser)
        QtCore.QMetaObject.connectSlotsByName(Laser)

    def retranslateUi(self, Laser):
        _translate = QtCore.QCoreApplication.translate
        Laser.setWindowTitle(_translate("Laser", "Tunable Laser - Virtual Telecom Lab"))
        self.groupBox.setTitle(_translate("Laser", "Wavelength Control"))
        self.label_3.setText(_translate("Laser", "Frequency (THz)"))
        self.label.setText(_translate("Laser", "Wavelength (nm)"))
        self.groupBox_2.setTitle(_translate("Laser", "Power Control"))
        self.label_4.setText(_translate("Laser", "Power (mW)"))
        self.label_2.setText(_translate("Laser", "Power (dBm)"))

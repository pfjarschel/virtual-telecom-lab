# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Stuff\SideWorks\VirtualTelecomLab\instruments\otdr.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OTDR(object):
    def setupUi(self, OTDR):
        OTDR.setObjectName("OTDR")
        OTDR.resize(926, 537)
        self.gridLayout = QtWidgets.QGridLayout(OTDR)
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
        self.startBut = QtWidgets.QPushButton(OTDR)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startBut.sizePolicy().hasHeightForWidth())
        self.startBut.setSizePolicy(sizePolicy)
        self.startBut.setMinimumSize(QtCore.QSize(0, 0))
        self.startBut.setMaximumSize(QtCore.QSize(72, 16777215))
        self.startBut.setObjectName("startBut")
        self.horizontalLayout_2.addWidget(self.startBut)
        self.stopBut = QtWidgets.QPushButton(OTDR)
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
        self.groupBox = QtWidgets.QGroupBox(OTDR)
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
        self.stopSpin.setDecimals(2)
        self.stopSpin.setMinimum(700.0)
        self.stopSpin.setMaximum(1700.0)
        self.stopSpin.setProperty("value", 1700.0)
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
        self.startSpin.setDecimals(2)
        self.startSpin.setMinimum(700.0)
        self.startSpin.setMaximum(1700.0)
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
        self.spanSpin.setDecimals(2)
        self.spanSpin.setMinimum(700.0)
        self.spanSpin.setMaximum(20000.0)
        self.spanSpin.setProperty("value", 700.0)
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
        self.centerSpin.setDecimals(2)
        self.centerSpin.setMinimum(700.0)
        self.centerSpin.setMaximum(1700.0)
        self.centerSpin.setProperty("value", 700.0)
        self.centerSpin.setObjectName("centerSpin")
        self.verticalLayout_10.addWidget(self.centerSpin)
        self.gridLayout_2.addLayout(self.verticalLayout_10, 3, 0, 1, 1)
        self.verticalLayout_9.addWidget(self.groupBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem1)
        self.saveBut = QtWidgets.QPushButton(OTDR)
        self.saveBut.setMaximumSize(QtCore.QSize(2560, 16777215))
        self.saveBut.setObjectName("saveBut")
        self.verticalLayout_9.addWidget(self.saveBut)
        self.horizontalLayout.addLayout(self.verticalLayout_9)
        self.graphHolder = QtWidgets.QGridLayout()
        self.graphHolder.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.graphHolder.setObjectName("graphHolder")
        self.horizontalLayout.addLayout(self.graphHolder)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(OTDR)
        QtCore.QMetaObject.connectSlotsByName(OTDR)

    def retranslateUi(self, OTDR):
        _translate = QtCore.QCoreApplication.translate
        OTDR.setWindowTitle(_translate("OTDR", "OTDR - Virtual Telecom Lab"))
        self.startBut.setText(_translate("OTDR", "Run"))
        self.stopBut.setText(_translate("OTDR", "Stop"))
        self.groupBox.setTitle(_translate("OTDR", "Pulse Control"))
        self.label_2.setText(_translate("OTDR", "Stop (nm)"))
        self.label.setText(_translate("OTDR", "Start (nm)"))
        self.label_4.setText(_translate("OTDR", "Span (nm)"))
        self.label_3.setText(_translate("OTDR", "Center (nm)"))
        self.saveBut.setText(_translate("OTDR", "Save"))
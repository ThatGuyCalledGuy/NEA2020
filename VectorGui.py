# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Vector_Gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Vector(object):
    def setupUi(self, Vector):
        Vector.setObjectName("Vector")
        Vector.resize(1560, 678)
        self.verticalLayoutWidget = QtWidgets.QWidget(Vector)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 771, 659))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(171, 0))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.PosVecX = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.PosVecX.setMinimum(-99.9)
        self.PosVecX.setObjectName("PosVecX")
        self.verticalLayout_2.addWidget(self.PosVecX)
        self.PosVecY = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.PosVecY.setMinimum(-99.99)
        self.PosVecY.setObjectName("PosVecY")
        self.verticalLayout_2.addWidget(self.PosVecY)
        self.PosVecZ = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.PosVecZ.setMinimum(-99.0)
        self.PosVecZ.setObjectName("PosVecZ")
        self.verticalLayout_2.addWidget(self.PosVecZ)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.D1X = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.D1X.setMinimum(-99.0)
        self.D1X.setObjectName("D1X")
        self.verticalLayout_4.addWidget(self.D1X)
        self.D1Y = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.D1Y.setMinimum(-99.0)
        self.D1Y.setObjectName("D1Y")
        self.verticalLayout_4.addWidget(self.D1Y)
        self.D1Z = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.D1Z.setMinimum(-99.99)
        self.D1Z.setObjectName("D1Z")
        self.verticalLayout_4.addWidget(self.D1Z)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(171, 0))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.D2X = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.D2X.setMinimum(-99.99)
        self.D2X.setObjectName("D2X")
        self.verticalLayout_3.addWidget(self.D2X)
        self.D2Y = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.D2Y.setMinimum(-99.99)
        self.D2Y.setObjectName("D2Y")
        self.verticalLayout_3.addWidget(self.D2Y)
        self.D2Z = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.D2Z.setMinimum(-99.99)
        self.D2Z.setObjectName("D2Z")
        self.verticalLayout_3.addWidget(self.D2Z)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.PosVecButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.PosVecButton.setObjectName("PosVecButton")
        self.horizontalLayout_5.addWidget(self.PosVecButton)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.ResVecButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ResVecButton.setObjectName("ResVecButton")
        self.horizontalLayout_5.addWidget(self.ResVecButton)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.LineButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.LineButton.setObjectName("LineButton")
        self.verticalLayout_6.addWidget(self.LineButton)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem12)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.PlaneButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.PlaneButton.setObjectName("PlaneButton")
        self.verticalLayout_7.addWidget(self.PlaneButton)
        self.NormButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.NormButton.setObjectName("NormButton")
        self.verticalLayout_7.addWidget(self.NormButton)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem13)
        self.ClearButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ClearButton.setObjectName("ClearButton")
        self.horizontalLayout_5.addWidget(self.ClearButton)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem14)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Vector)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(790, 10, 761, 661))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.InsertGraph = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.InsertGraph.setContentsMargins(0, 0, 0, 0)
        self.InsertGraph.setObjectName("InsertGraph")

        self.retranslateUi(Vector)
        QtCore.QMetaObject.connectSlotsByName(Vector)

    def retranslateUi(self, Vector):
        _translate = QtCore.QCoreApplication.translate
        Vector.setWindowTitle(_translate("Vector", "Vector Modelling"))
        self.label.setText(_translate("Vector", "Position Vector"))
        self.label_3.setText(_translate("Vector", "<html><head/><body><p>Direction Vector (Lines and Planes)</p><p>(Also 2nd vector with Resultants)</p></body></html>"))
        self.label_2.setText(_translate("Vector", "Direction Vector 2 (Planes Only)"))
        self.PosVecButton.setText(_translate("Vector", "Vector"))
        self.ResVecButton.setText(_translate("Vector", "Resultant"))
        self.LineButton.setText(_translate("Vector", "Line"))
        self.PlaneButton.setText(_translate("Vector", "Plane"))
        self.NormButton.setText(_translate("Vector", "Normal"))
        self.ClearButton.setText(_translate("Vector", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Vector = QtWidgets.QDialog()
    ui = Ui_Vector()
    ui.setupUi(Vector)
    Vector.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Complex_Gui_1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainGui(object):
    def setupUi(self, MainGui):
        MainGui.setObjectName("MainGui")
        MainGui.resize(1469, 515)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainGui.sizePolicy().hasHeightForWidth())
        MainGui.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QtWidgets.QWidget(MainGui)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 661, 491))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(16, 14))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.RealPartBox = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.RealPartBox.setMinimum(-99.99)
        self.RealPartBox.setObjectName("RealPartBox")
        self.verticalLayout_2.addWidget(self.RealPartBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.ImaginaryPartBox = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.ImaginaryPartBox.setMinimum(-99.99)
        self.ImaginaryPartBox.setObjectName("ImaginaryPartBox")
        self.verticalLayout_3.addWidget(self.ImaginaryPartBox)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.AddToGraphButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.AddToGraphButton.setObjectName("AddToGraphButton")
        self.horizontalLayout_3.addWidget(self.AddToGraphButton)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.LociButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.LociButton.setObjectName("LociButton")
        self.horizontalLayout_5.addWidget(self.LociButton)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.RootButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.RootButton.setObjectName("RootButton")
        self.horizontalLayout_5.addWidget(self.RootButton)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem12)
        self.VectorButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.VectorButton.setObjectName("VectorButton")
        self.horizontalLayout_5.addWidget(self.VectorButton)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem13)
        self.MatrixButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.MatrixButton.setObjectName("MatrixButton")
        self.horizontalLayout_5.addWidget(self.MatrixButton)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem14)
        self.CalculatorButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.CalculatorButton.setObjectName("CalculatorButton")
        self.horizontalLayout_5.addWidget(self.CalculatorButton)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem15)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(MainGui)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(680, 10, 201, 491))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.ClearGraphListButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.ClearGraphListButton.setObjectName("ClearGraphListButton")
        self.verticalLayout_4.addWidget(self.ClearGraphListButton)
        self.ListDisplay = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.ListDisplay.setObjectName("ListDisplay")
        self.verticalLayout_4.addWidget(self.ListDisplay)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem16)
        self.LabelRadio = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.LabelRadio.setObjectName("LabelRadio")
        self.horizontalLayout_6.addWidget(self.LabelRadio)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem17)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.MakeGraphButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.MakeGraphButton.setObjectName("MakeGraphButton")
        self.verticalLayout_4.addWidget(self.MakeGraphButton)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(MainGui)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(890, 10, 571, 501))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.InsertGraph = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.InsertGraph.setContentsMargins(0, 0, 0, 0)
        self.InsertGraph.setObjectName("InsertGraph")

        self.retranslateUi(MainGui)
        QtCore.QMetaObject.connectSlotsByName(MainGui)

    def retranslateUi(self, MainGui):
        _translate = QtCore.QCoreApplication.translate
        MainGui.setWindowTitle(_translate("MainGui", "Argand Diagram"))
        self.label.setText(_translate("MainGui", "Real Part"))
        self.label_2.setText(_translate("MainGui", "Imaginary Part"))
        self.AddToGraphButton.setText(_translate("MainGui", "Add to Graph List"))
        self.LociButton.setText(_translate("MainGui", "Loci"))
        self.RootButton.setText(_translate("MainGui", "Roots"))
        self.VectorButton.setText(_translate("MainGui", "Vectors"))
        self.MatrixButton.setText(_translate("MainGui", "Matrices"))
        self.CalculatorButton.setText(_translate("MainGui", "Calculator"))
        self.ClearGraphListButton.setText(_translate("MainGui", "Clear"))
        self.LabelRadio.setText(_translate("MainGui", "Labels"))
        self.MakeGraphButton.setText(_translate("MainGui", "Make Graph"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainGui = QtWidgets.QDialog()
    ui = Ui_MainGui()
    ui.setupUi(MainGui)
    MainGui.show()
    sys.exit(app.exec_())

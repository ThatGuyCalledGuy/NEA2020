# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Complex_Roots.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 757)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 771, 691))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.InsertGraph = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.InsertGraph.setContentsMargins(0, 0, 0, 0)
        self.InsertGraph.setObjectName("InsertGraph")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 771, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.MakeRootButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.MakeRootButton.setObjectName("MakeRootButton")
        self.horizontalLayout_3.addWidget(self.MakeRootButton)
        self.NthRoot = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.NthRoot.setMinimum(1)
        self.NthRoot.setMaximum(100)
        self.NthRoot.setObjectName("NthRoot")
        self.horizontalLayout_3.addWidget(self.NthRoot)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Roots of Unity"))
        self.MakeRootButton.setText(_translate("Dialog", "Plot"))
        self.label.setText(_translate("Dialog", "th Roots"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


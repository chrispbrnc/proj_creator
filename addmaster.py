# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addmaster.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_AddMasterDialog(object):
    def setupUi(self, AddMasterDialog):
        AddMasterDialog.setObjectName(_fromUtf8("AddMasterDialog"))
        AddMasterDialog.resize(394, 303)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        AddMasterDialog.setFont(font)
        self.buttonBox = QtGui.QDialogButtonBox(AddMasterDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.le_key = QtGui.QLineEdit(AddMasterDialog)
        self.le_key.setGeometry(QtCore.QRect(162, 40, 181, 24))
        self.le_key.setObjectName(_fromUtf8("le_key"))
        self.le_area = QtGui.QLineEdit(AddMasterDialog)
        self.le_area.setGeometry(QtCore.QRect(162, 100, 181, 24))
        self.le_area.setObjectName(_fromUtf8("le_area"))
        self.le_line = QtGui.QLineEdit(AddMasterDialog)
        self.le_line.setGeometry(QtCore.QRect(162, 160, 181, 24))
        self.le_line.setObjectName(_fromUtf8("le_line"))
        self.label = QtGui.QLabel(AddMasterDialog)
        self.label.setGeometry(QtCore.QRect(70, 40, 51, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(AddMasterDialog)
        self.label_2.setGeometry(QtCore.QRect(70, 100, 61, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(AddMasterDialog)
        self.label_3.setGeometry(QtCore.QRect(70, 160, 51, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(AddMasterDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AddMasterDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AddMasterDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddMasterDialog)

    def retranslateUi(self, AddMasterDialog):
        AddMasterDialog.setWindowTitle(_translate("AddMasterDialog", "Add Master Flow", None))
        self.label.setText(_translate("AddMasterDialog", "Key:", None))
        self.label_2.setText(_translate("AddMasterDialog", "Area:", None))
        self.label_3.setText(_translate("AddMasterDialog", "Line:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    AddMasterDialog = QtGui.QDialog()
    ui = Ui_AddMasterDialog()
    ui.setupUi(AddMasterDialog)
    AddMasterDialog.show()
    sys.exit(app.exec_())


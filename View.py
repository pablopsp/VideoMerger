# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(400, 300)
        MainWindow.setMouseTracking(False)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.look_for_dir_button = QtWidgets.QPushButton(self.centralwidget)
        self.look_for_dir_button.setGeometry(QtCore.QRect(40, 40, 91, 21))
        self.look_for_dir_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.look_for_dir_button.setObjectName("look_for_dir_button")
        self.dir_name = QtWidgets.QLineEdit(self.centralwidget)
        self.dir_name.setGeometry(QtCore.QRect(140, 40, 221, 21))
        self.dir_name.setAutoFillBackground(False)
        self.dir_name.setReadOnly(True)
        self.dir_name.setObjectName("dir_name")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 12, 321, 16))
        self.label.setObjectName("label")
        self.init_video_maker = QtWidgets.QPushButton(self.centralwidget)
        self.init_video_maker.setEnabled(False)
        self.init_video_maker.setGeometry(QtCore.QRect(200, 70, 161, 21))
        self.init_video_maker.setObjectName("init_video_maker")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Video bitrate change"))
        self.look_for_dir_button.setText(_translate("MainWindow", "Buscar directorio"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Busque el directorio el cual contiene los videos trozeados</span></p></body></html>"))
        self.init_video_maker.setText(_translate("MainWindow", "Juntar videos y cambiar bitrate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BotonSalir = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BotonSalir.setGeometry(QtCore.QRect(340, 250, 120, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BotonSalir.sizePolicy().hasHeightForWidth())
        self.BotonSalir.setSizePolicy(sizePolicy)
        self.BotonSalir.setMinimumSize(QtCore.QSize(120, 20))
        self.BotonSalir.setMaximumSize(QtCore.QSize(120, 20))
        self.BotonSalir.setStyleSheet("")
        self.BotonSalir.setObjectName("BotonSalir")
        self.lblTitulo = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblTitulo.setGeometry(QtCore.QRect(340, 130, 120, 20))
        self.lblTitulo.setMinimumSize(QtCore.QSize(120, 20))
        self.lblTitulo.setMaximumSize(QtCore.QSize(240, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.lblTitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblTitulo.setObjectName("lblTitulo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(parent=self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Salir = QtGui.QAction(parent=MainWindow)
        self.Salir.setObjectName("Salir")
        self.actionAcerca_de = QtGui.QAction(parent=MainWindow)
        self.actionAcerca_de.setObjectName("actionAcerca_de")
        self.menuArchivo.addAction(self.Salir)
        self.menuHelp.addAction(self.actionAcerca_de)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CarTest"))
        self.BotonSalir.setText(_translate("MainWindow", "Salir"))
        self.lblTitulo.setText(_translate("MainWindow", "CAR TEIS"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuHelp.setTitle(_translate("MainWindow", "Ayuda"))
        self.Salir.setText(_translate("MainWindow", "Salir"))
        self.actionAcerca_de.setText(_translate("MainWindow", "Acerca de ..."))
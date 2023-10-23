# Form implementation generated from reading ui file '.\templates\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.5.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1078, 822)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 768))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\templates\\../../.designer/backup/img/Logo1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.TabPrincipal = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.TabPrincipal.setEnabled(True)
        self.TabPrincipal.setMinimumSize(QtCore.QSize(300, 20))
        self.TabPrincipal.setObjectName("TabPrincipal")
        self.panelDrivers = QtWidgets.QWidget()
        self.panelDrivers.setObjectName("panelDrivers")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.panelDrivers)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(parent=self.panelDrivers)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(800, 200))
        self.frame.setMaximumSize(QtCore.QSize(1100, 250))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.txtDni = QtWidgets.QLineEdit(parent=self.frame)
        self.txtDni.setGeometry(QtCore.QRect(210, 10, 160, 20))
        self.txtDni.setMinimumSize(QtCore.QSize(50, 20))
        self.txtDni.setMaximumSize(QtCore.QSize(200, 20))
        self.txtDni.setText("")
        self.txtDni.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txtDni.setObjectName("txtDni")
        self.txtNombre = QtWidgets.QLineEdit(parent=self.frame)
        self.txtNombre.setGeometry(QtCore.QRect(460, 50, 300, 20))
        self.txtNombre.setMinimumSize(QtCore.QSize(300, 20))
        self.txtNombre.setMaximumSize(QtCore.QSize(300, 20))
        self.txtNombre.setObjectName("txtNombre")
        self.lblApel = QtWidgets.QLabel(parent=self.frame)
        self.lblApel.setGeometry(QtCore.QRect(10, 50, 50, 20))
        self.lblApel.setMinimumSize(QtCore.QSize(50, 20))
        self.lblApel.setMaximumSize(QtCore.QSize(100, 20))
        self.lblApel.setObjectName("lblApel")
        self.lblFechaAlta = QtWidgets.QLabel(parent=self.frame)
        self.lblFechaAlta.setGeometry(QtCore.QRect(490, 10, 50, 20))
        self.lblFechaAlta.setMinimumSize(QtCore.QSize(50, 20))
        self.lblFechaAlta.setMaximumSize(QtCore.QSize(50, 20))
        self.lblFechaAlta.setObjectName("lblFechaAlta")
        self.lblNombre = QtWidgets.QLabel(parent=self.frame)
        self.lblNombre.setGeometry(QtCore.QRect(390, 50, 50, 20))
        self.lblNombre.setMinimumSize(QtCore.QSize(50, 20))
        self.lblNombre.setObjectName("lblNombre")
        self.lblDNI = QtWidgets.QLabel(parent=self.frame)
        self.lblDNI.setGeometry(QtCore.QRect(180, 10, 91, 20))
        self.lblDNI.setMinimumSize(QtCore.QSize(50, 20))
        self.lblDNI.setMaximumSize(QtCore.QSize(100, 20))
        self.lblDNI.setObjectName("lblDNI")
        self.lblcod = QtWidgets.QLabel(parent=self.frame)
        self.lblcod.setGeometry(QtCore.QRect(10, 10, 91, 20))
        self.lblcod.setMinimumSize(QtCore.QSize(50, 20))
        self.lblcod.setMaximumSize(QtCore.QSize(100, 20))
        self.lblcod.setObjectName("lblcod")
        self.txtApel = QtWidgets.QLineEdit(parent=self.frame)
        self.txtApel.setGeometry(QtCore.QRect(70, 50, 300, 20))
        self.txtApel.setMinimumSize(QtCore.QSize(300, 20))
        self.txtApel.setMaximumSize(QtCore.QSize(300, 20))
        self.txtApel.setObjectName("txtApel")
        self.lblcoddb = QtWidgets.QLabel(parent=self.frame)
        self.lblcoddb.setGeometry(QtCore.QRect(90, 10, 81, 20))
        self.lblcoddb.setMinimumSize(QtCore.QSize(50, 20))
        self.lblcoddb.setMaximumSize(QtCore.QSize(100, 20))
        self.lblcoddb.setAutoFillBackground(False)
        self.lblcoddb.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.lblcoddb.setText("")
        self.lblcoddb.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblcoddb.setObjectName("lblcoddb")
        self.txtFecha = QtWidgets.QLineEdit(parent=self.frame)
        self.txtFecha.setGeometry(QtCore.QRect(570, 10, 150, 20))
        self.txtFecha.setMinimumSize(QtCore.QSize(150, 20))
        self.txtFecha.setMaximumSize(QtCore.QSize(150, 20))
        self.txtFecha.setObjectName("txtFecha")
        self.btnCalendar = QtWidgets.QPushButton(parent=self.frame)
        self.btnCalendar.setGeometry(QtCore.QRect(720, 10, 50, 20))
        self.btnCalendar.setMinimumSize(QtCore.QSize(50, 20))
        self.btnCalendar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\templates\\../../.designer/backup/img/Calendar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnCalendar.setIcon(icon1)
        self.btnCalendar.setIconSize(QtCore.QSize(25, 25))
        self.btnCalendar.setDefault(False)
        self.btnCalendar.setFlat(True)
        self.btnCalendar.setObjectName("btnCalendar")
        self.lblValidarDni = QtWidgets.QLabel(parent=self.frame)
        self.lblValidarDni.setGeometry(QtCore.QRect(360, 10, 60, 30))
        self.lblValidarDni.setMinimumSize(QtCore.QSize(60, 30))
        self.lblValidarDni.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lblValidarDni.setFont(font)
        self.lblValidarDni.setText("")
        self.lblValidarDni.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblValidarDni.setObjectName("lblValidarDni")
        self.lblDir = QtWidgets.QLabel(parent=self.frame)
        self.lblDir.setGeometry(QtCore.QRect(10, 90, 50, 20))
        self.lblDir.setMinimumSize(QtCore.QSize(50, 20))
        self.lblDir.setObjectName("lblDir")
        self.txtDir = QtWidgets.QLineEdit(parent=self.frame)
        self.txtDir.setGeometry(QtCore.QRect(70, 90, 300, 20))
        self.txtDir.setMinimumSize(QtCore.QSize(300, 20))
        self.txtDir.setObjectName("txtDir")
        self.lblTlf = QtWidgets.QLabel(parent=self.frame)
        self.lblTlf.setGeometry(QtCore.QRect(10, 130, 50, 20))
        self.lblTlf.setMinimumSize(QtCore.QSize(50, 20))
        self.lblTlf.setObjectName("lblTlf")
        self.txtTlf = QtWidgets.QLineEdit(parent=self.frame)
        self.txtTlf.setGeometry(QtCore.QRect(70, 130, 100, 20))
        self.txtTlf.setMinimumSize(QtCore.QSize(100, 20))
        self.txtTlf.setMaximumSize(QtCore.QSize(100, 20))
        self.txtTlf.setObjectName("txtTlf")
        self.lblLocalidad = QtWidgets.QLabel(parent=self.frame)
        self.lblLocalidad.setGeometry(QtCore.QRect(650, 90, 50, 20))
        self.lblLocalidad.setMinimumSize(QtCore.QSize(50, 20))
        self.lblLocalidad.setObjectName("lblLocalidad")
        self.cmbProv = QtWidgets.QComboBox(parent=self.frame)
        self.cmbProv.setGeometry(QtCore.QRect(450, 90, 191, 22))
        self.cmbProv.setMinimumSize(QtCore.QSize(120, 20))
        self.cmbProv.setObjectName("cmbProv")
        self.lblProvincia = QtWidgets.QLabel(parent=self.frame)
        self.lblProvincia.setGeometry(QtCore.QRect(390, 90, 50, 20))
        self.lblProvincia.setMinimumSize(QtCore.QSize(50, 20))
        self.lblProvincia.setObjectName("lblProvincia")
        self.lblSalario = QtWidgets.QLabel(parent=self.frame)
        self.lblSalario.setGeometry(QtCore.QRect(180, 130, 50, 20))
        self.lblSalario.setMinimumSize(QtCore.QSize(50, 20))
        self.lblSalario.setObjectName("lblSalario")
        self.txtSalario = QtWidgets.QLineEdit(parent=self.frame)
        self.txtSalario.setGeometry(QtCore.QRect(240, 130, 100, 20))
        self.txtSalario.setMinimumSize(QtCore.QSize(100, 20))
        self.txtSalario.setMaximumSize(QtCore.QSize(100, 20))
        self.txtSalario.setObjectName("txtSalario")
        self.lblCarnet = QtWidgets.QLabel(parent=self.frame)
        self.lblCarnet.setGeometry(QtCore.QRect(10, 160, 100, 20))
        self.lblCarnet.setMinimumSize(QtCore.QSize(100, 20))
        self.lblCarnet.setMaximumSize(QtCore.QSize(100, 20))
        self.lblCarnet.setObjectName("lblCarnet")
        self.chkA = QtWidgets.QCheckBox(parent=self.frame)
        self.chkA.setGeometry(QtCore.QRect(100, 160, 70, 17))
        self.chkA.setObjectName("chkA")
        self.chkB = QtWidgets.QCheckBox(parent=self.frame)
        self.chkB.setGeometry(QtCore.QRect(140, 160, 70, 17))
        self.chkB.setObjectName("chkB")
        self.chkC = QtWidgets.QCheckBox(parent=self.frame)
        self.chkC.setGeometry(QtCore.QRect(180, 160, 70, 17))
        self.chkC.setObjectName("chkC")
        self.chkD = QtWidgets.QCheckBox(parent=self.frame)
        self.chkD.setGeometry(QtCore.QRect(220, 160, 70, 17))
        self.chkD.setObjectName("chkD")
        self.lblHistorico = QtWidgets.QLabel(parent=self.frame)
        self.lblHistorico.setGeometry(QtCore.QRect(390, 130, 50, 20))
        self.lblHistorico.setMinimumSize(QtCore.QSize(50, 20))
        self.lblHistorico.setObjectName("lblHistorico")
        self.rbtAlta = QtWidgets.QRadioButton(parent=self.frame)
        self.rbtAlta.setGeometry(QtCore.QRect(440, 130, 82, 20))
        self.rbtAlta.setMinimumSize(QtCore.QSize(50, 20))
        self.rbtAlta.setObjectName("rbtAlta")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.rbtAlta)
        self.rbtBaja = QtWidgets.QRadioButton(parent=self.frame)
        self.rbtBaja.setGeometry(QtCore.QRect(490, 130, 82, 20))
        self.rbtBaja.setMinimumSize(QtCore.QSize(50, 20))
        self.rbtBaja.setObjectName("rbtBaja")
        self.buttonGroup.addButton(self.rbtBaja)
        self.rbtTodos = QtWidgets.QRadioButton(parent=self.frame)
        self.rbtTodos.setGeometry(QtCore.QRect(540, 130, 82, 20))
        self.rbtTodos.setMinimumSize(QtCore.QSize(50, 20))
        self.rbtTodos.setChecked(True)
        self.rbtTodos.setObjectName("rbtTodos")
        self.buttonGroup.addButton(self.rbtTodos)
        self.btnAltaDriver = QtWidgets.QPushButton(parent=self.frame)
        self.btnAltaDriver.setGeometry(QtCore.QRect(300, 220, 75, 20))
        self.btnAltaDriver.setMinimumSize(QtCore.QSize(75, 20))
        self.btnAltaDriver.setMaximumSize(QtCore.QSize(75, 20))
        self.btnAltaDriver.setObjectName("btnAltaDriver")
        self.btnModifDriver = QtWidgets.QPushButton(parent=self.frame)
        self.btnModifDriver.setGeometry(QtCore.QRect(400, 220, 90, 20))
        self.btnModifDriver.setMinimumSize(QtCore.QSize(90, 20))
        self.btnModifDriver.setMaximumSize(QtCore.QSize(90, 20))
        self.btnModifDriver.setObjectName("btnModifDriver")
        self.btnBajaDriver = QtWidgets.QPushButton(parent=self.frame)
        self.btnBajaDriver.setGeometry(QtCore.QRect(520, 220, 75, 20))
        self.btnBajaDriver.setMinimumSize(QtCore.QSize(75, 20))
        self.btnBajaDriver.setMaximumSize(QtCore.QSize(75, 20))
        self.btnBajaDriver.setObjectName("btnBajaDriver")
        self.cmbProv_2 = QtWidgets.QComboBox(parent=self.frame)
        self.cmbProv_2.setGeometry(QtCore.QRect(700, 90, 191, 22))
        self.cmbProv_2.setMinimumSize(QtCore.QSize(120, 20))
        self.cmbProv_2.setObjectName("cmbProv_2")
        self.lblValidarDni.raise_()
        self.txtNombre.raise_()
        self.lblApel.raise_()
        self.lblFechaAlta.raise_()
        self.lblNombre.raise_()
        self.lblDNI.raise_()
        self.lblcod.raise_()
        self.txtApel.raise_()
        self.lblcoddb.raise_()
        self.txtFecha.raise_()
        self.btnCalendar.raise_()
        self.txtDni.raise_()
        self.lblDir.raise_()
        self.txtDir.raise_()
        self.lblTlf.raise_()
        self.txtTlf.raise_()
        self.lblLocalidad.raise_()
        self.cmbProv.raise_()
        self.lblProvincia.raise_()
        self.lblSalario.raise_()
        self.txtSalario.raise_()
        self.lblCarnet.raise_()
        self.chkA.raise_()
        self.chkB.raise_()
        self.chkC.raise_()
        self.chkD.raise_()
        self.lblHistorico.raise_()
        self.rbtAlta.raise_()
        self.rbtBaja.raise_()
        self.rbtTodos.raise_()
        self.btnAltaDriver.raise_()
        self.btnModifDriver.raise_()
        self.btnBajaDriver.raise_()
        self.cmbProv_2.raise_()
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.tabDrivers = QtWidgets.QTableWidget(parent=self.panelDrivers)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabDrivers.sizePolicy().hasHeightForWidth())
        self.tabDrivers.setSizePolicy(sizePolicy)
        self.tabDrivers.setAlternatingRowColors(True)
        self.tabDrivers.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tabDrivers.setObjectName("tabDrivers")
        self.tabDrivers.setColumnCount(6)
        self.tabDrivers.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabDrivers.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabDrivers.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabDrivers.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabDrivers.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabDrivers.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabDrivers.setHorizontalHeaderItem(5, item)
        self.tabDrivers.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.tabDrivers, 1, 0, 1, 1)
        self.TabPrincipal.addTab(self.panelDrivers, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(160, 100, 201, 101))
        self.label_2.setObjectName("label_2")
        self.TabPrincipal.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.TabPrincipal, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1078, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(parent=self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(parent=MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionSalir = QtGui.QAction(parent=MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\templates\\../../.designer/backup/img/exit_icon-icons.com_70975.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionSalir.setIcon(icon2)
        self.actionSalir.setObjectName("actionSalir")
        self.actionAcerca_de = QtGui.QAction(parent=MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\templates\\../../.designer/backup/img/sign-question-icon_34359.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionAcerca_de.setIcon(icon3)
        self.actionAcerca_de.setObjectName("actionAcerca_de")
        self.barSalir = QtGui.QAction(parent=MainWindow)
        self.barSalir.setIcon(icon2)
        self.barSalir.setObjectName("barSalir")
        self.barLimpiarPanel = QtGui.QAction(parent=MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(".\\templates\\../../.designer/backup/img/reload_icon-icons.com_64795.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.barLimpiarPanel.setIcon(icon4)
        self.barLimpiarPanel.setObjectName("barLimpiarPanel")
        self.menuArchivo.addAction(self.actionSalir)
        self.menuHelp.addAction(self.actionAcerca_de)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.barLimpiarPanel)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.barSalir)

        self.retranslateUi(MainWindow)
        self.TabPrincipal.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txtDni, self.txtFecha)
        MainWindow.setTabOrder(self.txtFecha, self.btnCalendar)
        MainWindow.setTabOrder(self.btnCalendar, self.txtApel)
        MainWindow.setTabOrder(self.txtApel, self.txtNombre)
        MainWindow.setTabOrder(self.txtNombre, self.txtDir)
        MainWindow.setTabOrder(self.txtDir, self.cmbProv)
        MainWindow.setTabOrder(self.cmbProv, self.txtTlf)
        MainWindow.setTabOrder(self.txtTlf, self.txtSalario)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CarTest"))
        self.lblApel.setText(_translate("MainWindow", "Apellidos"))
        self.lblFechaAlta.setText(_translate("MainWindow", "Fecha Alta"))
        self.lblNombre.setText(_translate("MainWindow", "Nombre"))
        self.lblDNI.setText(_translate("MainWindow", "DNI"))
        self.lblcod.setText(_translate("MainWindow", "Codigo Driver"))
        self.lblDir.setText(_translate("MainWindow", "Direccion"))
        self.lblTlf.setText(_translate("MainWindow", "Telefono"))
        self.lblLocalidad.setText(_translate("MainWindow", "Localidad"))
        self.lblProvincia.setText(_translate("MainWindow", "Provincia"))
        self.lblSalario.setText(_translate("MainWindow", "Salario"))
        self.lblCarnet.setText(_translate("MainWindow", "Tipo de Carnet"))
        self.chkA.setText(_translate("MainWindow", "A"))
        self.chkB.setText(_translate("MainWindow", "B"))
        self.chkC.setText(_translate("MainWindow", "C"))
        self.chkD.setText(_translate("MainWindow", "D"))
        self.lblHistorico.setText(_translate("MainWindow", "Historico"))
        self.rbtAlta.setText(_translate("MainWindow", "Alta"))
        self.rbtBaja.setText(_translate("MainWindow", "Baja"))
        self.rbtTodos.setText(_translate("MainWindow", "Todos"))
        self.btnAltaDriver.setText(_translate("MainWindow", "Alta Driver"))
        self.btnModifDriver.setText(_translate("MainWindow", "Modificar Driver"))
        self.btnBajaDriver.setText(_translate("MainWindow", "Baja Driver"))
        item = self.tabDrivers.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Código"))
        item = self.tabDrivers.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tabDrivers.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Apellidos"))
        item = self.tabDrivers.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Telefono"))
        item = self.tabDrivers.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Tipo de Carnet"))
        item = self.tabDrivers.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Fecha Baja"))
        self.TabPrincipal.setTabText(self.TabPrincipal.indexOf(self.panelDrivers), _translate("MainWindow", "Conductores"))
        self.label_2.setText(_translate("MainWindow", "Esto es la Pestaña 2"))
        self.TabPrincipal.setTabText(self.TabPrincipal.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuHelp.setTitle(_translate("MainWindow", "Ayuda"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionAcerca_de.setText(_translate("MainWindow", "Acerca de ..."))
        self.barSalir.setText(_translate("MainWindow", "Salir"))
        self.barLimpiarPanel.setText(_translate("MainWindow", "LimpiarPanel"))

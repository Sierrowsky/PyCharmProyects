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
        MainWindow.resize(1079, 822)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 768))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\templates\\../../../.designer/backup/img/Logo1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
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
        self.gridLayout_2.addWidget(self.tabDrivers, 2, 0, 1, 1)
        self.frame = QtWidgets.QFrame(parent=self.panelDrivers)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(800, 200))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 250))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 161, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblcod = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.lblcod.setMinimumSize(QtCore.QSize(50, 20))
        self.lblcod.setMaximumSize(QtCore.QSize(100, 20))
        self.lblcod.setObjectName("lblcod")
        self.horizontalLayout.addWidget(self.lblcod)
        self.lblcoddb = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.lblcoddb.setMinimumSize(QtCore.QSize(50, 20))
        self.lblcoddb.setMaximumSize(QtCore.QSize(100, 20))
        self.lblcoddb.setAutoFillBackground(False)
        self.lblcoddb.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.lblcoddb.setText("")
        self.lblcoddb.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblcoddb.setObjectName("lblcoddb")
        self.horizontalLayout.addWidget(self.lblcoddb)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.frame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(190, 10, 251, 32))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblDNI = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        self.lblDNI.setMinimumSize(QtCore.QSize(50, 20))
        self.lblDNI.setMaximumSize(QtCore.QSize(100, 20))
        self.lblDNI.setObjectName("lblDNI")
        self.horizontalLayout_2.addWidget(self.lblDNI)
        self.txtDni = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_2)
        self.txtDni.setMinimumSize(QtCore.QSize(50, 20))
        self.txtDni.setMaximumSize(QtCore.QSize(200, 20))
        self.txtDni.setText("")
        self.txtDni.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txtDni.setObjectName("txtDni")
        self.horizontalLayout_2.addWidget(self.txtDni)
        self.lblValidarDni = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
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
        self.horizontalLayout_2.addWidget(self.lblValidarDni)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(parent=self.frame)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(470, 10, 264, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblFechaAlta = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_3)
        self.lblFechaAlta.setMinimumSize(QtCore.QSize(50, 20))
        self.lblFechaAlta.setMaximumSize(QtCore.QSize(50, 20))
        self.lblFechaAlta.setObjectName("lblFechaAlta")
        self.horizontalLayout_3.addWidget(self.lblFechaAlta)
        self.txtFecha = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_3)
        self.txtFecha.setMinimumSize(QtCore.QSize(150, 20))
        self.txtFecha.setMaximumSize(QtCore.QSize(150, 20))
        self.txtFecha.setObjectName("txtFecha")
        self.horizontalLayout_3.addWidget(self.txtFecha)
        self.btnCalendar = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_3)
        self.btnCalendar.setMinimumSize(QtCore.QSize(50, 20))
        self.btnCalendar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\templates\\../../../.designer/backup/img/Calendar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnCalendar.setIcon(icon1)
        self.btnCalendar.setIconSize(QtCore.QSize(25, 25))
        self.btnCalendar.setDefault(False)
        self.btnCalendar.setFlat(True)
        self.btnCalendar.setObjectName("btnCalendar")
        self.horizontalLayout_3.addWidget(self.btnCalendar)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(parent=self.frame)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 50, 361, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lblApel = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_4)
        self.lblApel.setMinimumSize(QtCore.QSize(50, 20))
        self.lblApel.setMaximumSize(QtCore.QSize(50, 20))
        self.lblApel.setObjectName("lblApel")
        self.horizontalLayout_4.addWidget(self.lblApel)
        self.txtApel = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_4)
        self.txtApel.setMinimumSize(QtCore.QSize(300, 20))
        self.txtApel.setMaximumSize(QtCore.QSize(300, 20))
        self.txtApel.setObjectName("txtApel")
        self.horizontalLayout_4.addWidget(self.txtApel)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(parent=self.frame)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 90, 361, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lblDir = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_5)
        self.lblDir.setMinimumSize(QtCore.QSize(50, 20))
        self.lblDir.setObjectName("lblDir")
        self.horizontalLayout_5.addWidget(self.lblDir)
        self.txtDir = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_5)
        self.txtDir.setMinimumSize(QtCore.QSize(300, 20))
        self.txtDir.setObjectName("txtDir")
        self.horizontalLayout_5.addWidget(self.txtDir)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(parent=self.frame)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(390, 50, 358, 31))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lblNombre = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_6)
        self.lblNombre.setMinimumSize(QtCore.QSize(50, 20))
        self.lblNombre.setObjectName("lblNombre")
        self.horizontalLayout_6.addWidget(self.lblNombre)
        self.txtNombre = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_6)
        self.txtNombre.setMinimumSize(QtCore.QSize(300, 20))
        self.txtNombre.setMaximumSize(QtCore.QSize(300, 20))
        self.txtNombre.setObjectName("txtNombre")
        self.horizontalLayout_6.addWidget(self.txtNombre)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(parent=self.frame)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(390, 90, 178, 31))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lblProvincia = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_7)
        self.lblProvincia.setMinimumSize(QtCore.QSize(50, 20))
        self.lblProvincia.setObjectName("lblProvincia")
        self.horizontalLayout_7.addWidget(self.lblProvincia)
        self.cmbProv = QtWidgets.QComboBox(parent=self.horizontalLayoutWidget_7)
        self.cmbProv.setMinimumSize(QtCore.QSize(120, 20))
        self.cmbProv.setObjectName("cmbProv")
        self.horizontalLayout_7.addWidget(self.cmbProv)
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(parent=self.frame)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(570, 90, 178, 31))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lblLocalidad = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_8)
        self.lblLocalidad.setMinimumSize(QtCore.QSize(50, 20))
        self.lblLocalidad.setObjectName("lblLocalidad")
        self.horizontalLayout_8.addWidget(self.lblLocalidad)
        self.cmbMun = QtWidgets.QComboBox(parent=self.horizontalLayoutWidget_8)
        self.cmbMun.setMinimumSize(QtCore.QSize(120, 20))
        self.cmbMun.setObjectName("cmbMun")
        self.horizontalLayout_8.addWidget(self.cmbMun)
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(parent=self.frame)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(10, 120, 241, 32))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lblTlf = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_9)
        self.lblTlf.setMinimumSize(QtCore.QSize(50, 20))
        self.lblTlf.setObjectName("lblTlf")
        self.horizontalLayout_9.addWidget(self.lblTlf)
        self.txtTlf = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_9)
        self.txtTlf.setMinimumSize(QtCore.QSize(100, 20))
        self.txtTlf.setMaximumSize(QtCore.QSize(100, 20))
        self.txtTlf.setObjectName("txtTlf")
        self.horizontalLayout_9.addWidget(self.txtTlf)
        self.lblValidarTlf = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_9)
        self.lblValidarTlf.setMinimumSize(QtCore.QSize(60, 30))
        self.lblValidarTlf.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lblValidarTlf.setFont(font)
        self.lblValidarTlf.setText("")
        self.lblValidarTlf.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblValidarTlf.setObjectName("lblValidarTlf")
        self.horizontalLayout_9.addWidget(self.lblValidarTlf)
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(parent=self.frame)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(250, 120, 264, 31))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lblSalario = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_10)
        self.lblSalario.setMinimumSize(QtCore.QSize(50, 20))
        self.lblSalario.setObjectName("lblSalario")
        self.horizontalLayout_10.addWidget(self.lblSalario)
        self.txtSalario = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_10)
        self.txtSalario.setMinimumSize(QtCore.QSize(100, 20))
        self.txtSalario.setMaximumSize(QtCore.QSize(100, 20))
        self.txtSalario.setObjectName("txtSalario")
        self.horizontalLayout_10.addWidget(self.txtSalario)
        self.lblSalarioT = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_10)
        self.lblSalarioT.setMinimumSize(QtCore.QSize(100, 20))
        self.lblSalarioT.setText("")
        self.lblSalarioT.setObjectName("lblSalarioT")
        self.horizontalLayout_10.addWidget(self.lblSalarioT)
        self.horizontalLayoutWidget_11 = QtWidgets.QWidget(parent=self.frame)
        self.horizontalLayoutWidget_11.setGeometry(QtCore.QRect(530, 120, 220, 31))
        self.horizontalLayoutWidget_11.setObjectName("horizontalLayoutWidget_11")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lblHistorico = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_11)
        self.lblHistorico.setMinimumSize(QtCore.QSize(50, 20))
        self.lblHistorico.setObjectName("lblHistorico")
        self.horizontalLayout_11.addWidget(self.lblHistorico)
        self.rbtBaja = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget_11)
        self.rbtBaja.setMinimumSize(QtCore.QSize(50, 20))
        self.rbtBaja.setObjectName("rbtBaja")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.rbtBaja)
        self.horizontalLayout_11.addWidget(self.rbtBaja)
        self.rbtAlta = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget_11)
        self.rbtAlta.setMinimumSize(QtCore.QSize(50, 20))
        self.rbtAlta.setObjectName("rbtAlta")
        self.buttonGroup.addButton(self.rbtAlta)
        self.horizontalLayout_11.addWidget(self.rbtAlta)
        self.rbtTodos = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget_11)
        self.rbtTodos.setMinimumSize(QtCore.QSize(50, 20))
        self.rbtTodos.setChecked(True)
        self.rbtTodos.setObjectName("rbtTodos")
        self.buttonGroup.addButton(self.rbtTodos)
        self.horizontalLayout_11.addWidget(self.rbtTodos)
        self.horizontalLayoutWidget_12 = QtWidgets.QWidget(parent=self.frame)
        self.horizontalLayoutWidget_12.setGeometry(QtCore.QRect(10, 150, 245, 31))
        self.horizontalLayoutWidget_12.setObjectName("horizontalLayoutWidget_12")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_12)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.lblCarnet = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_12)
        self.lblCarnet.setMinimumSize(QtCore.QSize(100, 20))
        self.lblCarnet.setMaximumSize(QtCore.QSize(100, 20))
        self.lblCarnet.setObjectName("lblCarnet")
        self.horizontalLayout_12.addWidget(self.lblCarnet)
        self.chkA = QtWidgets.QCheckBox(parent=self.horizontalLayoutWidget_12)
        self.chkA.setObjectName("chkA")
        self.horizontalLayout_12.addWidget(self.chkA)
        self.chkB = QtWidgets.QCheckBox(parent=self.horizontalLayoutWidget_12)
        self.chkB.setObjectName("chkB")
        self.horizontalLayout_12.addWidget(self.chkB)
        self.chkC = QtWidgets.QCheckBox(parent=self.horizontalLayoutWidget_12)
        self.chkC.setObjectName("chkC")
        self.horizontalLayout_12.addWidget(self.chkC)
        self.chkD = QtWidgets.QCheckBox(parent=self.horizontalLayoutWidget_12)
        self.chkD.setObjectName("chkD")
        self.horizontalLayout_12.addWidget(self.chkD)
        self.horizontalLayoutWidget_13 = QtWidgets.QWidget(parent=self.frame)
        self.horizontalLayoutWidget_13.setGeometry(QtCore.QRect(310, 200, 341, 41))
        self.horizontalLayoutWidget_13.setObjectName("horizontalLayoutWidget_13")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_13)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.btnAltaDriver = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_13)
        self.btnAltaDriver.setMinimumSize(QtCore.QSize(75, 20))
        self.btnAltaDriver.setMaximumSize(QtCore.QSize(75, 20))
        self.btnAltaDriver.setObjectName("btnAltaDriver")
        self.horizontalLayout_13.addWidget(self.btnAltaDriver)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem)
        self.btnModifDriver = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_13)
        self.btnModifDriver.setMinimumSize(QtCore.QSize(90, 20))
        self.btnModifDriver.setMaximumSize(QtCore.QSize(90, 20))
        self.btnModifDriver.setObjectName("btnModifDriver")
        self.horizontalLayout_13.addWidget(self.btnModifDriver)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem1)
        self.btnBajaDriver = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_13)
        self.btnBajaDriver.setMinimumSize(QtCore.QSize(75, 20))
        self.btnBajaDriver.setMaximumSize(QtCore.QSize(75, 20))
        self.btnBajaDriver.setObjectName("btnBajaDriver")
        self.horizontalLayout_13.addWidget(self.btnBajaDriver)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1079, 21))
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
        icon2.addPixmap(QtGui.QPixmap(".\\templates\\../../../.designer/backup/img/exit_icon-icons.com_70975.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionSalir.setIcon(icon2)
        self.actionSalir.setObjectName("actionSalir")
        self.actionAcerca_de = QtGui.QAction(parent=MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\templates\\../../../.designer/backup/img/sign-question-icon_34359.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionAcerca_de.setIcon(icon3)
        self.actionAcerca_de.setObjectName("actionAcerca_de")
        self.barSalir = QtGui.QAction(parent=MainWindow)
        self.barSalir.setIcon(icon2)
        self.barSalir.setObjectName("barSalir")
        self.barLimpiarPanel = QtGui.QAction(parent=MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(".\\templates\\../../../.designer/backup/img/reload_icon-icons.com_64795.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
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
        MainWindow.setTabOrder(self.cmbProv, self.cmbMun)
        MainWindow.setTabOrder(self.cmbMun, self.txtTlf)
        MainWindow.setTabOrder(self.txtTlf, self.txtSalario)
        MainWindow.setTabOrder(self.txtSalario, self.rbtBaja)
        MainWindow.setTabOrder(self.rbtBaja, self.rbtAlta)
        MainWindow.setTabOrder(self.rbtAlta, self.rbtTodos)
        MainWindow.setTabOrder(self.rbtTodos, self.chkA)
        MainWindow.setTabOrder(self.chkA, self.chkB)
        MainWindow.setTabOrder(self.chkB, self.chkC)
        MainWindow.setTabOrder(self.chkC, self.chkD)
        MainWindow.setTabOrder(self.chkD, self.btnAltaDriver)
        MainWindow.setTabOrder(self.btnAltaDriver, self.btnModifDriver)
        MainWindow.setTabOrder(self.btnModifDriver, self.btnBajaDriver)
        MainWindow.setTabOrder(self.btnBajaDriver, self.tabDrivers)
        MainWindow.setTabOrder(self.tabDrivers, self.TabPrincipal)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CarTest"))
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
        self.lblcod.setText(_translate("MainWindow", "Codigo Driver"))
        self.lblDNI.setText(_translate("MainWindow", "DNI"))
        self.lblFechaAlta.setText(_translate("MainWindow", "Fecha Alta"))
        self.lblApel.setText(_translate("MainWindow", "Apellidos"))
        self.lblDir.setText(_translate("MainWindow", "Direccion"))
        self.lblNombre.setText(_translate("MainWindow", "Nombre"))
        self.lblProvincia.setText(_translate("MainWindow", "Provincia"))
        self.lblLocalidad.setText(_translate("MainWindow", "Localidad"))
        self.lblTlf.setText(_translate("MainWindow", "Telefono"))
        self.lblSalario.setText(_translate("MainWindow", "Salario"))
        self.lblHistorico.setText(_translate("MainWindow", "Historico"))
        self.rbtBaja.setText(_translate("MainWindow", "Baja"))
        self.rbtAlta.setText(_translate("MainWindow", "Alta"))
        self.rbtTodos.setText(_translate("MainWindow", "Todos"))
        self.lblCarnet.setText(_translate("MainWindow", "Tipo de Carnet"))
        self.chkA.setText(_translate("MainWindow", "A"))
        self.chkB.setText(_translate("MainWindow", "B"))
        self.chkC.setText(_translate("MainWindow", "C"))
        self.chkD.setText(_translate("MainWindow", "D"))
        self.btnAltaDriver.setText(_translate("MainWindow", "Alta Driver"))
        self.btnModifDriver.setText(_translate("MainWindow", "Modificar Driver"))
        self.btnBajaDriver.setText(_translate("MainWindow", "Baja Driver"))
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

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
        MainWindow.resize(1079, 880)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 768))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\templates\\../../../../../.designer/backup/img/Logo1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
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
        self.tabDrivers.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabDrivers.sizePolicy().hasHeightForWidth())
        self.tabDrivers.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabDrivers.setFont(font)
        self.tabDrivers.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.tabDrivers.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.tabDrivers.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tabDrivers.setAlternatingRowColors(True)
        self.tabDrivers.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tabDrivers.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
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
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.lblcod = QtWidgets.QLabel(parent=self.frame)
        self.lblcod.setMinimumSize(QtCore.QSize(50, 20))
        self.lblcod.setMaximumSize(QtCore.QSize(100, 20))
        self.lblcod.setObjectName("lblcod")
        self.horizontalLayout_36.addWidget(self.lblcod)
        self.lblcoddb = QtWidgets.QLabel(parent=self.frame)
        self.lblcoddb.setMinimumSize(QtCore.QSize(50, 20))
        self.lblcoddb.setMaximumSize(QtCore.QSize(100, 20))
        self.lblcoddb.setAutoFillBackground(False)
        self.lblcoddb.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.lblcoddb.setText("")
        self.lblcoddb.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblcoddb.setObjectName("lblcoddb")
        self.horizontalLayout_36.addWidget(self.lblcoddb)
        self.horizontalLayout_35.addLayout(self.horizontalLayout_36)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_35.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblDNI = QtWidgets.QLabel(parent=self.frame)
        self.lblDNI.setMinimumSize(QtCore.QSize(25, 20))
        self.lblDNI.setMaximumSize(QtCore.QSize(25, 20))
        self.lblDNI.setObjectName("lblDNI")
        self.horizontalLayout.addWidget(self.lblDNI)
        self.txtDni = QtWidgets.QLineEdit(parent=self.frame)
        self.txtDni.setMinimumSize(QtCore.QSize(200, 20))
        self.txtDni.setMaximumSize(QtCore.QSize(200, 20))
        self.txtDni.setText("")
        self.txtDni.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txtDni.setObjectName("txtDni")
        self.horizontalLayout.addWidget(self.txtDni)
        self.lblValidarDni = QtWidgets.QLabel(parent=self.frame)
        self.lblValidarDni.setMinimumSize(QtCore.QSize(30, 30))
        self.lblValidarDni.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lblValidarDni.setFont(font)
        self.lblValidarDni.setText("")
        self.lblValidarDni.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblValidarDni.setObjectName("lblValidarDni")
        self.horizontalLayout.addWidget(self.lblValidarDni)
        self.btnBuscarDni = QtWidgets.QPushButton(parent=self.frame)
        self.btnBuscarDni.setMinimumSize(QtCore.QSize(24, 24))
        self.btnBuscarDni.setMaximumSize(QtCore.QSize(24, 24))
        self.btnBuscarDni.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\templates\\../../../.designer/img/3844432-magnifier-search-zoom_110300.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnBuscarDni.setIcon(icon1)
        self.btnBuscarDni.setIconSize(QtCore.QSize(24, 24))
        self.btnBuscarDni.setObjectName("btnBuscarDni")
        self.horizontalLayout.addWidget(self.btnBuscarDni)
        self.horizontalLayout_35.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_35.addItem(spacerItem2)
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.horizontalLayout_35.addLayout(self.horizontalLayout_37)
        self.lblFechaAlta = QtWidgets.QLabel(parent=self.frame)
        self.lblFechaAlta.setMinimumSize(QtCore.QSize(60, 20))
        self.lblFechaAlta.setMaximumSize(QtCore.QSize(60, 20))
        self.lblFechaAlta.setObjectName("lblFechaAlta")
        self.horizontalLayout_35.addWidget(self.lblFechaAlta)
        self.txtFecha = QtWidgets.QLineEdit(parent=self.frame)
        self.txtFecha.setMinimumSize(QtCore.QSize(150, 20))
        self.txtFecha.setMaximumSize(QtCore.QSize(150, 20))
        self.txtFecha.setObjectName("txtFecha")
        self.horizontalLayout_35.addWidget(self.txtFecha)
        self.btnCalendar = QtWidgets.QPushButton(parent=self.frame)
        self.btnCalendar.setMinimumSize(QtCore.QSize(50, 20))
        self.btnCalendar.setMaximumSize(QtCore.QSize(50, 20))
        self.btnCalendar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\templates\\../../../.designer/img/Calendar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnCalendar.setIcon(icon2)
        self.btnCalendar.setIconSize(QtCore.QSize(25, 25))
        self.btnCalendar.setDefault(False)
        self.btnCalendar.setFlat(True)
        self.btnCalendar.setObjectName("btnCalendar")
        self.horizontalLayout_35.addWidget(self.btnCalendar)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_35.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_35)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.lblApel = QtWidgets.QLabel(parent=self.frame)
        self.lblApel.setMinimumSize(QtCore.QSize(50, 20))
        self.lblApel.setMaximumSize(QtCore.QSize(50, 20))
        self.lblApel.setObjectName("lblApel")
        self.horizontalLayout_39.addWidget(self.lblApel)
        self.txtApel = QtWidgets.QLineEdit(parent=self.frame)
        self.txtApel.setMinimumSize(QtCore.QSize(300, 20))
        self.txtApel.setMaximumSize(QtCore.QSize(300, 20))
        self.txtApel.setObjectName("txtApel")
        self.horizontalLayout_39.addWidget(self.txtApel)
        self.horizontalLayout_38.addLayout(self.horizontalLayout_39)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_38.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_38.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_38.addItem(spacerItem7)
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.horizontalLayout_38.addLayout(self.horizontalLayout_40)
        self.lblNombre = QtWidgets.QLabel(parent=self.frame)
        self.lblNombre.setMinimumSize(QtCore.QSize(50, 20))
        self.lblNombre.setObjectName("lblNombre")
        self.horizontalLayout_38.addWidget(self.lblNombre)
        self.txtNombre = QtWidgets.QLineEdit(parent=self.frame)
        self.txtNombre.setMinimumSize(QtCore.QSize(300, 20))
        self.txtNombre.setMaximumSize(QtCore.QSize(300, 20))
        self.txtNombre.setObjectName("txtNombre")
        self.horizontalLayout_38.addWidget(self.txtNombre)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_38.addItem(spacerItem8)
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.horizontalLayout_38.addLayout(self.horizontalLayout_41)
        self.verticalLayout_2.addLayout(self.horizontalLayout_38)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem9)
        self.horizontalLayout_47 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_47.setObjectName("horizontalLayout_47")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lblDir = QtWidgets.QLabel(parent=self.frame)
        self.lblDir.setMinimumSize(QtCore.QSize(50, 20))
        self.lblDir.setMaximumSize(QtCore.QSize(50, 20))
        self.lblDir.setObjectName("lblDir")
        self.horizontalLayout_5.addWidget(self.lblDir)
        self.txtDir = QtWidgets.QLineEdit(parent=self.frame)
        self.txtDir.setMinimumSize(QtCore.QSize(300, 20))
        self.txtDir.setMaximumSize(QtCore.QSize(300, 20))
        self.txtDir.setObjectName("txtDir")
        self.horizontalLayout_5.addWidget(self.txtDir)
        self.horizontalLayout_47.addLayout(self.horizontalLayout_5)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_47.addItem(spacerItem10)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lblProvincia = QtWidgets.QLabel(parent=self.frame)
        self.lblProvincia.setMinimumSize(QtCore.QSize(50, 20))
        self.lblProvincia.setObjectName("lblProvincia")
        self.horizontalLayout_7.addWidget(self.lblProvincia)
        self.cmbProv = QtWidgets.QComboBox(parent=self.frame)
        self.cmbProv.setMinimumSize(QtCore.QSize(120, 20))
        self.cmbProv.setObjectName("cmbProv")
        self.horizontalLayout_7.addWidget(self.cmbProv)
        self.horizontalLayout_47.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lblLocalidad = QtWidgets.QLabel(parent=self.frame)
        self.lblLocalidad.setMinimumSize(QtCore.QSize(50, 20))
        self.lblLocalidad.setObjectName("lblLocalidad")
        self.horizontalLayout_8.addWidget(self.lblLocalidad)
        self.cmbMun = QtWidgets.QComboBox(parent=self.frame)
        self.cmbMun.setMinimumSize(QtCore.QSize(120, 20))
        self.cmbMun.setObjectName("cmbMun")
        self.horizontalLayout_8.addWidget(self.cmbMun)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem11)
        self.horizontalLayout_47.addLayout(self.horizontalLayout_8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_47)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem12)
        self.horizontalLayout_44 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_44.setObjectName("horizontalLayout_44")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lblTlf = QtWidgets.QLabel(parent=self.frame)
        self.lblTlf.setMinimumSize(QtCore.QSize(50, 20))
        self.lblTlf.setObjectName("lblTlf")
        self.horizontalLayout_9.addWidget(self.lblTlf)
        self.txtTlf = QtWidgets.QLineEdit(parent=self.frame)
        self.txtTlf.setMinimumSize(QtCore.QSize(100, 20))
        self.txtTlf.setMaximumSize(QtCore.QSize(100, 20))
        self.txtTlf.setObjectName("txtTlf")
        self.horizontalLayout_9.addWidget(self.txtTlf)
        self.lblValidarTlf = QtWidgets.QLabel(parent=self.frame)
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
        self.horizontalLayout_44.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lblSalario = QtWidgets.QLabel(parent=self.frame)
        self.lblSalario.setMinimumSize(QtCore.QSize(50, 20))
        self.lblSalario.setObjectName("lblSalario")
        self.horizontalLayout_10.addWidget(self.lblSalario)
        self.txtSalario = QtWidgets.QLineEdit(parent=self.frame)
        self.txtSalario.setMinimumSize(QtCore.QSize(100, 20))
        self.txtSalario.setMaximumSize(QtCore.QSize(100, 20))
        self.txtSalario.setObjectName("txtSalario")
        self.horizontalLayout_10.addWidget(self.txtSalario)
        self.lblSalarioT = QtWidgets.QLabel(parent=self.frame)
        self.lblSalarioT.setMinimumSize(QtCore.QSize(100, 20))
        self.lblSalarioT.setMaximumSize(QtCore.QSize(10, 20))
        self.lblSalarioT.setText("")
        self.lblSalarioT.setObjectName("lblSalarioT")
        self.horizontalLayout_10.addWidget(self.lblSalarioT)
        self.horizontalLayout_44.addLayout(self.horizontalLayout_10)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_44.addItem(spacerItem13)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_44.addItem(spacerItem14)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lblHistorico = QtWidgets.QLabel(parent=self.frame)
        self.lblHistorico.setMinimumSize(QtCore.QSize(50, 20))
        self.lblHistorico.setObjectName("lblHistorico")
        self.horizontalLayout_11.addWidget(self.lblHistorico)
        self.rbtBaja = QtWidgets.QRadioButton(parent=self.frame)
        self.rbtBaja.setMinimumSize(QtCore.QSize(50, 20))
        self.rbtBaja.setObjectName("rbtBaja")
        self.rbGroup = QtWidgets.QButtonGroup(MainWindow)
        self.rbGroup.setObjectName("rbGroup")
        self.rbGroup.addButton(self.rbtBaja)
        self.horizontalLayout_11.addWidget(self.rbtBaja)
        self.rbtAlta = QtWidgets.QRadioButton(parent=self.frame)
        self.rbtAlta.setMinimumSize(QtCore.QSize(50, 20))
        self.rbtAlta.setObjectName("rbtAlta")
        self.rbGroup.addButton(self.rbtAlta)
        self.horizontalLayout_11.addWidget(self.rbtAlta)
        self.rbtTodos = QtWidgets.QRadioButton(parent=self.frame)
        self.rbtTodos.setMinimumSize(QtCore.QSize(50, 20))
        self.rbtTodos.setChecked(True)
        self.rbtTodos.setObjectName("rbtTodos")
        self.rbGroup.addButton(self.rbtTodos)
        self.horizontalLayout_11.addWidget(self.rbtTodos)
        self.horizontalLayout_44.addLayout(self.horizontalLayout_11)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_44.addItem(spacerItem15)
        self.verticalLayout_2.addLayout(self.horizontalLayout_44)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem16)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.lblCarnet = QtWidgets.QLabel(parent=self.frame)
        self.lblCarnet.setMinimumSize(QtCore.QSize(100, 20))
        self.lblCarnet.setMaximumSize(QtCore.QSize(100, 20))
        self.lblCarnet.setObjectName("lblCarnet")
        self.horizontalLayout_12.addWidget(self.lblCarnet)
        self.chkA = QtWidgets.QCheckBox(parent=self.frame)
        self.chkA.setObjectName("chkA")
        self.horizontalLayout_12.addWidget(self.chkA)
        self.chkB = QtWidgets.QCheckBox(parent=self.frame)
        self.chkB.setObjectName("chkB")
        self.horizontalLayout_12.addWidget(self.chkB)
        self.chkC = QtWidgets.QCheckBox(parent=self.frame)
        self.chkC.setObjectName("chkC")
        self.horizontalLayout_12.addWidget(self.chkC)
        self.chkD = QtWidgets.QCheckBox(parent=self.frame)
        self.chkD.setObjectName("chkD")
        self.horizontalLayout_12.addWidget(self.chkD)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem17)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem18)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_13.addLayout(self.horizontalLayout_3)
        self.btnAltaDriver = QtWidgets.QPushButton(parent=self.frame)
        self.btnAltaDriver.setMinimumSize(QtCore.QSize(75, 20))
        self.btnAltaDriver.setMaximumSize(QtCore.QSize(75, 20))
        self.btnAltaDriver.setObjectName("btnAltaDriver")
        self.horizontalLayout_13.addWidget(self.btnAltaDriver)
        self.btnModifDriver = QtWidgets.QPushButton(parent=self.frame)
        self.btnModifDriver.setMinimumSize(QtCore.QSize(90, 20))
        self.btnModifDriver.setMaximumSize(QtCore.QSize(90, 20))
        self.btnModifDriver.setObjectName("btnModifDriver")
        self.horizontalLayout_13.addWidget(self.btnModifDriver)
        self.btnBajaDriver = QtWidgets.QPushButton(parent=self.frame)
        self.btnBajaDriver.setMinimumSize(QtCore.QSize(75, 20))
        self.btnBajaDriver.setMaximumSize(QtCore.QSize(75, 20))
        self.btnBajaDriver.setObjectName("btnBajaDriver")
        self.horizontalLayout_13.addWidget(self.btnBajaDriver)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_13.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem19, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)
        self.TabPrincipal.addTab(self.panelDrivers, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(160, 100, 201, 101))
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.tab_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 290, 891, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.horizontalLayout_14.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.horizontalLayout_14.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.horizontalLayout_14.addLayout(self.horizontalLayout_17)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.horizontalLayout_19.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.horizontalLayout_19.addLayout(self.horizontalLayout_20)
        self.verticalLayout.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.horizontalLayout_21.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.horizontalLayout_21.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.horizontalLayout_21.addLayout(self.horizontalLayout_24)
        self.verticalLayout.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.horizontalLayout_25.addLayout(self.horizontalLayout_26)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.horizontalLayout_25.addLayout(self.horizontalLayout_27)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.horizontalLayout_25.addLayout(self.horizontalLayout_28)
        self.verticalLayout.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.verticalLayout.addLayout(self.horizontalLayout_31)
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.verticalLayout.addLayout(self.horizontalLayout_29)
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
        self.menuHerramientas = QtWidgets.QMenu(parent=self.menubar)
        self.menuHerramientas.setObjectName("menuHerramientas")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(parent=MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionSalir = QtGui.QAction(parent=MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\templates\\../../../../../.designer/backup/img/exit_icon-icons.com_70975.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionSalir.setIcon(icon3)
        self.actionSalir.setObjectName("actionSalir")
        self.actionAcerca_de = QtGui.QAction(parent=MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(".\\templates\\../../../../../.designer/backup/img/sign-question-icon_34359.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionAcerca_de.setIcon(icon4)
        self.actionAcerca_de.setObjectName("actionAcerca_de")
        self.barSalir = QtGui.QAction(parent=MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(".\\templates\\../../../.designer/img/exit_icon-icons.com_70975.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.barSalir.setIcon(icon5)
        self.barSalir.setObjectName("barSalir")
        self.barLimpiarPanel = QtGui.QAction(parent=MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(".\\templates\\../../../.designer/img/reload_icon-icons.com_64795.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.barLimpiarPanel.setIcon(icon6)
        self.barLimpiarPanel.setObjectName("barLimpiarPanel")
        self.actionCrear_Copias_Seguridad = QtGui.QAction(parent=MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(".\\templates\\../img/web_ui_database_icon_233606.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionCrear_Copias_Seguridad.setIcon(icon7)
        self.actionCrear_Copias_Seguridad.setShortcutVisibleInContextMenu(False)
        self.actionCrear_Copias_Seguridad.setObjectName("actionCrear_Copias_Seguridad")
        self.actionRestaurar_Copias_Seguridad = QtGui.QAction(parent=MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(".\\templates\\../img/web_ui_database_icon_233572.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionRestaurar_Copias_Seguridad.setIcon(icon8)
        self.actionRestaurar_Copias_Seguridad.setObjectName("actionRestaurar_Copias_Seguridad")
        self.menuArchivo.addAction(self.actionSalir)
        self.menuHelp.addAction(self.actionAcerca_de)
        self.menuHerramientas.addAction(self.actionCrear_Copias_Seguridad)
        self.menuHerramientas.addAction(self.actionRestaurar_Copias_Seguridad)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuHerramientas.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.barLimpiarPanel)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.barSalir)

        self.retranslateUi(MainWindow)
        self.TabPrincipal.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CarTest"))
        item = self.tabDrivers.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Código"))
        item = self.tabDrivers.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Apellidos"))
        item = self.tabDrivers.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nombre"))
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
        self.lblNombre.setText(_translate("MainWindow", "Nombre"))
        self.lblDir.setText(_translate("MainWindow", "Direccion"))
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
        self.menuHerramientas.setTitle(_translate("MainWindow", "Herramientas"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionAcerca_de.setText(_translate("MainWindow", "Acerca de ..."))
        self.barSalir.setText(_translate("MainWindow", "Salir"))
        self.barLimpiarPanel.setText(_translate("MainWindow", "LimpiarPanel"))
        self.actionCrear_Copias_Seguridad.setText(_translate("MainWindow", "Crear Copias Seguridad"))
        self.actionCrear_Copias_Seguridad.setShortcut(_translate("MainWindow", "Alt+S"))
        self.actionRestaurar_Copias_Seguridad.setText(_translate("MainWindow", "Restaurar Copias Seguridad"))
        self.actionRestaurar_Copias_Seguridad.setShortcut(_translate("MainWindow", "Alt+R"))

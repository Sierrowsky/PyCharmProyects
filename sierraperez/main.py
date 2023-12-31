import datetime

import clientes
import conexion
import drivers
import drivers3
import eventos
import var
from MainWindow import *
from windowAux import *
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)  # Encargado de generar la interfaz
        var.calendar = Calendar()
        var.salir = Salir()
        var.about = About()
        var.clientes = clientes.Clientes()
        var.driver = drivers.Drivers()
        var.dlgAbrir = FileDialogAbrir()
        conexion.Conexion.conexion()
        conexion.Conexion.cargaprov()
        conexion.Conexion.cargaprovCli()
        conexion.Conexion.mostrardriver()
        conexion.Conexion.mostrarCliente()
        """
        Zona de eventos de botones del panel drivers
        """
        var.ui.btnCalendar.clicked.connect(eventos.Eventos.abrirCalendar)
        var.ui.btnAltaDriver.clicked.connect(drivers.Drivers.altadriver)
        var.ui.btnBuscarDni.clicked.connect(drivers.Drivers.buscarDri)
        var.ui.btnModifDriver.clicked.connect(drivers.Drivers.modifDri)
        var.ui.btnBajaDriver.clicked.connect(drivers.Drivers.borrarDri)
        """
        Zona de eventos de botones del panel clientes
        """
        var.ui.btnAltaCliente.clicked.connect(clientes.Clientes.altacliente)
        var.ui.btnBajaCliente.clicked.connect(clientes.Clientes.bajacli)
        """    
        Zona de eventos del MenuBar
        """
        var.ui.actionSalir.triggered.connect(eventos.Eventos.Salir)
        var.ui.actionAcerca_de.triggered.connect(eventos.Eventos.acercade)
        var.ui.actionCrear_Copias_Seguridad.triggered.connect(eventos.Eventos.crearCopiaSeguridad)
        var.ui.actionRestaurar_Copias_Seguridad.triggered.connect(eventos.Eventos.restaurarCopiaSeguridad)
        var.ui.actionExportar_Datos_xls.triggered.connect(eventos.Eventos.exportardatosxls)
        var.ui.actionImportar_Datos_xls.triggered.connect(eventos.Eventos.importardatosxls)
        var.ui.actionImportar_Datos_Clientes_xls.triggered.connect(eventos.Eventos.importardatosxlscli)

        """
        Zona de eventos de las cajas de texto panel drivers
        """
        var.ui.txtDni.editingFinished.connect(drivers.Drivers.validarDNI)
        var.ui.txtNombre.editingFinished.connect(eventos.Eventos.CajaText)
        var.ui.txtApel.editingFinished.connect(eventos.Eventos.CajaText)
        var.ui.txtSalario.editingFinished.connect(eventos.Eventos.CajaText)
        var.ui.txtTlf.editingFinished.connect(eventos.Eventos.valTelefono)
        var.ui.txtSalario.editingFinished.connect(eventos.Eventos.valSalario)
        """
        Zona de eventos de las cajas de texto panel clientes
        """
        var.ui.txtDniCli.editingFinished.connect(clientes.Clientes.validardnicli)
        """
        Eventos del ToolBar
        """
        var.ui.barSalir.triggered.connect(eventos.Eventos.Salir)
        var.ui.barLimpiarPanel.triggered.connect(drivers.Drivers.limpiapanel)
        var.ui.barLimpiarPanel.triggered.connect(clientes.Clientes.limpiarpanelcli)


        """
        Eventos en tablas drivers
        """
        eventos.Eventos.resizetabdrivers(self)
        var.ui.tabDrivers.clicked.connect(drivers.Drivers.cargadriver)
        """
        Eventos en tablas clientes
        """
        eventos.Eventos.resizetabdriverscli(self)
        var.ui.tabClientes.clicked.connect(clientes.Clientes.cargarcliente)
        """
        eventos Combobox panel drivers
        """
        var.ui.cmbProv.currentIndexChanged.connect(conexion.Conexion.selMuni)

        """
        eventos Combobox panel Clientes
        """
        var.ui.cmbProvCli.currentIndexChanged.connect(conexion.Conexion.selMuniCli)
        """
        Ejecucion de diferentes funciones al lanzar la APP
        """
        eventos.Eventos.cargarstatusvar(self)
        var.ui.buttonGroup.buttonClicked.connect(conexion.Conexion.selEstado)




    def closeEvent(self, event):
        mbox = QtWidgets.QMessageBox.information(self, " Salir ", "¿Estas seguro que quieres salir?",
                                                 QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)

        if mbox == QtWidgets.QMessageBox.StandardButton.Yes:
            app.quit()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())

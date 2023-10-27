import datetime
import conexion
import drivers
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
        var.driver = drivers.Drivers()
        conexion.Conexion.conexion()
        conexion.Conexion.cargaprov()
        """
        Zona de eventos de botones
        """
        var.ui.btnCalendar.clicked.connect(eventos.Eventos.abrirCalendar)
        var.ui.btnAltaDriver.clicked.connect(drivers.Drivers.altadriver)
        """
        Zona de eventos del MenuBar
        """
        var.ui.actionSalir.triggered.connect(eventos.Eventos.Salir)
        var.ui.actionAcerca_de.triggered.connect(eventos.Eventos.acercade)

        """
        Zona de eventos de las cajas de texto
        """
        var.ui.txtDni.editingFinished.connect(drivers.Drivers.ValidarDni)
        var.ui.txtNombre.editingFinished.connect(eventos.Eventos.CajaText)
        var.ui.txtApel.editingFinished.connect(eventos.Eventos.CajaText)
        var.ui.txtSalario.editingFinished.connect(eventos.Eventos.CajaText)
        var.ui.txtTlf.editingFinished.connect(drivers.Drivers.valTelefono)
        var.ui.txtSalario.editingFinished.connect(drivers.Drivers.valSalario)
        """
        Eventos del ToolBar
        """
        var.ui.barSalir.triggered.connect(eventos.Eventos.Salir)
        var.ui.barLimpiarPanel.triggered.connect(drivers.Drivers.LimpiarPanel)
        """
        Eventos en tablas
        """
        eventos.Eventos.resizetabdrivers(self)
        """
        Ejecucion de diferentes funciones al lanzar la APP
        """
        eventos.Eventos.cargarstatusvar(self)
        eventos.Eventos.cargapropia(self)
        rbtDriver = [var.ui.rbtTodos, var.ui.rbtAlta, var.ui.rbtBaja]
        for i in rbtDriver:
            i.toggled.connect(eventos.Eventos.selEstado)

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

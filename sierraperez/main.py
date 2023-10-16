import datetime

from MainWindow import *
from windowAux import *


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)  # Encargado de generar la interfaz
        var.calendar = Calendar()
        var.salir = Salir()
        var.about = About()
        var.driver = drivers.Drivers()


        """
        Zona de eventos de botones
        """
        var.ui.btnCalendar.clicked.connect(eventos.Eventos.abrirCalendar)

        """
        Zona de eventos del MenuBar
        """
        var.ui.actionSalir.triggered.connect(eventos.Eventos.Salir)
        var.ui.actionAcerca_de.triggered.connect(eventos.Eventos.acercade)
        """
        Zona de eventos de las cajas de texto
        """
        var.ui.txtDni.editingFinished.connect(drivers.Drivers.ValidarDni)
        """
        Eventos del ToolBar
        """
        var.ui.barSalir.triggered.connect(eventos.Eventos.Salir)
        var.ui.barLimpiarPanel.triggered.connect(drivers.Drivers.LimpiarPanel)
        """
        StatusBar
        """
        fecha = str(datetime.now())
        var.ui.statusbar.showMessage(fecha)
        """
        Ejecucion de diferentes funciones al lanzar la APP
        """
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

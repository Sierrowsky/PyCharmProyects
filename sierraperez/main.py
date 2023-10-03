import sys
import var

import eventos
from MainWindow import *


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)  ## Encargado de generar la interfaz
        """
        
        Zona de eventos de botones
        """
        var.ui.BotonSalir.clicked.connect(eventos.Eventos.Saludo)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())

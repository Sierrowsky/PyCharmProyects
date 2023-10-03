import var
class Eventos():
    def Saludo(self):
        try:
            var.ui.lblTitulo.setText("Hola, pulsaste el boton")
        except Exception as error:
            print(error,"en modulo eventos")
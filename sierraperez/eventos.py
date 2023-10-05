import var, sys
class Eventos():
    def Salir(self):
        try:
            sys.exit()
        except Exception as error:
            print(error,"en modulo eventos")

    @staticmethod
    def abrirCalendar(self):
        try:
            var.calendar.show()
        except Exception as error:
            print("error al abrir calendario", error)
    @staticmethod
    def acercade(self):
        try:
            pass
        except Exception as error:
            print("Error abrir ventana acerca de ", error)
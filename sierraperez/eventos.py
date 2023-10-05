import var, sys
class Eventos():
    def Salir(self):
        try:
            sys.exit()
        except Exception as error:
            print(error,"en modulo eventos")
    def abrirCalendar(self):
        try:
            var.calendar.show()
        except Exception as error:
            print("error al abrir calendario", error)
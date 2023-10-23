from PyQt6 import QtWidgets, QtSql, QtCore
class conexion():
    def conexion(self = None):
        db = QtSql.QSqlQuery.addDataBase('QSQLITE')
        db.setDatabaseName('bbdd.sqlite')
        if not db.open(self):
            print("error de conexion")
            return False
        else:
            print("conexion realizada?")
            return True


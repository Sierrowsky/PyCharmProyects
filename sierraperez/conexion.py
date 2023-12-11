from datetime import datetime

from PyQt6 import QtWidgets, QtSql, QtCore

import clientes
import drivers
import drivers3
import var


class Conexion():
    @staticmethod
    def conexion(self=None):
        var.bbdd = 'bbdd.sqlite'
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(var.bbdd)
        if not db.open():
            print("error de conexion")
            return False
        else:
            print("conexion realizada")
            return True

    @staticmethod
    def cargaprov(self=None):
        try:
            var.ui.cmbProv.clear()
            query = QtSql.QSqlQuery()
            query.prepare("select provincia from provincias")
            if query.exec():
                var.ui.cmbProv.addItem(' ')
                while query.next():
                    var.ui.cmbProv.addItem(query.value(0))
        except Exception as error:
            print("Error en cargaProv", error)

    @staticmethod
    def selMuni(self=None):
        try:
            id = 0
            var.ui.cmbMun.clear()
            prov = var.ui.cmbProv.currentText()
            query = QtSql.QSqlQuery()
            query.prepare("select IdProv from provincias where provincia  = :prov")
            query.bindValue(':prov', prov)
            if query.exec():
                while query.next():
                    id = query.value(0)
            queryM = QtSql.QSqlQuery()
            queryM.prepare("select municipio from municipios where IdProv = :id")
            queryM.bindValue(':id', int(id))
            if queryM.exec():
                var.ui.cmbMun.addItem('')
                while queryM.next():
                    var.ui.cmbMun.addItem(queryM.value(0))
        except Exception as error:
            print("Error en cargaMun", error)

    @staticmethod
    def guardardri(newdrivers):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('insert into drivers(dnidri, altadri, apeldri, nombredri, direcciondri, '
                          ' provdri, munidri, movildri, salario, carnet) VALUES(:dni, :alta, :apel '
                          ' , :nombre, :direccion, :provincia, :municipio, :movil, :salario, :carnet)')
            query.bindValue(':dni', str(newdrivers[0]))
            query.bindValue(':alta', str(newdrivers[1]))
            query.bindValue(':apel', str(newdrivers[2]))
            query.bindValue(':nombre', str(newdrivers[3]))
            query.bindValue(':direccion', str(newdrivers[4]))
            query.bindValue(':provincia', str(newdrivers[5]))
            query.bindValue(':municipio', str(newdrivers[6]))
            query.bindValue(':movil', str(newdrivers[7]))
            query.bindValue(':salario', str(newdrivers[8]))
            query.bindValue(':carnet', str(newdrivers[9]))
            if query.exec():
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Listo')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText('Empleado dado de alta')
                mbox.exec()
                Conexion.mostrardriver()
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText(query.lastError().text())
                mbox.exec()

        except Exception as error:
            print("Error guardardri ", error)

    def mostrardriver(self=None):
        try:
            registros = []
            query1 = QtSql.QSqlQuery()
            query1.prepare('select codigo, apeldri, nombredri, movildri, carnet, bajadri from drivers')
            if query1.exec():
                while query1.next():
                    row = [query1.value(i) for i in range(query1.record().count())]
                    registros.append(row)
            drivers.Drivers.cargartabladri(registros)
        except Exception as error:
            print('Error al mostrar resultados', error)

    @staticmethod
    def SelectDrivers(estado):
        try:
            registros = []
            if int(estado) == 0:
                query = QtSql.QSqlQuery()
                query.prepare('select codigo, apeldri, nombredri, movildri, carnet, bajadri from drivers')
                if query.exec():
                    while query.next():
                        row = [query.value(i) for i in range(query.record().count())]
                        registros.append(row)
                    drivers.Drivers.cargartabladri(registros)
            elif int(estado) == 1:
                query = QtSql.QSqlQuery()
                query.prepare(
                    'select codigo, apeldri, nombredri, movildri, carnet, '
                    'bajadri from drivers where bajadri is null')
                if query.exec():
                    while query.next():
                        row = [query.value(i) for i in range(query.record().count())]
                        registros.append(row)
                    drivers.Drivers.cargartabladri(registros)
            elif int(estado) == 2:
                query = QtSql.QSqlQuery()
                query.prepare(
                    'select codigo, apeldri, nombredri, movildri, carnet, bajadri '
                    'from drivers where bajadri is not null')
                if query.exec():
                    while query.next():
                        row = [query.value(i) for i in range(query.record().count())]
                        registros.append(row)
                    drivers.Drivers.cargartabladri(registros)
        except Exception as error:
            print("Error SelectDrivers ", error)

    @staticmethod
    def onedriver(codigo):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('select * from drivers where codigo = :codigo')
            query.bindValue(':codigo', int(codigo))
            if query.exec():
                while query.next():
                    for i in range(12):
                        registro.append(str(query.value(i)))
            return registro
        except Exception as error:
            print('Error en onedriver', error)

    @staticmethod
    def codDri(dni):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('select codigo from drivers where dnidri= :dni')
            query.bindValue(':dni', str(dni))
            if query.exec():
                while query.next():
                    codigo = query.value(0)
                    registro = Conexion.onedriver(codigo)
                    return registro

                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText('El conductor no existe')
                mbox.exec()
        except Exception as error:
            print('Error al buscar driver', error)

    @staticmethod
    def modifDriver(modifdriver):
        try:
            registro = Conexion.onedriver(int(modifdriver[0]))
            if modifdriver == registro[:-1]:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('No hay datos que modificar. Desea cambiar la fecha o eliminar fecha de baja?')
                msg.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No |
                    QtWidgets.QMessageBox.StandardButton.Cancel)
                msg.button(QtWidgets.QMessageBox.StandardButton.Yes).setText("Alta")
                msg.button(QtWidgets.QMessageBox.StandardButton.No).setText("Modificar")
                msg.button(QtWidgets.QMessageBox.StandardButton.Cancel).setText('Cancelar')
                opcion = msg.exec()
                if opcion == QtWidgets.QMessageBox.StandardButton.Yes:
                    if registro[11] != '':
                        query1 = QtSql.QSqlQuery()
                        query1.prepare('update drivers set bajadri = NULL where '
                                       ' dnidri = :dni')
                        query1.bindValue(':dni', str(modifdriver[1]))
                        if query1.exec():
                            msg = QtWidgets.QMessageBox()
                            msg.setWindowTitle('Aviso')
                            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                            msg.setText('Datos Conductor Modificados')
                            msg.exec()
                            Conexion.SelectDrivers(0)
                    else:
                        msg = QtWidgets.QMessageBox()
                        msg.setWindowTitle('Aviso')
                        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                        msg.setText('El conductor está en alta. Nada que modificar')
                        msg.exec()
                        Conexion.SelectDrivers(1)
                elif opcion == QtWidgets.QMessageBox.StandardButton.No:
                    var.calendar.show()
                    dia = datetime.now().day
                    mes = datetime.now().month
                    ano = datetime.now().year
                    data = var.calendar.Calendar.selectionChanged.connect(drivers.Drivers.cargaFecha(QtCore.QDate))
                    data = drivers.Drivers.cargaFecha(QtCore.QDate)

                    if registro[11] != '':
                        query1 = QtSql.QSqlQuery()
                        query1.prepare('update drivers set bajadri = :data where '
                                       ' dnidri = :dni')
                        query1.bindValue(':data', str(data))
                        query1.bindValue(':dni', str(modifdriver[1]))
                        if query1.exec():
                            msg = QtWidgets.QMessageBox()
                            msg.setWindowTitle('Aviso')
                            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                            msg.setText('Baja Modificada. Nueva Fecha Baja:', str(data))
                            msg.exec()
                        Conexion.SelectDrivers(0)
                    else:
                        msg = QtWidgets.QMessageBox()
                        msg.setWindowTitle('Aviso')
                        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                        msg.setText('El conductor está en alta. Nada que modificar')
                        msg.exec()
                        Conexion.SelectDrivers(1)
                elif opcion == QtWidgets.QMessageBox.StandardButton.Cancel:
                    pass
            else:
                query = QtSql.QSqlQuery()
                query.prepare('update drivers set dnidri = :dni, altadri= :alta, apeldri = :apel, nombredri = :nombre, '
                              ' direcciondri = :direccion, provdri = :provincia, mundri = :municipio, '
                              ' movildri = :movil, salario = :salario, carnet = :carnet where codigo = :codigo')

                query.bindValue(':codigo', int(modifdriver[0]))
                query.bindValue(':dni', str(modifdriver[1]))
                query.bindValue(':alta', str(modifdriver[2]))
                query.bindValue(':apel', str(modifdriver[3]))
                query.bindValue(':nombre', str(modifdriver[4]))
                query.bindValue(':direccion', str(modifdriver[5]))
                query.bindValue(':provincia', str(modifdriver[6]))
                query.bindValue(':municipio', str(modifdriver[7]))
                query.bindValue(':movil', str(modifdriver[8]))
                query.bindValue(':salario', str(modifdriver[9]))
                query.bindValue(':carnet', str(modifdriver[10]))
                if query.exec():
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Aviso')
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    msg.setText('Datos Conductor Modificados')
                    msg.exec()
                    Conexion.SelectDrivers(1)
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Aviso')
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    msg.setText(query.lastError().text())
                    msg.exec()
        except Exception as error:
            print('error en modificar driver en conexion ', error)

    @staticmethod
    def borrarDri(dni):
        try:
            query1 = QtSql.QSqlQuery()
            query1.prepare('Select bajadri from drivers')
            fecha = datetime.today()
            fecha = fecha.strftime('%d/%m/%y')
            query = QtSql.QSqlQuery()
            query.prepare(' Update drivers set bajadri = :fechabaja where '
                          'dnidri = :dni')
            query.bindValue(':fechabaja', str(fecha))
            query.bindValue(':dni', str(dni))

            if query.exec():
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText('Todo bien')
                mbox.exec()
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText(query.lastError().text() + 'Error baja Driver')
                mbox.exec()
        except Exception as error:
            print('Error al borrar Driver', error)

    @staticmethod
    def selEstado(self):
        try:
            if var.ui.rbtTodos.isChecked():
                estado = 0
                Conexion.SelectDrivers(estado)
            elif var.ui.rbtAlta.isChecked():
                estado = 1
                Conexion.SelectDrivers(estado)
            elif var.ui.rbtBaja.isChecked():
                estado = 2
                Conexion.SelectDrivers(estado)
        except Exception as error:
            print("Error en selEstado", error)

    @staticmethod
    def consulta_drivers(fechaBaja):
        try:
            registros = []
            query1 = QtSql.QSqlQuery()

            if fechaBaja == 2:
                query1.prepare("select codigo, apellidos,nombre,telefono, carnet, fechaBaja from drivers")
            elif fechaBaja == 1:
                query1.prepare(
                    "select codigo, apellidos,nombre,telefono, carnet, fechaBaja from drivers where fechaBaja is null")
            elif fechaBaja == 0:
                query1.prepare(
                    "select codigo, apellidos,nombre,telefono, carnet, fechaBaja from drivers where fechaBaja is not null")

            if query1.exec():
                while query1.next():
                    row = [query1.value(i) for i in range(query1.record().count())]
                    registros.append(row)
            return registros

        except Exception as error:
            print('Erros mostrar Resultados', error)

    def SelectDriverstodos(self):
        try:
            registros = []
            query = QtSql.QSqlQuery()
            query.prepare('Select * from drivers order by apeldri')
            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]  # funcion lambda
                    registros.append(row)
            return registros
        except Exception as error:
            print('SelectDriversTodos', error)

    def guardarImp(new):
        try:

            query = QtSql.QSqlQuery()

            if new[11] == '':
                query.prepare('insert into drivers VALUES(null, :dni, :alta, :apel '
                              ' , :nombre, :direccion, :provincia, :municipio, :movil, :salario, :carnet, null)')
                query.bindValue(':dni', str(new[1]))
                query.bindValue(':alta', str(new[2]))
                query.bindValue(':apel', str(new[3]))
                query.bindValue(':nombre', str(new[4]))
                query.bindValue(':direccion', str(new[5]))
                query.bindValue(':provincia', str(new[6]))
                query.bindValue(':municipio', str(new[7]))
                query.bindValue(':movil', str(new[8]))
                query.bindValue(':salario', str(new[9]))
                query.bindValue(':carnet', str(new[10]))

            else:
                query.prepare('insert into drivers VALUES(null, :dni, :alta, :apel '
                              ' , :nombre, :direccion, :provincia, :municipio, :movil, :salario, :carnet, :bajadri)')
                query.bindValue(':dni', str(new[1]))
                query.bindValue(':alta', str(new[2]))
                query.bindValue(':apel', str(new[3]))
                query.bindValue(':nombre', str(new[4]))
                query.bindValue(':direccion', str(new[5]))
                query.bindValue(':provincia', str(new[6]))
                query.bindValue(':municipio', str(new[7]))
                query.bindValue(':movil', str(new[8]))
                query.bindValue(':salario', str(new[9]))
                query.bindValue(':carnet', str(new[10]))
                query.bindValue(':bajadri', str(new[11]))
            if query.exec():
                pass
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText(query.lastError().text())
                mbox.exec()

        except Exception as error:
            print("Error guardarImp ", error)

    @staticmethod
    def cargaprovCli(self=None):
        try:
            var.ui.cmbProvCli.clear()
            query = QtSql.QSqlQuery()
            query.prepare("select provincia from provincias")
            if query.exec():
                var.ui.cmbProvCli.addItem(' ')
                while query.next():
                    var.ui.cmbProvCli.addItem(query.value(0))
        except Exception as error:
            print("Error en cargaProv", error)

    @staticmethod
    def selMuniCli(self=None):
        try:
            id = 0
            var.ui.cmbMunCli.clear()
            prov = var.ui.cmbProvCli.currentText()
            query = QtSql.QSqlQuery()
            query.prepare("select IdProv from provincias where provincia  = :prov")
            query.bindValue(':prov', prov)
            if query.exec():
                while query.next():
                    id = query.value(0)
            queryM = QtSql.QSqlQuery()
            queryM.prepare("select municipio from municipios where IdProv = :id")
            queryM.bindValue(':id', int(id))
            if queryM.exec():
                var.ui.cmbMunCli.addItem('')
                while queryM.next():
                    var.ui.cmbMunCli.addItem(queryM.value(0))
        except Exception as error:
            print("Error en cargaMun", error)

    @staticmethod
    def guardarcliente(newcliente):
        try:
            query = QtSql.QSqlQuery()
            # query.prepare('insert into clientes(dnicli,razonsocialcli,direccioncli,telefonocli,provcli,muncli'
            # ')VALUES(?,? ,?,?,?,?)')
            query.prepare(
                'insert into clientes(dnicli,razonsocialcli,direccioncli,telefonocli,provcli,municli)VALUES(:dni,:razonsocial,'
                ':direccion,:telefono,:prov,:muni)')
            query.bindValue(":dni", str(newcliente[0]))
            query.bindValue(":razonsocial", str(newcliente[1]))
            query.bindValue(":direccion", str(newcliente[2]))
            query.bindValue(":telefono", str(newcliente[3]))
            query.bindValue(":prov", str(newcliente[4]))
            query.bindValue(":muni", str(newcliente[5]))

            if query.exec():
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Listo')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText('Cliente dado de alta')
                mbox.exec()
                Conexion.mostrarCliente()
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText(query.lastError().text())
                mbox.exec()
        except Exception as error:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText("Error en guardar cliente (conexion.Conexion.guardarCliente) ,", error)
            mbox.exec()

    def mostrarCliente(self=None):
        try:
            registro = []
            query1 = QtSql.QSqlQuery()
            query1.prepare('Select codigocli,razonsocialcli,telefonocli,provcli from clientes')

            if query1.exec():
                while query1.next():
                    row = [query1.value(i) for i in range(query1.record().count())]
                    registro.append(row)
                    clientes.Clientes.cargarTablaCli(registro)
        except Exception as error:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText("Error en mostrar cliente(conexion.Conexion.mostrarCliente), ", error)
            mbox.exec()

    def onecliente(codigo):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('select * from clientes where codigo = :codigo')
            query.bindValue(':codigo', int(codigo))
            if query.exec():
                while query.next():
                    for i in range(8):
                        registro.append(str(query.value(i)))
            return registro
        except Exception as error:
            print('Error en onedriver', error)

    @staticmethod
    def bajacli(dni):
        try:
            query1 = QtSql.QSqlQuery()
            query1.prepare('Select bajacli from clientes')
            fecha = datetime.today()
            fecha = fecha.strftime('%d/%m/%y')
            query = QtSql.QSqlQuery()
            query.prepare(' Update clientes set bajacli = :fechabaja where '
                          'dnicli = :dni')
            query.bindValue(':fechabaja', str(fecha))
            query.bindValue(':dni', str(dni))

            if query.exec():
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText('Cliente dado de baja')
                mbox.exec()
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText(query.lastError().text() + 'Error de baja al cliente')
                mbox.exec()
        except Exception as error:
            print('Error al dar de baja al cliente', error)

    def guardarImpcli(newcliente):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('insert into(codigocli,dnicli,razonsocialcli,direccioncli,'
                              'telefonocli,provcli,municli) clientes VALUES(null, :dni,:razonsocial,'
                              ':direccion,:telefono,:prov,:muni)')
            query.bindValue(":dni", str(newcliente[1]))
            query.bindValue(":razonsocial", str(newcliente[2]))
            query.bindValue(":direccion", str(newcliente[3]))
            query.bindValue(":telefono", str(newcliente[4]))
            query.bindValue(":prov", str(newcliente[5]))
            query.bindValue(":muni", str(newcliente[6]))
            if query.exec():
                pass
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText(query.lastError().text())
                mbox.exec()

        except Exception as error:
            print("Error guardarImpCli ", error)

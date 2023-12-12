import sqlite3 as sql
import datetime as dt
import os

conexion = sql.connect('Helados.db')
volumenes = []
sabores = []
cursor = conexion.cursor()
try:
    cursor.execute("CREATE TABLE Helados (sabor VARCHAR(20), volumen VARCHAR(10), existencias INTEGER, vendido INTEGER, costo DECIMAL(10, 5), venta DECIMAL(10, 5))")
    volumenes = ['1/2 L', 'L', 'Gal']
    sabores = ["Coco", "Zapote", "Galleta", "Tamarindo", "Mora", "Leche", "Caramelo", "Nance", "Tres leches"]
    datosIniciales = []
    for sabor in sabores:
        for vol in volumenes:
            temp = (sabor, vol, 0, 0, 0, 0)
            datosIniciales.append(temp)
    cursor.executemany("INSERT INTO Helados VALUES (?, ?, ?, ?, ?, ?)", datosIniciales)
    conexion.commit()
    cursor.execute("CREATE TABLE Registros (id INTEGER PRIMARY KEY AUTOINCREMENT, fecha DATE)")
    os.mkdir('.\Registro')
except sql.OperationalError:
    print('Ya existen las tablas del db')
    cursor.execute("SELECT * FROM Helados")
    helados = cursor.fetchall()
    for helado in helados:
        if helado[0] not in sabores:
            sabores.append(helado[0])
        if helado[1] not in volumenes:
            volumenes.append(helado[1])
cursor.close()
conexion.close()

def FechaActual():
    fecha = dt.datetime.now()
    return fecha.strftime('%Y-%m-%d')

def Conectar():
    global conexion
    global cursor
    conexion = sql.connect('Helados.db')
    cursor = conexion.cursor()

def Cerrar():
    global conexion
    conexion.close()

def RegistrarVenta(cantidad, helado, volumenH):
    conexion = sql.connect('Helados.db')
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM Helados WHERE sabor = ? AND volumen = ?', (helado, volumenH))
    actual = cursor.fetchone()
    if actual[2] < cantidad:
        Cerrar()
        return 0
    cursor.execute("UPDATE Helados SET vendido = vendido + ? WHERE sabor = ? AND volumen = ?", (cantidad, helado, volumenH))
    cursor.execute("UPDATE Helados SET existencias = existencias - ? WHERE sabor = ? AND volumen = ?", (cantidad, helado, volumenH))
    conexion.commit()
    cursor.close()
    conexion.close()
    return 1

def AgregarExistencias(cantidad, helado, volumenH):
    conexion = sql.connect('Helados.db')
    cursor = conexion.cursor()
    cursor.execute("UPDATE Helados SET existencias = existencias + ? WHERE sabor = ? AND volumen = ?", (cantidad, helado, volumenH))
    conexion.commit()
    cursor.close()
    conexion.close()
    return
    
    
def GenerarRegistro():
    conexion = sql.connect('Helados.db')
    cursor = conexion.cursor()
    Fecha = FechaActual()
    totalCosto = 0
    totalVenta = 0
    totalVendidos = 0
    cursor.execute("SELECT * FROM Helados")
    Vendidos = []
    Todos = cursor.fetchall()
    for i, IC in enumerate(Todos):
        if(Todos[i][3] > 0):
            Vendidos.append(Todos[i])
    cursor.execute('INSERT INTO Registros (fecha) VALUES (?)', (Fecha,))
    conexion.commit()
    cursor.close()
    conexion.close()
    conexion = sql.connect('Helados.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Registros")
    Todos = cursor.fetchall()
    ValorAsignar = str(Todos[-1][0])
    nuevoRegistro = open(f"Registro/{ValorAsignar} - {Fecha}.txt", 'w')
    nuevoRegistro.write("|--------------------|-----|-----|------|------|\n")
    nuevoRegistro.write("|Sabor               |Vol  |Cant.|Pago  |Venta |\n")
    nuevoRegistro.write("|--------------------|-----|-----|------|------|\n")
    for sorbete in Vendidos:
        nuevoRegistro.write(f"|{sorbete[0].ljust(20)}|{sorbete[1].ljust(5)}|{str(sorbete[3]).ljust(5)}|{str(round(sorbete[3]*sorbete[4], 2)).ljust(6)}|{str(round(sorbete[3]*sorbete[5], 2)).ljust(6)}|\n")
        totalVendidos += sorbete[3]
        totalCosto += sorbete[3]*sorbete[4]
        totalVenta += sorbete[3]*sorbete[5]
    nuevoRegistro.write("|--------------------|-----|-----|------|------|\n")
    nuevoRegistro.write(f"|Total               |-----|{str(totalVendidos).ljust(5)}|{str(round(totalCosto, 2)).ljust(6)}|{str(round(totalVenta, 2)).ljust(6)}|\n")
    nuevoRegistro.write("|--------------------|-----|-----|------|------|\n")
    nuevoRegistro.close()
    cursor.execute('UPDATE Helados SET vendido = 0')
    conexion.commit()
    cursor.close()
    conexion.close()

def TodosHelados():
    conexion = sql.connect('Helados.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Helados ORDER BY sabor")
    Todos = cursor.fetchall()
    cursor.close()
    conexion.close()
    return Todos

def ModCosto(nuevoValor, sabor, volumenH):
    conexion = sql.connect('Helados.db')
    cursor = conexion.cursor()
    cursor.execute("UPDATE Helados SET costo = ? WHERE sabor = ? AND volumen = ?", (nuevoValor, sabor, volumenH))
    conexion.commit()
    cursor.close()
    conexion.close()
    return

def ModPrecio(nuevoValor, sabor, volumenH):
    conexion = sql.connect('Helados.db')
    cursor = conexion.cursor()
    cursor.execute("UPDATE Helados SET venta = ? WHERE sabor = ? AND volumen = ?", (nuevoValor, sabor, volumenH))
    conexion.commit()
    cursor.close()
    conexion.close()
    return

def CrearSabor(nuevoSabor):
    global sabores
    conexion = sql.connect('Helados.db')
    cursor = conexion.cursor()
    sabores.append(nuevoSabor)
    nuevasFilas = []
    for vol in volumenes:
        temp = (nuevoSabor, vol, 0, 0, 0, 0)
        nuevasFilas.append(temp)
    cursor.executemany('INSERT INTO Helados VALUES (?, ?, ?, ?, ?, ?)', nuevasFilas)
    conexion.commit()
    cursor.close()
    conexion.close()
    return

def EliminarSabor(Del):
    global sabores
    conexion = sql.connect('Helados.db')
    cursor = conexion.cursor()
    sabores.remove(Del)
    cursor.execute('DELETE FROM Helados WHERE sabor = ?', (Del,))
    conexion.commit()
    cursor.close()
    conexion.close()
    return

def CrearVol(nuevoVol):
    global volumenes
    conexion = sql.connect('Helados.db')
    cursor = conexion.cursor()
    volumenes.append(nuevoVol)
    nuevasFilas = []
    for sabor in sabores:
        temp = (sabor, nuevoVol, 0, 0, 0, 0)
        nuevasFilas.append(temp)
    cursor.executemany('INSERT INTO Helados VALUES (?, ?, ?, ?, ?, ?)', nuevasFilas)
    conexion.commit()
    cursor.close()
    conexion.close()
    return

def EliminarVol(Del):
    global volumenes
    conexion = sql.connect('Helados.db')
    cursor = conexion.cursor()
    volumenes.remove(Del)
    cursor.execute('DELETE FROM Helados WHERE volumen = ?', (Del,))
    conexion.commit()
    cursor.close()
    conexion.close()
    return







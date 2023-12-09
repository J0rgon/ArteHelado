import sqlite3 as sql

conexion = sql.connect('Helados.db')
volumenes = ('1/2 L', 'L', 'Gal')
sabores = ("Coco", "Zapote", "Galleta", "Tamarindo", "Mora", "Leche", "Caramelo", "Nance", "Tres leches")
datosIniciales = []
for sabor in sabores:
    datoMedio = (sabor, volumenes[0], 0, 0, 0, 0)
    datoLitro = (sabor, volumenes[1], 0, 0, 0, 0)
    datoGal = (sabor, volumenes[2], 0, 0, 0, 0)
    datosIniciales.append(datoMedio)
    datosIniciales.append(datoLitro)
    datosIniciales.append(datoGal)
cursor = conexion.cursor()

try:
    cursor.execute("CREATE TABLE Helados (sabor VARCHAR(20), volumen VARCHAR(10), existencias INTEGER, vendido INTEGER, costo DECIMAL(10, 5), venta DECIMAL(10, 5))")
    cursor.executemany("INSERT INTO Helados VALUES (?, ?, ?, ?, ?, ?)", datosIniciales)
    conexion.commit()    

    cursor.execute("CREATE TABLE Registros (nombre VARCHAR(100), vendidos INTEGER, fecha DATE)")
except sql.OperationalError:
    print('Ya existen las tablas del db')

cursor.close()
conexion.close()

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
        return
    cursor.execute("UPDATE Helados SET vendido = vendido + ? WHERE sabor = ? AND volumen = ?", (cantidad, helado, volumenH))
    cursor.execute("UPDATE Helados SET existencias = existencias - ? WHERE sabor = ? AND volumen = ?", (cantidad, helado, volumenH))
    conexion.commit()
    cursor.close()
    conexion.close()
    return

def AgregarExistencias(cantidad, helado, volumenH):
    conexion = sql.connect('Helados.db')
    cursor = conexion.cursor()
    print('Se llega a la función agregar')
    cursor.execute("UPDATE Helados SET existencias = existencias + ? WHERE sabor = ? AND volumen = ?", (cantidad, helado, volumenH))
    conexion.commit()
    cursor.close()
    conexion.close()
    print('Se cierra todo')
    







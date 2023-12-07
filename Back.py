import sqlite3
conexion = sqlite3.connect('Helados.db')
cursor = conexion.cursor


conexion.close()
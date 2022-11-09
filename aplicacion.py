#ExamenParcial
import sqlite3
#Creando tabla

conexion=sqlite3.connect("Cachay_almacen.db")
tabla_producto="""CREATE TABLE producto(
                    idproducto INTEGER PRIMARY KEY AUTOINCREMENT,
                    codigo TEXT,
                    nombre TEXT,
                    precio FLOAT
                    )
                """
cursor=conexion.cursor()
cursor.execute(tabla_producto)
conexion.close()

def menu():
    print("MENU OPCIONES")
    print("1.Registrar")
    print("2.Eliminar")
    print("3.Editar")
    print("4.Listar")
    print("5.Salir")
    
menu()
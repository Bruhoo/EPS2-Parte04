#ExamenParcialLP3
import sqlite3
from pathlib import Path
#Cachay
def crear_tabla():
    #Creando la tabla
    conexion=sqlite3.connect("Ciriaco_almacen.db")
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
#Delgado    
def menu():
    if Path("Ciriaco_almacen.db").exists()==False:
        crear_tabla()
    #Crando el menu
    print("\tMENU OPCIONES")
    print("1.Registrar")
    print("2.Eliminar")
    print("3.Editar")
    print("4.Listar")
    print("5.Salir")
    #Solicitar eleccion
    opcion=int(input("\nEscoja una de las opciones: "))
    if opcion==1:
        registrar()
    elif opcion==2:
        eliminar()
    elif opcion==3:
        editar()
    elif opcion==4:
        listar()
    elif opcion==5:
        print("Hasta luego :)")
#Creando funcion registrar        
def registrar():
    conexion=sqlite3.connect("Ciriaco_almacen.db")
    print("Ingrese los siguientes datos")
    nombre_p=input("Digite el nombre del producto: ")
    codigo_p=input("Digite el codigo del producto: ")
    precio_p=float(input("Digite el precio del producto: "))
    consulta="INSERT INTO producto(codigo,nombre,precio) values (?,?,?)"
    conexion.execute(consulta, (codigo_p,nombre_p,precio_p))
    conexion.commit()
    conexion.close()
    volver()
#Creando funcion listar    
def listar():
    conexion=sqlite3.connect("Ciriaco_almacen.db")
    cursor=conexion.cursor()
    consulta="SELECT * FROM producto"
    cursor.execute(consulta)
    records = cursor.fetchall()
    print("Cantidad de productos: ", len(records))
    print("Esta es la lista de productos")
    print("{:>5}  {:>5}  {:>10}   {:>6}".format("Id","Codigo","Nombre","Precio"))
    for row in records:        
        print("{:>5}  {:>5}  {:>10}   {:>6}".format(*row))
        print("\n")
    conexion.commit()
    conexion.close()
    volver()
#Creando funcion editar    
def editar():
    conexion=sqlite3.connect("Ciriaco_almacen.db")
    cursor=conexion.cursor()
    mod_nombre=input("Ingrese el nombre del producto a modificar: ")
    codex=input("Ingrese el nuevo codigo del producto:")
    nombre=input("Ingrese el nuevo nombre del producto:")
    precio=float(input("Ingrese el nuevo precio del producto:"))
    consulta="""UPDATE producto
            SET
                codigo=?,nombre=?,precio=?
            WHERE
                nombre=?
                """
    cursor.execute(consulta,(codex,nombre,precio,mod_nombre))
    conexion.commit()
    conexion.close()
    volver()
#Creando funcion eliminar
def eliminar():
    conexion=sqlite3.connect("Ciriaco_almacen.db")
    cursor=conexion.cursor()
    id_producto=int(input("Ingrese el id del producto a eliminar: "))
    consulta="DELETE FROM producto WHERE idproducto=?"
    cursor.execute(consulta,(id_producto,))
    conexion.commit()
    conexion.close()
    volver()
#Creando funcion volver
def volver():
    opcion_1=input("Desea regresar al menu anterior(SI/NO):  ")
    if opcion_1.lower()=='si':
        menu()
    else:
        print("Bye")
#Ejecuntando menu para iniciar todo
menu()    
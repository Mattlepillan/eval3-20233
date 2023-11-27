import os
os.system("cls")

menu = """  MENU  
1. Grabar vehiculo
2. Buscar Vehiculo
3. Imprimir certificados
0. Salir
"""

listaTipo = ["Auto", "Camioneta" ]
listaPatente = ["NYYL23", "KTHH54"]
listaMarca = ["Chevrolet", "Toyota"]
listaPrecio = [5700000, 8100000]
montoMulta = [85000, 130000]
fechaMulta = ["02-10-2016", "05-01-2020"]
fechaReg_vehiculo = ["03-12-2013", "17-08-2017"]
listaNombre_dueño = ["Sebastian Carrillo", "Andres Bello"]

listaCont = [1700, 2000]
anotVig = [2500, 3100]
# Datos dueño
listarut = ["21582676-7", "11449433-K"]
fechaNac = ["20-01-1978", ""]



def grabarVehiculo():
    tipo = input("ingrese tipo de vehiculo: ")
    listaTipo.append(tipo)

    # Validacion patente
    while True:
        try:
            patente = input("Ingrese patente: ")
            if len(patente) == 6 and patente[5:].isdigit:
                listaPatente.append(patente)
                break
            else:
                print("Patente invalida")
        except:
            print("Excepcion en codigo")

    # Validacion marca
    while True:
        try:
            marca = input("Ingrese marca del vehiculo: ")
            if len(marca) >= 2 and len(marca) <= 15:
                listaMarca.append(marca)
                break
            else:
                print("Marca invalida")
        except:
            print("Excepcion en codigo")

    # Validacion precio
    while True:
        try:
            precio = int(input("Ingrece precio del vehiculo: "))
            if precio > 5000000:
                listaPrecio.append(precio)
                break
            else:
                print("Precio invalido")
        except:
            print("Excepcion en codigo")

    monto_multa = int(input("Ingrese el monto de la multa: "))
    montoMulta.append(monto_multa)

    fecha_multa = input("ingrese fecha de la multa (dd-mm-aaaa): ")
    fechaMulta.append(fecha_multa)

    fecha_registro = input("ingrese la fecha de regitro del vehiculo (dd-mm-aaaa): ")
    fechaReg_vehiculo.append(fecha_registro)

    nombre = input("Ingrese el nombre del dueño: ")
    listaNombre_dueño.append(nombre)                
                                

def buscarVehiculo():
    print(f"{listaPatente}")
    patentes = input("Ingrese patente: ")
    if not patentes in listaPatente:
        print("La patente no existe")
    else:
        indice = listaPatente.index(patentes)
        print(f"Nombre del dueño : {listaNombre_dueño[indice]}")
        print(f"Tipo             : {listaTipo[indice]}") 
        print(f"Marca            : {listaMarca[indice]}")
        print(f"Precio           : {listaPrecio[indice]}")
        print(f"Multa            : {montoMulta[indice]}")
        print(f"Fecha de multa   : {fechaMulta[indice]}")
        print(f"Fecha de registro: {fechaReg_vehiculo[indice]}")




def imprimirCertificados():
    rut = input("Ingrese rut: ")
    listarut.append(rut)
    fecha_nac = input("ingrese fecha de nacimiento: ")
    fechaNac.append(fecha_nac)
    opcion = int(input("Elija una opcion\n1. Certificado de Emisio de contaminantes\n2. Certificado de anotaciones vigentes\n3. Certificado de multas\n"))
    if opcion == 1:
        monto = int(input("Ingrese monto: "))
        listaCont.append(monto)
        print(listaPatente)
        patente = input("Ingrese patente: ")
        indice = listaPatente.index(patente)
        print(" CERTIFICADO DE EMISION DE CONTAMINANTES")
        print(f"Nombre dueño       : {listaNombre_dueño[indice]}")
        print(f"rut                : {listarut[indice]}")
        print(f"Fecha de nacimiento: {fechaNac[indice]}")
        print(f"Monto              : {listaCont[indice]}")
    elif opcion == 2: 
        monto = int(input("Ingrese monto: "))
        anotVig.append(monto)
        print(listaPatente)
        patente = input("Ingrese patente: ")
        indice = listaPatente.index(patente)
        print(" CERTIFICADO DE EMISION DE ANOTACIONES VIGENTES")
        print(f"Nombre dueño       : {listaNombre_dueño[indice]}")
        print(f"rut                : {listarut[indice]}")
        print(f"Fecha de nacimiento: {fechaNac[indice]}")
        print(f"Monto              : {anotVig[indice]}")   
    else:
        print(listaPatente)
        patente = input("Ingrese patente: ")
        indice = listaPatente.index(patente)
        print(" CERTIFICADO DE EMISION DE CONTAMINANTES")
        print(f"Nombre dueño       : {listaNombre_dueño[indice]}")
        print(f"rut                : {listarut[indice]}")
        print(f"Fecha de nacimiento: {fechaNac[indice]}")
        print(f"Monto              : {montoMulta[indice]}")    






# Programa principal
import os
os.system("cls")

while True:
    try:
        opc = int(input(menu))
        if opc >= 0 and opc <= 3:
            if opc == 0:
                break
            elif opc == 1:
                grabarVehiculo()
            elif opc == 2:
                buscarVehiculo()
            else:
                imprimirCertificados()
        else:
            print("Opcion invalida")
    except:
        print("Excepcion en codigo")                        


print("Hasta pronto, Matthew Lepillan")
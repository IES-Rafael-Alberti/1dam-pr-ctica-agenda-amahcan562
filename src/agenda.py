"""
27/11/2023

Práctica del examen para realizar en casa
-----------------------------------------

* El programa debe estar correctamente documentado.

* Debes intentar ajustarte lo máximo que puedas a lo que se pide en los comentarios TODO.

* Tienes libertad para desarrollar los métodos o funciones que consideres, pero estás obligado a usar como mínimo todos los que se solicitan en los comentarios TODO.

* Además, tu programa deberá pasar correctamente las pruebas unitarias que se adjuntan en el fichero test_agenda.py, por lo que estás obligado a desarrollar los métodos que se importan y prueban en la misma: pedir_email(), validar_email() y validar_telefono()

"""

import os
import pathlib
from os import path

# Constantes globales
RUTA = pathlib.Path(__file__).parent.absolute() 

NOMBRE_FICHERO = 'contactos.csv'

RUTA_FICHERO = path.join(RUTA, NOMBRE_FICHERO)

# Crear un conjunto con las posibles opciones del menú de la agenda

OPCIONES_MENU = set(["1", "2", "3", "4", "5", "6", "7", "8"])

#TODO: Utiliza este conjunto en las funciones agenda() y pedir_opcion()


def borrar_consola():
    """ Limpia la consola
    """
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def cargar_contactos(contactos: list) -> list:
    """ Carga los contactos iniciales de la agenda desde un fichero
        :param contactos: Lista de contactos.
    """
    # Controlar los posibles problemas derivados del uso de ficheros...
    try:
        with open(RUTA_FICHERO, 'r') as fichero:
            for linea in fichero:
                datos = linea.split(";")
                contacto = {"nombre": datos[0], "apellido": datos[1], "correo": datos[2], "telefonos": datos[3:]}
                contactos.append(contacto)
    except FileNotFoundError:
        print("ERROR! El fichero no existe.")
    except Exception:
        print("Se ha producido un ERROR!")
    
    return contactos


def agregar_contacto(contactos: list):
    """ Añade un nuevo contacto 
        :param contactos: Lista de contactos.
    """
    nuevo_contacto = {}

    nombre = input("Introduzca el nombre: ").title()
    
    while nombre == "":
        print("ERROR! Los campos no pueden estar vacíos. ")
        nombre = input("Introduzca el nombre: ").title()
    
    nuevo_contacto["nombre"] = nombre
    
    apellido = input("Introduzca el apellido: ").title()

    while apellido == "":
        print("ERROR! Los campos no pueden estar vacíos. ")
        apellido = input("Introduzca el apellido: ").title()

    nuevo_contacto["apellido"] = apellido

    correo = input("Introduzca el correo electrónico: ")

    while correo == "" or (not "@" in correo):
        print("ERROR! El correo introducido no es válido o ya existe. ")
        correo = input("Introduzca el correo electrónico: ")

    nuevo_contacto["correo"] = correo

    telefonos = []
    telefono = input("Introduzca un teléfono (pulse ENTER para finalizar): ")
    
    while telefono:
        telefono = telefono.replace(" ","")
        if telefono.startswith("+34"):
            telefono = telefono[3:]

        if len(telefono) == 9 and telefono.isdigit():
            telefonos.append(telefono)
        else:
            print("ERROR! El correo introducido no es válido o ya existe. ")

        telefono = input("Introduzca otro teléfono (pulse ENTER para finalizar): ")

    nuevo_contacto["telefonos"] = telefonos

    contactos.append(nuevo_contacto)


def eliminar_contacto(contactos: list):
    """ Elimina un contacto de la agenda
        :param contactos: Lista de contactos.
    """

    pos = buscar_contacto(contactos)

    try:
        #TODO: Crear función buscar_contacto para recuperar la posición de un contacto con un email determinado

        if pos != None:
            del contactos[pos]
            print("Se eliminó 1 contacto")
        else:
            print("No se encontró el contacto para eliminar")
    except Exception as e:
        print(f"**Error** {e}")
        print("No se eliminó ningún contacto")


def buscar_contacto(contactos: list):
    """ Busca contacto a eliminar especificando el correo electrónico.
        :param contactos: Lista de contactos.
    """
    correo_a_borrar = str(input("Introduzca el correo del contacto a borrar: "))
    for pos, contacto in enumerate(contactos):
        if contacto.get("correo") == correo_a_borrar:
            return pos


def modificar_contacto(contactos: list):
    """ 
    """
    

def mostrar_contactos(contactos: list):
    """ Muestra todos los contactos de la agenda
        :param contactos: Lista de contactos.
    """
    print("AGENDA")
    print("------")

    for contacto in contactos:
        print(f"Nombre: {contacto['nombre']} {contacto['apellido']} ({contacto['correo']})")
        telefonos = " / ".join([f"34-{tel[:3]}{tel[3:6]}{tel[6:9]}" for tel in contacto.get('telefonos', [])])
        print(f"Teléfonos: {telefonos if telefonos else 'ninguno'}")
        print("------")

    print(f"** Total de contactos: {len(contactos)} **")


def vaciar_agenda(contactos: list):
    """ Vacía la agenda de contactos
        :param contactos: Lista de contactos.
    """
    try:
        contactos.clear()
        print("Se ha vaciado la agenda.")
    except Exception as e:
        print(f"**Error** {e}")
        print("ERROR al vaciar la agenda.")
        


def agenda(contactos: list):
    """ Ejecuta el menú de la agenda con varias opciones
        :param contactos: Lista de contactos. 
    """
    #TODO: Crear un bucle para mostrar el menú y ejecutar las funciones necesarias según la opción seleccionada...

    opcion = 0
    while opcion != 8:
        mostrar_menu()
        opcion = pedir_opcion()

        #TODO: Se valorará que utilices la diferencia simétrica de conjuntos para comprobar que la opción es un número entero del 1 al 6
        if opcion in OPCIONES_MENU:
            if opcion == "1":
                borrar_consola()
                agregar_contacto(contactos)

            elif opcion == "2":
                borrar_consola()
                email = input("Introduzca el correo del contacto a modificar: ")
                modificar_contacto(contactos, email)

            elif opcion == "3":
                borrar_consola()
                email = input("Introduzca el correo del contacto a eliminar: ")

            elif opcion == "4":
                borrar_consola()
                vaciar_agenda(contactos)

            elif opcion == "5":
                borrar_consola()
                cargar_contactos(contactos)

            elif opcion == "6":
                borrar_consola()
                correo = input("Introduzca el correo del contacto a buscar: ")
                print(buscar_contacto(contactos, email))

            elif opcion == "7":
                borrar_consola()
                mostrar_contactos(contactos)


def mostrar_menu():
    """ Muestra las opciones a elegir.
    """
    print("AGENDA")
    print("------")
    print("1. Nuevo contacto")
    print("2. Modificar contacto")
    print("3. Eliminar contacto")
    print("4. Vaciar agenda")
    print("5. Cargar agenda inicial")
    print("6. Mostrar contactos por criterio")
    print("7. Mostrar la agenda completa")
    print("8. Salir\n\n")


def pedir_opcion():
    """ Pide una opción entre las 8.
        :return opcion: Devuelve la opcion
    """
    try:
        opcion = input(">> Seleccione una opción: ")
    except ValueError:
        print("ERROR! Caracter no válido.")

    return opcion


def pulse_tecla_para_continuar():
    """ Muestra un mensaje y realiza una pausa hasta que se pulse una tecla
    """
    print("\n")
    os.system("pause")


def main():
    """ Función principal del programa
    """
    borrar_consola()

    #TODO: Asignar una estructura de datos vacía para trabajar con la agenda
    contactos = []

    #TODO: Modificar la función cargar_contactos para que almacene todos los contactos del fichero en una lista con un diccionario por contacto (claves: nombre, apellido, email y telefonos)
    #TODO: Realizar una llamada a la función cargar_contacto con todo lo necesario para que funcione correctamente.
    cargar_contactos(contactos)

    #TODO: Crear función para agregar un contacto. Debes tener en cuenta lo siguiente:
    # - El nombre y apellido no pueden ser una cadena vacía o solo espacios y se guardarán con la primera letra mayúscula y el resto minúsculas (ojo a los nombre compuestos)
    # - El email debe ser único en la lista de contactos, no puede ser una cadena vacía y debe contener el carácter @.
    # - El email se guardará tal cuál el usuario lo introduzca, con las mayúsculas y minúsculas que escriba. 
    #  (CORREO@gmail.com se considera el mismo email que correo@gmail.com)
    # - Pedir teléfonos hasta que el usuario introduzca una cadena vacía, es decir, que pulse la tecla <ENTER> sin introducir nada.
    # - Un teléfono debe estar compuesto solo por 9 números, aunque debe permitirse que se introduzcan espacios entre los números.
    # - Además, un número de teléfono puede incluir de manera opcional un prefijo +34.
    # - De igual manera, aunque existan espacios entre el prefijo y los 9 números al introducirlo, debe almacenarse sin espacios.
    # - Por ejemplo, será posible introducir el número +34 600 100 100, pero guardará +34600100100 y cuando se muestren los contactos, el telófono se mostrará como +34-600100100. 
    #TODO: Realizar una llamada a la función agregar_contacto con todo lo necesario para que funcione correctamente.
    agregar_contacto(contactos)

    pulse_tecla_para_continuar()
    borrar_consola()

    #TODO: Realizar una llamada a la función eliminar_contacto con todo lo necesario para que funcione correctamente, eliminando el contacto con el email rciruelo@gmail.com
    eliminar_contacto(contactos)

    pulse_tecla_para_continuar()
    borrar_consola()

    #TODO: Crear función mostrar_contactos para que muestre todos los contactos de la agenda con el siguiente formato:
    # ** IMPORTANTE: debe mostrarlos ordenados según el nombre, pero no modificar la lista de contactos de la agenda original **
    #
    # AGENDA (6)
    # ------
    # Nombre: Antonio Amargo (aamargo@gmail.com)
    # Teléfonos: niguno
    # ......
    # Nombre: Daniela Alba (danalba@gmail.com)
    # Teléfonos: +34-600606060 / +34-670898934
    # ......
    # Nombre: Laura Iglesias (liglesias@gmail.com)
    # Teléfonos: 666777333 / 666888555 / 607889988
    # ......
    # ** resto de contactos **
    #
    #TODO: Realizar una llamada a la función mostrar_contactos con todo lo necesario para que funcione correctamente.
    mostrar_contactos(contactos)

    pulse_tecla_para_continuar()
    borrar_consola()

    #TODO: Crear un menú para gestionar la agenda con las funciones previamente desarrolladas y las nuevas que necesitéis:
    # AGENDA
    # ------
    # 1. Nuevo contacto
    # 2. Modificar contacto
    # 3. Eliminar contacto
    # 4. Vaciar agenda
    # 5. Cargar agenda inicial
    # 6. Mostrar contactos por criterio
    # 7. Mostrar la agenda completa
    # 8. Salir
    #
    # >> Seleccione una opción: 
    #
    #TODO: Para la opción 2, modificar un contacto, deberás desarrollar las funciones necesarias para actualizar la información de un contacto.
    #TODO: También deberás desarrollar la opción 6 que deberá preguntar por el criterio de búsqueda (nombre, apellido, email o telefono) y el valor a buscar para mostrar los contactos que encuentre en la agenda.
    borrar_consola()
    contactos = agenda(contactos)


if __name__ == "__main__":
    main()
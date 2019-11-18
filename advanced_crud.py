import crud
import re
import MySQLdb as my
import create_random_data as crd
from progressbar import *
import colorama as c

c.init(autoreset=True)

widgets = ['Test: ', Percentage(), ' ', Bar(marker='#',left='[',right=']'), ' ', ETA(), ' ']


#Pasar True de primer argumento para devolver todos los registros #False para especificar
#Pasar True de segundo argumento para devolver profesores #False para alumnos
def ver(todos, bo):
    ar = ["Teléfono", "id_empleado", "telefono", "profesor"] if bo else ["Grupo", "id_alumno", "id_grupo", "alumno"]
    h = "0" if todos else input("Inserte un ID, Nombre o Apellido: ")
    
    while (re.match(r"^\d*$", h) == None and re.match(r"^[A-Za-z]*$", h) == None) or h == "": h = input(c.Fore.YELLOW + "Inserte un ID/Nombre/Apellido válido: ")

    base = "{4}{0:^5}{4} {4}{1:^40}{4} {4}{2:^50}{4} {4}{3:^12}{4}"
    f = base.format("N", "Nombre", "Correo", ar[0], '|')

    if re.match(r"^\d*$", h): todos = "1 = 1" if todos else "{} = {}".format(ar[1], h)
    else: 
        todos = "1 = 1" if todos else "{} = {}".format("1 ", 
        " 2 or (nombre like '%{0}%' or primer_apellido like '%{0}%' or segundo_apellido like '%{0}%')".format(h))

    print("-"*len(f) + "\n" + f + "\n" + "-"*len(f))

    arpa = crud.ver("{}, concat(nombre, ' ', primer_apellido, ' ', segundo_apellido), correo, {}".format(ar[1], ar[2]),
    ar[3],todos)
    
    for i in arpa:
        print(base.format(i[0], i[1], i[2], i[3], '|'))

    print("-"*len(f))

def gen_a_lot(p, a):
    widgets[0] = "Creando profesores: "
    pbar = ProgressBar(widgets=widgets, maxval=p)
    pbar.start()
    for i in range(p):
        crd.insertar_profesor()
        pbar.update(i)
    pbar.finish()

    widgets[0] = "Creando alumnos: "
    pbar = ProgressBar(widgets=widgets, maxval=a)
    pbar.start()
    for i in range(a):
        crd.insertar_alumno()
        pbar.update(i)
    pbar.finish() 

def insertar(bol):
    if input("Confirmar inserción (Y/N)\n").lower() == "y":
        try:
            if bol:
                crud.crear("alumno", "", crear_persona(False))
            else:
                crud.crear("profesor", "", crear_persona(True))
        except ValueError:
            print(c.Fore.YELLOW + "No se recibió un número, intente otra vez:\n")
        except my.IntegrityError as e:
            print(c.Fore.RED + "\nEl correo ya está en uso, cancelando inserción\n")

        if bol: print(c.Fore.GREEN + "\nALUMNO INSERTADO CORRECTAMENTE\n")
        else: print(c.Fore.GREEN + "\nPROFESOR INSERTADO CORRECTAMENTE\n")

    else: print(c.Fore.RED + "\nOPERACIÓN CANCELADA\n")

def text_valid(text): #Solo letras
    while re.match(r"^[A-Za-z]*$", text) == None or text == "":
        test = input(c.Fore.YELLOW + "Fortmato inválido, verifique el texto y pruebe otra vez: ")

def num_valid(text): #Solo letras
    while re.match(r"^[0-9]*$", text) == None or text == "":
        test = input(c.Fore.YELLOW + "Fortmato inválido, verifique el número y pruebe otra vez: ")

def crear_persona(profesor): #True / False
    sa = [0, "Primer apellido: ", "Segundo apellido: ", "Nombre: ", 
    "Correo: ", "Telefono: " if profesor else "Grupo: "]

    ar = [sa[0], 
        input(sa[1]),
        input(sa[2]),
        input(sa[3]),
        input(sa[4]),
        input(sa[5])]

    for i in range(1, 3):
        while not re.match(r"\w\D{2,}", ar[i]):
            ar[i] = input(c.Fore.YELLOW + "El {} que introdujo no es válido, intente otra vez\n"
            .format(sa[i][:-2].lower()))

    while not re.match(r".+\@(\w\D{2,})\..*", ar[4]):
        ar[4] = input(c.Fore.YELLOW + "El correo que introdujo no es válido, intente otra vez\n")

    while not re.match(r"\d", ar[5]):
        ar[5] = input(c.Fore.YELLOW + "El {} que introdujo no es válido, intente otra vez\n".format(sa[5][:-2].lower()))

    return "{}, '{}', '{}', '{}', '{}', '{}'".format(
        ar[0], ar[4], ar[2], ar[3], ar[1], ar[5])

def reset_database(): #Cambiar a borrado uno por uno para la barra?
    print("ENTRANDO A BORRADO TOTAL, CONTINUE BAJO SU PROPIO RIESGO")
    if input(c.Fore.RED + "¿Estás seguro de querer eliminar TODOS LOS REGISTROS asociados a 'ALUMNO'? (Y/N)\n").lower() == "y":
        crud.eliminar("alumno", "1 = 1")
        print("Eliminados todos los alumnos")
    if input(c.Fore.RED + "¿Estás seguro de querer eliminar TODOS LOS REGISTROS asociados a 'PROFESOR'? (Y/N)\n").lower() == "y":
        crud.eliminar("profesor", "1 = 1")
        print("Eliminados todos los profesores")

def borrar(alumno): #True/False
    print(c.Fore.RED + "Procediendo a borrar, inserte no numéricos para cancelar")

    a = "alumno" if alumno else "profesor"
    b = "id_alumno" if alumno else "id_empleado"
    c = input("Inserte ID: ")

    try: 
        c = int(c)
        crud.eliminar(a, "{} = {}".format(b,c))
        print(c.Fore.GREEN + "\nBORRADO EXITOSO\n")
    except ValueError:
        print(c.Fore.RED + "\nCANCELANDO OPERACIÓN\n")
    except: 
        print(c.Fore.RED + "\nError desconocido, cancelando...\n")
    

def modificar(alumno): #True/False
    print("Procediendo a actualizar, inserte no numéricos para cancelar")

    a = "alumno" if alumno else "profesor"
    b = "id_alumno" if alumno else "id_empleado"
    b2 = ["nombre", "primer_apellido", "segundo_apellido", "correo", "id_grupo" if alumno else "telefono"]
    e = input(c.Fore.RESET + "Inserte ID: ")

    print("\nDeje en blanco para no modificar\n")

    try: 
        e = int(e)
        d = list(crud.ver("{},{},{},{},{}".format(b2[0], b2[1], b2[2], b2[3], b2[4]), a, "{} = {}".format(b, e))[0])

        for i in range(0, 5):
            temp = input("{} --> ".format(d[i]))
            if temp != "": d[i] = temp

        for i in range(0,5):
            crud.modificar(a, b2[i], "'" + d[i] + "'", b, e)

        print(c.Fore.GREEN + "\nACTUALIZACIÓN EXITOSA\n")
    except ValueError:
        print(c.Fore.RED + "\nCANCELANDO OPERACIÓN\n")
    except: 
        print(c.Fore.RED + "\nError desconocido, cancelando...\n")

####FALTA ESTO:
# Averiguar por qué a veces al terminar una operación dentro de un submenú se activa otra opción sin querer
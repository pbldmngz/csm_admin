import crud
import create_random_data as crd
from progressbar import *
widgets = ['Test: ', Percentage(), ' ', Bar(marker='#',left='[',right=']'), ' ', ETA(), ' ']

#Pasar True de primer argumento para devolver todos los registros #False para especificar
#Pasar True de segundo argumento para devolver profesores #False para alumnos
def ver(todos, bo):
    ar = ["Teléfono", "id_empleado", "telefono", "profesor"] if bo else ["Grupo", "id_alumno", "id_grupo", "alumno"]
    h = 0 if todos else input("Inserte ID: ")
    base = "{4}{0:^5}{4} {4}{1:^40}{4} {4}{2:^50}{4} {4}{3:^12}{4}"
    f = base.format("N", "Nombre", "Correo", ar[0], '|')
    todos = "1 = 1" if todos else "{} = {}".format(ar[1], int(h))

    print("-"*len(f) + "\n" + f + "\n" + "-"*len(f))
    
    for i in crud.ver("{}, concat(nombre, ' ', primer_apellido, ' ', segundo_apellido), correo, {}".format(ar[1], ar[2]),
    ar[3],todos):
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

def insertar(): #Aún no se ha hecho nada
    while True:
        v = input("Escriba 1 para ALUMNO, 2 para PROFESOR o 3 para SALIR")
        if v == 1:
            crud.crear("alumno", "", "")
        elif v == 2:
            crud.crear("profesor", "", "")
        else:
            break

def reset_database(): #Cambiar a borrado uno por uno para la barra?
    if input("¿Estás seguro de querer eliminar TODOS LOS REGISTROS asociados a 'ALUMNO'?").lower() == "y":
        crud.eliminar("alumno", "1 = 1")
    if input("¿Estás seguro de querer eliminar TODOS LOS REGISTROS asociados a 'PROFESOR'?").lower() == "y":
        crud.eliminar("profesor", "1 = 1")

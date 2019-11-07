import generador as g
import crud
import random
import re

def get_next_id(table, col):
    return int(re.sub(r'[\D_]+', '', str(crud
    .ver("max({})".format(col), table, "1 = 1")))) + 1
    #Obtener el index donde debe ser colocado

def insertar_materia(alumno, a):
    s = "materia_alumno" if alumno else "materia_profesor"
    h = "id_alumno" if alumno else "id_empleado"
    for i in range(0, 7):
        if random.randint(0,1) == 1: crud.crear(s, "{}, id_materia"
        .format(h), "{}, {}".format(a, i))

def insertar_profesor():
    p = g.generar_persona(get_next_id("profesor", "id_empleado") , False)
    crud.crear("profesor", "", "{},'{}','{}','{}','{}','{}'"
    .format(0,p[5],p[4],p[1],p[2],p[3]))
    insertar_materia(False, int(p[0]))

def insertar_alumno():
    a = g.generar_persona(get_next_id("alumno", "id_alumno"), True)
    crud.crear("alumno", "", "{},'{}','{}','{}','{}','{}'"
    .format(0,a[5],a[1],a[2],a[3],a[6]))
    insertar_materia(True, int(a[0]))
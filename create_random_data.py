import generador as g
import crud
import re

def get_id(table, col):
    return int(re.sub(r'[\D_]+', '', str(crud
    .ver("max({})".format(col), table, "1 = 1")))) + 1
    #Obtener el index donde debe ser colocado

def insertar_profesor():
    p = g.generar_persona(get_id("profesor", "id_empleado") , False)
    crud.crear("profesor", "", "{},'{}','{}','{}','{}','{}'"
    .format(p[0],p[5],p[4],p[1],p[2],p[3]))

def insertar_alumno():
    a = g.generar_persona(get_id("alumno", "id_alumno"), True)
    crud.crear("alumno", "", "{},'{}','{}','{}','{}','{}'"
    .format(a[0],a[5],a[1],a[2],a[3],a[6]))

insertar_alumno()
#Recuerda que para consola que podrá usar el usuario puedes utilizar re para evitar sql injection
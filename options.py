import crud

#Pasar True de primer argumento para devolver todos los registros
#Pasar True de segundo argumento para devolver profesores
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

ver(True, True)

import keyboard
import os
import advanced_crud as ac

clear = lambda: os.system('cls')
selected = 1
limit = 4

submenu = 0
# 0 == Menu principal
# 1 == Menú de vista

control = False

def show_menu():
    global selected
    setter()
    clear()
    opt = ["", "VER REGISTROS", "INSERTAR REGISTRO ", "ELIMINAR REGISTRO", "MODIFICAR REGISTRO"]
    defin = ["", "Ver datos de alumnos o profesores", "Dar de alta nuevos estudiantes y profesores",
    "Eliminar registros disponibles directamente en la base de datos", "Cambiar datos a alumnos y profesores"]
    print("Elige una opción:")
    for i in range(1, len(opt)):
        print("{1} {0}. {3:25} {2}".format(i, ">" if selected == i else " ", "<" if selected == i else " ", opt[i]))
    
    print("\n\n" + defin[selected])

def show_sm1():
    global selected
    setter()
    clear()
    opt = ["", "LISTADO ALUMNOS", "LISTADO PROFESORES", "UN ALUMNO", "UN PROFESOR"]
    print("Elige una opción:")
    for i in range(1, len(opt)):
        print("{1} {0}. {3:25} {2}".format(i, ">" if selected == i else " ", "<" if selected == i else " ", opt[i]))

def menu_selector():
    if submenu == 0:
        show_menu()
    elif submenu == 1:
        show_sm1()


def up():
    global selected
    global submenu
    selected -= 1
    if submenu == 0: show_menu()
    elif submenu == 1: show_sm1()

def down():
    global selected
    global submenu
    selected += 1
    if submenu == 0: show_menu()
    elif submenu == 1: show_sm1()

def setter():
    global selected
    global limit #Esto cambiará depende de las opciones que se den
    if selected > limit: selected = 1
    elif selected < 1: selected = 4

def r_menu():
    global selected
    global submenu
    global control

    selected = 1
    
    if not control: 
        submenu = 0

    menu_selector()


def toDo():
    global selected
    global submenu
    global control

    if control: 
        r_menu()
        control = False
        return
    clear()

    keyboard.unhook_all_hotkeys()
    input()

    if submenu == 0:
        if selected == 1: 
            submenu = 1
            show_sm1()
        elif selected == 2: 
            submenu = 2

        elif selected == 3: 
            submenu = 3

        elif selected == 4: 
            submenu = 4

    elif submenu == 1:
        control = True
        if selected == 1: 
            ac.ver(True, False)
        elif selected == 2: 
            ac.ver(True, True)
        elif selected == 3: 
            ac.ver(False, False)
        elif selected == 4: 
            ac.ver(False, False)
        os.system("pause")
        
    
    basic()
    #show_menu()
    #Si está seleccionado algo mostrar abajo la definición

def basic():
    keyboard.add_hotkey('up', up)
    keyboard.add_hotkey('down', down)
    keyboard.add_hotkey('enter', toDo)
    keyboard.add_hotkey('esc', r_menu)

show_menu()
basic()
keyboard.wait()

#Siguiente paso hacer menus anidados
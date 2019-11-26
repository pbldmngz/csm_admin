import keyboard
import os
import advanced_crud as ac
import colorama as c
c.init(autoreset=True)

clear = lambda: os.system('cls')
selected = 5
limit = 4

submenu = 0
# 0 == Menu principal
# 1 == Menú de vista

control = False

def show_menu():
    global selected
    global limit
    limit = 5
    setter()
    clear()
    opt = ["", "VER REGISTROS", "INSERTAR REGISTRO ", "ELIMINAR REGISTRO", "MODIFICAR REGISTRO", c.Fore.CYAN + "AYUDA" + c.Fore.RESET]
    defin = ["", "Ver datos de alumnos o profesores", "Dar de alta nuevos estudiantes y profesores",
    "Eliminar registros disponibles directamente en la base de datos", "Cambiar datos a alumnos y profesores",
    "MANUAL DE USO:\n - Flechas de teclado UP y DOWN para desplazarse por los menús\n - ENTER para aceptar\n - ESC para regresar\n - Usar el teclado cuando se le solicite escribir"]
    print("Elige una opción:")
    for i in range(1, len(opt)):
        print("{1} {0}. {3:25} {2}".format(i, ">" if selected == i else " ", "<" if selected == i else " ", opt[i]))
    
    print("\n\n" + defin[selected])

def show_sm1():
    global selected
    global limit
    limit = 4
    setter()
    clear()
    opt = ["", "LISTADO ALUMNOS", "LISTADO PROFESORES", "UN ALUMNO", "UN PROFESOR"]
    print("Elige una opción:")
    for i in range(1, len(opt)):
        print("{1} {0}. {3:25} {2}".format(i, ">" if selected == i else " ", "<" if selected == i else " ", opt[i]))

def show_sm2():
    global selected
    global limit
    limit = 3
    setter()
    clear()
    opt = ["", "INSERTAR ALUMNO", "INSERTAR PROFESOR", c.Fore.RED + "INSERTAR TEST-DATA" + c.Fore.RESET]
    print("Elige una opción:")
    for i in range(1, len(opt)):
        print("{1} {0}. {3:25} {2}".format(i, ">" if selected == i else " ", "<" if selected == i else " ", opt[i]))

def show_sm3():
    global selected
    global limit
    limit = 3
    setter()
    clear()
    opt = ["", "ELIMINAR ALUMNO", "ELIMINAR PROFESOR", c.Fore.RED + "ELIMINAR TODO (TEST)" + c.Fore.RESET]
    print("Elige una opción:")
    for i in range(1, len(opt)):
        print("{1} {0}. {3:25} {2}".format(i, ">" if selected == i else " ", "<" if selected == i else " ", opt[i]))

def show_sm4():
    global selected
    global limit
    limit = 2
    setter()
    clear()
    opt = ["", "MODIFICAR ALUMNO", "MODIFICAR PROFESOR"]
    print("Elige una opción:")
    for i in range(1, len(opt)):
        print("{1} {0}. {3:25} {2}".format(i, ">" if selected == i else " ", "<" if selected == i else " ", opt[i]))

def menu_selector():
    if submenu == 0:
        show_menu()
    elif submenu == 1:
        show_sm1()
    elif submenu == 2:
        show_sm2()
    elif submenu == 3:
        show_sm3()
    elif submenu == 4:
        show_sm4()

def up():
    global selected
    global submenu
    selected -= 1
    if submenu == 0: show_menu()
    elif submenu == 1: show_sm1()
    elif submenu == 2: show_sm2()
    elif submenu == 3: show_sm3()
    elif submenu == 4: show_sm4()

def down():
    global selected
    global submenu
    selected += 1
    if submenu == 0: show_menu()
    elif submenu == 1: show_sm1()
    elif submenu == 2: show_sm2()
    elif submenu == 3: show_sm3()
    elif submenu == 4: show_sm4()

def setter():
    global selected
    global limit
    if selected > limit: selected = 1
    elif selected < 1: selected = limit

def r_menu():
    global selected
    global submenu
    global control

    selected = 1
    
    clear()

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
            selected = 1
            submenu = 1
            show_sm1()
        elif selected == 2: 
            selected = 1
            submenu = 2
            show_sm2()

        elif selected == 3: 
            selected = 1
            submenu = 3
            show_sm3()

        elif selected == 4: 
            selected = 1
            submenu = 4
            show_sm4()
        elif selected == 5:
            selected = 1
            submenu = 0
            show_menu()

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

    elif submenu == 2:
        control = True
        if selected == 1: 
            ac.insertar(True)
        elif selected == 2: 
            ac.insertar(False)
        elif selected == 3: 
            while True:
                p = input(c.Fore.CYAN + "¿Cuántos profesores? \n")
                print("")
                a = input(c.Fore.CYAN + "¿Cuántos alumnos? \n")
                try:
                    p = int(p)
                    a = int(a)
                    break
                except: print(c.Fore.YELLOW + "Formato incorrecto, intente otra vez")
            ac.gen_a_lot(p, a)
            #try:
               # ac.gen_a_lot(p, a)
            #except: print(c.Fore.RED + "Un error ha suscedido, cancelando...")
        os.system("pause")
    
    elif submenu == 3:
        control = True
        if selected == 1: 
            ac.borrar(True)
        elif selected == 2: 
            ac.borrar(False)
        elif selected == 3: 
            ac.reset_database()
        os.system("pause")

    elif submenu == 4:
        control = True
        if selected == 1: 
            ac.modificar(True)
        elif selected == 2: 
            ac.modificar(False)
        os.system("pause")
        
    
    basic()

def basic():
    keyboard.add_hotkey('up', up)
    keyboard.add_hotkey('down', down)
    keyboard.add_hotkey('enter', toDo)
    keyboard.add_hotkey('esc', r_menu)

show_menu()
basic()
keyboard.wait()
import random

nombre = [ "Andrea", "David", "Baldomero", "Balduino", "Baldwin", "Baltasar", "Barry", "Bartolo", "Bartolomé", "Baruc", 
"Baruj", "Candelaria", "Cándida", "Canela", "Caridad", "Carina", "Carisa", "Caritina", "Carlota", "Baltazar", "Arturo", 
"Juan", "José", "Luis", "José", "María", "Guadalupe", "Francisco", "Guadalupe", "María", "Juana", "Antonio", "Jesús", 
"Miguel", "Ángel", "Pedro", "Alejandro", "Manuel", "Margarita", "María", "Carmen", "Juan", "Carlos", "Roberto", 
"Fernando", "Daniel", "Carlos", "Jorge", "Ricardo", "Miguel", "Eduardo", "Javier", "Rafael", "Martín", "Raúl", "David", 
"Josefina", "José", "Antonio", "Arturo", "Marco", "Antonio", "José", "Manuel", "Francisco", "Javier", "Enrique", "Verónica", 
"Gerardo", "María", "Elena", "Leticia", "Rosa", "Mario", "Francisca", "Alfredo", "Teresa", "Alicia", "María", "Fernanda", 
"Sergio", "Alberto", "Luis", "Armando", "Alejandra", "Martha", "Santiago", "Yolanda", "Patricia", "María", 
"Ángeles", "Juan", "Manuel", "Rosa", "María", "Elizabeth", "Gloria", "Ángel", "Gabriela", "Salvador", "Víctor", "Manuel", 
"Silvia", "María", "Guadalupe", "María", "Jesús", "Gabriel", "Andrés", "Óscar", "Guillermo", "Ana", "María", 
"Ramón", "María", "Isabel", "Pablo", "Ruben", "Antonia", "María", "Luisa", "Luis", "Ángel", "María", "Rosario", 
"Felipe", "Jorge", "Jesús", "Jaime", "José", "Guadalupe", "Julio", "Cesar", "José", "Jesús", "Diego", "Araceli", 
"Andrea", "Isabel", "María", "Teresa", "Irma", "Carmen", "Lucía", "Adriana", "Agustín", "María", "Luz", "Gustavo"]

apellido = [ "Gomez", "Guerrero", "Cardenas", "Cardiel", "Cardona", "Cardoso", "Cariaga", "Carillo", "Carion", "Castiyo", 
"Castorena", "Castro", "Grande", "Grangenal", "Grano", "Grasia", "Griego", "Grigalva", "Fernandez", "Quevedo", "Pendragon", 
"Garcia", "Gonzalez", "Rodriguez", "Fernandez", "Lopez", "Martinez", "Sanchez", "Perez", "Gomez", "Martin", "Jimenez", 
"Ruiz", "Hernandez", "Diaz", "Moreno", "Alvarez", "Muñoz", "Romero", "Alonso", "Gutierrez", "Navarro", "Torres", 
"Dominguez", "Vazquez", "Ramos", "Gil", "Ramirez", "Serrano", "Blanco", "Suarez", "Molina", "Morales", "Ortega", "Delgado", 
"Castro", "Ortiz", "Rubio", "Marin", "Sanz", "Nuñez", "Iglesias", "Medina", "Garrido", "Santos", "Castillo", "Cortes", 
"Lozano", "Guerrero", "Cano", "Prieto", "Mendez", "Calvo", "Cruz", "Gallego", "Vidal", "Leon", "Herrera", "Marquez", "Peña", 
"Cabrera", "Flores", "Campos", "Vega", "Diez", "Fuentes", "Carrasco", "Caballero", "Nieto", "Reyes", "Aguilar", "Pascual", 
"Herrero", "Santana", "Lorenzo", "Hidalgo", "Montero", "Ibañez", "Gimenez", "Ferrer", "Duran", "Vicente", "Benitez", "Mora", 
"Santiago", "Arias", "Varga", "Carmona", "Crespo", "Roman", "Pastor", "Soto", "Saez", "Velasco", "Soler", "Moya", "Esteban", 
"Parra", "Bravo", "Gallardo", "Rojas" ]

def generador_persona (id, estudiante):
    def generador_telefono ():
        return "".join(map(str,[random.randint(0,9) for x in range(10)]))

    datos = [id]
    datos.append(nombre[random.randint(0, len(nombre) - 1)])
    datos.append(apellido[random.randint(0, len(apellido) - 1)])
    datos.append(apellido[random.randint(0, len(apellido) - 1)])
    datos.append(generador_telefono())

    if estudiante: 
        datos.append("cetys.edu.mx")
        datos.append(random.randint(0,7)) #Grupo
    else: datos.append("cetys.mx")

    datos[5] = ("{}.{}.{}@{}"
    .format(datos[1], datos[2], datos[0], datos[5])) #Correo

    return datos
    
print(generador_persona(1, True))

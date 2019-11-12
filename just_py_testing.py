import re
ar = ""
print("Comienzo")
while not re.match(r"\w\D{2,}", ar):
    print(ar)
    ar = input("Nuevo valor: ")
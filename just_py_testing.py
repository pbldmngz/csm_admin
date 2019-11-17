import re

h = "dd."

while (re.match(r"^\d*$", h) == None and re.match(r"^[A-Za-z]*$", h) == None) or h == "": 
    print(re.match(r"^\d*$", h) == None)
    print(re.match(r"^[A-Za-z]*$", h) == None)
    print(h)
    h = input("Inserte un ID válido: ")

print(h)
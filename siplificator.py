def main():
    string = []

    for i in range(int(input("Number of items: "))):
        x = input("object: \n")
        for n in range(len(x.split(" "))):
            string.append(x.split(" ")[n])

    res = []
    for i in range(len(string)):
        try: int(string[i])
        except: res.append('"' + string[i].title() + '"')
    return ', '.join(res)

print(main())

##Transforms a list of things into an usable list to copy-paste in java
### Very useful if you copy a list with line spacing and numbers
#Formatear los resultados
#{3}{0:8d}{3}
#{index 3}{index 0:8 de espaciado}{index 3}
#La letra ‘d’ se utiliza para indicar que son datos enteros, en el caso de datos de texto (string) se utiliza ‘s’
for x in range(1,11):
    print ('{3}{0:8d}{3} {3}{1:3d}{3} {3}{2:4d}{3}'.format(x, x * x, x * x * x, '|'))

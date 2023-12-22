edad = int(input())
if edad>=2:
    print('es verdadero')
    edad+=1
    print('tu edad en un anio sera de: {:0.0f}'.format(edad))
else:
    print('es falsos')
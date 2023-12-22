cadena1 = 'HOLA soy Huascar'
cadena2 = 'sos una maquina'

#la funcion dir te proporciona una lista e funciones que puedes hacer para una variable
for metodo in dir(cadena1):
    print(metodo)

#la diferencia entre funcion y metodos es el caso de funcion(variable) y variable.metodo()

#.upper() convierte a los caracteres en mayuscula
mayuscula = cadena1.upper()
print(mayuscula)

#.lower() convierte a los caracteres en minuscula 
minuscula = cadena1.lower()
print(minuscula)

#.capitalize() convierte todo em minuscula y luego convierte solamente la primer letra del string en mayuscula
primer_letra_mayuscula = cadena1.capitalize()
print(primer_letra_mayuscula)
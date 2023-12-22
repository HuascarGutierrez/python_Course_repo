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

#.fin(string) ayuda a encontrar la posicion inicial de un string que este dentro de otro
encontrar = cadena1.find("soy")
print(encontrar)
# en el caso de que el string que no este dentro del otro string, entonces da la posicion -1
no_encontrado = cadena1.find("waza")
print(no_encontrado)
#.index tiene da el mismo retorno que el .find(), excepto que en el caso que no lo encuentra. El cual da error en el .index
encontrar = cadena1.index('soy')
print(encontrar)

#.isnumeric() nos dice si el string es numerico 
numerico = "9951591".isnumeric()
print(numerico)

#.isalpha() nos dice si el string es alpha-numerico
alpha_numerico = "Ovnicat".isalpha()
print(alpha_numerico)
#hay que tomar en cuenta el tema del espacio

#.count(variable) devuelve la cantidad de coincidencias de una variable string dentro de la cadena
contando = "ovni9951591".count('9')
print(contando)

#.len() nos ayuda a saber la cantidad de caracteres que tenemos dentro de un string. Esto es una funcion
cantidad = len(cadena1)
print(cantidad)

#.startswith(variable) permite dar un valor booleano dependiendo si la cadena empieza con una variable tipo string
# mientras que .endswith(variable) hace lo mismo pero con el final en vez del inicio
saludo = 'Hola mundo!'
print(saludo.startswith("Hola"))
print(saludo.endswith("!"))

# .replace(variable_antigua,variable_nueva) es un metodo que reemplaze las subcadenas antiguas por nuevas
saludo = saludo.replace("Hola","Adios")
print(saludo)

# .split(variable) permite separar en una lista segun un parametro
string_largo = "hola que tal, soy un estudiante de python"
string_largo = string_largo.split(" ")
print(string_largo)
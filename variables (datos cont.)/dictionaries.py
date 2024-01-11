diccionario = dict(nombre='Huascar',apellido = 'Gutierrez')
#los diccionarios tambien se pueden crear de forma vacia si usamos la funcion dict() sin ningun valor
diccionario_2 = dict()
print(diccionario)
print(str(diccionario_2)+f'\nTipo: {type(diccionario_2)}')
#los diccionarios no pueden ser mutables

#algo interesante es que las keys que puedes utilizar puede ser tuplas y fronzensets.
diccionario = {('hola','mundo'):'saludo'}
print(str(diccionario)+f'\nTipo: {type(diccionario)}')

#la funcion fromkeys puede crear un diccionario dando como paarmetros una lista de keys que podamos usar, cuyos valores seran None
diccionario = dict().fromkeys(['nombre','apellido','cedula de identidad'])
print(diccionario) 
#en el caso de que queramos ponerle un valor fijo a las keys, entonces ponemos otro parametro con el valor 
#ejemplo. pondremos vacio como valor en vez de None
diccionario = dict().fromkeys(['cantidad','marca','nombre del articulo'],'espacio vacio')
print(diccionario)

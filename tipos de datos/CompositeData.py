#los datos compuestos son datos con mas datos

lista =["Lucas Dalto", "Huascar Gutierrez",True,4,"hola"]
print(lista)

#la diferencia estre las lista y la tupla es que la tupla no es modificable 
tupla = ("Lucas Dalto", "Huascar Gutierrez",True,4,"hola")
print (tupla)

#sets o conjuntos - la diferencia es que estos pueden no tener un orden aunque son casi commo las listas, aunque no se pueden modificar 
#a menos que se modifique todo
conjunto = {"Lucas Dalto", "Huascar Gutierrez",True,4,"hola"}
#conjunto[0] = 1
print(conjunto)
conjunto = {"esto puede servir para el ACID"}
print(conjunto)
#tampoco puede repetir valores - automaticamente se borra
conjunto = {1,1}
print(conjunto)
#no se puede llamar sus datos por su indice 
#print(conjunto[0])

#diccionanario - en vez de usar el indice, se puede usar el el nombre de la key ej. nombre 
diccionario = {
    'nombre': 'Lucas Dalto',
    'canal': 'Soy Dalto',
    'dato': 'Hola mundo'
}
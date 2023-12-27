# con te list() puedes crear una lista, esta lista puede tener datos como puede no tener nada.
lista1 = list()
lista_completa = list(['hola',' mundo',12,'como estas',3.21])
print(lista1,lista_completa)
for objeto in lista_completa:
    print(objeto)

# para el caso de len(lista), este devuelve la cantidad de elementos que tiene la lista
lista_tamano = list(['hola','que','tal','como','estas'])
tamano = len(lista_tamano)
print(tamano)

# .append(elemento nuevo) es un metodo que nos sirve para anadir un elemento al final de la lista
lista_agregar = ['hola', 'que', 'tal']
lista_agregar.append('como')
lista_agregar.append('estas')
print(lista_agregar)

# .insert(indice, elemento_nuevo) sirve para agregar un nuevo elemento a la lista en un indice en especifico
lista_insertar = ['hola','que','como','estas']
lista_insertar.insert(2,'tal')
print(lista_insertar)

# .extend([otra_lista]) sirve para agregar varios datos a una lista. Tambie se podria tomar como unir dos listas
lista_extend = list(['hola','como','te','sientes'])
lista_extend.extend(['tienes','tiempo','?'])
print(lista_extend)

# el metodo .pop() sirve para borrar el ultimo elemento de una lista
print(lista_completa)
lista_completa.pop()
print(lista_completa)
# tambien lo puedes usar para borrar un elemento segun el indice que le pongas, empezando por el 0 o tambien de reversa -1
lista_completa.pop(1)
print(lista_completa)

#el metodo remove(elemento_a_borrar) es un metodo que borra el primer elemento identico dentro de una lista, si el dato no 
#se encuentra en la lista, entonces lanza una exception
lista_ejemplo = ['hola','hola','adios','hola','adios','hola','adios']
lista_ejemplo.remove('adios')
print(lista_ejemplo)

#el metodo clear() elimina todos los elementos de una lista
lista_ejemplo.clear()
print(lista_ejemplo)

# el metodo .sort() es un metodo que ayuda al ordemnamiento de forma ascendente
lista = ['adsdf','absd','c','z','f','d']
lista2 = [56,8,2,-5,1]
lista.sort()
lista2.sort()
print(lista)
print(lista2)
#para este metodo podemos hacer un cambio con el reverse de la siguiente forma para cambiar el sentido
lista2.sort(reverse=True)
print(lista2)

# .reverse() es un metodo que sirve para invertir el sentido de la lista
lista = [1,2,3,4,5]
lista.reverse()
print(lista)

#al igual que para un string, tambien se puede usar un .index(elemento a encontrar) [5,4,3,2,1] por el reverse
indice = lista.index(4)
print(indice)
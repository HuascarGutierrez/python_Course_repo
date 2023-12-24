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
tupla = tuple(['dato1','dato2','dato3'])
print(tupla)
# tambien se puede crear tuplas sin la necesidad de poner parentesis ej

otra_tupla = "hola",'que','tal'
#se podria tomar como lo contrario del empaquetado
print(otra_tupla)

# si queremos crear una tupla de la segundo forma pero solo tenemos un datos, igual se puede hacer de la siguiente forma
otra_tupla = 'hola',
print(otra_tupla)

'''en CompositeData.py se menciono el porque es conveniente usar las tuplas, aqui el porque.
Se debe a que las variables mutables requieren dos espacios de memoria, uno para almacenar el dato y otro para almacenar el cambio.
Esto con el proposito de no perder la variable en caso de un error. 
Mientras que la tupla, como no es mutable, no hace esto. Sino que solo tiene un espacio de memoria'''
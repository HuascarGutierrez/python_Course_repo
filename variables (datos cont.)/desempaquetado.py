#creamos un tupla
datos = ("Huascar",'Gutierrez',9951591,'BO')
#hacemos el desempaquetado de la tupla 
nombre,apellido,ci,nacionalidad = datos 
#   tambien funciona de la siguiente manera
#nombre,apellido,ci,nacionalidad = ("Huascar",'Gutierrez',9951591,'BO') 
print(nombre)

#nota. es tanto par, como listas, como conjuntos ej
otros_datos = {'hola','que','tal'}
primero,segundo,tercero = otros_datos
print(segundo)
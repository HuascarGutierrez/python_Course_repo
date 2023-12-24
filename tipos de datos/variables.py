#este es un metodo de concatenacion con el format 
nombre = 5
bienvenida = f"hola {nombre:0.4f} como te encuentras"
print(bienvenida)
bienvenida2 = "hola {0:30f} como te encuentras".format(nombre)
bienvenida2 = "hola {0:20.4f} como te encuentras".format(nombre)
#aqui se utiliza la cantidad de espacios y luego la cantidad de decimales
print(bienvenida2)

#operador para borrar datos
hola  = 1
print(hola)
del hola 
# print (hola) al usar esta linea de comando saldra el error porque se borro la variable hola

#operadores de pertenencia (in / not in)
print ("hola" in "hola como estas") #true porque hola esta en el string
print("que tal" not in "hola como estas") #false porque que tal no esta en el string

#snake case - recomendacion de los desarroladores de python
nombre_completo_del_usuario = "Huascar Gutierrez Castro"


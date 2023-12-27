# pedirle un dato al usuario
nombre = input('Ingrese su nombre: ')
print(f'el nombre es: {nombre:23s}, que tal')
#el dato que da un input siempre sera un texto (str)

# para pasarle un numero entero se tiene que agregar la funcion int()
numero = int(input("Ingrese el numero: "))
print(f'el numero es: {numero:10.4f}')
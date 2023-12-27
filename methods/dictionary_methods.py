diccionario = {
    'nombre' : 'Huascar',
    'apellido' : 'Gutierrez',
    'id' : 9951591,
    'nacionalidad' : 'BO'
}

#el metodo .keys() nos permite ver las keys que tenemos en un diccionario
claves = diccionario.keys()
print(claves)

#el metodo .get(key) nos permite er el valor de la key. Ej el valor de nombre es Huascar
valor = diccionario.get('id')
print(valor)
# se puede hacer lo mismo con el diccionario['id'], la diferencia es que en el caso de no encontrar la key ingresada esta 
# da error mientras que .get() no
valor = diccionario.get('que paso wachos')
print(valor)

# el elemento .pop("key") eliminar la key juntamente con su dato
diccionario_prueba = diccionario.copy()
diccionario_prueba.pop('id')
print(diccionario_prueba)

# el elemento .clear(), al igual que en los otros casos, elimina todos los datos del diccionario
diccionario_prueba.clear()
print(diccionario_prueba)

# el metodo .items(), cambia las propuedades del diccionario a iterable, como si fuera un array
print(diccionario)
diccionario_prueba = diccionario.items()
print(diccionario_prueba)
print(diccionario_prueba)
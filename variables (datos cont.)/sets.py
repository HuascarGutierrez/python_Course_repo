# se puede crear un conjunto con la funcion set
conjunto_palabras = set(['hola','que','tal'])
print(conjunto_palabras)

# nota. Aqui no puedes tener datos mutables(que puedan canviares de forma simple), como ser una lista o array por ejemplo
# ej. set(['hola',['que','tal']])
# si quieres hacer eso, te conviene usar una tupla :3
conjunto_palabras = set(['hola',('que','tal'),123])
print(conjunto_palabras)

#nota. el conjunto es mutable por defecto pero existe una funcion para que no sea mutable y pueda ser hasheable
conjunto_congelado = frozenset(['dato1','dato2','dato3'])
conjunto_dentro_de_otro_conjunto = {conjunto_congelado,'dato4','dato5'}
print(conjunto_dentro_de_otro_conjunto)

# Parte de teoria de conjuntos
conjunto_impares = {1,3,5,7}
subconjunto_impares = {1,5,7}
# forma se saber si es un subconjunto
resultado = subconjunto_impares.issubset(conjunto_impares)
#otra forma de saber si es un subconjunto es por medio de los operadores logicos
otro_resultado = subconjunto_impares <= conjunto_impares
print(resultado,otro_resultado)
# forma de saber si es un superconjunto
resultado = conjunto_impares.issuperset(subconjunto_impares)
#aqui tambien se pueden utilizar los operadores logicos
otro_resultado = conjunto_impares >= subconjunto_impares
print(resultado,otro_resultado)

# forma para saber si un conjunto es disjunto (un conjunto es disjunto a otro si no tiene ningun dato similar)
# o tambien se le puede decir de forma matematica como A ^ B es un conjunto vacio
conjunto_disjunto_A = {'hola','hello','ohayou','wenas'}
conjunto_disjunto_B = {'adios','goodbye','sayounara','chau'}
resultado = conjunto_disjunto_A.isdisjoint(conjunto_disjunto_B)
print(resultado) #aca dara True porque el conjunto A no tiene ningun elemento del conjunto B y viceversa
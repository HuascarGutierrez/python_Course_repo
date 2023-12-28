# se puede crear un conjunto con la funcion set
conjunto_palabras = set(['hola','que','tal'])
print(conjunto_palabras)

# nota. Aqui no puedes tener datos mutables(que puedan canviares de forma simple), como ser una lista o array por ejemplo
# ej. set(['hola',['que','tal']])
# si quieres hacer eso, te conviene usar una tupla :3
conjunto_palabras = set(['hola',('que','tal'),123])
print(conjunto_palabras)
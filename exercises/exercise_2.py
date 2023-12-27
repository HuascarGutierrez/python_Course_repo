convertion_time = 1/2
convertion_words = 2/1
answer = 'Para flaco tampoco te pedi un testamento'
duration = 3*60 #180 seconds
dalto = 0.3

#answer A convertions
time = int(input('Ingrese la cantidad de palabras a decir: '))*convertion_time
words = int(input('Ingrese el tiempo que tardo para decir la frase: '))*convertion_words
print(f'El tiempo es: {time:4.2f}\nLa cantidad de palabras son: {words:4.2f}\n')

#answer B conditions
if int(input('Ingrese el tiempo: ')) > 60:
    print(answer)

#answer C convertion for Dalto
answer_dalto = int(input('Ingrese el tiempo de una persona normal: '))
answer_dalto *=(1-dalto)
print(f'Dalto lo hablaria en {answer_dalto:4.2f} segundos.')
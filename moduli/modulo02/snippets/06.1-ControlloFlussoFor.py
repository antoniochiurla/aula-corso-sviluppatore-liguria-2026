# Da eseguire nella console Python

# generiamo un range da 1 a 10
from_1_to_10 = range(1, 11)

# un range si comporta come se fosse una lista di valori, vedremo in seguito cosa sono le liste

for i in from_1_to_10:
    print(i)

number_to_exclude = 5
number_to_stop = 8
# scorriamo il range
for i in from_1_to_10:
    # se dobbiamo escluder passiamo al prossimo elemento
    if i == number_to_exclude:
        continue
    # se dobbiamo arrestare il ciclo lo interrompiamo con break
    if i == number_to_stop:
        break
    print(i)


number_to_find = 18
for i in from_1_to_10:
    if i == number_to_find:
        break
# il ciclo non è stato interrotto vuol dire che non abbiamo trovato quello che cercavamo
else:
    print("Non abbiamo trovato il numero che cercavamo")

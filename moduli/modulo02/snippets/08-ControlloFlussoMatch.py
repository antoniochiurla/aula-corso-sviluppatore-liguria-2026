# Da eseguire nella console Python

# importiamo la libreria random
import random

# generiamo un valore casuale tra 0 e 10
value = random.randint(0, 10)

# verifichiamo se value vale 0 o 3
match value:
    case 0:
        print('Il valore è 0')
    case 3:
        print('Il valore è 3')
    case _:
        print('Il valore è diverso da 0 e 3')

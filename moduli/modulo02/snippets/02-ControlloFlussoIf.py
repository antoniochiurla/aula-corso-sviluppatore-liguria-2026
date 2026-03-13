# Da eseguire nella console Python

# importiamo la libreria random
import random

# facciamo generare un valore casuale tra 0 e 10
value = random.randint(0, 10)

# verifichiamo se value vale 5
if value == 5:
    print('Il valore è uguale a 5')

# verifichiamo se value vale 5 o è diverso
if value == 5:
    print('Il valore è uguale a 5')
else:
    print('Il valore è diverso da 5')

# classifichiamo value
if value < 5:
    print('Il valore è minore di 5')
elif value == 5:
    print('Il valore è uguale a 5')
else:
    print('Il valore è maggiore di 5')

# verifichiamo se appartiene a un intervallo
if 5 <= value <= 8:
    print('Il valore è compreso tra 5 e 8')
else:
    print('Il valore non è compreso tra 5 e 8')


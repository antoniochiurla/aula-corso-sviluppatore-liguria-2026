# Da eseguire nella console Python

# creiamo una lista
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

# primo elemento NB: zero-based
fruits[0]

# secondo elemento
fruits[1]

# ultimo elemento
fruits[-1]

# dal secondo elemento fino al quinto elemento
fruits[1:5]

# dal secondo al quinto elemento ogni due elementi
fruits[1:5:2]

# dal secondo elemento fino all'ultimo
fruits[1:]

# dal primo elemento fino al quinto elemento
fruits[:5]

# tutti gli elementi ogni due elementi
fruits[::2]

# contiamo quante mele ci sono
fruits.count('apple')

# contiamo quante tangerine ci sono
fruits.count('tangerine')

# troviamo la posizione della banana
fruits.index('banana')

# troviamo la posizione della banana dopo la quarta
fruits.index('banana', 4)

# verifichiamo se la lista contiene la mela
'apple' in fruits

# oppure
if 'apple' in fruits:
    print('La lista contiene la mela')

# invertiamo la lista
fruits.reverse()
# visualizziamo la lista
fruits

# aggiungiamo un nuovo frutto
fruits.append('grape')
fruits

# ordiniamo la lista
fruits.sort()
fruits

# recuperiamo e rimuoviamo l'ultimo elemento
fruits.pop()
fruits


# creiamo una lista di caratteri da una stringa
letters = list('abracadabra')

# visualizziamo la lista
letters

# creiamo una lista da usare come stack
stack = [3, 4, 5]
# aggiungiamo elementi allo stack
stack.append(6)
stack.append(7)
# visualizziamo lo stack
stack

# rimuoviamo gli ultimi due elementi
stack.pop()
stack
stack.pop()
stack.pop()
stack


# creiamo una lista vuota per ospitare i quadrati
squares = []
# cicliamo da 0 a 9
for x in range(10):
    # aggiungiamo il quadrato alla lista
    squares.append(x**2)

squares

# sintetizziamo un modo alternativo
squares = list(map(lambda x: x**2, range(10)))

# ancora più sintetico
squares = [x**2 for x in range(10)]


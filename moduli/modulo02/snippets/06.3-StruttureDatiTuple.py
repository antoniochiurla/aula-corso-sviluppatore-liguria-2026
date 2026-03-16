# Da eseguire nella console Python

# creiamo una tupla
fruits = ('orange', 'apple', 'pear', 'banana', 'kiwi')

# visualizziamo la tupla
fruits

# primo elemento NB: zero-based
fruits[0]

# conteggi come per le liste
fruits.count('apple')

# troviamo la posizione della banana come le liste
fruits.index('banana')

# le tuple sono immutabili, non possiamo aggiungere o rimuovere elementi
# tentando di modificare il primo elemento si ottiene: TypeError: 'tuple' object does not support item assignment
fruits[0] = 'mango'

# suddividiamo la tupla in variabili separate
first, second, third, forth, fifth = fruits

# provando a suddividere in meno variabili di quante ci sono elementi nella tupla si ottiene: ValueError: too many values to unpack (expected 3)
first, second, third = fruits

# suddividiamo le prime tre posizioni in altrettante variabili
first, second, third = fruits[:3]

# creiamo una tupla di caratteri dalla stringa
a = set('abracadabra')
# un'altra
b = set('alacazam')

a + b

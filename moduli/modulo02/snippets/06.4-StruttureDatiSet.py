# Da eseguire nella console Python

# creiamo un set con valori duplicati
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

# altro modo di creare un set
basket = set(('apple', 'orange', 'apple', 'pear', 'orange', 'banana'))

# visualizziamo il set, notiamo che i duplicati sono stati rimossi
basket

# verifichiamo che un elemento appartenga al set
'orange' in basket

# verifichiamo che un elemento non appartenga al set
'crabgrass' in basket


# creiamo un set di caratteri dalla stringa
a = set('abracadabra')
# un altro
b = set('alacazam')

# notiamo che troviamo ogni lettera una sola volta
a

# operazioni con set

# sottraiamo i due set
a - b

# unione dei due set
a | b

# intersezione dei due set
a & b

# unione esclusiva dei due set
a ^ b

# non possiamo sommare i set come le tuple: TypeError: unsupported operand type(s) for +: 'set' and 'set'
a + b

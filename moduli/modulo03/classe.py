class Prova:
    def metodo(self, primo, secondo=None):
        if secondo != None:
            print(f'argomenti: {primo} e {secondo}')
        else:
            print(f'argomenti: {primo}')


def prova_pop():
    lista = [5,6,7,8,5,6,7]
    estratto = lista.pop(2)
    print(f'estratto: {estratto}')
    lista.remove(6)
    print('lista:', lista)
    del(lista[3])
    print('lista dopo del[3]:', lista)
    del(lista)
    print('lista dopo del:', lista)

if __name__ == '__main__':
    prova = Prova()
    prova.metodo('uno', 'due')
    prova.metodo('uno', 0)
    prova.metodo('uno')

    prova_pop()

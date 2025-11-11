def crealista (numero):
    lista = []
    for i in range(numero):
        print("palabra #",i+1,end="")
        palabra = input()
        lista.append(palabra)
    return lista

def contarpalabras (lista, palabra):
    contador = 0
    for i in lista:
        if i == palabra:
            contador += 1
    return contador


def escriealreves(lista):
    lista2 = []
    for i in range(len(lista)-1,-1,-1):
        lista2.append(lista[i])
    return lista2

def sustituirpala(lista,palabra,sustituye):
    if palabra in lista:
        for i in range(0,len(lista),1):
            if palabra == lista[i]:
                lista[i] = sustituye
        print(lista)
    else:
        print("No esta la palabra")

def eliminaPalabra (lista,palabra,numero):
    for i in range(numero-1,-1 , -1):
        if palabra == lista[i]:
            lista.pop(i)
    return lista

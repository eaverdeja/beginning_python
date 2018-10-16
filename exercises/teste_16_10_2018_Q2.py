"""
1)                  Considere a seguinte lista:

L=[10,-10,3,89,34,-66,23,9,89,12,23,34,-11,20,31,89,20]

a)      Construa uma função detMaior que receba esta lista e retorna o maior valor

b)      Construa uma função somaOutros  que receba esta lista e exibe a soma dos valores diferentes do maior. Esta função deve chamar a função do item a)
"""

L=[10,-10,3,89,34,-66,23,9,89,12,23,34,-11,20,31,89,20]
def detMaior(lista):
    maior = -1
    for (pos, elem) in enumerate(lista):
        if elem > maior:
            maior = elem
    return maior

def somaOutros(lista):
    maior = detMaior(lista)
    soma = 0
    for (pos, elem) in enumerate(lista):
        if elem != maior:
            soma += elem
    print(soma)

somaOutros(L)

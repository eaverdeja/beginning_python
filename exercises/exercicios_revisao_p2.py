print('Letra A')
#A) Faça uma função recursiva que receba uma lista de strings ou de lista de
#strings e retorne cada uma de suas strings traduzida para a língua do X. 
#Uma sttring traduzida para a língua do X tem antes de cada vogal a letra X.
#Exemplo:
#	querida  --> qxuxerxidxa
#	maxi  --> mxaxxi
#	prova --> prxovxa

def eVogal(char):
    if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
        return True
    return False

def traduzParaX(str):
    if(len(str) == 1):
        if(eVogal(str)):
            return 'x' + str
        else:
            return str
    else:
        if(eVogal(str[0])):
            return 'x' + str[0] + traduzParaX(str[1:])
        else:
            return str[0] + traduzParaX(str[1:])

def traduzListaParaX(lista):
    for (pos, str) in enumerate(lista):
        lista[pos] = traduzParaX(str)
    return lista

lista = ['querida', 'maxi', 'prova']
listaEmX = traduzListaParaX(lista)
for str in listaEmX:
    print(str)

print('\nLetraB')
#B) Um curso de dança de salão deseja saber se haverá ou não uma nova turma.
#Para abrir uma turma as seguintes regras devem ser obedecidas:
#No mínimo 6 casais (1 homem e 1 mulher)
#Nenhum participante pode ter menos de 14 anos
#Faça uma função que receba a lista de inscritos onde cada elemento
#é uma sublista com nome do inscrito, sexo e idade.
#Esta função deve exibir se é possível formar uma nova turma,
#mostrando o nome dos casais, ou se não é possível.

LInscritos = [
    ['João', 'M', 14],
    ['Carlos', 'M', 44],
    ['Maria', 'F', 16],
    ['Jorge', 'M', 25],
    ['Paula', 'F', 9],
    ['Caio', 'M', 13],
    ['Bernardo', 'M', 23],
    ['Joaquim', 'M', 33],
    ['Marcos', 'M', 53],
    ['Juliana', 'F', 29],
    ['Carla', 'F', 24],
    ['Beatriz', 'F', 25],
    ['Manuella', 'F', 15],
    ['Helena', 'F', 45],
]

def mostraCasais(homens, mulheres):
    print('Possíveis casais para a turma:')
    for (pos, homem) in enumerate(homens):
        print(homem + ' & ' + mulheres[pos])

def turmaPossivel(LInscritos):
    homens = []
    mulheres = []
    for inscrito in LInscritos:
        nome = inscrito[0]
        sexo = inscrito[1]
        idade = inscrito[2]
        if(idade >= 14):
            if(sexo == 'M'):
                homens.append(nome)
            if(sexo == 'F'):
                mulheres.append(nome)
    if(len(homens) >= 6 and len(mulheres) >= 6):
        mostraCasais(homens, mulheres)
    else:
        print('Não é possível formar uma turma com estes inscritos!')

turmaPossivel(LInscritos)

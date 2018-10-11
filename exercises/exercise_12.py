lQuestoes=['3+5=....', '9*3=....','2+3*4=....','7-5+9=....','4*6/3+2=....']
lGabarito=[8,27,14,11,10]
lProvas=[  ["Ana", [5,27,14,1,1]],
                ["Pedro", [8,8,14,11,10]]
              ]

print('#Questões')
print(lQuestoes)
print('#Gabarito')
print(lGabarito)
print('#Provas')
print(lProvas)

print('\n---------')
print('Versão "clássica"')
print('---------\n')

print('#Exibir o texto das questões')
for pos in range(len(lQuestoes)):
    print(lQuestoes[pos])
    
print('\n#Exibir o número da questão e o gabarito da questão')
for pos in range(len(lGabarito)):
    print(str(pos + 1) + ': ' + str(lGabarito[pos]))
    
print('\n#Exibir cada questão seguida do gabarito')
for pos in range(len(lQuestoes)):
    print(lQuestoes[pos] + ': ' + str(lGabarito[pos]))

print("""\n# Corrigir as provas dos alunos. Cada questão certa vale 2 pontos.
# Para cada aluno deve ser exibido  seu nome e sua nota'""")
def calculaNotaAluno(respostas, gabarito):
    nota = 0
    for (pos, el) in enumerate(gabarito):
        if respostas[pos] == el:
            nota += 2
    return nota

def exibeNotas(provas, gabarito):
    for (pos, prova) in enumerate(provas):
        nomeAluno = prova[0]
        nota = calculaNotaAluno(prova[1], gabarito)
        print(nomeAluno + ': ' + str(nota))

exibeNotas(lProvas, lGabarito)
        
print('\n---------')
print('Versão com callbacks')
print('---------\n')

def loopThrough(array, callback):
    for pos in range(len(array)):
        callback(array[pos], pos)

#Exibir o texto das questões        
def exibeQuestao(questao, pos):
    print(questao)
    
#Exibir o número da questão e o gabarito da questão
def exibeGabarito(gabarito, pos):
    print(str(pos + 1) + ': ' + str(gabarito))

#Exibir cada questão seguida do gabarito
def exibeQuestaoGabarito(questao, pos):
    print(questao + ': ' + str(lGabarito[pos]))

loopThrough(lQuestoes, exibeQuestao)
loopThrough(lGabarito, exibeGabarito)
loopThrough(lQuestoes, exibeQuestaoGabarito)

def exibetexto(lQuestoes):
    for el in lQuestoes:
        print(el)

def exibeNumeGab(l):
    for (pos,el) in enumerate(l):
        print("%d) %d"%(pos+1,el))

def exibeProva(lQ,lG):
    for pos in range(len(lQ)):
        print("Enunciado: %s  \tGabarito: %d"%(lQ[pos],lG[pos]))

lQuestoes=['3+5=....', '9*3=....','2+3*4=....','7-5+9=....','4*6/3+2=....']
lGabarito=[8,27,14,11,10]

print('\n---------')
print('Gabarito da Professora')
print('---------\n')

#Exibir o texto das questões
exibetexto(lQuestoes)
#Exibir o número da questão e o gabarito da questão
exibeNumeGab(lGabarito )
#Exibir cada questão seguida do gabarito
exibeProva(lQuestoes,lGabarito)

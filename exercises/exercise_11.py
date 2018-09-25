def determinaSala(nome, turma):
    if turma == 'A' or turma == 'B':
        if nome[0] in 'aeiouAEIOU' and nome[-1] in 'aeiouAEIOU':
            sala = 144
        else:
            sala = 148
    else:
        if nome[0] <= 'F':
            sala = 184
        else:
            sala = 188
    return sala

#nome = input('Nome?')
#turma = input('Turma?')
#sala = determinaSala(nome, turma)
#print('Sua sala é ' + str(sala))

import time
def temDireitoAposentadoria(idade, sexo, dataFiliacao):
    if (sexo == 'M' and idade < 65) or (sexo == 'F' and idade < 60):
        return 'Não'
    else:
        data = time.strptime(dataFiliacao, "%d/%m/%Y")
        dataMinima = time.strptime('25/07/1991', "%d/%m/%Y")
        if(data < dataMinima):
            return 'Sim'
        else:
            contribuicoes = input('Contribuições mensais?')
            if(int(contribuicoes) >= 180):
                return 'Sim'
            return 'Não'

#print(temDireitoAposentadoria(26, 'M', '28/08/1992'))
#print(temDireitoAposentadoria(66, 'M', '28/08/1992'))
#print(temDireitoAposentadoria(66, 'M', '28/08/1990'))

def maiorDeIdade(idade):
    return idade >= 18

#40,00 para cada 2 anos que é cliente, com acréscimo de R$ 15,00 a cada 5 anos    
def valorPorTempo(tempoDeCasa):
    return (40 * tempoDeCasa / 2) + (15 * (15/5))

#Apenas maiores de idade podem receber vales por livros lidos
#	• menos de 3 livros lidos: não tem direito 
#	•3 livros lidos mas apenas de um tipo: 100,00 
#	•3 livros lidos dos dois tipos: 150,00 
#	•a partir de 4 livros lidos: 200,00 
def valorPorLivros(idade, livrosTecnicos, livrosNaoTecnicos):
    livros = livrosTecnicos + livrosNaoTecnicos
    if maiorDeIdade(idade) == False or livros < 3:
        return 0
    elif livros >= 3 and (livrosTecnicos == 0 or livrosNaoTecnicos == 0):
        return 100
    elif livros == 3:
        return 150
    else:
        return 200
    
def exibeValorVale(idade, sexo, tempoDeCasa, livrosTecnicos, livrosNaoTecnicos):
    porTempo = valorPorTempo(tempoDeCasa)
    porLivros = valorPorLivros(idade, livrosTecnicos, livrosNaoTecnicos)
    return porTempo if porTempo > porLivros else porLivros

vale = exibeValorVale(26, 'M', 5, 20, 7)
print(vale)

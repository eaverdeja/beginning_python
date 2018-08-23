def nl(): print()

#1. Importe o módulo random
#a) Veja a função choice : help(random.choice)
#b) Crie a string alfabeto = "abcdefghijklmnopqrstuvwxyz"
#c) Exiba a letra escolhida pelo choice
import random
help(random.choice)
def printRandomLetter(string):
    print('[printRandomLetter] A letra aleatória é: ' + random.choice(string))
    nl()
    
#2. Guarde seu nome em uma variável. Crie uma string com seu nome precedido e sucedido
#por n astericos, sendo n igual a metade do comprimento de seu nome. Exemplo: Nome =
#Mia Maia Saída: '****Mia Maia****'
def asteriscoWrapper(string):
    asteriscos = '*' * (len(string) // 2)
    newString = asteriscos + string + asteriscos
    print('[asteriscoWrapper] A nova string é: ' + newString)
    nl()
    return newString

#3. Guarde o dia, mês e ano de seu nascimento em variáveis:
#a) Exiba a data de nascimento no formato 'dd/mm/aaaa'
#b) Exiba a frase: 'Não se esqueça do meu aniversário: dd/mm!!!'
def aniversario(dia, mes, ano):
    diaString = str(dia).zfill(2)
    mesString = str(mes).zfill(2)
    print('[aniversario] ' + diaString + '/' + mesString + '/' + str(ano))
    print('[aniversario] Não se esqueça do meu aniversário: ' + diaString + '/' + mesString + '!!!')
    nl()

#Uma encomenda pesa 34250g e a embalagem peso 178g. Exiba o peso da encomenda
#com a embalagem no formato '... Kg e...g'
def pesoTotal(pesoEncomenda, pesoEmbalagem):
    total = pesoEncomenda + pesoEmbalagem
    kilos = int(total / 1000)
    gramas = total % 1000
    print('[pesoTotal] O peso total é de: ' + str(kilos) + 'kg ' + str(gramas) + 'g')
    nl()

#5. Utilize a função str() para mostrar quantos algarismos tem o número 3
#1000
def intDigitCount(int, power):
    count = len(str(int ** power))
    print('[intDigitCount] ' + str(count))
    nl()

#6. DESAFIO: verifique no módulo random se há alguma função capaz de gerar um número
#inteiro aleatoriamente. Se houver, refaça o exercício 5 substituindo o expoente de 3
#(1000) pelo número gerado aleatoriamente
def intDigitCountRandomPower(int):
    power = random.randint(1, 1000)
    count = len(str(int ** power))
    print('[intDigitCount] ' + str(count))
    nl()

#1
alfabeto = "abcdefghijklmnopqrstuvwxyz"
printRandomLetter(alfabeto)

#2
wrappedString = asteriscoWrapper('Eduardo Verdeja')

#3
aniversario(28, 8, 1992)

#4
pesoTotal(34250, 178)

#5
intDigitCount(3, 1000)

#6
intDigitCountRandomPower(3)

""" Enunciado

  Um cinema necessita de um novo programa para o controle das compras realizadas por meio de cartões de crédito. O programa, em seu bloco principal, deve permitir registrar um número indeterminado de compras com cartão, até que o usuário decida encerrar o registro das compras, digitando o caractere F (Fim). Enquanto o usuário resolver registrar compras, digitando o caractere R (Registrar), as seguintes informações devem ser lidas, para cada compra:

·         O número do cartão de crédito;

·         A quantidade de ingressos desejada.

Caso o usuário digite uma operação diferente de R e de F, a mensagem Operação Inválida deve ser exibida no monitor e a digitação de uma nova operação deve ser solicitada ao usuário.

Em seguida, para cada ingresso, deve ser lido o tipo de sala, podendo ser normal ou 3D, e o tipo do ingresso, podendo ser inteiro ou estudante. Um ingresso inteiro custa R$ 30,00 em sala normal e R$ 40,00 em sala 3D. Um ingresso de estudante custa a metade do ingresso inteiro, qualquer que seja o tipo de sala. Concluída a compra de ingressos relativa a um cartão, o programa deverá exibir no monitor a seguinte mensagem:

Compra de R$ XXX.XX realizada no cartão XXXXXXXXXXXXXXXX

Valor médio pago pelos ingressos nesta compra: R$ XXX.XX

Caso o tipo de sala digitado não seja igual a 3D, deve-se assumir que o tipo de sala é normal. Caso o tipo de ingresso digitado não seja igual a E (estudante),
deve-se assumir que o tipo é inteiro.

Ao término dos registros de compras de TODOS os cartões, o programa deverá exibir no monitor os seguintes dados:

           I.            O somatório dos valores das compras feitas por todos os cartões;

         II.            O número médio de ingressos por compra;

O seu programa deverá, OBRIGATORIAMENTE, fazer uso das seguintes funções, escritas por você:

a) calculaValorIngresso: recebe o tipo de sala e o tipo do ingresso. Com base nestas informações, a função deverá calcular e retornar o valor do ingresso.

b) processaIngressos: recebe a quantidade de ingressos e, em seguida, para cada ingresso, solicita o tipo de sala e de ingresso. Esta função deverá, NECESSARIAMENTE, utilizar a função calculaValorIngresso para calcular o valor individual de cada um dos ingressos. Por fim, esta função deverá retornar o valor total da compra.

c) exibeResultadoFinal: recebe os parâmetros necessários à exibição no monitor dos dados descritos nos itens I e II.

Exemplo de interação esperada para a execução do programa, tendo como dados de entrada 2 cartões, em que um gastou R$ 50,00 e o outro, R$ 95,00:

Digite R para registrar compras ou F para finalizar o programa: R

Informe o cartão de crédito: 1234

Informe a quantidade de ingressos: 2

Tipo de sala do ingresso 1: N

Tipo de ingresso 1: I

Tipo de sala do ingresso 2: 3D

Tipo de ingresso 2: E

Compra de R$ 50.00 realizada no cartão 1234

Valor médio pago pelos ingressos nesta compra: R$ 25.00

Digite R para registrar compras ou F para finalizar o programa: R

Informe o cartão de crédito: 5678

Informe a quantidade de ingressos: 3

Tipo de sala do ingresso 1: 3D

Tipo de ingresso 1: I

Tipo de sala do ingresso 2: X

Tipo de ingresso 2: E

Tipo de sala do ingresso 3: 3D

Tipo de ingresso 3: X

Compra de R$ 95.00 realizada no cartão 5678

Valor médio pago pelos ingressos nesta compra: R$ 31.67

Digite R para registrar compras ou F para finalizar o programa: f

Operação Inválida

Digite R para registrar compras ou F para finalizar o programa: F

--------------------------------------------------------------------------

O valor total das compras feitas com cartão é R$ 145.00

O número médio de ingressos por compra é 2.5
"""
def main():
    operacao = None
    while True:
        operacao = input('Digite R para registrar compras ou F para finalizar o programa: ')
        if operacao == 'R':
            cartaoCredito = input('Informe o cartão de crédito: ')
            quantidadeIngressos = int(input('Informe a quantidade de ingressos: '))
            valorTotal = processaIngressos(quantidadeIngressos)
            exibeResultadoFinal(cartaoCredito, valorTotal, valorTotal / quantidadeIngressos)
        elif operacao == 'F':
            exit()
        else:
            print('Operacao Inválida!')

def calculaValorIngresso(tipoSala, tipoIngresso):
    valor = 0
    if tipoSala == '3D':
        valor = 40
    else:
        valor = 30
    if tipoIngresso == 'E':
        valor = valor / 2
    return valor

def processaIngressos(quantidadeIngressos):
    valorTotal = 0
    for pos in range(quantidadeIngressos):
        numeroSala = str(pos + 1)
        tipoSala = input('Tipo de sala do ingresso ' + numeroSala + ': ')
        if(tipoSala != 'N'):
            tipoSala = '3D'
        tipoIngresso = input('Tipo de ingresso ' + numeroSala + ': ')
        if(tipoIngresso != 'E'):
            tipoIngresso = 'I'
        valorTotal += calculaValorIngresso(tipoSala, tipoIngresso)
    return valorTotal

def exibeResultadoFinal(numeroCartao, somatorioCompras, valorMedioCompra):
    print('Compra de R$ ' + str(somatorioCompras) + ' realizada no cartão ' + numeroCartao)
    print('Valor médio pago pelos ingressos nesta compra: R$ ' + str(valorMedioCompra))
    return  

main()

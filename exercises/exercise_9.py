def geraDigitoVerificador(codigo):
    string = str(codigo)
    s = int(string[0]) * 6 + int(string[1]) * 5 + int(string[2]) * 4 + int(string[3]) * 3 + int(string[4]) * 2
    if(s % 10 == 0):
        s *= 3
    return s % 7

print('Número da agência:')
agencia = input()
print('Número da conta:')
conta = input()
digitoAg = geraDigitoVerificador(agencia)
digitoCC = geraDigitoVerificador(conta)
print('Agência: ' + str(agencia) + '-' + str(digitoAg))
print('Conta: ' + str(conta) + '-' + str(digitoCC))

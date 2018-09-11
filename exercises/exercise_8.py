def calculaReajusteDoOnibus(precoAtual, precoReajustado):
    diff = abs(precoReajustado - precoAtual)
    media = (precoReajustado + precoAtual) / 2
    reajuste = diff / media * 100
    if(reajuste > 7):
        valorMaximo = precoAtual * 1.07
        return 'Este reajuste é inconstitucional. O valor máximo permitido é de :' + str(valorMaximo)
    return reajuste

print(calculaReajusteDoOnibus(4, 4.2))
print(calculaReajusteDoOnibus(4, 4.3))

import math

def nl(): print('')

def perimetro(raio):
    res = 2*math.pi*raio
    print('[perimetro()] O perimetro é: ' + str(res) + ' cm')
    nl()

def caracol(raio, anel):
    res = 2*(3+raio/10)**anel
    print('[caracol] O diâmetro do ' + str(anel) + 'º anel é: ' + str(res)+ ' cm')
    nl()

def caixasDagua(vazao, volume):
    res = volume/vazao
    print('[caixasDagua] O tempo para encher uma caixa d\'água de ' + str(volume) + ' litros será de ' + str(res) + ' horas')
    nl()

def pecasEmCaixas(pecas, caixas):
    res = (pecas - pecas % caixas)/caixas
    sobra = pecas % caixas
    print('[pecasEmCaixas] Cada caixa terá ' + str(int(res)) + ' peças, com ' + str(sobra) + ' peças sobrando')
    nl()

def distanciaTotal(distancia, porcentagem):
    res = distancia * 100 / porcentagem
    print('[distanciaTotal] A distância total é: ' + str(res) + ' cm')
    nl()

def professoresDeMatematica(professores, porcentagem):
    res = professores * 100 // porcentagem
    print('[professoresDeMatematica] O total de professores de matemática na escola é: ' + str(res))
    nl()

def ladrilhosPorArea(altura, largura, tamanhoLadrilho):
    res = (altura*largura)//(tamanhoLadrilho*tamanhoLadrilho)+1
    print('[ladrilhosPorArea] Serão necessários ' + str(res) + ' ladrilhos para cobrir a área proposta')
    nl()

def tamanhoLadoTriangulo(ladoA, ladoB, anguloOposto):
    ladoC = (ladoA**2 + ladoB**2 - 2*ladoA*ladoB*math.cos(math.radians(anguloOposto)))**0.5
    print('[tamanhoLadoTriangulo] O tamanho do ladoC do triângulo é: ' + str(ladoC))
    nl()

perimetro(5)
caracol(2.1, 5)
caixasDagua(75, 3160)
pecasEmCaixas(188, 12)
distanciaTotal(600, 37.5)
professoresDeMatematica(25, 26)
ladrilhosPorArea(400, 550, 15)
tamanhoLadoTriangulo(10, 16, 60)

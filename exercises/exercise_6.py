def calc_imc(p, a):
    return(p/(a**2));

def my_print(nome, idade, altura, peso, imc):
    print("Nome: %s" %(nome));
    print("Idade: %s" %(idade));
    print("Altura: %.2f" %(altura));
    print("Peso: %3.1f" %(peso));
    print("IMC: %2.1f" %(imc));
    return;


nome = input("Digite seu nome: ");
idade = input("Digite sua idade: ");
altura = float(input("Digite sua altura(m): "));
peso = float(input("Digite sua peso(Kg): "));

imc = calc_imc(peso, altura);

my_print(nome, idade, altura, peso, imc);

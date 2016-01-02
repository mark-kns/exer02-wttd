'''
Desenvolva um programa que simule a entrega de notas quando um cliente efetuar um saque em um caixa eletrônico.
Os requisitos básicos são os seguintes:

- Entregar o menor número de notas;
- É possível sacar o valor solicitado com as notas disponíveis;
- Saldo do cliente infinito;
- Quantidade de notas infinito (pode-se colocar um valor finito de cédulas para aumentar a dificuldade do problema);
- Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00

Exemplos:
- Valor do Saque: R$ 30,00 – Resultado Esperado: Entregar 1 nota de R$20,00 e 1 nota de R$ 10,00.
- Valor do Saque: R$ 80,00 – Resultado Esperado: Entregar 1 nota de R$50,00 1 nota de R$ 20,00 e 1 nota de R$ 10,00.
'''

def caixa(valor):

    notas_disp = [100, 50, 20, 10, 5, 1]
    notas = []

    for nota in notas_disp:
        while valor >= nota:
            notas.append(nota)
            valor -= nota

    return notas



if __name__ == '__main__':
    assert caixa(10) == [10]
    assert caixa(20) == [20]
    assert caixa(50) == [50]
    assert caixa(100) == [100]

    assert caixa(30) == [20, 10]
    assert caixa(40) == [20, 20]
    assert caixa(60) == [50, 10]

    assert caixa(80) == [50, 20, 10]
    assert caixa(90) == [50, 20, 20]

    assert caixa(180) == [100, 50, 20, 10]
    assert caixa(190) == [100, 50, 20, 20]
    assert caixa(230) == [100, 100, 20, 10]

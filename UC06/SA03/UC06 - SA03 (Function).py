# UC06 SA02 (05/03/2022) - Calculadora de Troco (Gustavo Henrique P. Marquezinho) 

from decimal import Decimal


def calculateChange(total, received):
    value = Decimal(str(received)) - Decimal(str(total))

    if value < 0.0:
        print("x Valor da compra excedeu o valor recebido!")
    else:
        print(f"- Troco = R${value:.2f}")

        for i in [200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]:
            i = Decimal(str(i))
            
            if value >= i:
                print(f"- R${i:.2f} - {value // i:02}x")
                value -= value // i * i


while True:
    print("\nDigite um valor inválido para sair.")

    try:
        calculateChange(float(input("\nValor da Compra: R$")), float(input("Valor Recebido: R$")))
    except ValueError:
        break
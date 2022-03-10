# UC06 SA02 (05/03/2022) - Calculadora de Troco (Gustavo Henrique P. Marquezinho) 

from decimal import Decimal

valueReturned = Decimal(input("Valor Recebido: R$")) - Decimal(input("Valor da Compra: R$"))
print("- Troco = R${:.2f}" .format(valueReturned))

for i in [200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]:
    i = Decimal(str(i))
    
    if valueReturned >= i:
        print("R${:.2f} - {:02}x" .format(i, valueReturned // i))
        valueReturned -= valueReturned // i * i
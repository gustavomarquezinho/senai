# UC06 SA02 (02/03/2022) - Lista de Exercícios Python (Gustavo Henrique P. Marquezinho) 

"""
    • (01) Dada a lista [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as
      seguintes informações: 

        — Tamanho, maior, menor, soma, ordem crescente, ordem decrescente.
"""

numbers = [
    5, 7, 2, 9, 4, 1, 3
]

print(f"\n({numbers})\n\
Tamanho:        {len(numbers)}\n\
Maior:          {max(numbers)}\n\
Menor:          {min(numbers)}\n\
Soma:           {sum(numbers)}")

numbers.sort(reverse=False)
print(f"Crescente:      {str(numbers)[1:-1]}")

numbers.sort(reverse=True)
print(f"Decrescente:    {str(numbers)[1:-1]}\n")


"""
    • (02) Faça um programa que leia 4 valores, calcule a média e imprima positivo
      ou negativo (para ser positivo a média deve ser acima de 1).
"""

average = sum(list(\
    int(input(f'Valor Nº {i + 1:02}: ')) for i in range(4))) / 4

print(f"- Média ({average}) = {'POSITIVA' if average > 1 else 'NEGATIVA'}\n")


"""
    • (03) Escreva um programa que leia 20 valores inteiros e informe a média deles,
      o maior e o menor valor.
"""

numbers = [
    int(input(f"Valor Nº{i + 1:02}: ")) for i in range(20)
]

print(f"- Média, Maior e Menor = ({sum(numbers) / 20}, {max(numbers)}, {min(numbers)})\n")

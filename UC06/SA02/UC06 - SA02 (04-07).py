# UC06 SA02 (02/03/2022) - Lista de Exercícios Python (Gustavo Henrique P. Marquezinho) 

"""
    • (04) Crie uma função para desenhar uma linha, usando o caractere '_'. O tama-
      nho da linha deve ser definido na chamada da função.
"""

def createLine(size):
    print("_" * size, end="\n\n")

createLine(36)


"""
    • (05) Crie uma função que receba como parâmetro uma lista, com valores de qual-
      quer tipo. A função deve imprimir todos os elementos da lista, enumerando-os.
"""

def enumerateElements(elements):
    for i in range(len(elements)):
        print(f"{i + 1:02} - {elements[i]}")

    print()

enumerateElements(["Abacaxi", "Melancia", 10000, 10001, True, False])


"""
    • (06) Crie um programa que converta horas em segundos, conforme o valor que o
      usuário informar quando solicitado a ele.
"""

print(f"- Segundos = {int(input('Valor em Horas: ')) * 3600}\n")


"""
    • (07) Altere o código a seguir, para o menor número de linhas possível, manten-
      do o mesmo resultado.
"""

print("    *", "   * *", "  *   *", " *     *", "***   ***", "  *   *", "  *   *", "  *****", sep="\n")

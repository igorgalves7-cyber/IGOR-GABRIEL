# Leitura dos lados do triângulo
a = float(input("Digite o valor do lado A: "))
b = float(input("Digite o valor do lado B: "))
c = float(input("Digite o valor do lado C: "))

# Verifica a condição de existência do triângulo:
# cada lado deve ser menor que a soma dos outros dois
if a < b + c and b < a + c and c < a + b:

    # Classificação do triângulo
    if a == b and b == c:
        tipo = "Equilátero"
    elif a == b or a == c or b == c:
        tipo = "Isósceles"
    else:
        tipo = "Escaleno"

    print("Triângulo válido!")
    print("Classificação:", tipo)

else:
    print("Os valores informados não formam um triângulo válido.")
# Recebe os números do usuário.
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
oper = input('Digite a operação (+, -, *, /): ')

# Estrutura para executar a operação escolhida.
if oper == "+":
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")

elif oper == "-":
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado}")

elif oper == "*":
    resultado = num1 * num2
    print(f"{num1} * {num2} = {resultado}")

elif oper == "/":
    if num1 == 0 or num2 == 0 :
        print("Erro!")
    else:
        resultado = num1 / num2
        print(f"{num1} / {num2} = {resultado}")

# Se o usuário quiser dividir tal número com zero, vai dar erro.
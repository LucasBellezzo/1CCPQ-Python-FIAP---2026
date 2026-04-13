#Exercício 6
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
op = input("Agora, digite um operador entre: +, *, /, -: ")

if op == "+":
    print(f"Soma: {num1 + num2}")
elif op == "*":
    print(f"Produto: {num1 * num2}")
elif op == "/":
    print(f"Divisão: {num1 / num2}")
elif op == "-":
    print(f"Subtração {num1 - num2}")
else:
    print("Não é um operador válido!")

#Exercício 7

idade = int(input("Digite sua idade: "))

if idade >= 18 and idade < 70:
    print("Seu voto é OBRIGATÓRIO")
elif idade >= 16 and idade < 18 or idade >= 70:
    print("Seu voto é OPCIONAL")
else:
    print("Seu voto não é VALIDO")
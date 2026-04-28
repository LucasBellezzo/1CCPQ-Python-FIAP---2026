#Exercício 1:
from sqlalchemy.util.langhelpers import inject_param_text

#Exercício 2:

num = int(input("Digite um Número: "))
if num % 2 == 0:
    print("Este número é par!")
else:
    print("Este número é impar!")

#Exercício 3:

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 > num2:
    print(num1)
elif num1 == num2:
    print(f"{num1}, Eles são iguais!")
else:
    print(num2)
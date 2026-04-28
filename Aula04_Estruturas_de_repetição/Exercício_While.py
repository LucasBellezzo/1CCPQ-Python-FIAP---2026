
num = int(input("Digite um número n: "))
cont = 1
while cont <= num:
    print(cont)
    cont += 1

# ------------------------------------------------------------------------------------ #
# Exercício 1:

notaA = float(input("Digite a nota A: "))
while notaA < 0 or notaA > 10:
    print("A nota deve estar entre 0 e 10 ")
    notaA = float(input("Digite a nota novamente: "))


notaB = float(input("Digite a nota B: "))
while notaB < 0 or notaB > 10:
    print("A nota deve estar entre 0 e 10 ")
    notaB = float(input("Digite a nota novamente: "))

media = (notaA + notaB) / 2
print(media)

# ------------------------------------------------------------------------------------- #
# Melhorando o exercício 1 com uma função por termos linhas que se repetem

def validar_nota(nota):
    while nota < 0 or nota > 10:
        print("A nota deve estar entre 0 e 10 ")
        nota = float(input("Digite a nota novamente: "))
    return nota

notaA = float(input("Digite a 1 nota: "))
notaA = validar_nota(notaA)

notaB = float(input("Digite a 2 nota: "))
notaB = validar_nota(notaB)

media = (notaA + notaB ) / 2
print(media)




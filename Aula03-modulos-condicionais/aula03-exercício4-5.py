#Exercício 4:

def calcular_media(mat, port, fis, quim):
    return (mat + port + fis + quim) / 4


def verificar_status(media):
    if media >= 7:
        return "Aluno Aprovado!"
    elif media >= 5:
        return "Aluno Em Recuperação."
    else:
        return "Aluno Reprovado"



mat = float(input("Digite sua nota de Matemática: "))
port = float(input("Digite sua nota de Português: "))
fis = float(input("Digite sua nota de Física: "))
quim = float(input("Digite sua nota de Química: "))


media = calcular_media(mat, port, fis, quim)
status = verificar_status(media)

print(f"Média: {media:.2f}")
print(status)

#Exercício 5:

num1 = int(input("Digite um número: "))
num2 = int(input("Digte outro número: "))

if num1 % num2 == 0 or num2 % num1 == 0:
    print("Os números são multiplos!")
else:
    print("Os números não são múltiplos!")

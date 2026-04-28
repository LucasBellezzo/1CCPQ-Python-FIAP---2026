# Exercício 8

salario = float(input("Digite seu salário: R$: "))

if salario <= 280:
    percentual = 20
elif salario <= 700:
    percentual = 15
elif salario <= 1500:
    percentual = 10
else:
    percentual = 5

# Calculos

aumento = salario * (percentual / 100)
novo_salario = salario + aumento

# Saidas

print(f"Salário antes do reajuste: {salario}")
print(f"Percentual de aumento: {percentual}")
print(f"Valor do aumento: {aumento:.2f}")
print(f"Novo Salário: {novo_salario:.2f}")

# Exercício 9

imposto = int(input("Digite o código do estado de origem (1-5): "))
pesoton = int(input("Digite o peso da carga em toneladas: "))
carga = int(input("Digite o código da carga (10-40): "))

if imposto == 1:
    percentual = 35
elif imposto == 2:
    percentual = 25
elif imposto == 3:
    percentual = 15
elif imposto == 4:
    percentual = 5
elif imposto == 5:
    percentual = 0
else:
    print("Imposto invalido")

pesokg = pesoton * 1000

if 10 <= carga <= 20:
    preco_kg = 100
elif 21 <= carga <= 30:
    preco_kg = 250
elif 31 <= carga <= 40:
    preco_kg = 340

preco_carga = pesokg * preco_kg

imposto_valor = preco_carga * (percentual / 100)

valor_total = preco_carga + imposto_valor

print("Peso em kg:", pesokg)
print("Preço da carga:", preco_carga)
print("Imposto:", imposto_valor)
print("Total:", valor_total)
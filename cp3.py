temperaturas = [[28, 31, 34, 33],[25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]

for i in range(len(temperaturas)):
    soma = 0
    risco = 0

    for temp in temperaturas[i]:
        soma += temp

        if temp >= 33:
            risco += 1

    media = soma / len(temperaturas)
    print(f"Sala {i+1}")
    print(f"Média {media:.1f}")
    print(f'Registros Críticos: {risco}')
    print()

# Contador de produto recebe 0, enquanto ele for menor que 3: print produto.

cp = 0
while cp < 10:
    cp += 1         # Incremento: enquanto for Verdadeiro, ira somar 1

    if cp == 3 or cp == 5:
        continue

    if cp == 7: break

    print(f"Produto {cp}")

# -------------------------------------------------------------------------------------------- #
# While descrescente  de 4 até 1

i = 4
while i > 0:
    print(i)
    i -= 1


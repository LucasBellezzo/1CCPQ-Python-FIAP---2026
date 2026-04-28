# ESTRUTURA CONDICIONAL SIMPLES


nota_final = 8.0

if nota_final <6:
    print("Reprovado")

print("FIM")

# ESTRUTURA CONDICIONAL COMPOSTA

nota_final = 5.
if nota_final < 6:
    print("Reprovado")
else:
    print("Aprovado")

print("Fim")


# ESTRUTURA CONDICIONAL ENCADEADA

nota_final = 7.0
if nota_final < 4:
    print("Reprovado")
else:
    if nota_final < 6:
        print("Recuperação")
    else:
        print("Aprovado")

print("FIM")


# ESTRUTURA CONDICIONAL COMPOSTA - ELIF


nota_final = 2.0

if nota_final < 4:
    print("Reprovado")
elif nota_final < 6:
    print("Recuperação")
else:
    print("Aprovado")

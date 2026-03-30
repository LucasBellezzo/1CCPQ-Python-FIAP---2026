escolha_do_usuario = 1

# 0 -> sair do programa
# 1 -> entrar no programa
# >>>> erro!

match escolha_do_usuario:
    case 0:
        print("Sair do prorama")
    case 1:
        print("Bem vindo ao programa!")
    case _:
        print("Erro!!!!!!")
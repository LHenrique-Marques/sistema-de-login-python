administradores = [("Henrique","Luizinho433"),("Rennan","teste")]
logado = False
while not logado:
    try:
        escolha = int(input("""
        Menu:
        
        1 - Logar
        2 - Cadastrar

    Escolha: """))
        if escolha == 1:  
            login = input("Digite seu login: ")
            senha = input("Digite sua senha: ")     
            if (login,senha) in administradores:
                print("Logado com sucesso.")
                logado = True

            else:
                for x in range(len(administradores)):
                    if login not in administradores[x][0]:
                        print("Usuario não encontrado")
                        break

                    elif senha not in administradores[x][1]:
                        print("Senha invalida")
                        break


        elif escolha == 2:
            login = input("Digite o login de cadastro: ")
            senha = input("Digite a senha de cadastro: ")
            confirma_senha = input("Repita a senha: ")
            if senha == confirma_senha:
                administradores.append((login,senha))
                print("Cadastrado com sucesso")
            else:
                print("Senhas divergentes")



        else:
            print("Você não escolheu uma opção valida")
    except:
        print("Ops... Ocorreu um erro... Tente novamente digitando um valor númerico...")



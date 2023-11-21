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
            erros = []     
            if (login,senha) in administradores:
                print("Logado com sucesso.")
                logado = True

            elif (login,senha) not in administradores:
                for x in range(len(administradores)):
                    if login not in administradores[x][0]:
                        erros.append("a")
                    
                for x in range(len(administradores)):
                    if login in administradores[x][0] and senha not in administradores[x][1]:
                        erros.append("b")
                        
            if "b" in erros:
                print("Senha invalida.")

            elif "b" not in erros:
                print("Usuario não encontrado.")
                



        elif escolha == 2:
            login2 = input("Digite o login de cadastro: ")
            senha2 = input("Digite a senha de cadastro: ")
            confirma_senha = input("Repita a senha: ")
            if senha2 == confirma_senha:
                administradores.append((login2,senha2))
                print("Cadastrado com sucesso")
            else:
                print("Senhas divergentes")



        else:
            print("Você não escolheu uma opção valida")
    except:
        print("Ops... Ocorreu um erro... Tente novamente digitando um valor númerico...")

print("** Verificador de senha **")

def create_data():
    user = input("Digite seu usuário: ")
    password = input("Digite sua senha: ")

    new_password = password

    password = input("Confirme sua senha: ")

    if new_password != password:
        print("Acesso negado! Senha incorreta!\n")
        while new_password != password:
            password = input("Digite novamente sua senha: ")
    
    print("Acesso autorizado!")

def application():
    create_data()

application()

def verify_user():
    user = "admin"
    passw = "abc"

    usuario == input("Digite o user cadastrado: ")
    senha == input("Digite a user cadastrada: ")
    if usuario != user:
        print("User incorreto!")
        while usuario != user:
            usuario == input("Digite o user cadastrado: ")
        if senha != passw:
            print("Senha incorreta!")
            while senha != passw:
                senha == input("Digite o user cadastrado: ")
    print("User logado com sucesso!")

    def verify_login():
        print("\n** LOGIN DE SISTEMA **")
            opcao_login = input("Digite 1 para realizar o LOGIN e 2 para se CADASTRAR")
            if opcao_login == 1 or opcao_login == 2:
                if opcao_login == 1:
                    verify_user()
                else:
                    create_data()
                else:
                    print("Opção não encontrada! ")

def application():
    verify_login()
    
application()

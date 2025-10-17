print("** Verficador de senha **")

def create_data():
    user = input("Digite seu usuário: ")
    password = input("Digite sua senha: ")

    new_password = password

    password = input("Confirme sua senha: ")

if new_password != password:
    print("Acesso negado!\n")
    while new_password != password:
        password = input("Digite novamente sua senha: ")
    
    print("Acesso autorizado!")

def aplication():
    create_data()

aplication()

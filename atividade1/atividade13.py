usuario_correto = "admin"
senha_correta = 1234

usuario = input("Digite o usuario: ")
senha = int(input("Digite a senha: "))
if usuario == usuario_correto and senha == senha_correta:
    print("Acesso Liberado!")
else:
    print("Acesso Negado!")
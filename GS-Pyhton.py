def cadastrar_usuario(lista_usuarios):
    nome = input("Digite o nome do usuário: ")

    # Validar data de nascimento:
    data_nascimento = []
    while (len(data_nascimento) != 10):
        data_nascimento = input("Digite a data de nascimento do usuário (DD/MM/AAAA): ")
        if (len(data_nascimento) != 10 or data_nascimento[2] != '/' or data_nascimento[5] != '/'):
            print("Formato de data inválido. Tente novamente.")
    tipo_sanguineo = []
    while(tipo_sanguineo )
    tipo_sanguineo = input("Digite o tipo sanguíneo do usuário: ")
    telefone = input("Digite o telefone do usuário: ")


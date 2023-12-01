def cadastrar_usuario(lista_usuarios):
    nome = input("Digite o nome do usuário: ")

    # Validar data de nascimento:
    data_nascimento = []
    while (len(data_nascimento) != 10):
        data_nascimento = input("Digite a data de nascimento do usuário (DD/MM/AAAA): ")
        if (len(data_nascimento) != 10 or data_nascimento[2] != '/' or data_nascimento[5] != '/'):
            print("Formato de data inválido. Tente novamente.")
    tipo_sanguineo = input("Digite o tipo sanguíneo do usuário: ")
    telefone = input("Digite o telefone do usuário: ")

    # Lista para doenças em tratamento:
    doencas_em_tratamento = []
    resp = 1
    while (resp == 1):
        doencas_tratamento = input("Digite as doenças em tratamento do usuário: ")
        resp = int(input("Mais alguma doença? (1) - Não(0): "))
        doencas_em_tratamento.append(doencas_tratamento)

    # Adicionar pessoas de confiança ou não:
    resp = 2
    contatos_de_confianca = []
    while (resp == 2):
        nome_pessoa_confianca = input("Digite o nome da pessoa de confiança: ")
        tel_pessoa_confianca = input("Digite o telefone da pessoa de confiança: ")
        resp = int(input("Adicionar mais uma pessoa de confiança? (2) - Finalizar cadastro (0): "))
        contatos_de_confianca.append({"Nome": nome_pessoa_confianca, "Telefone": tel_pessoa_confianca})

    novo_usuario = {
        "Nome": nome,
        "Data de Nascimento": data_nascimento,
        "Tipo Sanguíneo": tipo_sanguineo,
        "Telefone": telefone,
        "Doenças em Tratamento": doencas_em_tratamento,
        "Contatos de Confiança": contatos_de_confianca,
    }

    lista_usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso!")

def exibir_usuarios(lista_usuarios):
    print(("_______________________"))
    print("\nLista de Usuários:")
    for usuario in lista_usuarios:
        print(f"\nNome: {usuario['Nome']}")
        print(f"Data de Nascimento: {usuario['Data de Nascimento']}")
        print(f"Tipo Sanguíneo: {usuario['Tipo Sanguíneo']}")
        print(f"Telefone: {usuario['Telefone']}")
        print(f"Doenças em Tratamento: {', '.join(usuario['Doenças em Tratamento'])}")
        for contato in usuario['Contatos de Confiança']:
            print(f"Pessoa de Confiança: {contato['Nome']}, Telefone: {contato['Telefone']}")


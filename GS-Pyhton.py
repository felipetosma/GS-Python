def cadastrar_usuario(lista_usuarios):
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento do usuário (DD/MM/AAAA): ")
    tipo_sanguineo = input("Digite o tipo sanguíneo do usuário: ")
    telefone = input("Digite o telefone do usuário: ")
    doencas_tratamento = input("Digite as doenças em tratamento do usuário (separadas por vírgula): ").split(',')
    doencas_cronicas = input("Digite as doenças crônicas do usuário (separadas por vírgula): ").split(',')

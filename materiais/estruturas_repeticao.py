def limpar_tela():
    for x in range(30):
        print("")

def exibir_lista(lista):
    for item in lista:
        print(item)

def exibir_funcionarios(lista):
    print("|      Funcionário      | Idade | Cargo |")
    count = 0
    for funcionario in lista:
        print(f"| {count:3} | {funcionario["nome"]:21} | {funcionario["idade"]:5} | {funcionario["cargo"]}")
        count = count + 1

def buscar_funcionario(lista, nome):
    for item in lista:
        print(f"PROCURANDO {nome} NO REGISTRO",item)
        if nome in item["nome"]:
            print("ACHEI:", item)
            return item
    return None

def alterar_funcionario(lista):
    exibir_funcionarios(lista)
    codigo = int(input("Digite o código do usuário:"))
    nome = input("Digite o nome do usuário:")
    idade = input("Digite a idade do usuário:")
    cargo = input("Digite o cargo do usuário:")
    print("Usuário que será alterado: ", lista[codigo])
    lista[codigo]["nome"] = nome
    lista[codigo]["idade"] = idade
    lista[codigo]["cargo"] = cargo
    return lista

def exibir_menu():
    limpar_tela()
    print("1 - Visualizar Funcionários")
    print("2 - Adicionar Funcionário")
    print("3 - Pesquisar Funcionários")
    print("4 - Alterar Funcionário")
    print("5 - Excluir Funcionário")
    print("0 - Sair")
    print("")
    return input("Digite a opção desejada:")

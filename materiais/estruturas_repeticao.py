def limpar_tela():
    for x in range(30):
        print("")

def exibir_lista(lista):
    for item in lista:
        print(item)

def exibir_funcionarios(lista):
    print("|      Funcionário      | Idade | Cargo |")
    for funcionario in lista:
        print(f"| {funcionario["nome"]:21} | {funcionario["idade"]:5} | {funcionario["cargo"]}")

def buscar_funcionario(lista, nome):
    for item in lista:
        print(f"PROCURANDO {nome} NO REGISTRO",item)
        if nome in item["nome"]:
            print("ACHEI:", item)
            return item
    return None


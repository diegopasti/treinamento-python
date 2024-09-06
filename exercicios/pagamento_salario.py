"""
Projeto: Crie um sistema onde para controle de pagamento salarial
onde o usuário poderá cadastrar funcionários, cargos e salarios.
para cada funcionário precisamos registrar:

  funcionario:
    - nome: str
    - idade: int
    - cargo: str

Feature 1: Cadastro de Funcionários
  UC01: O usuário precisa visualizar lista dos funcionarios
  UC02: O usuário precisa incluir um novo funcionário
  UC03: O usuário precisa pesquisar um funcionário
  UC04: O usuário precisa alterar um funcionário
  UC05: O Usuário precisa filtrar os funcionários
  UC06: O usuário precisa excluir um funcionário

Feature: Cadastro de Cargos

Feature: Controle de Pagamentos

"""
from materiais.estruturas_dados import dados_funcionario
from materiais.estruturas_repeticao import limpar_tela, exibir_funcionarios, buscar_funcionario, exibir_menu, \
    alterar_funcionario

funcionarios = [
    {'nome': 'DIEGO PASTI', 'idade': '32', 'cargo': 'DEV'},
    {'nome': 'GUSTAV AUGUSTIN', 'idade': '19', 'cargo': 'UX'},
    {'nome': 'PAULO FERNANDES', 'idade': '51', 'cargo': 'GESTOR'},
    {'nome': 'AMANDA SOUZA', 'idade': '23', 'cargo': 'DESIGN'},
]

while True:
    opcao = exibir_menu()


    if opcao == "0":
        break

    if opcao == "1":
        print("Vamos visualizar funcionarios")
        exibir_funcionarios(funcionarios)

    if opcao == "2":
        print("Vamos adicionar funcionario")
        funcionario = dados_funcionario()
        funcionarios.append(funcionario)

    if opcao == "3":
        print("Vamos pesquisar um funcionário")
        nome = input("Digite o nome do funcionario:")
        exibir_funcionarios(funcionarios)

    if opcao == "4":
        print("Vamos alterar funcionario")
        alterar_funcionario(funcionarios)
        exibir_funcionarios(funcionarios)

    if opcao == "5":
        print("Vamos excluir funcionario")

    input("Pressione enter para seguir.. ")

print("SAINDO DA APLICACAO")



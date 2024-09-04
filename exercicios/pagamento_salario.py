"""
Projeto: Crie um sistema onde para controle de pagamento salarial
onde o usuário poderá cadastrar funcionários, cargos e salarios.
para cada funcionário precisamos registrar:

  funcionario:
    - nome: str
    - idade: int
    - cargo: str
    - admissao: date

Feature 1: Cadastro de Funcionários
  UC01: O usuário precisa incluir um novo funcionário
  UC02: O usuário precisa alterar
  UC03: O usuário precisa visualizar lista completa dos funcionarios
  UC04: O Usuário precisa filtrar os funcionários
  UC05: O usuário precisa excluir um funcionário

Feature: Cadastro de Cargos

Feature: Controle de Pagamentos

"""

from materiais.estruturas_repeticao import limpar_tela

opcao = ""
while opcao != "0":
    limpar_tela()
    print("1 - Adicionar Funcionário")
    print("2 - Alterar Funcionário")
    print("3 - Visualizar Funcionários")
    print("4 - Pesquisar Funcionários")
    print("5 - Excluir Funcionário")
    print("0 - Sair")
    print("")
    opcao = input("Digite a opção desejada:")

print("SAINDO DA APLICACAO")



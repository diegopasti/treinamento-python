# Funções basicas
nome = input("DIGITE SEU NOME:")
print("SEU NOME É:", nome)

# Operações Matematica
soma = 10 + 20
subtracao = 10 - 20
multiplicao = 10 * 20
divisão = 10 / 20
potencia = 2 ** 3

# Operadores Lógicos
# maior/menor: ><
# Maior igual: >=
# E: and
# OU: or
# CONTEM: in


# Condicionais
if "PASTI" in nome:
    print("")
else:
    print("ESSE CARA NÂO É ITALIANO")

# Repetições

soma = 0
while soma < 10:
    valor = int(input("DIGITE UM NUMERO DE NOVO:"))
    soma = soma + valor
    print("SOMA:", soma)

print("ENFIM, SAI DESSE LOOP")



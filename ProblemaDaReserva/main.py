from hoteisCadastrados import *


opcoes_hoteis = []
opcoes_hoteis += [Lakewood()]
opcoes_hoteis += [Bridgewood()]
opcoes_hoteis += [Ridgewood()]

entrada = input("\nEntrada:\n")
for i in range(len(opcoes_hoteis)):
    opcoes_hoteis[i].fazer_orcamento(entrada)

melhor_opcao = opcoes_hoteis[0] if (opcoes_hoteis[0]>opcoes_hoteis[1] and opcoes_hoteis[0]>opcoes_hoteis[2])\
    else opcoes_hoteis[1] if (opcoes_hoteis[1]>opcoes_hoteis[2])\
        else opcoes_hoteis[2]

print(str(melhor_opcao))
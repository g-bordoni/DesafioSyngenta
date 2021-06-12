from hoteisCadastrados import *


entrada  = input("\nEntrada:\n")

opcoes_hoteis = []
opcoes_hoteis += [Lakewood(entrada)]
opcoes_hoteis += [Bridgewood(entrada)]
opcoes_hoteis += [Ridgewood(entrada)]

melhor_opcao = opcoes_hoteis[0] if (opcoes_hoteis[0]>opcoes_hoteis[1] and opcoes_hoteis[0]>opcoes_hoteis[2])\
    else opcoes_hoteis[1] if (opcoes_hoteis[1]>opcoes_hoteis[2])\
        else opcoes_hoteis[2]

print(str(melhor_opcao))
from hoteisCadastrados import *

def melhor_orcamento(entrada:str, opcoes: list):
    if(len(opcoes)==0):
        return None

    opcoes[0].fazer_orcamento(entrada)
    melhor_opcao = opcoes[0]
    for i in range(1, len(opcoes)):
        opcoes[i].fazer_orcamento(entrada)
        if opcoes[i]>melhor_opcao:
            melhor_opcao = opcoes[i]
    return melhor_opcao

opcoes_hoteis = []
opcoes_hoteis += [Lakewood()]
opcoes_hoteis += [Bridgewood()]
opcoes_hoteis += [Ridgewood()]
opcoes_hoteis += [OuroMinas()]

entrada = input("\nEntrada:\n")
hotel_escolhido = melhor_orcamento(entrada,opcoes_hoteis)


print(str(hotel_escolhido))
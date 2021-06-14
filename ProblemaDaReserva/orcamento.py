
class Orcamento():
    __FIM_DE_SEMANA = ['SAT','SUN']
    __orcamento = 0.0

    def __listar_datas(self, entrada: str)-> list:
        diarias_lista = entrada.split(",")
        return [diaria.replace(" ", "").upper() for diaria in diarias_lista]
        
    def __init__(self, custos_tupla: tuple, datas_string: str):

        datas_lista = self.__listar_datas(datas_string)

        diarias_fds = [diaria for diaria in datas_lista \
            if diaria.split("(")[1].split(")")[0] in self.__FIM_DE_SEMANA]

        self.__orcamento = custos_tupla[0]*(len(datas_lista)-len(diarias_fds))+ \
            custos_tupla[1]*len(diarias_fds)

    def get_orcamento(self) -> float:
        return self.__orcamento
    
    def __eq__(self, o: object) -> bool:
        return self.__orcamento == o.get_orcamento()
    def __lt__(self, o: object) -> bool:
        return self.__orcamento < o.get_orcamento()

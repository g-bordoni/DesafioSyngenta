
class Orcamento():
    __orcamento = 0.0

    def __init__(self, custos_tupla: tuple, datas_lista: list):

        diarias_fds = [diaria for diaria in datas_lista \
            if diaria.split("(")[1].split(")")[0] in ["SAT","SUN"]]

        diarias_semanais = [diaria for diaria in datas_lista if not diaria in diarias_fds]

        self.__orcamento = custos_tupla[0]*len(diarias_semanais)+ \
            custos_tupla[1]*len(diarias_fds)

    def get_orcamento(self) -> float:
        return self.__orcamento
    
    def __eq__(self, o: object) -> bool:
        return self.__orcamento == o.get_orcamento()
    
    def __lt__(self, o: object) -> bool:
        return self.__orcamento < o.get_orcamento()

    def __str__(self) -> str:
        return str(self.__orcamento)
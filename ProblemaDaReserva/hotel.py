from orcamento import Orcamento
from abc import ABC, abstractmethod


class Hotel(ABC):    
    __estrelas = None
    __valores_regulares = None
    __valores_fidelidade = None
    __orcamento = None
    
    def __init__(self, estrelas: int, valores_regulares: tuple, valores_fidelidade: tuple):
        self.__estrelas = estrelas
        self.__valores_regulares = valores_regulares
        self.__valores_fidelidade = valores_fidelidade

    def fazer_orcamento(self, entrada: str):
        cliente_tipo, diarias = entrada.split(":")
        valores_referencia = self.__valores_regulares if cliente_tipo.upper() == "REGULAR" \
            else self.__valores_fidelidade

        self.__orcamento = Orcamento(valores_referencia, diarias)

    def get_orcamento(self)->object:
        return self.__orcamento
    def get_estrelas(self)->int:
        return self.__estrelas

    def __gt__(self, o:object)->bool:
        if self.__orcamento < o.get_orcamento():
            return True
        elif self.__orcamento == o.get_orcamento() and self.__estrelas > o.get_estrelas():
            return True
        else :
            False

    @abstractmethod
    def __str__(self) -> str:
        pass


        

    


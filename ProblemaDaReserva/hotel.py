from orcamento import Orcamento
from abc import ABCMeta, abstractclassmethod


class Hotel(object):
    __metaclass__ = ABCMeta
    
    __estralas = None
    __valores_tupla = None
    __diarias_lista = None
    __orcamento = None

    def get_orcamento(self):
        return self.__orcamento
    def get_valores(self):
        return self.__valores_tupla
    def get_diarias_lista(self):
        return self.__diarias_lista
    def get_estrelas(self):
        return self.__estrelas

    def __gerar_orcamento(self):
        self.__orcamento = Orcamento(self.get_valores(), self.get_diarias_lista())
    
    def __init__(self, estrelas: int, valores: tuple, diarias: list):
        self.__estralas = estrelas
        self.__valores_tupla = valores
        self.__diarias_lista = diarias
        self.__gerar_orcamento()

    def __gt__(self, o:object)->bool:
        if self.__orcamento < o.get_orcamento():
            return True
        elif self.__orcamento == o.get_orcamento() and self.__estralas > o.get_estrelas:
            return True
        else :
            False


        

    


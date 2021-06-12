from hotel import Hotel

class Lakewood(Hotel):
    ESTRELAS = 3
    VALORES_NORMAIS = (110,90)
    VALORES_FIDELIDADE = (80, 80) 

    def __init__(self, entrada: str):
        cliente_tipo, diarias = entrada.split(":")
        diarias_lista = diarias.split(",")
        diarias_lista = [diaria.replace(" ", "").upper() for diaria in diarias_lista]

        valores_referencia = self.VALORES_NORMAIS if cliente_tipo.upper() == "REGULAR" \
            else self.VALORES_FIDELIDADE

        super().__init__(self.ESTRELAS, valores_referencia, diarias_lista)
    
    def __str__(self) -> str:
        return "Lakewood"

class Bridgewood(Hotel):
    ESTRELAS = 4
    VALORES_NORMAIS = (160,60)
    VALORES_FIDELIDADE = (110, 50) 

    def __init__(self, entrada: str):
        cliente_tipo, diarias = entrada.split(":")
        diarias_lista = diarias.split(",")
        diarias_lista = [diaria.replace(" ", "").upper() for diaria in diarias_lista]

        valores_referencia = self.VALORES_NORMAIS if cliente_tipo.upper() == "REGULAR" \
            else self.VALORES_FIDELIDADE

        super().__init__(self.ESTRELAS, valores_referencia, diarias_lista)
    
    def __str__(self) -> str:
        return "Bridgewood"


class Ridgewood(Hotel):
    ESTRELAS = 5
    VALORES_NORMAIS = (220,150)
    VALORES_FIDELIDADE = (100, 40) 

    def __init__(self, entrada: str):
        cliente_tipo, diarias = entrada.split(":")
        diarias_lista = diarias.split(",")
        diarias_lista = [diaria.replace(" ", "").upper() for diaria in diarias_lista]

        valores_referencia = self.VALORES_NORMAIS if cliente_tipo.upper() == "REGULAR" \
            else self.VALORES_FIDELIDADE

        super().__init__(self.ESTRELAS, valores_referencia, diarias_lista)

    def __str__(self) -> str:
        return "Ridgewood"

    


        

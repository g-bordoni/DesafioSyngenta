from hotel import Hotel

class Lakewood(Hotel): 

    def __init__(self):
        ESTRELAS = 3
        VALORES_REGULARES = (110,90)
        VALORES_FIDELIDADE = (200,200)

        super().__init__(ESTRELAS, VALORES_REGULARES, VALORES_FIDELIDADE)
    
    def __str__(self) -> str:
        return "Lakewood"

class Bridgewood(Hotel):

    def __init__(self):
        ESTRELAS = 4
        VALORES_REGULARES = (160,60)
        VALORES_FIDELIDADE = (200,200)

        super().__init__(ESTRELAS, VALORES_REGULARES, VALORES_FIDELIDADE)
    
    def __str__(self) -> str:
        return "Bridgewood"


class Ridgewood(Hotel):

    def __init__(self):
        ESTRELAS = 5
        VALORES_REGULARES = (220,150)
        VALORES_FIDELIDADE = (200,200)

        super().__init__(ESTRELAS, VALORES_REGULARES, VALORES_FIDELIDADE)

    def __str__(self) -> str:
        return "Ridgewood"

class OuroMinas(Hotel):

    def __init__(self):
        ESTRELAS = 6
        VALORES_REGULARES = (250,140)
        VALORES_FIDELIDADE = (150,100)

        super().__init__(ESTRELAS, VALORES_REGULARES, VALORES_FIDELIDADE)
    def __str__(self)->str:
        return "OuroMinas"
    


        

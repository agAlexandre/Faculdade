import math


class Ponto():
    '''
    Implementa a abstração de um ponto no plano Cartesiano 2D,
    que possui como atributos as coordenadas x e y
    '''

    def __init__(self, x: float, y: float) -> None:
        '''
        Construtor da classe
        '''
        pass

    def desloca(self, dx: float, dy: float) -> None:
        '''
        Desloca o ponto em dx no eixo x e dy no eixo y
        '''
        pass

    def distancia(self, ponto: 'Ponto') -> float:
        '''
        Calcula a distância euclidiana em relação a outro ponto
        passado como argumento
        '''
        pass


class Reta():
    '''
    Cria a abstração de uma reta no plano cartesiano 2D e tem como atributos
    o coeficiente deincl
    '''
    def __init__(self, a: float, b: float):
        pass

    def pertence(self, ponto: Ponto) -> bool:
        '''
        Devolve 'True se o ponto pertence a reta e 'False' caso contrário
        '''
        pass

    def eh_paralela(self, reta: 'Reta') -> bool:
        '''
        Retorna true se a reta é paralela a esta reta e 'False' caso contrário
        '''
        pass

    def interseccao(self, reta: 'Reta') -> Ponto:
        '''
        Retorna o ponto de intersecção com a reta passada como argumento
        caso não haja intersecção retorna 'None'
        '''
        pass

    def perpendicular(self, ponto: Ponto) -> 'Reta':
        '''
        BÔNUS:
        Cria uma reta perpencidular à esta reta que passa por ponto
        '''
        pass


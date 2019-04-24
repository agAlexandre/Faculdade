import math
import turtle

class Figura:
    def __init__(self, x, y, cor):
        self._x = x
        self._y = y
        self._cor = cor
        self._janela = turtle.Screen()
        self._tartaruga = turtle.Turtle()
        self._tartaruga.pen(fillcolor=cor, pencolor=cor, pensize=10)
        self._tartaruga.penup()
        self._tartaruga.setposition(x,y)
        self._tartaruga.pendown()

    def calculaArea(self):
        raise

    def desenha(self):
        raise

class Circulo(Figura):
    def __init__(self, x, y, cor, raio):
        #Figura.__init__(self, x, y, cor)
        super().__init__(x, y, cor)
        if raio < 0:
            raise ValueError 
        self.__raio = raio 

    def calculaArea(self):
        return math.pi * self.__raio**2

    def desenha(self):
        passo = 2*self.__raio*math.tan(math.pi/45)
        for i in range(45):
            self._tartaruga.forward(passo)
            self._tartaruga.left(8)


class Quadrado(Figura):
    def __init__(self, x, y, cor, lado):
        #Figura.__init__(self, x, y, cor)
        super().__init__(x, y, cor)
        if lado < 0:
            raise ValueError
        self.__lado = lado 

    def calculaArea(self):
        return self.__lado**2

    def desenha(self):
        for i in range(4):
            self._tartaruga.forward(self.__lado)
            self._tartaruga.left(90)



class Triangulo(Figura):
     self._tartaruga.forward(self.__lado)
     self._tartaruga.left(120)

    


c1 =  Circulo(10, 10, 'red', 50)
c2 =  Circulo(100, 100, 'orange', 50)
c3 =  Circulo(-100, 50, 'blue', 50)
q1 =  Quadrado(50, 50, 'red', 50)
q2 =  Quadrado(150, 200, 'green', 100)
q3 =  Quadrado(-200, -150, 'blue', 150)
lista=[]
lista.append(c1)
lista.append(c2)
lista.append(c3)
lista.append(q1)
lista.append(q2)
lista.append(q3)

for f in lista:
    f.desenha()

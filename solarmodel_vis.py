# coding: utf-8
# license: GPLv3


class Star:
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """
    def __init__(self,m,x,y,Vx,Vy,Fx,Fy,r,color,image):
        self.type = "star"
        self.m = m
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.Fx = Fx
        self.Fy = Fy
        self.r = 5
        self.color = "red"
        self.image = image




class Planet:
    def __init__(self, m, x, y, Vx, Vy, Fx, Fy, r, color, image):
        self.type = "planet"
        self.m = m
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.Fx = Fx
        self.Fy = Fy
        self.r = 5
        self.color = "green"
        self.image = image

import math

class Shape():
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def print_size(self):
        print("{} by {}".format(self.width,self.length))
        
class Square(Shape):
    def area(self):
        return self.width * self.length

    def print_size(self):
        print("I am {} by {}".format(self.width, self.length))

class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

    def change_size(self, w, l):
        self.width = w
        self.len = l

class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return (self.radius ** 2) * math.pi

class Triangle():
    def __init__(self, s1, s2, s3):
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3

    def area(self):
        s1 = self.side1
        s2 = self.side2
        s3 = self.side3         
        s = (s1 + s2 + s3)/2
        return math.sqrt(s*(s - s1) * (s - s2) * (s - s3))

class Hexagon():
    def __init__(self, s):
        self.sides = s

    def perimeter(self):
        perim = 0
        for i in range(0, len(self.sides)):
            perim += self.sides[i]
        return perim


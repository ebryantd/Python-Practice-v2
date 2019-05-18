class Orange():
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")

    def rot(self, days, temp):
        self.mold = days * temp

class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

    def change_size(self, w, l):
        self.width = w
        self.len = l

rect1 = Rectangle(10, 25)
#print(rect1.area())
rect1.change_size(20, 50)
#print(rect1.area())
    

o1 = Orange(10, "dark orange")
o2 = Orange(45, "purple")

"""
print(o1.weight)
print(o1.color)
print(o1.mold)

print(o2.weight)
print(o2.color)

o1.weight = 100
o1.color = "green"

print(o1.weight)
print(o1.color)

o1.rot(5, 100)
print(o1.mold)
"""

class Shapes:
    def __init__(self, name, side):
        self.name = name
        self.side = side
    def Area(self):
        print("I am a :" + self.name + "\n" +"I have" + self.side)
obj_shape=Shapes("shapes", " so many")
obj_shape.Area()

class Rectangle(Shapes):
    def __init__(self, len1, wid1):
        self.lenght=len1
        self.width=wid1
    def Area(self):
        result= self.lenght * self.width
        return result
obj_book=Rectangle(10, 7)
print( "The area of a book is" , obj_book.Area())


class Circle(Shapes):
    def __init__(self, rad, pi):
        self.radius=rad
        self.pi=pi
    def Area(self):
        result= self.radius * self.pi
        return result
obj_radius=Circle(10, 3)
print("The radius is", obj_radius.Area())

class Triangle(Shapes):
    def __init__(self, base, height):
        self.bas=base
        self.hei=height
    def Area(self):
        result= self.bas * self.hei
        return result
obj_tri=Triangle(15, 5)
print("The base is ", obj_tri.Area())
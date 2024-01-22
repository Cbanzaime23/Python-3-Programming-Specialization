# class Point:
#     """ Point class for representing and manipulating x,y coordinates. """
#
#     def getX(self):
#         return self.x
#
#     def getY(self):
#         return self.y
#
# point1 = Point()         # Instantiate an object of type Point
# point2 = Point()         # and make a second point
#
# point1.x = 5
# point2.x = 10
#
# print(point1.getX())
#
# print(point2.getX())

# class Point:
#     """ Point class for representing and manipulating x,y coordinates. """
#
#     def __init__(self, initX, initY):
#         self.x = initX
#         self.y = initY
#
#     def getX(self):
#         return self.x
#
#     def getY(self):
#         return self.y
#
#     def distanceFromOrigin(self):
#         return ((self.x ** 2) + (self.y ** 2)) ** 0.5
#
#
#
#
# p = Point(1,1)
# print(p.distanceFromOrigin())

# import math
#
# class Point:
#     """ Point class for representing and manipulating x,y coordinates. """
#
#     def __init__(self, initX, initY):
#
#         self.x = initX
#         self.y = initY
#
#     def getX(self):
#         return self.x
#
#     def getY(self):
#         return self.y
#
#     def distanceFromOrigin(self):
#         return ((self.x ** 2) + (self.y ** 2)) ** 0.5
#
# def distanceFormula(point1, point2):
#     """The parameters must a Point Object
#     """
#     xdiff = point2.getX()-point1.getX()
#     ydiff = point2.getY()-point1.getY()
#
#     dist = math.sqrt(xdiff**2 + ydiff**2)
#     return dist
#
# p = Point(4,3)
# q = Point(3,4)
# print(distanceFormula(p,q))


# import math
""" Point class
"""

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    printed_rep = "*"

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def distance(self, point2):
        xdiff = point2.getX()-self.getX()
        ydiff = point2.getY()-self.getY()

        dist = math.sqrt(xdiff**2 + ydiff**2)
        return dist

    def __str__(self):
        return 'Point ({}, {})'.format(self.x, self.y)

    def __add__(self, otherPoint):
        return Point(self.x + otherPoint.x,
                    self.y + otherPoint.y)

    def __sub__(self, otherPoint):
        return Point(self.x - otherPoint.x,
                    self.y - otherPoint.y)

    def slope(self, otherPoint):
        m = (otherPoint.y - self.y) / (otherPoint.x - self.x)
        return m

    def halfway(self, otherPoint):
        mx = (self.x + otherPoint.x)/2
        my = (self.y + otherPoint.y)/2
        return Point(mx,my)

    def graph(self):
        rows = []
        size = max(int(self.x), int(self.y)) + 2
        for j in range(size-1) :
            if (j+1) == int(self.y):
                special_row = str((j+1) % 10) + (" "*(int(self.x) -1)) + self.printed_rep
                rows.append(special_row)
            else:
                rows.append(str((j+1) % 10))
        rows.reverse()  # put higher values of y first
        x_axis = ""
        for i in range(size):
            x_axis += str(i % 10)
        rows.append(x_axis)

        return "\n".join(rows)

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

p1 = Point(-5, 10)
p2 = Point(15, 10)
m = p1.slope(p2)
print(m)

# p1 = Point(2, 3)
# p2 = Point(3, 12)
# print(p1.graph())
# print()
# print(p2.graph())

# p1 = Point(-5, 10)
# p2 =Point(15, 20)
# print(p1)
# print(p2)
# print(p1 + p2)
# print(p1 - p2)
# mid = p1.halfway(p2)
# print(mid)
# print(mid.getX())
# print(mid.getY())


# cityNames = ["Detroit", "Ann Arbor", "Pittsburgh", "Mars", "New York"]
# populations = [680250, 117070, 304391, 1683, 8406000]
# states = ["MI", "MI", "PA", "PA","NY"]
#
# city_tuples = zip(cityNames, populations, states)
#
# class City:
#     def __init__(self, n, p, s):
#         self.name = n
#         self.populations = p
#         self.states = s
#
#     def __str__(self):
#         return '{}, {} (pop: {})'.format(self.name, self.states, self.populations)
#
# cities = [City(n, p, s) for (n ,p, s) in city_tuples]
# for i in range(0,5):
#     print(cities[i])




# class Cereal:
#     def __init__(self, name, brand, fiber):
#         self.name = name
#         self.brand = brand
#         self.fiber = fiber
#
#     def __str__(self):
#         return '{} cereal is produced by {} and has {} grams of fiber in every serving!'.format(self.name, self.brand, self.fiber)
#
#
# c1 = Cereal("Corn Flakes", "Kellogg's", 2)
# c2 = Cereal("Honey Nut Cheerios", "General Mills", 3)
#
# print(c1)
# print(c2)

# class Fruit():
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def sort_priority(self):
#         return self.price
#
# L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]
# print("-----sorted by price, referencing a class method-----")
# for f in sorted(L, key=Fruit.sort_priority):
#     print(f.name)
#
# print("---- one more way to do the same thing-----")
# for f in sorted(L, key=lambda x: x.sort_priority()):
#     print(f.name)

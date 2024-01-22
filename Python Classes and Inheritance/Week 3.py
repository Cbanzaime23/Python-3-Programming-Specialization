# """ Point class
# """
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
#     def distance(self, point2):
#         xdiff = point2.getX()-self.getX()
#         ydiff = point2.getY()-self.getY()
#
#         dist = math.sqrt(xdiff**2 + ydiff**2)
#         return dist
#
#     def move(self, dx, dy):
#         self.x = self.x + dx
#         self.y = self.y + dy
#
# import test
# p = Point(3,4)
# test.testEqual(p.y, 4)


# try:
#     for i in range(5):
#         print(1.0 / (3-i))
# except Exception as error_inst:
#     print("Got an error", error_inst)
""" Example of Try Except Clause
"""

students = [('Timmy', 95, 'Will pass'), ('Martha', 70), ('Betty', 82, 'Will pass'), ('Stewart', 50, 'Will not pass'), ('Ashley', 68), ('Natalie', 99, 'Will pass'), ('Archie', 71), ('Carl', 45, 'Will not pass')]

passing = {'Will pass': 0, 'Will not pass': 0}
for tup in students:
    try:
        if tup[2] == 'Will pass':
            passing['Will pass'] += 1
        elif tup[2] == 'Will not pass':
            passing['Will not pass'] += 1
    except:
        continue

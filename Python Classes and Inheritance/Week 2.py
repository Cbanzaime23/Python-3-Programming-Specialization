# from random import randrange
#
# class Pet():
#     boredom_decrement = 4
#     hunger_decrement = 6
#     boredom_threshold = 5
#     hunger_threshold = 10
#     sounds = ['Mrrp']
#     def __init__(self, name = "Kitty", pet_type="dog"):
#         self.name = name
#         self.hunger = randrange(self.hunger_threshold)
#         self.boredom = randrange(self.boredom_threshold)
#         self.sounds = self.sounds[:]  # copy the class attribute, so that when we make changes to it, we won't affect the other Pets in the class
#         self.pet_type = pet_type
#
#     def clock_tick(self):
#         self.boredom += 1
#         self.hunger += 1
#
#     def mood(self):
#         if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
#             if self.pet_type == "dog": # if the pet is a dog, it will express its mood in different ways from a cat or any other type of animal
#                 return "happy"
#             elif self.pet_type == "cat":
#                 return "happy, probably"
#             else:
#                 return "HAPPY"
#         elif self.hunger > self.hunger_threshold:
#             if self.pet_type == "dog": # same for hunger -- dogs and cats will express their hunger a little bit differently in this version of the class definition
#                 return "hungry, arf"
#             elif self.pet_type == "cat":
#                 return "hungry, meeeeow"
#             else:
#                 return "hungry"
#         else:
#             return "bored"
#
#     def __str__(self):
#         state = "     I'm " + self.name + ". "
#         state += " I feel " + self.mood() + ". "
#         return state
#
#     def hi(self):
#         print(self.sounds[randrange(len(self.sounds))])
#         self.reduce_boredom()
#
#     def teach(self, word):
#         self.sounds.append(word)
#         self.reduce_boredom()
#
#     def feed(self):
#         self.reduce_hunger()
#
#     def reduce_hunger(self):
#         self.hunger = max(0, self.hunger - self.hunger_decrement)
#
#     def reduce_boredom(self):
#         self.boredom = max(0, self.boredom - self.boredom_decrement)

"""
Example of Interitance
"""
# CURRENT_YEAR = 2019
#
# class Person:
#     def __init__(self, name, year_born):
#         self.name = name
#         self.year_born = year_born
#     def getAge(self):
#         return CURRENT_YEAR - self.year_born
#     def __str__(self):
#         return '{} ({})'.format(self.name, self.getAge())
#
# class Student(Person):
#     def __init__(self, name, year_born):
#         Person.__init__(self, name, year_born)
#         self.knowledge = 0
#     def study(self):
#         self.knowledge += 1
#
# alice = Student('Alice Smith', 1990)
# alice.study()
# alice.study()
# alice.study()
# print(alice.knowledge)



from random import randrange

# Here's the original Pet class
class Pet():
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = ['Mrrp']
    def __init__(self, name = "Kitty"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]  # copy the class attribute, so that when we make changes to it, we won't affect the other Pets in the class

    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "     I'm " + self.name + ". "
        state += " I feel " + self.mood() + ". "
        # state += "Hunger %d Boredom %d Words %s" % (self.hunger, self.boredom, self.sounds)
        return state

    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

    def teach(self, word):
        self.sounds.append(word)
        self.reduce_boredom()

    def feed(self):
        self.reduce_hunger()

    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)

# Here's the new definition of class Cat, a subclass of Pet.
class Cat(Pet): # the class name that the new class inherits from goes in the parentheses, like so.
    sounds = ['Meow']

    def chasing_rats(self):
        return "What are you doing, Pinky? Taking over the world?!"


class Cheshire(Cat): # this inherits from Cat, which inherits from Pet

    def smile(self): # this method is specific to instances of Cheshire
        print(":D :D :D")

class Dog(Pet):
    sounds = ["Woof", "Ruff"]

    def feed(self):
        Pet.feed(self)
        print("Arf! Thanks")

d1 = Dog("Astro")

d1.feed()


"""Book Class
"""
# class Book():
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#     def __str__(self):
#         return '"{}" by {}'.format(self.title, self.author)
#
class PaperBook(Book):
    def __init__(self, title, author,numPages):
        Book.__init__(self, title, author)
        self.numPages = numPages
# #
# class EBook(Book):
#     def __init__(self, title, author,size):
#         Book.__init__(self, title, author)
#         self.size = size
#
# class Library:
#     def __init__(self):
#         self.books = []
#
#     def addBook(self, book):
#         self.books.append(book)
#
#     def getNumBooks(self):
#         return len(self.books)
#
#
#
# myBook = EBook('The Odyssey', 'Homer', 2)
# myPaperBook = PaperBook('The Odyssey', 'Homer', 500)
#
# print(myBook.size)
# print(myPaperBook.numPages)
#
# aadl = Library()
# aadl.addBook(myBook)
# aadl.addBook(myPaperBook)
#
# print(aadl.getNumBooks())

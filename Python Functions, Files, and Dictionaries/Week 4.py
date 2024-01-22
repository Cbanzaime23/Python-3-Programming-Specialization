# def sumTo(aBound):
#     """ Return the sum of 1+2+3 ... n """
#
#     theSum  = 0
#     aNumber = 1
#     while aNumber <= aBound:
#         theSum = theSum + aNumber
#         aNumber = aNumber + 1
#     return theSum
#
# print(sumTo(4))
#
# print(sumTo(1000))



# def checkout():
#     """This function outputs a reciept
#     """
#     total = 0
#     count = 0
#     moreItems = True
#     while moreItems:
#         price = float(input('Enter price of item (0 when done): '))
#         if price != 0:
#             count = count + 1
#             total = total + price
#             print('Subtotal: $', total)
#         else:
#             moreItems = False
#     average = total / count
#     print('Total items:', count)
#     print('Total $', total)
#     print('Average price per item: $', average)
#
# checkout()


# def get_yes_or_no(message):
#     valid_input = False
#     while not valid_input:
#         answer = input(message)
#         answer = answer.upper() # convert to upper case
#         if answer == 'Y' or answer == 'N':
#             valid_input = True
#         else:
#             print('Please enter Y for yes or N for no.')
#     return answer
#
# response = get_yes_or_no('Do you like lima beans? Y)es or N)o: ')
# if response == 'Y':
#     print('Great! They are very healthy.')
# else:
#     print('Too bad. If cooked right, they are quite tasty.')
#
# import random
# import turtle
#
#
# def isInScreen(w, t):
#     if random.random() > 0.1:
#         return True
#     else:
#         return False
#
#
# t = turtle.Turtle()
# wn = turtle.Screen()
#
# t.shape('turtle')
# while isInScreen(wn, t):
#     coin = random.randrange(0, 2)
#     if coin == 0:              # heads
#         t.left(90)
#     else:                      # tails
#         t.right(90)
#
#     t.forward(50)
#
# wn.exitonclick()

import random
import turtle

def isInScreen(w,t):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True

    #Check left and right
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    #Check top and bottom
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False

    return stillIn

t = turtle.Turtle()
wn = turtle.Screen()

t.shape('turtle')
while isInScreen(wn,t):
    coin = random.randrange(0, 2)
    if coin == 0:
        t.left(90)
    else:
        t.right(90)

    t.forward(50)

wn.exitonclick()

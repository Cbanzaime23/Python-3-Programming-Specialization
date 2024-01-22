# import turtle
#
# def drawSquare(t, sz):
#     """Make turtle t draw a square of with side sz."""
#
#     for i in range(4):
#         t.forward(sz)
#         t.left(90)
#
#
# wn = turtle.Screen()      # Set up the window and its attributes
# wn.bgcolor("lightgreen")
#
# alex = turtle.Turtle()    # create alex
# drawSquare(alex, 100)      # Call the function to draw the square passing the actual turtle and the actual side size
#
# wn.exitonclick()

def most_common_letter(s):
    frequencies = count_freqs(s)
    return best_key(frequencies)

def count_freqs(st):
    d = {}
    for c in st:
        if c not in d:
             d[c] = 0
        d[c] = d[c] + 1
    return d

def best_key(dictionary):
    ks = dictionary.keys()
    best_key_so_far = list(ks)[0]  # Have to turn ks into a real list before using [] to select an item
    for k in ks:
        if dictionary[k] > dictionary[best_key_so_far]:
            best_key_so_far = k
    return best_key_so_far

print(most_common_letter("abbbbbbbbbbbccccddddd"))

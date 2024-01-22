# def triple(value):
#     return 3*value
#
# def tripleStuff(a_list):
#     new_seq = map(triple, a_list)
#     return list(new_seq)
#
# def quadrupleStuff(a_list):
#     new_seq = map(lambda value: 4*value, a_list)
#     return list(new_seq)
#
# things = [2, 5, 9]
# things3 = tripleStuff(things)
# print(things3)
# things4 = quadrupleStuff(things)
# print(things4)

"""MAP FUNCTION"""
things = [[2, 5, 9],[2, 5, 9]]
things = [2, 5, 9]

things4 = map((lambda value: 4*value), things)
print(list(things4))

# or all on one line
print(list(map((lambda value: 5*value), [1, 2, 3])))



"""FILTER FUNCTION"""
def keep_evens(nums):
    new_seq = filter(lambda num: num % 2 == 0, nums)
    return list(new_seq)

print(keep_evens([3, 4, 6, 7, 0, 1]))



"""LIST COMPREHENSION"""
def keep_evens(nums):
    new_list = [num for num in nums if num % 2 == 0]
    return new_list

print(keep_evens([3, 4, 6, 7, 0, 1,2,3,6,8,7,9,2,3,5]))


things = [3, 4, 6, 7, 0, 1]
#chaining together filter and map:
# first, filter to keep only the even numbers
# double each of them
print(map(lambda x: x*2, filter(lambda y: y % 2 == 0, things)))

# equivalent version using list comprehension
lstComp = [x*2 for x in things if x % 2 == 0])
print(lstComp)



""" Extracting each the value of each "name" key in the "tester" dictionary using the List Comprehension """
tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}

compri = [tester['info'][i]["name"] for i in range(0,6)]




"""Zip"""

L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = []
L4 = list(zip(L1, L2))
#------------
for (x1, x2) in L4:
    L3.append(x1+x2)

print(L3)

#------------
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = [x1 + x2 for (x1, x2) in list(zip(L1, L2))]
print(L3)

#------------
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = map(lambda x: x[0] + x[1], zip(L1, L2))
print(L3)

#------------

L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]

L3 = [x1 + x2 for x1, x2 in zip(L1, L2) if x1 > 10 and x2 < 5]


"""Write code using zip and filter so that these lists (l1 and l2) are combined into one big list and assigned to the variable opposites if they are both longer than 3 characters each.
"""
l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']

opposites = filter(lambda tups: len(tups[0]) > 3 and len(tups[1]) > 3, zip(l1,l2))

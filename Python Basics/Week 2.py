# sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
# 
# 
# last = sports[-3:]
# print(last)
# 
# 
# by = "You are"
# az = "doing a great "
# io = "job"
# qy = "keep it up!"
# 
# 
# message = by + " " + az + io + ", " + qy
# print(message)

# 
# ls = ['run', 'world', 'travel', 'lights', 'moon', 'baseball', 'sea']
# new = ls[2:4]
# print(new)

# l = ['w', '7', 0, 9]
# m = l[1:2]
# print(m)


# 
# b = "My, what a lovely day"
# x = b.split(',')
# print(x)


# b = "My, what a lovely day"
# x = b.split(',')
# z = "".join(x)
# y = z.split()
# a = "".join(y)
# print(a)



# 
# lst = [1,2,3,4,5]
# 
# print(lst.index(5))


lst = ['plan', 'answer', 5, 9.29, 'order, items', [4]]
s = 0
for item in lst:
    if type(item) == type("string"):
        s = s + 1
        
print(s)
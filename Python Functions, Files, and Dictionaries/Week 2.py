product = "iphone and android phones"
lett_d  = {}

for word in product:
    if word in lett_d:
        lett_d[word] = lett_d[word] + 1
    else:
        lett_d[word] = 1

keys = list(lett_d.keys())

max_value = keys[0]
for key in keys:
    if lett_d[key] > lett_d[max_value]:
        max_value = key

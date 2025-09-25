a = [1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5]
d = {}
for i in a:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
print(d)

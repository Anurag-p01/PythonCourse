l = [4, 5, 53,53,233, 989, 57 , 23, 90]
largest = l[0]
index = 0
for i in range (len(l)):
    if l[i] > largest:
        largest = l[i]
        index = i   
print(f"largest number is {largest} and its index is {index}")

l= [4, 5, 53, 53, 233, 989, 57, 23, 90]
largest = l[0]
sec_largest = l[0]
for i in l:
    if i > largest:
        sec_largest = largest
        largest = i
    elif i > sec_largest: 
        sec_largest = i
print(f"Second largest number is {sec_largest}")    
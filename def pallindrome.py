def pallindrome(str):
    rev = ""
    for i in range(len(str)-1, -1, -1):
        rev = rev + str[i]
    if rev == str:
        print("Yes it is Pallindrome")
    else:
        print("Not a Pallindrome")
pallindrome("madam")
pallindrome("hello")

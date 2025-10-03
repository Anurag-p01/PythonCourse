# def addition(**kwargs):
#     print(kwargs)
# addition (a = 12, b = 13, c = 14, d = 15)
    


from multiprocessing.util import info


def addition(**kwargs):
    print("Your information is \n\n")

    for i in kwargs:
        print(f"{i} : {kwargs[i]}")
addition(name="John", age=25, city="New York", country="USA")
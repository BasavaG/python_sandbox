# *args and *kwargs
# normal functions works as per parameters passed in and work correctly when we pass exact number of args when calling
# a function. example

# def add(a, b):  # function takes 2 args
#     return a + b
#
#
# res = add(10, 20)  # calling function with only 2 args, works fine
# #print(res)
#
# #res1 = add(10, 20, 30)  # Throws error because [TypeError: add() takes 2 positional arguments but 3 were given]
# #print(res1)  # So we need to add as many as arguments every time. ahh thats not good.
#
#
# # to overcome above problem use " *args ".
# # *args takes all inputs and store it as tuples.
# def addition(*args):  # * indicates zero or more arguments can be passed
#     print("*args takes inputs as tuple ie ", args)
#     return sum(args)
#
#
# res2 = addition(10, 20, 30, 40, 80, 100, 200) # works perfectly fine now.
# print(res2)
#
# res3 = addition()
# print("when no args are specified result is ", res3)

# def myfunc(*args):
#     mylist = []
#     for x in args:
#         if x % 2 == 0:
#             mylist.append(x)
#         else:
#             pass
#     return mylist
#
#
#
#
# res4 = myfunc(2, 9, 10, 12, 13)
# print(res4)

# case letters

def letters(a):
    mylist1 = []
    for i in range(len(a)): # dont forget range function
        if i % 2 == 0:
            mylist1.append(a[i].lower()) # lower is a method as well as upper
        else :

            mylist1.append(a[i].upper())
    return ''.join(mylist1)

res5 = letters('hello')
print(res5)

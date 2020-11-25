####################################Guruve Namaha#########################
# map() function returns a map object(which is an iterator) of the results after applying the given
# function to each item of a given iterable (list, tuple etc.)
# syntax : map(fun, iter)
# fun : It is a function to which map passes each element of given iterable.
# iter : It is a iterable which is to be mapped.
# NOTE : The returned value from map() (map object) then can be passed to functions like list() (to create a list), set() (to create a set)

def square(num):
    return num**2;

my_num = [1,2,3,4,5]

print(list(map(square,my_num))) # dont use for loop when we have list

def stringoperation(text):
    if len(text)%2 == 0:
        return text
    else:
        return text[0]
mytext = ["raj", "Yamuna", "Hi"]
print(list(map(stringoperation,mytext)))


# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd
# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5

# def lesser_of_two_evens(a, b):
#     if a % 2 == 0 and b % 2 == 0:
#         return min(a, b)
#     else:
#         return max(a, b)
#
#
# #
# #
# res = lesser_of_two_evens(10, 20)
# print("result is -->", res)


# Get your hands dirty :)
# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter¶
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False
# check w3 for more about strings: methods : slice(), strip(), split(), lower(), upper(), in (), not in(), concat(), join(), format() etc

# def animal_crackers(text):
#     list_of_string = text.split(" ")
#     # l = len(list_of_string)
#     # for x in list_of_string:
#     #     if x[0] == list_of_string[0][0]:
#     #         return True
#     #     else:
#     #         return False
#
#     if list_of_string[0][0] == list_of_string[1][0]:
#         return True
#     else:
#         return False
#
#
# res1 = animal_crackers('Levelheaded Lama Li')
# print(res1)


# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False
#
# def makes_twenty(a, b):
#     if (a == 20) or (b == 20) or (a + b == 20):
#         return True
#     else:
#         return False
#
#
# res2 = makes_twenty(12, 8)
# print(res2)


# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald
#
# Note: 'macdonald'.capitalize() returns 'Macdonald'
#
# def old_macdonald(text):
#     # divide the string into two or more part
#     first_half = text[0:3]
#     second_half = text[3:]
#     # capitalize first bit of string to get required output
#     return first_half.capitalize() + second_half.capitalize()
#
#
# print(old_macdonald("basavaraj"))


# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'
#
# Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:
#
# >>> "--".join(['a','b','c'])
# >>> 'a--b--c'
#
# This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a single space string:
#
# >>> " ".join(['Hello','world'])
# >>> "Hello world"
#
# def revestring(text1):
#     textlist = text1.split()  # split the text into words using spaces in between which return list.
#     lengthoftextlist = len(textlist)  # find the lenght of list
#     for i in reversed(
#             range(lengthoftextlist)):  # use reverse function to traverse the list by ranges in reverse direction
#         print(textlist[i], end=" ")  # use end = " " to avoid next line printing
#
#
# revestring("hi hello how are you")
#
# print()


# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True
#
# NOTE: abs(num) returns the absolute value of a number abs(-50) = 50
# Python number method abs() returns absolute value of x - the (positive) distance between x and zero

# def check_num(n):
#     return (abs(100 -n) <=10) or (abs(200 -n) <=10)
#
#
#
# print("result is", check_num(210))
#
# print(abs(250-300))


# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
#
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

def has_nn(mylist):
    mylistlength = len(mylist) - 1  # if you use len(mylist) and traverse you will get list out of index problem.
    for i in range(0, mylistlength):
        if mylist[i] == mylist[i + 1]:
            return True
    # here no else condition because we need to check only one condition. be careful about indentation
    return False


# Guruve Namaha#
res5 = has_nn([1, 2, 3, 4, 4, 5])
print("has nn -->", res5)


# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters¶
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def repeat_letter(text):
    textlenght = len(text)
    for i in range(textlenght):
        for x in range(3):
            print(text[i], end="")


repeat_letter("Mississippi")


# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If
# their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment)
# exceeds 21, return 'BUST'¶ blackjack(5,6,7) --> 18 blackjack(9,9,9) --> 'BUST' blackjack(9,9,11) --> 19

print ()
def blackjack(a, b, c):

    if sum([a,b,c]) <= 21:
        return  sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c]) -10 <=21:  # check the condition for both
        return sum([a,b,c]) -10
    else :
        return "BUST"



res6 = blackjack(9,11,2)

print("the result is ", res6)

# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and
# extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.¶ summer_69([1, 3,
# 5]) --> 9 summer_69([4, 5, 6, 7, 8, 9]) --> 9 summer_69([2, 1, 6, 9, 11]) --> 14

def summer_69(arr):
    arraylength = len(arr)
    for i in range(arraylength ):
        if arr[i] == 6 and arr[i+1] == 9:
            return sum(arr) - 15
        elif 6 and 9 in arr:
            res = 9
        else:
            res = sum(arr)
    return res

res8 = summer_69([4, 5, 6, 7, 8, 9])
print(res8)


# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(arr):
   code = [0,0,7,'x']
   # list containing 0 0 7 and x if values match in given array the pop elements of code and once the code length reaches 1 i mean only'x' then return True
   # as all elements of are present in given array
   for num in arr:
       if num == code[0]:
           code.pop(0)
   return len(code) == 1




res9 = spy_game([1,2,4,0,0,7,5])
print(res9)

# function to find prime numbers
def isprime():
    num = int(input("Enter the number"))
    count =0
    if num >1:
        for i in range(2,num):
            if (num % i) == 0 :
                print("Number is not prime")


        else:
            count += 1



    print(count)

isprime()
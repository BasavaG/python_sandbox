# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2

# def swapcase():
#     print("Enter the string")
#     string = input()
#     for i in string:
#         if i.isupper() == True:
#
#             string= ''.join(i.lower())
#         else:
#             string= ''.join(i.upper())
#     return string

# def swapcase():
#     string = input()
#     return ''.join([i.lower() if i.isupper() else i.upper() for i in string])

#############################################################################################

# def number():
#     sum = 0
#     for i in range(10):
#         print(i)
#         sum += i+2
#     return sum
#
# print(number())

# uisng list
# def swapcase():
#     print("Enter the string")
#     string = list(input()) # Accept string in a list
#     str1 =""  # create empty string
#     print( f"{string} type is {type(string)}")
#     for i in range(len(string)): # traverse list elements one by one
#         if string[i].isupper() == True: # check each index is upper or not
#             string[i]= string[i].lower() # convert to lower if we found string is upper and update in string
#         else:
#             string[i]=string[i].upper() # if element is lower convert it to lower and upadte in string.
#     return str1.join(string) # to convert list to string.
# print(swapcase())
#
# # Convert string to mutable using lists
# string = "abcde"
# l = list(string)
# string
# l[4]
# l[2] = 'z'
# l
# string = " ".join(l)
# string
#
# # Another way is slice the string and join it
# string1 = "BasavarajPrakashGangadhar"
# len(string1)
# # now add spaces between first name and last name
# string1 = string1[:9] + " " + string1[9:16] + " " + string1[16:]
# string1
# Find the substring in given string
def count_substring(string,substring):
    counts= 0
    for i in range(0, len(string)):
        if string[i:].startswith(substring): # string[i:] here traverse all chars and check with substring.
            counts = counts +1
        else:
            pass

    print(counts)


count_substring('abcdabc', 'abc')









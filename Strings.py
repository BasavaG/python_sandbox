############Guruve Namaha################

# def reverse_String():
#     print("Enter the name:")
#     name = input()
#     l = len(name)
#
#     print(name[::-1])
#
# reverse_String()
def reverse_String(s):
    str="" # create a empty string
    # print(str)
    for i in s: # iterate through all chars in the string
        str= i + str # char + empty string ex 1st iteration: h + "", 2nd iteration i + h. total = ih
    print(str)

reverse_String("hi")

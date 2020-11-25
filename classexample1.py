# # primitive datastrucures list, tuple, string, dictionary
# emp = ['raj',10,'7000']
# print(emp)
# print(type(emp))
# # class is :non_primitive
# # class dont have data, its blue print, but it contains atrributes.
# # functions within class is called methods.
# # define class
# class cat:
#     pass
#
#
# # instance(object); real time entity. it contains data.
# # how to create instance
# a= cat()
# print(a)
#
# #attribute
# class cat1:
#     spicies = "Mammal" # class attribute
#     def __init__(self,name,color):
#         self.name = name    # instance variables
#         self.color = color
# a = cat1('jammy', 'black') # assigning values to each instance
# print(a.spicies + " " + a.name + " " + a.color) # accessing class instance values
#
# b = cat1('jammy', 'black') # second instance
#
#
# print(a==b) # checking whether both instances are same.? they are not because both are at different address. each instance of class have distinct address.
#
# # Assigning values
# b.name = "asbc"
# print(b.spicies + " " + b.name + " " + b.color)
# print(b.name)
#
# names =  ('abc','xyz','pwq')
#
#
# print(names)
#

## Guruve Namaha##
# Instance Methods:

class student:
    university_name= "FRA UAS"    # class variables
    def __init__(self,name,rollno): #Initiliase method
        self.name=name    #instance variables
        self.rollno=rollno #

    def read(self,subject): # instance method
        return f"{self.name}  reads {subject}"

    def play(self):
        print(f"{self.name} plays football")


a = student('Pavan', '129890')
a.read('HIS')
a.play()

b = student('raj', '12455')

for student in (a,b):
    print(f"{student.name}'s rollnumber is :  {student.rollno}")

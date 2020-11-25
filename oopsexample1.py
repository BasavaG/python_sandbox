#################Guruve Namaha#############
################################################# Inheritance ##################################################
# Inheritance is the  process of deriving a classes from other classes to reuse code
# Deriving class is called parent class or base class and derived class is called child class.
# child classes inherit the features of parent class and child classes can have their own private features in  terms of methods.
# Below are the examples

class animal():
    # create constuctor
    def __init__(self):
        print("Animal Created when you called me using my instance animal()")

    #Lets create some more features of animal
    def __eat__(self):
        print (" Animal eats ")

    def sleep(self):
        print("Animal  sleeps")


# lets try running the animal class
a1 = animal()
a1.__eat__()
a1.sleep()

# Animal has 2 methods
# eat and sleep
# now any other animals can inherit our class. when it happens our main class becomes parent class.
# example
# creating child classes now

class Dog(animal):  # mentioning animal class in dog class for inheritance
    # create constructor of this class
    def __init__(self):
        # call animal
       # animal.__init__(self)
        print("Dog created")
    def sleep(self):   # override method.
        print("Dog sleeps")
    def bark(self):
        print("Bow-- Bow--")

mydog = Dog() # calling dog instance
mydog.__eat__() # i can call the methods of parent class because i inherited them.
mydog.sleep()   # i am calling overrided method sleep here.

mydog.bark()  # this method only belongs to dog class.

# Multilevel Inheritance class by class by inheritance
# class class1():
# class class2 (class1):
# class class3(class2):
# exmaple

class addition():
    def __init__(self):
        print("Class1 addition class is created")

    def add(self,num1,num2):
        return f"addition of number is {num1+num2}"

obj1 = addition()
obj1.add(20,20)

# create class 2(inherit from class1) with more feature here class1 features with will be inherited

class subtract(addition):
    def __init__(self):
        print("Class2 substract is created")

    def sub(self,num1,num2):
        return f"substraction is {num1-num2}"

obj2=subtract()
print(obj2.add(30,40))
print(obj2.sub(30,70))

# create 3rd class inherit 2nd class here class1 and class2 features are inherited automatically
class multiplicationwithaddsub(subtract):
    def __init__(self):
        print("class3 is created")

    def mul(self,num1,num2):
        return f"multiplication is {num1*num2}"

obj3= multiplicationwithaddsub()
print(obj3.add(20,30)) # add is feature of 1st class
print(obj3.sub(40,20)) # sub is feature of second class
print(obj3.mul(2,7)) # mul is class3 own feature
# in class3 we reduced lot of code

#Multiple Inheritance: many base classes and one child class
# we use this when we want features from different base classes
# example
class addition1():
    def __init__(self):
        print("Class1 addition class is created")

    def add(self,num1,num2):
        return f"addition of number is {num1+num2}"


class subtract1():
    def __init__(self):
        print("Class2 substract is created")

    def sub(self,num1,num2):
        return f"substraction is {num1-num2}"

class multiplication1():
    def __init__(self):
        print("class3 is created")

    def mul(self,num1,num2):
        return f"multiplication is {num1*num2}"
# above are 3 base classes
# below is one child class exracting all features of bases classes

class mathoperation(addition1,subtract1,multiplication1):
    def __init__(self):
        print("this derived class using math operation of add,sub and mul classes.")

# create instance of derived class
obj = mathoperation()
print("addition from base class additio1" + obj.add(20,30))
print("Substraction from base class substract2" + obj.sub(30,10))
print("Multiplication from base class multiplication1" + obj.mul(2,100))

# To check the relationship between classes use issubclass(sub,sup)

res = issubclass(mathoperation,multiplication1)
print(f"is mathoperation subclass of multiplication.?? {res}")

res1 = issubclass(mathoperation,addition)
print(f"is mathoperation subclass of addition.?? {res1}")

# To check the relationship between instances and class
res3 = isinstance(obj,mathoperation)
print(f"is obj is instance of mathoperation class..? {res3}")

from sklearn.model_selection import train_test_split

print("HI")

print("how are you")
#Encapsulation is process of hiding ddata from other classes. using access mmodifier
#Protected members are variables which cannot be accessed outside the class but can be accessed within class and its baseclasses
# we can achieve this using "_" single underscore.
#example
class base:
    def __init__(self):
        self._id=2;

    def display(self):
        print(self._id)

obj4 = base()
obj4.display()

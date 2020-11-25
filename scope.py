# Local Vaiables : Variables inside a function and accessible only inside a function. Global Varibales:  Variables
# outside function and accessible throughout the code. Scope : Scope of variable: to which part of code does variable
# belongs to. Namespace : Python is dynamically types programming language and variables are stored inside a
# "namespace" Python scopes are implemented as dictionaries that map names to objects. These dictionaries are
# commonly called namespaces. These are the concrete mechanisms that Python uses to store names. They’re stored in a
# special attribute called .__dict__. Using the LEGB Rule for Python Scope Local (or function) scope is the code
# block or body of any Python function or lambda expression. This Python scope contains the names that you define
# inside the function. These names will only be visible from the code of the function. It’s created at function call,
# not at function definition, so you’ll have as many different local scopes as function calls. This is true even if
# you call the same function multiple times, or recursively. Each call will result in a new local scope being created.
#
# Enclosing (or nonlocal) scope is a special scope that only exists for nested functions. If the local scope is an
# inner or nested function, then the enclosing scope is the scope of the outer or enclosing function. This scope
# contains the names that you define in the enclosing function. The names in the enclosing scope are visible from the
# code of the inner and enclosing functions.
#
# Global (or module) scope is the top-most scope in a Python program, script, or module. This Python scope contains
# all of the names that you define at the top level of a program or a module. Names in this Python scope are visible
# from everywhere in your code.
#
# Built-in scope is a special Python scope that’s created or loaded whenever you run a script or open an interactive
# session. This scope contains names such as keywords, functions, exceptions, and other attributes that are built
# into Python. Names in this Python scope are also available from everywhere in your code. It’s automatically loaded
# by Python when you run a program or script
import ipython as ipython

%load_ext sql 


x = 50


def func():
    x = 25
    return x


print(x)  # This will return x value as 50. because its in global scope

print(func())  # This will return x value as 25. we are calling method and value inside the method is 25

# How LEGB works:

value = "I am at Global Level (G)"


def func1():
    # value = "I am inside local function (L)"

    def hello():
        # value = "I am enclosed inside the function (E)"
        print(
            "Hi" + value)  # value here checks for enclosed function if no match then checks in local function if no match checks in global scope if
        # no match then finally in built in functions.

    hello()


print(func1())

# How to change the value of variables defined in global scope

x = 50  # Global variable


def inside():
    x = "new value"
    return x


print(x)  # returns 50

x = inside()  # Change the value of global variable x to new x .i.e. local variable value.
print(x)
# We can perform same operation using "global" keyword but its dangerous and good programmer should not use it...
# Difficult to debug: Almost any statement in the program can change the value of a global name.
# Hard to understand: You need to be aware of all the statements that access and modify global names.
# Impossible to reuse: The code is dependent on global names that are specific to a concrete program.
# Good programming practice recommends using local names rather than global names. Here are some tips:
#
# Write self-contained functions that rely on local names rather than global ones.
# Try to use unique objects names, no matter what scope you’re in.
# Avoid global name modifications throughout your programs.
# Avoid cross-module name modifications.
# Use global names as constants that don’t change during your program’s execution.

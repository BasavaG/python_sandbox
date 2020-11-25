import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 0 and 1<n<6:
        print("Not Weird")
    elif n%2==0 and 5<n<21:
        print("Weird")
    elif n%2==0 and n>20:
        print("Not Weird")
    else:
        print("Weird")

print(range(5))
for i in range(5):
    print(i ** 2)


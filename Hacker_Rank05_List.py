##### Guruve Namaha ############
#Consider a list (list = []). You can perform the following commands:
# Sample Input 0
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
#Output#[6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]
from pip._vendor.distlib.compat import raw_input


def list_commands():
    print("Enter number of commands")
    n = int(input())
    l = []

    for _ in range(n):
        s = raw_input().split()
        cmd = s[0]
        args = s[1:]
        if cmd != "print":
            cmd += "(" + ",".join(args) + ")"
            eval("l." + cmd)
        else:
            print(l)



print(list_commands())

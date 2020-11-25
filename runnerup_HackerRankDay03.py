def nestedlist():
    markslist = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        markslist.append([name,score])
    var = sorted(list(set([score for name,score in markslist])))[1]
    print(var)
    print(type(var))
    print("\n".join([a for a,b in sorted(markslist) if b == var] ))

nestedlist()
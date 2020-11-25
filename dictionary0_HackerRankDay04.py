def percentage():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    marks= student_marks[query_name]
    avgmarks= sum(marks) / len(marks)
    print(round(avgmarks, 2))
    print(format(avgmarks, '.2f'))

percentage()
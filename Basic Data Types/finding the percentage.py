if __name__ == '__main__':
    amountStudents = int(input())
    studentMarks = {}
    for i in range(amountStudents):
        name, *line = input().split()
        scores = list(map(float, line))
        studentMarks[name] = scores
    queryStudent = input()

    scoreStudent = studentMarks.get(queryStudent)

    print("%.2f" % (sum(scoreStudent)/len(scoreStudent)))

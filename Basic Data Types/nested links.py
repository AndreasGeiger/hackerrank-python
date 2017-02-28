amountStudents = int(input())
students = []
for i in range(amountStudents):
    students.append([input(),float(input())])

secondLowestStudent = sorted(set([i[1] for i in students]))[1]

print("\n".join(sorted([i[0] for i in students if i[1] == secondLowestStudent])))

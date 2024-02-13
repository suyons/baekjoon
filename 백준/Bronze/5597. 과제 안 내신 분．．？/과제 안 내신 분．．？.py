students = [0 for _ in range(30)]
for i in range(len(students)-2):
    students[i] = int(input())
for i in range(1, len(students) + 1):
    if not students.count(i):
        print(i)
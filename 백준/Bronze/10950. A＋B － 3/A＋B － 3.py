row = int(input())
c = []
for i in range(0, row):
    a, b = [int(e) for e in input().split()]
    c.append(a + b)
for i in c:
    print(i)
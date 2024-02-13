import sys
row = int(sys.stdin.readline())
for i in range(row):
    a, b = [int(e) for e in sys.stdin.readline().split()]
    print(a + b)
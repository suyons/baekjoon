result = []
while True:
    a, b = [int(e) for e in input().split()]
    if(a == 0 and b == 0):
        break
    result.append(a + b)
for i in result:
    print(i)
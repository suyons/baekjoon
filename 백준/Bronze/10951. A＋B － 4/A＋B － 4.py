import sys
result = []
try:
    while True:
        user_input = input().split()
        if not user_input:
            break
        a, b = [int(e) for e in user_input]
        result.append(a + b)
    for i in result:
        print(i)
except EOFError:
    for i in result:
        print(i)
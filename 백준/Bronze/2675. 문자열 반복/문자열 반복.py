count = int(input())
for i in range(count):
    repeat, text = input().split()
    repeat = int(repeat)
    for t in text:
        print(t * repeat, end='')
    print()
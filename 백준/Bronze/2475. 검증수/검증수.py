serial = [int(e) for e in input().split()]
parity = 0
for i in serial:
    parity += i ** 2
print(parity % 10)
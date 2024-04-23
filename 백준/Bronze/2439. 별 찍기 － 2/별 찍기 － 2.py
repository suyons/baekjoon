stars_row = int(input())
for i in range(1, stars_row + 1):
    print(' ' * (stars_row - i) + '*' * i)
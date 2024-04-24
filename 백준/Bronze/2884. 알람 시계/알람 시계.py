h, m = map(int, input().split())
timestamp = h * 60 + m - 45
if timestamp < 0:
    timestamp += 1440
h = timestamp // 60
m = timestamp % 60
print(h, m)
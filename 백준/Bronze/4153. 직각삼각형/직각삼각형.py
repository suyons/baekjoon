def is_right_triangle(a, b, c):
    cond_1 = a > 0 and b > 0 and c > 0
    cond_2 = a**2 + b**2 == c**2
    if cond_1 and cond_2:
        print("right")
    if not cond_1:
        return
    if not cond_2:
        print("wrong")


if __name__ == "__main__":
    while True:
        a, b, c = sorted(map(int, input().split()))
        is_right_triangle(a, b, c)
        if a == 0 and b == 0 and c == 0:
            break

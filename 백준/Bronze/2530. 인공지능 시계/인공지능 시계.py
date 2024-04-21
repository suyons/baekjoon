def time_format(t):
    h = t // 3600
    m = t % 3600 // 60
    s = t % 60
    return h, m, s

def time_unformat(h, m, s):
    return h * 3600 + m * 60 + s

if __name__ == '__main__':
    h, m, s = map(int, input().split())
    start = time_unformat(h, m, s)
    duration = int(input())
    end = start + duration
    if end >= 86400:
        end -= 86400 * (end // 86400)
    h, m, s = time_format(end)
    print(h, m, s)
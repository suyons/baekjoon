if __name__ == '__main__':
    numlist = []
    for i in range(9):
        num = int(input())
        numlist.append(num)
    max_value = max(numlist)
    max_index = numlist.index(max_value) + 1
    print(f"{max_value}\n{max_index}")
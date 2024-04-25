test_case = int(input())
for i in range(test_case):
    score = input()
    total_score = 0
    score_count = 0
    for s in score:
        if s == 'O':
            score_count += 1
            total_score += score_count
        else:
            score_count = 0
    print(total_score)
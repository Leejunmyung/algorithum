lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]

def solution(lotto, win_num):
    answer = []
    collect_num = [0,0]

    for i in lotto:
        for j in win_num:
            if i == j:
                collect_num[0] += 1
        if i == 0:
            collect_num[0] += 1

    for i in lotto:
        for j in win_num:
            if i == j:
                collect_num[1] += 1

    for i in collect_num:
        if i == 6:
            answer.append(1)
        elif i == 5:
            answer.append(2)
        elif i == 4:
            answer.append(3)
        elif i == 3:
            answer.append(4)
        elif i == 2:
            answer.append(5)
        else:
            answer.append(6)


    return answer




result = solution(lottos, win_nums)
print(result)


input = [1,3,2]
output = [1,2,3]


def solution(enter, leave):
    answer = []
    for index in range(len(enter)):
        in_human = enter[index]
        for n in range(len(leave)):
            out_human = leave[n]
            if in_human == out_human:
                answer.append(0)



result = solution(input, output)
print(result)

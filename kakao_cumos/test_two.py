gift = [5, 4, 5, 4, 5]
wants = [1, 2, 3, 5, 4]


def solution(gifts, want):
    index = 0
    answer = 0
    while index < len(gifts):
        if gifts[index] != want[index]:
            for i in range(index,len(want)):
                if gifts[index] == want[i]:
                    want[index], want[i] = want[i], want[index]
                    index += 1
                else:
                    answer += 1
                    index += 1
        else:
            index += 1



        return answer


result = solution(gift, wants)
print(result)


total_dict = {}

while True:
    question = input("질문을 입력해주세요 : ")

    if question == "q":
        break
    else:
        total_dict[question] = ""

print(total_dict)

for i in total_dict:
    print(i)
    answer = input("답변을 입력해주세요 : ")

    total_dict[i] = answer

print(total_dict)

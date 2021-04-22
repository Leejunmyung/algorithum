input = "AaTa+!12-3"



def solution(inp_str):
    answer = []
    up = ["A","B","C","D","E","F","G","H","I","J","K","L",
          "M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    down = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                      "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                      "u", "v", "w", "x", "y", "z"]
    number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    special = ["~", "!", "@", "#", "$", "%", "^", "&", "*"]
    all = [up,down,number,special]
    if 15 >= len(inp_str) >= 8:
        for char in inp_str:
            if char not in up and down and number and special:
                return answer.append(2)
            for
    else:
         answer.append(1)


result = solution(input)
print(result)
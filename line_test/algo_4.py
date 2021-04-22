prog = "line"
flag_rule = ["-s STRING", "-n NUMBER", "-e NULL"]
command = ["line -n 100 -s hi -e", "lien -s Bye"]

def solution(program, flag_rules, commands):
    answer = []
    for command in commands:
        if command.split(" ")[0] == program:
            return True




result = solution(prog, flag_rule, command)
print(result)

all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]



def get_absent_student(all_array, present_array):
    student_dicts = {}

    for key in all_array:
        student_dicts[key] = True

    for key in present_array:
        del student_dicts[key]

    for key in student_dicts.keys():
        return key

    return


print(get_absent_student(all_students, present_students))
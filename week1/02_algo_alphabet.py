def find_alphabet_occurrence_array(string):
    alphabet_ouccurrence_array = [0]*26

    for char in string:
        if not char.isalpha():
            continue
        alphabet_array = ord(char)-ord("a")
        alphabet_ouccurrence_array[alphabet_array] += 1
    return alphabet_ouccurrence_array

print(find_alphabet_occurrence_array("hello my name is sparta"))
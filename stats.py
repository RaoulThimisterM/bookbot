def number_of_words(file_path):
    file_contents = file_path.split()
    return len(file_contents)


def number_of_unique_characters(file_path):
    lower_case_string = file_path.lower()
    unique_characters = {}
    for character in lower_case_string:
        if character in unique_characters:
            unique_characters[character] += 1
        elif character not in unique_characters:
            unique_characters[character] = 1
    return unique_characters

def sorted_number_of_unique_characters(char_dict):
    list_of_dict = []
    for unique_character in char_dict:
        temp_dict = {"char": unique_character, "num": char_dict[unique_character]}
        list_of_dict.append(temp_dict)
    #return list_of_dict.sort(reverse=True, key=lambda x: x["num"])
    return sorted(list_of_dict, key=lambda x: x["num"], reverse=True)
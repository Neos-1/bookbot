def sort_on(dict):
    for dict_item in dict:
        return dict[dict_item]

def get_num_words(text_from_book):
    words = text_from_book.split()
    num_words = 0
    for word in words:
        num_words += 1
    return print (f"Found {num_words} total words")

def get_num_characters(text_from_book):
    text_lowered = text_from_book.lower()
    characters_dict = {}
    for character in text_lowered:
        if character.isalpha():
            if character in characters_dict:
                characters_dict[character] += 1
            else:
                characters_dict[character] = 1
    return characters_dict
        
def sorted_list_of_dict(list_of_dict):
    new_list_of_dict = []
    for a in list_of_dict:
        temp_dict = {}
        b = list_of_dict[a]
        temp_dict[a] = b
        new_list_of_dict.append(temp_dict)

    new_list_of_dict.sort(reverse=True, key=sort_on)

    for dict in new_list_of_dict:
        for item in dict:
            character = item
            number = dict[item]
            print(f"{character}: {number}")

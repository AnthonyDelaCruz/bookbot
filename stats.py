def count_words(string):
    split_words = string.split()
    return len(split_words)

def count_chars(string):
    char_count = {}
    for char in string:
        lowercased_char = char.lower()
        if lowercased_char in char_count:
            char_count[lowercased_char] += 1
        else:
            char_count[lowercased_char] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

def sort_dict_by_count(dict):
    list = []
    for item in dict:
            list.append({"char": item, "num": dict[item]})
    list.sort(key=sort_on, reverse=True)

    return list
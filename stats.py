def count_words(text):
    number_words = len(text.split())
    return number_words

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def chars_list(chars_dict):
    dict_list = []
    for char in chars_dict:
        dict_list.append({"char": char, "num": chars_dict[char]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def sort_on(items):
    return items["num"]

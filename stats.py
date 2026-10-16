def get_num_words(text):
    return len(text.split())


def sort_on(items):
    return items["num"]


def char_freq(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        chars[lowered] = chars.get(lowered, 0) + 1
    return chars


def get_sorted_list(chars_dict):
    sorted_list = []
    for char in chars_dict:
        # Only this line should be inside the loop
        sorted_list.append({"char": char, "num": chars_dict[char]})

    # These must be outside the loop (back one level of indentation)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

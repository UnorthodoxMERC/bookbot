def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    count = {}
    char_text = text.lower()
    
    for i in char_text:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    return count

def sorted_print(char_dict):
    chars_list = []

    for char, count in char_dict.items():
        char_dict = {"char": char, "count": count}
        chars_list.append(char_dict)

    def sort_on(dict):
        return dict["count"]
    
    chars_list.sort(reverse=True, key=sort_on)       


    return chars_list
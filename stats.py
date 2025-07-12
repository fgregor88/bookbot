def get_text(file_path):
    with open(file_path) as f:
        return f.read()

def get_num_words(file_path):
    text = get_text(file_path)
    return len(text.split())

def sort_on(items):
    return items["num"]

def count_characters(file_path):
    text = get_text(file_path)
    text = text.lower()
    char_dic = {}
    counter = 0
    for c in text:
        if c not in char_dic:
            char_dic[c] = 1
        else:
            char_dic[c] = char_dic[c] + 1

    result = [{'char': k, 'num': v} for k, v in char_dic.items()]

    result.sort(reverse=True, key=sort_on)

    return result

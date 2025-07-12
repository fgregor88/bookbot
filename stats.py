def get_text(file_path):
    with open(file_path) as f:
        return f.read()

def get_num_words(file_path):
    text = get_text(file_path)
    return len(text.split())

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

    for entry in char_dic:
        print(f"'{entry}': {char_dic[entry]}")

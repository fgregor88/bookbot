from stats import get_num_words, count_characters

def main():
    path = "books/frankenstein.txt"
    num_words = (get_num_words(path))
    # report output
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_dic = count_characters(path)
    for entry in char_dic:
        char = entry['char']
        value = entry['num']
        if char.isalpha():
            print(f"{char}: {value}")



main()

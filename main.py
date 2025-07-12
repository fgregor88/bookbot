from stats import get_num_words, count_characters
import sys

def main():
    if(len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    for path in sys.argv[1:]:
        num_words = (get_num_words(path))
        # report output
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
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

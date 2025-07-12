from stats import get_num_words, count_characters

def main():
    path = "books/frankenstein.txt"
    num_words = (get_num_words(path))
    print(f"{num_words} words found in the document")

    count_characters(path)


main()

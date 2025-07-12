def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def word_count(text):
    return len(text.split())

def main():
    path = "books/frankenstein.txt"
    num_words = (word_count(get_book_text(path)))
    print(f"{num_words} words found in the document")


main()

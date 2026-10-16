import sys
from stats import get_num_words, char_freq, get_sorted_list


def get_book_text(rel_path):
    with open(rel_path, "r") as f:
        text = f.read()
        print(text)
        return text


def main():
    args = sys.argv
    if not len(args) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = args[1]
    # path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_num_words(text)

    counts_dicts = char_freq(text)
    sorted_chars = get_sorted_list(counts_dicts)

    print("============ BOOKBOT ============\n")
    print(f"Analyzing book found at {path}...\n")
    print("----------- Word Count ----------\n")
    print(f"Found {num_words} total words\n")
    print("--------- Character Count -------\n")

    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()

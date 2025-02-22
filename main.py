import sys

try:
    path_to_book = sys.argv[1]
except Exception as e:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import get_num_words
from stats import get_num_characters
from stats import sorted_list_of_dict

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    get_num_words(get_book_text(path_to_book))
    print("--------- Character Count -------")
    sorted_list_of_dict(get_num_characters(get_book_text(path_to_book)))
    print("============= END ===============")

main()
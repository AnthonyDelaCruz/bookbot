from stats import count_words, count_chars, sort_dict_by_count
from sys import argv, exit

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    path_to_file = argv[1]
    contents = get_book_text(path_to_file)
    word_count = count_words(contents) 
    char_count_dict = count_chars(contents)
    sorted_chars_list = sort_dict_by_count(char_count_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("------------ Word Count ------------")
    print(f"Found {word_count} total words")
    print("------------ Character Count ------------")
    for char_item in sorted_chars_list:
        if char_item["char"].isalpha():
            print(f"{char_item["char"]}: {char_item["num"]}")

main()
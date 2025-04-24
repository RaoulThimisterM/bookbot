from stats import number_of_words, number_of_unique_characters, sorted_number_of_unique_characters
import sys

def get_book_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        file_contents = f.read()
    return file_contents


def main():
    file_path = sys.argv[1]
    number_of_word = number_of_words(get_book_text(file_path))
    unique_characters = number_of_unique_characters(get_book_text(file_path))
    unique_characters_sorted = sorted_number_of_unique_characters(unique_characters)
    print("============ BOOKBOT ============" )
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_word} total words")
    print("--------- Character Count -------")
    for unique_character in unique_characters_sorted:
        if unique_character["char"].isalpha():
            print(f" {unique_character["char"]}: {unique_character["num"]}")
    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main()
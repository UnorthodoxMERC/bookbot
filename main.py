from stats import word_count, char_count, sorted_print
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        

    return file_contents

def main():
    file_contents = get_book_text(sys.argv[1])
    num_words = word_count(file_contents)
    character_count = char_count(file_contents)
    
    # Assuming you have a dictionary called char_counts
    sorted_chars = sorted_print(character_count)

    # Print the report header
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    # Print each character and its count
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        # Only print alphabetical characters
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

main()
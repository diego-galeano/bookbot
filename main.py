from stats import get_num_words
from stats import get_dic_letter_counter
import sys

def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {get_num_words(sys.argv[1])} total words")	
        print("--------- Character Count -------")
        dict_char_count = get_dic_letter_counter(sys.argv[1])
        for char in dict_char_count:
            print(f"{char['char']}: {char['num']}")

main()

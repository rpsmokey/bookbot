from stats import count_words, get_chars_dict, chars_list

def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    number_words = count_words(text)
    chars_dict = get_chars_dict(text)
    sorted_chars = chars_list(chars_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path[2:]}...")
    print("----------- Word Count ----------")
    print(f"Found {number_words} total words")
    print("--------- Character Count -------")
    
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
            
    print("============= END ===============")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents
    
main()

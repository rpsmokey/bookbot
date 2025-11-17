from stats import count_words, get_chars_dict

def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    number_words = count_words(text)
    chars_dict = get_chars_dict(text)
    print(f"Found {number_words} total words, {chars_dict}")
    #print(chars_dict)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents
    
main()

def main():
    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    print(get_num_words(text))


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)
    
main()
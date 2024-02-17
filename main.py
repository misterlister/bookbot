def main():
    book_path = get_book_path()
    text = get_book_text(book_path)
    if text is not None:
        make_report(book_path, text)

def get_book_path():
    path = input("Please enter the path to the book you wish to analyze (eg. books/frankenstein.txt): ")
    return path

def get_book_text(path):
    try:
        with open(path) as f:
            return f.read()
    except:
        print("Error. That is not a valid book path.")
        return None

def get_num_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_count = {}
    for letter in text:
        lower_letter = letter.lower()
        if lower_letter not in letter_count:
            letter_count[lower_letter] = 0
        letter_count[lower_letter] += 1
    return letter_count
def make_report(path, text):
    num_words = get_num_words(text)
    character_count = count_letters(text)
    sorted_count = dict(sorted(character_count.items(), key = lambda x:x[1], reverse = True))
    letter_count = []
    for character in sorted_count:
        if character.isalpha():
            letter_count.append(character)
            letter_count.append(sorted_count[character])
    count_formatted = ""
    for i in range (0, len(letter_count), 2):
        count_formatted += f"The character '{letter_count[i]}' appears {letter_count[i+1]} times\n"
    print(f"\n--- Report of {path} ---\n")
    print(f"There are {num_words} words in this document")
    print(count_formatted)
    print("--- End of report ---\n")
    
main()
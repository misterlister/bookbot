max_top_words = 100
lg_border = "---"
sm_border = "-"

def main():
    book_path = get_book_path()
    text = get_book_text(book_path)
    if text is not None:
        make_report(book_path, text)

def get_book_path():
    path = input("Please enter the path to the book you wish to analyze (eg. books/Frankenstein.txt): ")
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

def count_of_each_word(text):
    words = text.split()
    word_count = {}
    for word in words:
        first_letter = word[0].lower()
        if len(word) > 1:
            entry = first_letter + word[1:]
        else:
            entry = first_letter
        if entry not in word_count:
            word_count[entry] = 0
        word_count[entry] += 1
    return word_count

def count_letters(text):
    letter_count = {}
    for letter in text:
        lower_letter = letter.lower()
        if lower_letter not in letter_count:
            letter_count[lower_letter] = 0
        letter_count[lower_letter] += 1
    return letter_count

def sorted_dict(dictionary):
    return dict(sorted(dictionary.items(), key = lambda x:x[1], reverse = True))

def filter_top_words(dictionary, filter_number):
    word_list = []
    actual_filter_number = 0
    for word in dictionary:
        word_list.append(word)
        word_list.append(dictionary[word])
        actual_filter_number += 1
        if len(word_list) >= (filter_number * 2):
            return word_list, actual_filter_number
    return word_list, actual_filter_number

def filter_non_alpha(dictionary) -> list:
    alpha_list = []
    for character in dictionary:
        if character.isalpha():
            alpha_list.append(character)
            alpha_list.append(dictionary[character])
    return alpha_list

def format_count(count_list, count_type) -> str:
    formatted = ""
    for i in range (0, len(count_list), 2):
        formatted += f"The {count_type} '{count_list[i]}' appears {count_list[i+1]} times\n"
    return formatted

def make_report(path, text):
    num_words = get_num_words(text)

    all_words_count = count_of_each_word(text)
    sorted_words = sorted_dict(all_words_count)
    top_words, top_word_num = filter_top_words(sorted_words, max_top_words)
    words_formatted = format_count(top_words, "word")

    all_character_count = count_letters(text)
    sorted_count = sorted_dict(all_character_count)
    letter_count = filter_non_alpha(sorted_count)
    letter_formatted = format_count(letter_count, "character")

    print(f"\n{lg_border} Report of {path} {lg_border}\n")
    print(f"There are {num_words} words in this document\n")
    print(f"{sm_border} Top {top_word_num} words in this document {sm_border}\n")
    print(words_formatted)
    print(f"{sm_border} Character count {sm_border}\n")
    print(letter_formatted)
    print(f"{lg_border} End of report {lg_border}\n")
    
main()
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = text.split()
    print(f"--- Begin report of {book_path} ---")
    print(f"{len(words)} words found in the document")
    print(f"\n")
    characters = get_number_characters(words)
    sorted_list = sort_report(characters)
    for item in sorted_list:
        print(f"The '{item['name']}' character was found {item['num']} times")
    print("--- End Report ---")
        
def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_number_characters(words):
    total = {}
    for word in words:
        for letter in word:
            if letter.isalpha():
                if letter.lower() in total:
                    total[letter.lower()] = total[letter.lower()] +1
                else:
                    total[letter.lower()] = 1
    return total

def sort_on(dict):
    return dict['num']


def sort_report(letters_dict):
    dict_list = []
    sorted_list = []
    for letter in letters_dict:
        dict_list.append({"name": letter, "num":letters_dict[letter]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

main()

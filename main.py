from stats import count_words
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    file_contents = open_book(path_to_book)
    print(f"{count_words(file_contents)} words found in the document\n")
    alphabet_report(count_letters(file_contents))

def output_text(text):
    print(text)



def count_letters(string):
    count_dict = {}
    for character in string.lower():
        if character in count_dict:
            count_dict[character] += 1
        else:
            count_dict[character] = 1
    return count_dict

def open_book(path):
    with open(path) as f:
        return f.read()
    
def alphabet_report(dictionary):
    for d in sorted(dictionary.keys()):
        if d.isalpha():
            print(f"{d}: {dictionary[d]}")

main()
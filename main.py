def main():
    path_to_book = "books/frankenstein.txt"
    file_contents = open_book(path_to_book)
    print(f"{count_words(file_contents)} words found in the document\n")
    alphabet_report(count_letters(file_contents))

def output_text(text):
    print(text)

def count_words(text):
    words = text.split()
    return len(words)

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
            print(f"The '{d}' character was found {dictionary[d]} times")

main()
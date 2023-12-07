def main():
    book_path = "github.com/LeVperda/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    get_report(book_path, text)

def get_letter_count(text):
    text = text.lower()
    letters = {}

    for x in text:
        if x not in letters.keys():
            letters[x] = 1
        if x in letters.keys():
            letters[x] += 1
    
    return letters

def get_report(book_path, text):
    print(f"--- Begin report of {book_path} ---")

    num_words = get_num_words(text)
    print(f"{num_words} words found in the document\n")
    
    chars = get_letter_count(text)
    lst_chars = []
    for x in chars:
        if x.isalpha():
            lst_chars.append({"char": x, "num": chars[x]})

    lst_chars = sorted(lst_chars, key=lambda char: -char["num"])
    
    for each in lst_chars:
            print(f"The '{each['char']}' character was found {each['num']} times")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()
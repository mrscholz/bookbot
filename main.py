from stats import get_book_text, count_words, count_chars, print_report

def main():
    url = "./books/frankenstein.txt"
    text = get_book_text(url)
    words = count_words(text)
    char_count = count_chars(text)
    print_report(url, words, char_count)



if __name__ == "__main__":
    main()

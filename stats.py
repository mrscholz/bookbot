def get_book_text(url: str):
    text = ""
    with open(url) as f:
        text = f.read()
    return text

def count_words(text: str):
    words = text.split()
    return len(words)


def count_chars(text: str):
    char_count = {}
    text = text.lower()
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else: 
            char_count[char] = 1
    return char_count


def sort_on(items):
    return items["num"]


def create_char_count_list(char_count: dict[str, int]):
    char_count_list = []
    for key, val in char_count.items():
        temp_dict = {"char": key, "num": val}
        char_count_list.append(temp_dict)
    char_count_list.sort(reverse=True, key=sort_on)
    return char_count_list


def print_report(url: str, words: int, char_count: dict[str, int]):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {url}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    char_count_list = create_char_count_list(char_count)
    for char_dict in char_count_list:
        if char_dict["char"].isalpha():
            print(f"{char_dict["char"]}: {char_dict["num"]}")
    print("--------------- End -------------")



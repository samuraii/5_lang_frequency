
from collections import Counter


def load_text_file():
    path_to_text_file = input('Input path to file: ')
    with open(path_to_text_file, 'r') as f:
        return f.read()


def get_most_frequent_words(text, counter):
    return dict(Counter(text.lower().split()).most_common(counter))


if __name__ == '__main__':
    text_from_file = load_text_file()
    print(get_most_frequent_words(text_from_file, 10))

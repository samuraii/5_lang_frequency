import sys
import re
from collections import Counter


def load_text_file(path_to_file):
    with open(path_to_file, 'r') as f:
        return re.sub(r'[^\w\s]', '', f.read().lower())


def get_most_frequent_words(text):
    top_words = 10
    return dict(Counter(text.lower().split()).most_common(top_words))


if __name__ == '__main__':
    text_from_file = load_text_file(sys.argv[1])
    print('10 most fequnent words in given file:')
    print(get_most_frequent_words(text_from_file))

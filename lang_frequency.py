
# -*- coding: utf-8 -*-
from collections import Counter


def load_data(filepath):
    with open(filepath, 'r') as f:
        return f.read()


def get_most_frequent_words(text):
    return dict(Counter(text.lower().split()).most_common(10))


if __name__ == '__main__':
    text_from_file = load_data('Hamlet.txt')
    print(get_most_frequent_words(text_from_file))

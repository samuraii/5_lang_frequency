import sys
from collections import Counter


def load_data_from_file(filepath):
    try:
        with open(filepath) as data_file:
            return data_file.read()
    except IOError:
        print('There is no such file.')


def get_most_frequent_words(text):
    top_words = 10
    return dict(Counter(text.lower().split()).most_common(top_words))


if __name__ == '__main__':
    try:
        path_to_file = sys.argv[1]
        data_from_file = load_data_from_file(path_to_file)
        frequent_words = get_most_frequent_words(data_from_file)
        print('10 frequent words in the file:\n{}'.format(frequent_words))
    except IndexError:
        print('Missing arguments to script.')

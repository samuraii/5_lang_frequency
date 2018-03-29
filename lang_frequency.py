import sys
import re
from collections import Counter


def load_text_file(path_to_file):
    with open(path_to_file, 'r') as file_data:
        return file_data.read().lower()


def filter_text(raw_text):
    return re.sub(r'[^\w\s]', '', raw_text)


def get_most_frequent_words(text, words_count=10):
    return Counter(text.split()).most_common(words_count)


def display_words(words):
    print('#', 'count', 'word')
    for number, (word, amount) in enumerate(words):
        print('{0:<1} {1:^6} {2}'.format(number, word, amount))

if __name__ == '__main__':
    try:
        raw_text = load_text_file(sys.argv[1])
    except IndexError:
        exit('File not passed to script.')
    except FileNotFoundError:
        exit('File not found.')

    filtered_text = filter_text(raw_text)
    words_count = get_most_frequent_words(filtered_text)
    display_words(words_count)

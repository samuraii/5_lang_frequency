import sys
import re
from collections import Counter


def load_text_file(path_to_file):
    with open(path_to_file, 'r') as file_data:
        return file_data.read()


def remove_punctuation(raw_text):
    return re.sub(r'[^\w\s]', '', raw_text)


def get_most_frequent_words(text, words_count=10):
    return Counter(text.lower().split()).most_common(words_count)


def print_words(words):
    print('#', 'word', 'count')
    for number, (word, amount) in enumerate(words, 1):
        print('{0:<1} {1:^6} {2}'.format(number, word, amount))

if __name__ == '__main__':
    try:
        raw_text = load_text_file(sys.argv[1])
    except IndexError:
        exit('File not passed to script.')
    except FileNotFoundError:
        exit('File not found.')
    except UnicodeDecodeError:
        exit('File encoding is not UTF-8')

    text_without_punctuation = remove_punctuation(raw_text)
    words_count = get_most_frequent_words(text_without_punctuation)
    print_words(words_count)

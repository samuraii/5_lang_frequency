import sys
import re
from collections import Counter


def load_text_file(path_to_file):
    with open(path_to_file, 'r') as file_data:
        return re.sub(r'[^\w\s]', '', file_data.read().lower())


def get_most_frequent_words(text):
    top_words = 10
    return Counter(text.split()).most_common(top_words)


if __name__ == '__main__':
    try:
        text = load_text_file(sys.argv[1])
        words = get_most_frequent_words(text)
        print('Кол-во', 'Слово')
        for word in words:
            print('{0:^6} {1}'.format(word[1], word[0]))
    except IndexError:
        print('Для корректной работы нужно передать файл.')
    except FileNotFoundError:
        print('Файл не найден.')

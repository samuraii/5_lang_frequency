# Frequency Analysis of Words

This program allows to analyze word frequency in text file. Can be used with any language as long as text file is encoding is 'utf-8'

# Example of usage

```python
import lang_frequency as lf

text_from_file = lf.load_data('Hamlet.txt')
print(lf.get_most_frequent_words(text_from_file))
```

Output:
```bash
{'the': 1101, 'and': 912, 'to': 752, 'of': 692, 'a': 542, 'i': 532, 'you': 512, 'my': 503, 'in': 401, 'it': 368}
```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

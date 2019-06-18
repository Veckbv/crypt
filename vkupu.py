from collections import Counter
import re

with open('/home/jimbo/Загрузки/ciphertext', 'r') as f:
    text = f.read()

letter_frequency = Counter(re.findall(r'(?=([a-zA-Z]{1}))', text)).most_common()

count_letter = sum(j for i, j  in letter_frequency)
letter_frequency = [(_[0], _[1] / count_letter * 100) for _ in                                                                     letter_frequency]

bigrams = re.findall(r'(?=([a-zA-Z]{2}))', text)
most_frequinct_bigrams = Counter(bigrams).most_common()[:10]
trigrams = re.findall(r'(?=([a-zA-Z]{3}))', text)
most_frequinct_trigrams = Counter(trigrams).most_common()[:10]

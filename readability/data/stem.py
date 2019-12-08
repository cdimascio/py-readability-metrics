import os
from nltk.stem.porter import PorterStemmer

porter_stemmer = PorterStemmer()

file = 'spache_easy.txt'
cur_path = os.path.dirname(os.path.realpath(__file__))
dale_chall_path = os.path.join(cur_path, file)
words = None
with open(dale_chall_path) as f:
    words = list(line.strip() for line in f)

for w in words:
    print(porter_stemmer.stem(w))

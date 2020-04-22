import os
import re
from .syllables import count as count_syllables
from nltk.tokenize import sent_tokenize, TweetTokenizer
from nltk.stem.porter import PorterStemmer


class AnalyzerStatistics:
    def __init__(self, stats):
        self.stats = stats

    @property
    def num_poly_syllable_words(self):
        return self.stats['num_poly_syllable_words']

    @property
    def num_syllables(self):
        return self.stats['num_syllables']

    @property
    def num_letters(self):
        return self.stats['num_letters']

    @property
    def num_words(self):
        return self.stats['num_words']

    @property
    def num_sentences(self):
        return self.stats['num_sentences']

    @property
    def num_gunning_complex(self):
        return self.stats['num_gunning_complex']

    @property
    def num_dale_chall_complex(self):
        return self.stats['num_dale_chall_complex']

    @property
    def num_spache_complex(self):
        return self.stats['num_spache_complex']

    @property
    def avg_words_per_sentence(self):
        return self.num_words / self.num_sentences

    @property
    def avg_syllables_per_word(self):
        return self.num_syllables / self.num_words

    def __str__(self):
        return str(self.stats) + \
            ", avg_words_per_sentence " + str(self.avg_words_per_sentence) + \
            ", avg_syllables_per_word " + str(self.avg_syllables_per_word)


class Analyzer:
    def __init__(self):
        pass

    def analyze(self, text):
        self._dale_chall_set = self._load_dale_chall()
        self._spache_set = self._load_spache()
        stats = self._statistics(text)
        self.sentences = stats['sentences']  # hack for smog
        return AnalyzerStatistics(stats)

    def _statistics(self, text):
        tokens = self._tokenize(text)
        syllable_count = 0
        poly_syllable_count = 0
        word_count = 0
        letters_count = 0
        gunning_complex_count = 0
        dale_chall_complex_count = 0
        spache_complex_count = 0
        porter_stemmer = PorterStemmer()

        def is_gunning_complex(t, syllable_count):
            return syllable_count >= 3 and \
                not (self._is_proper_noun(t) or
                     self._is_compound_word(t))

        def is_dale_chall_complex(t):
            stem = porter_stemmer.stem(t.lower())
            return stem not in self._dale_chall_set

        def is_spache_complex(t):
            stem = porter_stemmer.stem(t.lower())
            return stem not in self._spache_set

        for t in tokens:

            if not self._is_punctuation(t):
                word_count += 1
                word_syllable_count = count_syllables(t)
                syllable_count += word_syllable_count
                letters_count += len(t)
                poly_syllable_count += 1 if word_syllable_count >= 3 else 0
                gunning_complex_count += \
                    1 if is_gunning_complex(t, word_syllable_count) \
                    else 0
                dale_chall_complex_count += \
                    1 if is_dale_chall_complex(t) else 0
                spache_complex_count += \
                    1 if is_spache_complex(t) else 0

        sentences = self._tokenize_sentences(text)
        sentence_count = len(sentences)

        return {
            'num_syllables': syllable_count,
            'num_poly_syllable_words': poly_syllable_count,
            'num_words': word_count,
            'num_sentences': sentence_count,
            'num_letters': letters_count,
            'num_gunning_complex': gunning_complex_count,
            'num_dale_chall_complex': dale_chall_complex_count,
            'num_spache_complex': spache_complex_count,
            'sentences': sentences,
        }

    def _tokenize_sentences(self, text):
        return sent_tokenize(text)

    def _tokenize(self, text):
        tokenizer = TweetTokenizer()
        return tokenizer.tokenize(text)

    def _is_punctuation(self, token):
        match = re.match('^[.,\/#!$%\'\^&\*;:{}=\-_`~()]$', token)
        return match is not None

    def _is_proper_noun(self, token):
        # pos = pos_tag(token)[0][1]
        # return pos == 'NNP'
        return token[0].isupper()

    def _is_compound_word(self, token):
        return re.match('.*[-].*', token) is not None

    def _load_dale_chall(self):
        file = 'dale_chall_porterstem.txt'
        cur_path = os.path.dirname(os.path.realpath(__file__))
        dale_chall_path = os.path.join(cur_path, '..', 'data', file)
        with open(dale_chall_path) as f:
            return set(line.strip() for line in f)

    def _load_spache(self):
        file = 'spache_easy_porterstem.txt'
        cur_path = os.path.dirname(os.path.realpath(__file__))
        spache_path = os.path.join(cur_path, '..', 'data', file)
        with open(spache_path) as f:
            return set(line.strip() for line in f)

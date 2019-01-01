import re
from .syllables import count as count_syllables
from nltk.tokenize import sent_tokenize, TweetTokenizer
# from nltk.tag import pos_tag


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
    def __init__(self, text):
        stats = self._statistics(text)
        self.statistics = AnalyzerStatistics(stats)

    def _tokenize_sentences(self, text):
        return sent_tokenize(text)

    def _tokenize(self, text):
        tokenizer = TweetTokenizer()
        return tokenizer.tokenize(text)

    def _is_punctuation(self, token):
        match = re.match('^[.,\/#!$%\'\^&\*;:{}=\-_`~()]$', token)
        return match is not None

    def _statistics(self, text):
        tokens = self._tokenize(text)
        syllable_count = 0
        poly_syllable_count = 0
        word_count = 0
        letters_count = 0
        gunning_complex_count = 0

        def is_gunning_complex(t, syllable_count):
            return syllable_count >= 3 and \
                not (self._is_proper_noun(t) or
                     self._is_compound_word(t))

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

        sentence_count = len(self._tokenize_sentences(text))

        return {
            'num_syllables': syllable_count,
            'num_poly_syllable_words': poly_syllable_count,
            'num_words': word_count,
            'num_sentences': sentence_count,
            'num_letters': letters_count,
            'num_gunning_complex': gunning_complex_count,
        }

    def _is_proper_noun(self, token):
        # pos = pos_tag(token)[0][1]
        # return pos == 'NNP'
        return token[0].isupper()

    def _is_compound_word(self, token):
        return re.match('.*[-].*', token) is not None

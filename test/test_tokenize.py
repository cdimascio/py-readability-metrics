import unittest

from nltk import word_tokenize

from readability import Readability


class WordTokenizeTest(unittest.TestCase):
    """
    Tests non-default word-tokenization
    """

    def setUp(self):
        # taken from https://en.wikipedia.org/wiki/Word#Summary
        self.text = """
        What makes a word? 
        In linguistics, a word of a spoken language can be defined as the smallest sequence of phonemes that can be 
        uttered in isolation with objective or practical meaning.
        There have been many proposed criteria for identifying words. 
        However, no definition has been found to apply to all languages. 
        Dictionaries categorize a language's lexicon (i.e., its vocabulary) into lemmas.
        These can be taken as an indication of what constitutes a "word" in the opinion of the writers of that language.
        The most appropriate means of measuring the length of a word is by counting its syllables or morphemes. 
        When a word has multiple definitions or multiple senses, it may result in confusion in a debate or discussion.
        """

    def test_nltk_treebank_tokenizer(self):
        r = Readability(self.text, f_tokenize_words=word_tokenize).ari()
        self.assertEqual(8.730483870967742, r.score)
        self.assertEqual(['9'], r.grade_levels)
        self.assertEqual([14, 15], r.ages)

    def test_default_tokenizer(self):
        r = Readability(self.text).ari()
        self.assertEqual(8.578548387096774, r.score)
        self.assertEqual(['9'], r.grade_levels)
        self.assertEqual([14, 15], r.ages)

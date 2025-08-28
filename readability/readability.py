import warnings

import nltk

from .scorers import (ARI, ColemanLiau, DaleChall, Flesch, FleschKincaid,
                      GunningFog, LinsearWrite, LixLesbarkeitsIndex,
                      MiyazakiReadabilityIndex, Smog, Spache,
                      WienerSachtextformel, Gsmog)
from .text import Analyzer

nltk.download('punkt_tab')

class Readability:
    def __init__(self, text, min_words=100, language='en'):
        self._analyzer = Analyzer()
        self._statistics = self._analyzer.analyze(text)
        self._min_words = min_words
        self._language = language
        if self._min_words < 100:
            warnings.warn(
                "Documents with fewer than 100 words may affect the accuracy of readability tests"
            )

    def ari(self):
        """Calculate Automated Readability Index (ARI)."""
        return ARI(self._statistics, self._min_words).score()

    def coleman_liau(self):
        """Calculate Coleman Liau Index."""
        return ColemanLiau(self._statistics, self._min_words).score()

    def dale_chall(self):
        """Calculate Dale Chall."""
        return DaleChall(self._statistics, self._min_words).score()

    def flesch(self):
        """Calculate Flesch Reading Ease score."""
        return Flesch(self._statistics, self._min_words, self._language).score()

    def flesch_kincaid(self):
        """Calculate Flesch-Kincaid Grade Level."""
        return FleschKincaid(self._statistics, self._min_words).score()

    def gunning_fog(self):
        """Calculate Gunning Fog score."""
        return GunningFog(self._statistics, self._min_words).score()

    def linsear_write(self):
        """Calculate Linsear Write."""
        return LinsearWrite(self._statistics, self._min_words).score()

    def smog(self,all_sentences=False, ignore_length=False):
        """SMOG Index.
        `all_sentences` indicates whether SMOG should use a sample of 30 sentences, as described in the original paper, or if it should use all sentences in the text"""
        return Smog(self._statistics, self._analyzer.sentences,
                    all_sentences=all_sentences, ignore_length=ignore_length).score()
    
    def gsmog(self, ignore_length=False):
        """GSMOG Index. Measure the SMOG score adapted for German text"""
        return Gsmog(self._statistics, ignore_length=ignore_length).score()

    def erste_wiener_sachtextformel(self):
        """erste Wiener Sachtextformel."""
        return WienerSachtextformel(self._statistics, self._min_words).erste_wiener_sachtextformel_score()

    def zweite_wiener_sachtextformel(self):
        """zweite Wiener Sachtextformel."""
        return WienerSachtextformel(self._statistics, self._min_words).zweite_wiener_sachtextformel_score()

    def dritte_wiener_sachtextformel(self):
        """dritte Wiener Sachtextformel."""
        return WienerSachtextformel(self._statistics, self._min_words).dritte_wiener_sachtextformel_score()

    def vierte_wiener_sachtextformel(self):
        """vierte Wiener Sachtextformel."""
        return WienerSachtextformel(self._statistics, self._min_words).vierte_wiener_sachtextformel_score()

    def lix_lesbarkeits_index(self):
        """LIX Lesbarkeitsindex."""
        return LixLesbarkeitsIndex(self._statistics, self._min_words).score()
    
    def miyazaki_readability_index(self):
        """Miyazaki Readability Index."""
        return MiyazakiReadabilityIndex(self._statistics, self._min_words).score()

    def spache(self):
        """Spache Index."""
        return Spache(self._statistics, self._min_words).score()

    def statistics(self):
        return {
            'num_letters': self._statistics.num_letters,
            'num_words': self._statistics.num_words,
            'num_sentences': self._statistics.num_sentences,
            'num_polysyllabic_words': self._statistics.num_poly_syllable_words,
            'avg_words_per_sentence': self._statistics.avg_words_per_sentence,
            'avg_syllables_per_word': self._statistics.avg_syllables_per_word,
            'num_six_letter_words': self._statistics.num_six_letter_words,
            'num_mono_syllable_words': self._statistics.num_mono_syllable_words,
        }

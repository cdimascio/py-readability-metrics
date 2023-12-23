from .text import Analyzer
from .scorers import ARI, ColemanLiau, DaleChall, Flesch, \
    FleschKincaid, GunningFog, LinsearWrite, Smog, Spache
import warnings

class Readability:
    def __init__(self, text, length_exception=True):
        self._analyzer = Analyzer()
        self._statistics = self._analyzer.analyze(text)
        self._length_exception = length_exception
        if not self._length_exception:
            if self._statistics.num_words < 100:
                warnings.warn(
                    "Documents with fewer than 100 words may affect the accuracy of readability tests. {} words found"
                    .format(self._statistics.num_words))

    def ari(self):
        """Calculate Automated Readability Index (ARI)."""
        return ARI(self._statistics, self._length_exception).score()

    def coleman_liau(self):
        """Calculate Coleman Liau Index."""
        return ColemanLiau(self._statistics, self._length_exception).score()

    def dale_chall(self):
        """Calculate Dale Chall."""
        return DaleChall(self._statistics, self._length_exception).score()

    def flesch(self):
        """Calculate Flesch Reading Ease score."""
        return Flesch(self._statistics, self._length_exception).score()

    def flesch_kincaid(self):
        """Calculate Flesch-Kincaid Grade Level."""
        return FleschKincaid(self._statistics, self._length_exception).score()

    def gunning_fog(self):
        """Calculate Gunning Fog score."""
        return GunningFog(self._statistics, self._length_exception).score()

    def linsear_write(self):
        """Calculate Linsear Write."""
        return LinsearWrite(self._statistics, self._length_exception).score()

    def smog(self,all_sentences=False):
        """SMOG Index.
        `all_sentences` indicates whether SMOG should use a sample of 30 sentences, as described in the original paper, or if it should use all sentences in the text"""
        return Smog(self._statistics, self._analyzer.sentences,
                    all_sentences=all_sentences,length_exception=self._length_exception).score()

    def spache(self):
        """Spache Index."""
        return Spache(self._statistics, self._length_exception).score()

    def statistics(self):
        return {
            'num_letters': self._statistics.num_letters,
            'num_words': self._statistics.num_words,
            'num_sentences': self._statistics.num_sentences,
            'num_polysyllabic_words': self._statistics.num_poly_syllable_words,
            'avg_words_per_sentence': self._statistics.avg_words_per_sentence,
            'avg_syllables_per_word': self._statistics.avg_syllables_per_word,
        }

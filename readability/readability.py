from .text import Analyzer
from .scorers import ARI, ColemanLiau, DaleChall, Flesch, \
    FleschKincaid, GunningFog, LinearWrite, Smog


class Readability:
    def __init__(self, text):
        self._analyzer = Analyzer()
        self._statistics = self._analyzer.analyze(text)

    def ari(self):
        """Calculate Automated Readability Index (ARI)."""
        return ARI(self._statistics).score()

    def coleman_liau(self):
        """Calculate Coleman Liau Index."""
        return ColemanLiau(self._statistics).score()

    def dale_chall(self):
        """Calculate Dale Chall."""
        return DaleChall(self._statistics).score()

    def flesch(self):
        """Calculate Flesch Reading Ease score."""
        return Flesch(self._statistics).score()

    def flesch_kincaid(self):
        """Calculate Flesch Kincaid Grade Level."""
        return FleschKincaid(self._statistics).score()

    def gunning_fog(self):
        """Calculate Gunning Fog score."""
        return GunningFog(self._statistics).score()

    def linear_write(self):
        """Calculate Linear Write."""
        return LinearWrite(self._statistics).score()

    def smog(self):
        """SMOG Index."""
        return Smog(self._statistics, self._analyzer.sentences).score()

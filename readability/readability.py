from .text import Analyzer
from .scorers import ColemanLiau, DaleChall, Flesch, FleschKincaid, GunningFog


class Readability:
    def __init__(self, text):
        self.analyzer = Analyzer(text)

    def coleman_liau(self):
        """Calculate Coleman Liau Index."""
        return ColemanLiau(self.analyzer.statistics).score()

    def dale_chall(self):
        """Calculate Dale Chall."""
        return DaleChall(self.analyzer.statistics).score()

    def flesch(self):
        """Calculate Flesch Reading Ease score."""
        return Flesch(self.analyzer.statistics).score()

    def flesch_kincaid(self):
        """Calculate Flesch Kincaid Grade Level."""
        return FleschKincaid(self.analyzer.statistics).score()

    def gunning_fog(self):  # , abbr=None, hyphen=None, vars={}):
        """Calculate Gunning Fog score."""
        return GunningFog(self.analyzer.statistics).score()

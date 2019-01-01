from .text import Analyzer
from .scorers import Flesch, FleschKincaid, GunningFog


class Readability:
    def __init__(self, text):
        self.analyzer = Analyzer(text)

    def gunning_fog(self):  # , abbr=None, hyphen=None, vars={}):
        """Calculate Gunning Fog score."""
        return GunningFog(self.analyzer.statistics).score()

    def flesch_kincaid(self):
        """Calculate Flesch Kincaid Grade Level."""
        return FleschKincaid(self.analyzer.statistics).score()

    def flesch(self):
        """Calculate Flesch Reading Ease score."""
        return Flesch(self.analyzer.statistics).score()

import math
from readability.text.analyzer import Analyzer
from readability.exceptions import ReadabilityException


class Result:
    def __init__(self, score, grade_level):
        self.score = score
        self.grade_level = grade_level

    def __str__(self):
        return "score: {}, grade_level: {}". \
            format(self.score, self.grade_level)


class Smog:
    def __init__(self, stats, sentences, all_sentences=False):
        """
        Computes the SMOG readability score (Harry McLaughlin, 1969 https://ogg.osu.edu/media/documents/health_lit/WRRSMOG_Readability_Formula_G._Harry_McLaughlin__1969_.pdf)
        If all_sentences is false, computes the score as described in McLaughlin, 1969, using exactly 30 sentences
        If all_sentences is true, adjusts the score to use all sentences in the text
        """
        if stats.num_sentences < 30:
            raise ReadabilityException(
                'SMOG requires 30 sentences. {} found'
                .format(stats.num_sentences))

        self._stats = stats
        self.all_sentences = all_sentences
        if not self.all_sentences:
            self._smog_stats = self._smog_text_stats(sentences)
            

    def score(self):
        score = self._score()
        grade_level = self._grade_level(score)
        return Result(
            score=score,
            grade_level=grade_level
        )

    def _score(self):
        if self.all_sentences:
            smog_stats = self._stats
            num_sentences = smog_stats.num_sentences
        else:
            smog_stats = self._smog_stats
            num_sentences = 30
        
        num_complex_words = smog_stats.num_poly_syllable_words
        return 1.0430 * math.sqrt(30 * num_complex_words / num_sentences) + 3.1291

    def _grade_level(self, score):
        return str(round(score))

    def _smog_text_stats(self, sentences):
        mid = int(math.floor(len(sentences) / 2))
        first_10_sents = sentences[:10]
        mid_10_sents = sentences[mid-5: mid+5]
        last_10_sents = sentences[-10:]

        smog_text = ' '.join(first_10_sents + mid_10_sents + last_10_sents)
        return Analyzer().analyze(smog_text)

from readability.exceptions import ReadabilityException


class Result:
    def __init__(self, score, grade_levels, ease):
        self.score = score
        self.ease = ease
        self.grade_levels = grade_levels

    def __str__(self):
        return "score: {}, ease: '{}', grade_levels: {}". \
            format(self.score, self.ease, self.grade_levels)


class WienerSachtextformel:
    def __init__(self, stats, min_words=100):
        self._stats = stats
        if stats.num_words < min_words:
            raise ReadabilityException('{} words required.'.format(min_words))

    def erste_wiener_sachtextformel_score(self):
        score = self._erste_wiener_sachtextformel_score()
        return Result(
            score=score,
            ease=self._ease(score),
            grade_levels=self._grade_levels(score)
        )
    
    def zweite_wiener_sachtextformel_score(self):
        score = self._zweite_wiener_sachtextformel_score()
        return Result(
            score=score,
            ease=self._ease(score),
            grade_levels=self._grade_levels(score)
        )
    
    def dritte_wiener_sachtextformel_score(self):
        score = self._dritte_wiener_sachtextformel_score()
        return Result(
            score=score,
            ease=self._ease(score),
            grade_levels=self._grade_levels(score)
        )
    
    def vierte_wiener_sachtextformel_score(self):
        score = self._vierte_wiener_sachtextformel_score()
        return Result(
            score=score,
            ease=self._ease(score),
            grade_levels=self._grade_levels(score)
        )

    def _erste_wiener_sachtextformel_score(self):
        """
        The first Wiener Sachtextformel
        WSTF1 considers all four main factors: sentence length, sentence count, proportion of long words, and proportion of monosyllabic words.

        The formula is:
            0.1935 * ratio of words with >= 3 syllables + 0.1672 * mean sentence length +
            0.1297 * ratio of words with >= 6 letters - 0.0327 * ratio of words with 1 syllable - 0.875
        """
        stats = self._stats
        return (0.1935 * (stats.num_poly_syllable_words / stats.num_words)) + (0.1672 * stats.avg_words_per_sentence) + \
               (0.1297 * (stats.num_six_letter_words / stats.num_words)) - (0.0327 * (stats.num_mono_syllable_words / stats.num_words)*100) - 0.875

    def _zweite_wiener_sachtextformel_score(self):
        """
        The second Wiener Sachtextformel
        WSTF2 is similar to WSTF1, but weights the factors slightly differently, omitting the proportion of monosyllabic words.

        The formula is:
            0.2007 * ratio of words with >= 3 syllables + 0.1682 * mean sentence length +
            0.1373 * ratio of words with >= 6 letters - 2.779
        """
        stats = self._stats
        return (0.2007 * (stats.num_poly_syllable_words / stats.num_words)) + (0.1682 * stats.avg_words_per_sentence) + \
               (0.1373 * (stats.num_six_letter_words / stats.num_words)) - 2.779

    def _dritte_wiener_sachtextformel_score(self):
        """
        The third Wiener Sachtextformel
        WSTF3 is the simplest formula because it only takes into account the mean sentence length and the proportion of long words.

        The formula is:
            0.2963 * ratio of words with >= 3 syllables + 0.1905 * mean sentence length - 1.1144
        """
        stats = self._stats
        return (0.2963 * (stats.num_poly_syllable_words / stats.num_words)) + (0.1905 * stats.avg_words_per_sentence) - 1.1144

    def _vierte_wiener_sachtextformel_score(self):
        """
        The fourth Wiener Sachtextformel
        WSTF4 focuses specifically on readability in relation to school levels, which is why the weighting of sentence length is greater.

        The formula is:
            0.2744 * ratio of words with >= 3 syllables + 0.2656 * mean sentence length - 1.693
        """
        stats = self._stats
        return (0.2744 * (stats.num_poly_syllable_words / stats.num_words)) + (0.2656 * stats.avg_words_per_sentence) - 1.693

    def _ease(self, score):
        if score >= 4 and score <= 5:
            return 'very_easy'
        elif score >=6 and score <=7:
            return 'easy'
        elif score >=8 and score <=10:
            return 'average'
        elif score >=11 and score <=12:
            return 'difficult'
        else:
            return 'very_difficult'

    def _grade_levels(self, score):
        if score >= 4 and score <= 5:
            return ['4', '5']
        elif score >=6 and score <=7:
            return ['6', '7']
        elif score >=8 and score <=10:
            return ['8', '9', '10']
        elif score >=11 and score <=12:
            return ['11', '12']
        else:
            return ['college level and above']

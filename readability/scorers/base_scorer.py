from readability.exceptions import ReadabilityException
from readability.text import AnalyzerStatistics


class Result:
    def __init__(self, scorer_name, score, grade_level, age, scale_value, cloze_score, description):
        self.name = scorer_name

        self.score = score
        self.grade_level = grade_level
        self.age = age
        self.scale_value = scale_value
        self.cloze_score = cloze_score
        self.description = description

    def __str__(self):
        if self.name is not None:
            result = "{}: ".format(self.name)
        else:
            result = ""

        if self.score is not None:
            if isinstance(self.score, float):
                result += "score = {:.2f}, ".format(self.score)
            else:
                result += "score = {}, ".format(self.score)

        if self.grade_level is not None:
            result += "grade_level = {}, ".format(self.grade_level)
        if self.age is not None:
            result += "age = {}, ".format(self.age)
        if self.scale_value is not None:
            result += "scale_value = {:.2f}, ".format(self.scale_value)
        if self.cloze_score is not None:
            result += "cloze_score = {:.2f}, ".format(self.cloze_score)
        if self.description is not None:
            result += "{}, ".format(self.description)

        return result[:-2]


class ReadabilityScorer:
    def __init__(self, stats: AnalyzerStatistics, min_words=100):
        if stats.num_words < min_words:
            raise ReadabilityException('{} words required.'.format(min_words))

        self._stats = stats
        self.scorer_name = None

    def results(self):
        self._score = self._raw_score()
        return Result(
            scorer_name=self.scorer_name,
            score=self._score,
            grade_level=self._grade_level(),
            age=self._age(),
            scale_value=self._scale_value(),
            cloze_score=self._cloze_score(),
            description=self._description(),
        )

    def _raw_score(self):
        return None

    def _grade_level(self):
        return None

    def _age(self):
        return None

    def _scale_value(self):
        return None

    def _cloze_score(self):
        return None

    def _description(self):
        return None

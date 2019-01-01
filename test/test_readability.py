import unittest
from readability import Readability


class ReadabilityTest(unittest.TestCase):
    def setUp(self):
        text = """
        In linguistics, the Gunning fog index is a readability test for English writing. The index estimates the years of formal education a person needs to understand the text on the first reading. For instance, a fog index of 12 requires the reading level of a United States high school senior (around 18 years old). The test was developed in 1952 by Robert Gunning, an American businessman who had been involved in newspaper and textbook publishing.
        The fog index is commonly used to confirm that text can be read easily by the intended audience. Texts for a wide audience generally need a fog index less than 12. Texts requiring near-universal understanding generally need an index less than 8.
        """
        self.readability = Readability(text)

    def test_flesch_kincaid(self):
        r = self.readability.flesch_kincaid()
        print(r)
        self.assertEqual(10.125531135531137, r.score)
        self.assertEqual('10', r.grade_level)

    def test_flesch(self):
        r = self.readability.flesch()
        print(r)
        self.assertEqual(51.039230769230784, r.score)
        self.assertEqual(['10', '11', '12'], r.grade_levels)
        self.assertEqual('fairly_difficult', r.ease)

    def test_gunning_fog(self):
        r = self.readability.gunning_fog()
        print(r)
        self.assertEqual(6.754090354090355, r.score)
        self.assertEqual('7', r.grade_level)

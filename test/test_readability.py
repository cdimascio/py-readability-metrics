import unittest
from readability import Readability


class ReadabilityTest(unittest.TestCase):
    def setUp(self):
        text = """
        In linguistics, the Gunning fog index is a readability test for English writing. The index estimates the years of formal education a person needs to understand the text on the first reading. For instance, a fog index of 12 requires the reading level of a United States high school senior (around 18 years old). The test was developed in 1952 by Robert Gunning, an American businessman who had been involved in newspaper and textbook publishing.
        The fog index is commonly used to confirm that text can be read easily by the intended audience. Texts for a wide audience generally need a fog index less than 12. Texts requiring near-universal understanding generally need an index less than 8.
        """
        self.readability = Readability(text)

    def test_ari(self):
        r = self.readability.ari()
        print(r)
        self.assertEqual(9.551245421245422, r.score)
        self.assertEqual(['10'], r.grade_levels)
        self.assertEqual([15, 16], r.ages)

    def test_coleman_liau(self):
        r = self.readability.coleman_liau()
        print(r)
        self.assertEqual(10.673162393162393, r.score)
        self.assertEqual('11', r.grade_level)

    def test_dale_chall(self):
        r = self.readability.dale_chall()
        print(r)
        self.assertEqual(9.32399010989011, r.score)
        self.assertEqual(['college'], r.grade_levels)

    def test_flesch(self):
        r = self.readability.flesch()
        print(r)
        self.assertEqual(51.039230769230784, r.score)
        self.assertEqual(['10', '11', '12'], r.grade_levels)
        self.assertEqual('fairly_difficult', r.ease)

    def test_flesch_kincaid(self):
        r = self.readability.flesch_kincaid()
        print(r)
        self.assertEqual(10.125531135531137, r.score)
        self.assertEqual('10', r.grade_level)

    def test_gunning_fog(self):
        r = self.readability.gunning_fog()
        print(r)
        self.assertEqual(12.4976800976801, r.score)
        self.assertEqual('12', r.grade_level)

    def test_linear_write(self):
        r = self.readability.linear_write()
        print(r)
        self.assertEqual(11.214285714285714, r.score)
        self.assertEqual('11', r.grade_level)

    def test_smog(self):
        text = """
        In linguistics, the Gunning fog index is a readability test for English writing. The index estimates the years of formal education a person needs to understand the text on the first reading. For instance, a fog index of 12 requires the reading level of a United States high school senior (around 18 years old). The test was developed in 1952 by Robert Gunning, an American businessman who had been involved in newspaper and textbook publishing.
        The fog index is commonly used to confirm that text can be read easily by the intended audience. Texts for a wide audience generally need a fog index less than 12. Texts requiring near-universal understanding generally need an index less than 8.
        """
        text = ' '.join(text for i in range(0, 5))

        readability = Readability(text)
        r = readability.smog()

        print(r)
        self.assertEqual(12.516099999999998, r.score)
        self.assertEqual('13', r.grade_level)

    def test_print_stats(self):
        stats = self.readability.statistics()
        self.assertEqual(562, stats['num_letters'])
        self.assertEqual(117, stats['num_words'])
        self.assertEqual(7, stats['num_sentences'])
        self.assertEqual(20, stats['num_polysyllabic_words'])

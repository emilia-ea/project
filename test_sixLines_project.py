import unittest

from core import get_trigram, get_changed_lines, get_hexagram_result
from hexagrams import text_dict, yin, yang


# TURTLE SCALING TEST
def scale_distance_to_number(total_distance):
    return int(100 + (min(total_distance, 8000) / 8000) * 899)

class TestTurtleScaling(unittest.TestCase):
    def test_minimum_distance(self):
        self.assertEqual(scale_distance_to_number(0), 100)

    def test_maximum_distance(self):
        self.assertEqual(scale_distance_to_number(8000), 999)

    def test_mid_distance(self):
        mid = scale_distance_to_number(4000)
        self.assertTrue(500 < mid < 600)


# CORE LOGIC, TRIGRAM GENERATION, LINE CHANGEs

class TestCoreFunctions(unittest.TestCase):
    def test_get_trigram_format(self):
        trigram = get_trigram(0)
        self.assertIsInstance(trigram, str)
        self.assertEqual(len(trigram.splitlines()), 3)
        self.assertTrue(all(line in [yin, yang] for line in trigram.splitlines()))

    def test_get_changed_lines_format(self):
        original = f"{yang}\n{yang}\n{yang}"
        changed = get_changed_lines(original, 2)
        self.assertNotEqual(original, changed.strip())
        self.assertEqual(len(changed.strip().splitlines()), 3)

    def test_get_hexagram_result_structure(self):
        result = get_hexagram_result(f"{yang}\n{yang}\n{yang}\n{yang}\n{yang}\n{yang}")
        self.assertTrue(isinstance(result, str))
        self.assertGreater(len(result), 0)


# HEXAGRAM DICTIONARY

class TestHexagramDictionary(unittest.TestCase):
    def test_has_64_entries(self):
        self.assertEqual(len(text_dict), 64)

    def test_sample_keys_exist(self):
        self.assertIn(f"{yang}\n{yang}\n{yang}\n{yang}\n{yang}\n{yang}", text_dict)
        self.assertIn(f"{yin}\n{yin}\n{yin}\n{yin}\n{yin}\n{yin}", text_dict)



# CHECK ALL TRIGRAM COMBINATIONS, LINE CHANGES WORK 

class TestAllHexagramCombos(unittest.TestCase):
    def test_all_trigram_combinations_have_results(self):
        errors = []
        for i in range(8):
            for j in range(8):
                for k in range(6):
                    upper = get_trigram(i)
                    lower = get_trigram(j)
                    original = f"{upper}\n{lower}"
                    changed = get_changed_lines(original, k)
                    result1 = get_hexagram_result(original)
                    result2 = get_hexagram_result(changed)

                    if result1 == "No corresponding text.":
                        errors.append(f"Missing original: {original}")
                    if result2 == "No corresponding text.":
                        errors.append(f"Missing changed: {changed}")
        
        if errors:
            self.fail(f"Some hexagram results were missing:\n" + "\n".join(errors))

if __name__ == "__main__":
    unittest.main()
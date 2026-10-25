import unittest

from string_calculator import add


class StringCalculatorTests(unittest.TestCase):
    def test_empty_string_returns_zero(self):
        self.assertEqual(0, add(""))

    def test_one_number_is_returned(self):
        self.assertEqual(1, add("1"))

    def test_two_comma_separated_numbers_are_added(self):
        self.assertEqual(3, add("1,2"))

    def test_an_unknown_number_of_comma_separated_numbers_are_added(self):
        self.assertEqual(10, add("1,2,3,4"))

    def test_newlines_are_supported_alongside_commas(self):
        self.assertEqual(6, add("1\n2,3"))

    def test_a_custom_delimiter_can_be_declared(self):
        self.assertEqual(3, add("//;\n1;2"))

    def test_the_catalog_custom_delimiter_format_is_supported(self):
        self.assertEqual(3, add(";\n1;2"))

    def test_a_negative_number_is_rejected(self):
        with self.assertRaisesRegex(ValueError, r"negatives not allowed: -1"):
            add("1,-1")

    def test_all_negative_numbers_are_listed_in_the_exception(self):
        with self.assertRaisesRegex(ValueError, r"negatives not allowed: -1, -4"):
            add("-1,2,-4")

    def test_custom_delimiter_with_regex_special_characters(self):
        self.assertEqual(3, add("//*\n1*2"))

    def test_multi_character_custom_delimiter(self):
        self.assertEqual(3, add("//sep\n1sep2"))

    def test_all_negative_numbers_are_rejected(self):
        with self.assertRaisesRegex(ValueError, r"negatives not allowed: -2, -5, -8"):
            add("-2,-5,-8")

    def test_delimiter_only_string_returns_zero(self):
        self.assertEqual(0, add(","))

    def test_consecutive_delimeters(self):
        self.assertEqual(5, add("1,,4"))

    def test_delimeter_at_the_end_of_string(self):
        self.assertEqual(4, add("1,3,"))

    def test_different_delimeters_sequence(self):
        self.assertEqual(6, add("4,\n2"))

if __name__ == "__main__":
    unittest.main()
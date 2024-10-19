import data
import hw1
import unittest
from data import Price, Rectangle, Point, Book

from hw1 import vowel_count, short_lists, ascending_pairs, add_prices, rectangle_area, books_by_author


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count_1(self):
        self.assertEqual((vowel_count("atta boy")), 3)
    def test_vowel_count_2(self):
        self.assertEqual((vowel_count("wahoo!!! haha~")), 5)
    # Part 2
    def test_short_lists_1(self):
        self.assertEqual(short_lists(hw1.temp_lists), [[12, 16], [14, 155]])
    def test_short_lists_2(self):
        self.assertEqual(short_lists([[4], [1, 2], [], [9, 0]]), [[1, 2], [9, 0]])
    # Part 3
    def test_ascending_pairs_1(self):
        self.assertEqual(ascending_pairs(hw1.temp_lists), [[12, 16], [4], [72, 90, 98], [14, 155]])
    def test_ascending_pairs_2(self):
        self.assertNotEqual(ascending_pairs(hw1.temp_lists), [[12, 16], [14, 155]])
    # Part 4
    def test_add_prices_1(self):
        self.assertEqual((add_prices(hw1.newprice1, hw1.newprice2)), Price(21, 25))
    def test_add_prices_2(self):
        self.assertEqual((add_prices(Price(4, 10), Price(7, 20))), Price(11, 30))
    # Part 5
    def test_rectangle_area_1(self):
        tester = rectangle_area(Rectangle(Point(0, 4), Point(4, 0)))
        self.assertEqual(tester, 16)
    def test_rectangle_area_2(self):
        tester = rectangle_area(Rectangle(Point(1, 4), Point(5, 0)))
        self.assertEqual(tester, 16)
    # Part 6
    def test_books_by_author_1(self):
        tester = [Book(['Mark Twain'], 'Huckleberry Finn'), Book(['Mark Twain', 'Charles Dickens'], 'A Tale of Finn'), Book(['Mark Twain', 'C.S. Lewis'], 'Huckleberry Narnia')]
        self.assertEqual(books_by_author("Mark Twain", hw1.inputBooks), tester)
    def test_books_by_author_2(self):
        self.assertEqual(books_by_author("Tom Sawyer", hw1.inputBooks), [])
    # Part 7
    def

    # Part 8





if __name__ == '__main__':
    unittest.main()

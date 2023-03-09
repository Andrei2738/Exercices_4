import math
import random
import string
import unittest


def ex1(number):                                             #Check if a number is a perfect square
    if (math.isqrt(number) ** 2 == number):
        return ("number is a perfect square")
    else:
        return ("number is not a perfect square")


def ex2(number):                                             #Find the sum of the digits of a number
    string = str(number)
    sum = 0
    for i in range(len(string)):
        sum += int(string[i])
    return (sum)


def ex3(number):                                             #Check if a number is a palindrome or not
    if str(number) == str(number)[::-1]:
        return ("The number is a palindrome")
    else:
        return ("The number is not a palindrome")


def ex4(phrase):                                             #Find the most common word in a phrase
    # Convert the phrase to lowercase to ensure case-insensitivity
    phrase = phrase.lower()

    # Split the phrase into words
    words = phrase.split()

    # Create a dictionary to count the frequency of each word
    word_counts = {}
    for word in words:
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1

    # Find the most common word
    most_common_word = None
    max_count = 0
    for word, count in word_counts.items():
        if count > max_count:
            most_common_word = word
            max_count = count

    return (most_common_word)


def ex5(length):                                             #Generate a random password
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return (password)


#Unit tests


class TestEx1(unittest.TestCase):

    def test_perfect_square(self):
        self.assertEqual(ex1(0), "number is a perfect square")  # 0 is a perfect square
        self.assertEqual(ex1(1), "number is a perfect square")  # 1 is a perfect square
        self.assertEqual(ex1(4), "number is a perfect square")  # 4 is a perfect square
        self.assertEqual(ex1(9), "number is a perfect square")  # 9 is a perfect square
        self.assertEqual(ex1(16), "number is a perfect square")  # 16 is a perfect square
        self.assertEqual(ex1(25), "number is a perfect square")  # 25 is a perfect square
        self.assertEqual(ex1(36), "number is a perfect square")  # 36 is a perfect square

    def test_not_perfect_square(self):
        self.assertEqual(ex1(2), "number is not a perfect square")  # 2 is not a perfect square
        self.assertEqual(ex1(3), "number is not a perfect square")  # 3 is not a perfect square
        self.assertEqual(ex1(5), "number is not a perfect square")  # 5 is not a perfect square
        self.assertEqual(ex1(7), "number is not a perfect square")  # 7 is not a perfect square
        self.assertEqual(ex1(10), "number is not a perfect square")  # 10 is not a perfect square
        self.assertEqual(ex1(13), "number is not a perfect square")  # 13 is not a perfect square
        self.assertEqual(ex1(15), "number is not a perfect square")  # 15 is not a perfect square


class TestEx2(unittest.TestCase):
    def test_sum_of_digits(self):
        self.assertEqual(ex2(12345), 15)
        self.assertEqual(ex2(987654321), 45)
        self.assertEqual(ex2(123456789), 45)
        self.assertEqual(ex2(11111), 5)
        self.assertEqual(ex2(0), 0)


class TestEx3(unittest.TestCase):
    def test_palindrome_numbers(self):
        self.assertEqual(ex3(121), "The number is a palindrome")
        self.assertEqual(ex3(1221), "The number is a palindrome")
        self.assertEqual(ex3(123454321), "The number is a palindrome")
        self.assertEqual(ex3(7), "The number is a palindrome")
        self.assertEqual(ex3(0), "The number is a palindrome")

    def test_non_palindrome_numbers(self):
        self.assertEqual(ex3(123), "The number is not a palindrome")
        self.assertEqual(ex3(1234), "The number is not a palindrome")
        self.assertEqual(ex3(123456789), "The number is not a palindrome")
        self.assertEqual(ex3(-121), "The number is not a palindrome")  # Negative numbers are not palindromes


class TestEx4(unittest.TestCase):
    def test_single_word_phrase(self):
        self.assertEqual(ex4("hello"), "hello")

    def test_phrase_with_most_common_word(self):
        self.assertEqual(ex4("the quick brown fox jumps over the lazy dog"), "the")
        self.assertEqual(ex4("to be or not to be that is the question"), "to")

    def test_phrase_with_multiple_most_common_words(self):
        self.assertIn(ex4("the quick brown fox jumps over the lazy dog the"), ["the", "over"])
        self.assertIn(ex4("to be or not to be that is the question be or not be"), ["be", "or", "to"])

    def test_empty_phrase(self):
        self.assertIsNone(ex4(""))

    def test_whitespace_only_phrase(self):
        self.assertIsNone(ex4("  \t \n"))


class TestEx5(unittest.TestCase):
    def test_password_length(self):
        for length in range(1, 21):
            password = ex5(length)
            self.assertEqual(len(password), length)

    def test_password_characters(self):
        for length in range(1, 21):
            password = ex5(length)
            for character in password:
                self.assertIn(character, string.ascii_letters + string.digits + string.punctuation)

    def test_password_uniqueness(self):
        passwords = [ex5(8) for i in range(100)]
        self.assertEqual(len(set(passwords)), 100)


if __name__ == '__main__':
    unittest.main()
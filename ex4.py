import math
import random
import string


def ex1():                                             #Check if a number is a perfect square
    number = int(input("Input a number:"))
    if (math.isqrt(number) ** 2 == number):
        print("number is a perfect square")
    else:
        print("number is not a perfect square")

def ex2():                                             #Find the sum of the digits of a number
    number = input("Input a number:")
    string = str(number)
    sum = 0
    for i in range(len(string)):
        sum += int(string[i])
    print(sum)

def ex3():                                             #Check if a number is a palindrome or not
    number = input("Input a number:")
    if number == number[::-1]:
        print("The number is a palindrome")
    else:
        print("The number is not a palindrome")

def ex4():                                            #Find the most common word in a phrase
    phrase = input("Input a phrase: ")
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

    print(most_common_word)

def ex5():                                             #Generate a random password
    length = int(input("Input password length:"))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    print (password)

ex4()
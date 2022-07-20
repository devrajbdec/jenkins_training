import string
from functools import reduce
from typing import List

apple_color = "red"


def get_apple_color():
    return apple_color


def change_apple_color(new_color):
    global apple_color
    apple_color = new_color


#optionally add a class
#class WordCounter:


def get_word_frequency_pythonic(words):
    word1 = map(words, lambda x: (x, 1))
    reducer = reduce(word1, lambda x, y: (x, y + 1))
    return dict(reducer)


def get_word_frequency(words):
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] = frequency[word] + 1
        else:
            frequency[word] = 1
    return frequency


def get_word_frequency_from_file(list_of_files: List):
    pass


def get_word_frequency_from_text(text_string: string):
    text_block = text_string.replace("\n", '')
    frequency = get_word_frequency(text_block)
    return frequency

import csv
import json

ALPHABET = {x for x in 'abcdefghijklmnopqrstuvwxyz'}
KEY_LETTER = 'c'
GOOD_LETTERS = {'c', 'e', 'l', 'a', 't', 'f', 'u'}
BAD_LETTERS = ALPHABET - GOOD_LETTERS


MINWORDLEN = 4

myfile = 'wordlists/unigram_freq.csv'

all_words = dict()
word_index = dict()
valid_words = set()


# initialize word index
# each dict entry is a set with words with letter in any spot
for letter in ALPHABET:
    word_index[letter] = set()

# read in words from file
with open(myfile, newline='') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    next(lines)
    for row in lines:
        word = row[0]
        freq = int(row[1])
        if len(word) >= MINWORDLEN and word.isalpha() and word.isascii():
            all_words[word] = freq
            for letter in word:
                word_index[letter].add(word)


def is_valid(word):
    for check_letter in BAD_LETTERS:
        if word in word_index[check_letter]:
            return False
        if word not in word_index[KEY_LETTER]:
            return False
    return True


# reduce to valid words
solution = dict()
for word in all_words.keys():
    if is_valid(word):
        solution[word] = all_words[word]
sorts = sorted(solution.keys(), key=lambda word: solution[word])
print(sorts[-100:])
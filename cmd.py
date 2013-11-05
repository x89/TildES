#!/usr/bin/env python3
import sys, re, random

filename = "tilde_words"
if len(sys.argv) > 1:
    filename = sys.argv[1]

read_stripped_line = lambda fh: fh.readline().strip("\n")
words = []

# Array of all our spanish words
fh = open(filename, mode="r")
word = read_stripped_line(fh)
while word:
    words.append(word)
    word = read_stripped_line(fh)
fh.close()

words = random.sample(words, 20)

# áéíóú > aeiou
rx_áéíóú = re.compile(r'(.*)([áéíóú])(.*)')
for word in words:
    aeiou = re.search(rx_áéíóú, word)
    print(aeiou.groups())

def syllabicate(word):
    """Splits words into their syllabicated form, for example the words:
    superextraordinarísimamente -> su-pe-rex-tra-or-di-na-rí-si-ma-men-te
    electroencefalografistas -> e-lec-tro-en-ce-fa-lo-gra-fis-tas

    Takes a string, returns an array.
    The accent is always in the final four syllabols.

    There are quite a few rules in Spanish, and some rare exceptions.
    Good explanation: http://i1stspanish.com/syllabication-silabeo-lesson-two
    """
    return(['Th', 'is', 'Is', 'Not', 'Com', 'plete'])

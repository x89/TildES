#!/usr/bin/env python3

'''A script to help Spanish learners practice word stresses.

In spanish the stress is within the syllable containing the character with the
stress, there is at most one in any word, the technical words for them are:
 Aguda (stress on the final syllable)
 Grave/Llana (stress on the penultimate syllable)
 Esdrújula (3rd to last)
 Sobresdrújula (4th+ syllable)

In the case of aguda/grave there isn't always an accent, but where the stress
is is governed by rules. In the case of esdrújula/sobresdrújula words the
stress is always accented.
'''

import sys
import re
import random

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


class Word:
    def __init__(self, word):
        self.word = word

    def deaccent(self):
        '''Replace our accented character with a non-accented character.'''
        word = self.word
        word = word.replace('á', 'a')
        word = word.replace('é', 'e')
        word = word.replace('í', 'i')
        word = word.replace('ó', 'o')
        word = word.replace('ú', 'u')
        return word

    def syllabicate(self):
        """Splits words into their syllabicated form, for example the words:
        superextraordinarísimamente -> su-pe-rex-tra-or-di-na-rí-si-ma-men-te
        electroencefalografistas -> e-lec-tro-en-ce-fa-lo-gra-fis-tas

        Takes a string, returns an array.
        The accent is always in the final four syllabols.

        There are quite a few rules in Spanish, and some rare exceptions.
        Good explanation: http://i1stspanish.com/syllabication-silabeo-lesson-two
        """
        word = self.word

        return(['Th', 'is', 'Is', 'Not', 'Com', 'plete'])

words = random.sample(words, 20)
rx_áéíóú = re.compile(r'(.*)([áéíóú])(.*)')
for word in words:
    aeiou = re.search(rx_áéíóú, word)
    word = Word(word)
    print(aeiou.groups(), word.deaccent())


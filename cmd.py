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
import itertools

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
        # 1a. Dos vocales se separan si las dos son fuertes.
        hard_vowels = [''.join(_) for _ in itertools.combinations('aaooee', 2)]
        hard_vowels += ['aí', 'aú', 'oí', 'oú', 'eí', 'eú', 'ía', 'ío', \
            'íe', 'úa', 'úo', 'úe']
        for vowels in hard_vowels:
            word = re.sub(vowels, '{0} {1}'.format(vowels[0], vowels[1]), word)
        # 2. Consonants are *normally* split, exceptions added.
        consonant_pairs = [''.join(_) for _ in \
                itertools.permutations('bcdfghjklmnpqrstvwxyz'*2, 2)]
        consonant_pairs.remove('ch')  # ch are always together
        for pair in consonant_pairs:
            if pair[1] in ['l', 'r']:  # If the pair ends in l or r don't split
                consonant_pairs.remove(pair)
        for pair in consonant_pairs:
            word = re.sub(pair, '{0} {1}'.format(pair[0], pair[1]), word)
        return word.split(' ')

#rx_áéíóú = re.compile(r'(.*)([áéíóú])(.*)')

words = random.sample(words, 20)
for word in words:
    word = Word(word)
    print(word.syllabicate(), word.deaccent())


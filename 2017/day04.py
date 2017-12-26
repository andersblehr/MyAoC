#!/usr/bin/env python

import aocinput

'''
--- Day 4: High-Entropy Passphrases ---

A new system policy has been put in place that requires all accounts to
use a passphrase instead of simply a password. A passphrase consists of a
series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

  - aa bb cc dd ee is valid.
  - aa bb cc dd aa is not valid - the word aa appears more than once.
  - aa bb cc dd aaa is valid - aa and aaa count as different words.

The system's full passphrase list is available as your puzzle input. How
many passphrases are valid?

Your puzzle answer was 455.
'''
def puzzle_1(test_input=None):
    passphrases = test_input if test_input else aocinput.input_for_day(4)
    return day04_shared(passphrases, 1)

'''
For added security, yet another system policy has been put in place. Now,
a valid passphrase must contain no two words that are anagrams of each
other - that is, a passphrase is invalid if any word's letters can be
rearranged to form any other word in the passphrase.

For example:

  - abcde fghij is a valid passphrase.
  - abcde xyz ecdab is not valid - the letters from the third word can be
    rearranged to form the first word.
  - a ab abc abd abf abj is a valid passphrase, because all letters need
    to be used when forming another word.
  - iiii oiii ooii oooi oooo is valid.
  - oiii ioii iioi iiio is not valid - any of these words can be
    rearranged to form any other word.

Under this new system policy, how many passphrases are valid?

Your puzzle answer was 186.
'''
def puzzle_2(test_input=None):
    passphrases = test_input if test_input else aocinput.input_for_day(4)
    return day04_shared(passphrases, 2)

# Day 04 shared code
def day04_shared(passphrases, puzzle):
    valid_passphrases = 0
    for passphrase in passphrases:
        words = passphrase.split(' ')
        if puzzle == 1:
            unique = set(words)
        else:
            unique = set(map(lambda word: ''.join(sorted(list(word))), words))
        if len(unique) == len(words):
            valid_passphrases += 1
    return valid_passphrases

'''
Command line entry point
'''
if __name__ == '__main__':
    print("#1: %s" % puzzle_1())
    print("#2: %s" % puzzle_2())

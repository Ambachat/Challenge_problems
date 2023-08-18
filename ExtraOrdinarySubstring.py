#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 19:52:20 2023

@author: ambarish
We are given a mapping like 1-> ab, 2->cde, 3->fgh, ....., 9->xyz like a keypad phone.
Now if any string is given, we need to check how many substrings can be made from that, including that string itself,
such that the sum of the values of the letters constituting that substring, is divisible by the length of the 
substring. Those substrings are extraordinary substrings and we need to find that number given the string.
"""

def is_extraordinary(substring, mapping):
    total_value = sum(mapping[letter] for letter in substring)
    return total_value % len(substring) == 0

def count_extraordinary_substrings(input_string, mapping):
    count = 0
    for start in range(len(input_string)):
        for end in range(start + 1, len(input_string) + 1):
            substring = input_string[start:end]
            if is_extraordinary(substring, mapping):
                count += 1
    return count

# Mapping of letters to numerical values
mapping = {'a': 1, 'b': 1, 'c': 2, 'd': 2, 'e': 2, 'f': 3, 'g': 3, 'h': 3, 'i': 4,
           'j': 4, 'k': 4, 'l': 5, 'm': 5, 'n': 5, 'o': 6, 'p': 6, 'q': 6,
           'r': 7, 's': 7, 't': 7, 'u': 8, 'v': 8, 'w': 8, 'x': 9, 'y': 9, 'z': 9}

input_string = "sup"
result = count_extraordinary_substrings(input_string, mapping)
print("Number of extraordinary substrings:", result)

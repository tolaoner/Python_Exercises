'''Write a Python program to create all possible strings 
by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.'''
import itertools
vowel_list=['a','e','i','o','u']
all_possible_strings=list(itertools.permutations(vowel_list,5))
print(all_possible_strings)
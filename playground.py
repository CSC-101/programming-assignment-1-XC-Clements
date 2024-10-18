#checking out some interesting timing functions!! not part of the assignemtn just for
#the fun of optimization
import re

vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
pattern = re.compile("[AEIOUaeiou]")

def intersection():
    return bool(vowels.intersection("TWYNDYLLYNGS"))

def any_version():
    return any(char in vowels for char in "TWYNDYLLYNGS")

def re_version():
    return bool(pattern.search("TWYNDYLLYNGS"))

def disjoint():
    return vowels.isdisjoint("TWYNDYLLYNGS")

from timeit import timeit

print (timeit("intersection()", "from __main__ import intersection, vowels"))
print (timeit("any_version()", "from __main__ import any_version, vowels"))
print (timeit("re_version()", "from __main__ import re_version, vowels"))
print (timeit("disjoint()", "from __main__ import disjoint, vowels"))

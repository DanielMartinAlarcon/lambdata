"""
You are given two strings, str1 and str2, and want to determine if one could
possibly represent the other in a simple substitution cipher. In a simple
substitution cipher each character is represented by one and only one "new"
character. "New" is in quotations here because the substituted character
could be the original character. Every time the character occurs it must be
replaced by the same character as indicated in the cipher. No two characters
can be represented by the same character and no character can have more than
one representation.

Characters can be alphanumeric (lower- and upper-case are separate characters)
or symbolic. This is not a two-way cipher. That means that if "a" in str1
 represents "d" in str2 that "d" in str1 does not have to represent "a" in
 str2. See the illustration below the examples. In this "a" is represented
 by "c" but "c" is represented by "y".

Your task:
Complete the sub_cipher() function to return "True" if the strings entered
as parameters could represent each other in a simple substitution cipher,
and return "False" if they could not.

Examples:
>>> sub_cipher('toot', 'peep')
True

Here "t" could be represented by "p" and "o" could be represented by "e",
so we return "True" because the two strings could represent each other in
a simple one-for-one substitution cipher.

>>> sub_cipher('lambda', 'school')
False

This returns "False" because "l" can map to "s", "a" to "c", and "m" to "h",
 but then both "b" and "d" map to "o", which nullifies this per our
 restriction of characters only having one representation in the cipher.

>>> sub_cipher('kazoo', 'i too')
True

Here each character maps one-to-one to a "new" character so we return
"True": "k" to "i", "a" to " ", "z" to "t", and "o" to "o".

Other examples:

>>> sub_cipher('o', 'lambda')
False

>>> sub_cipher('', '')
True
"""


def sub_cipher(str1, str2):
    keys = list(str1)
    values = list(str2)

    cipher_dict = {}
    cipher = False

    if len(keys) != len(values):
        return cipher

    # For loop that returns cipher=False for all cases that break
    # the acceptable pattern
    for i in range(len(keys)):

        # Has this key been used before?
        if keys[i] in cipher_dict.keys():
            # If it has been used, did it have a different value?
            if cipher_dict[keys[i]] != values[i]:
                # If so, cipher is false
                return cipher

        # If the key has not been used before,
        else:
            # Has the value been assigned to a different key?
            if values[i] in cipher_dict.values():
                # If so, cipher is false
                return cipher
            # If not, assign value to key
            cipher_dict[keys[i]] = values[i]

    # If you got this far, it's a cipher
    cipher = True
    return cipher


if __name__ == '__main__':
    import doctest
    doctest.testmod()

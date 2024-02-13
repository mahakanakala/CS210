'''
In this problem, you will be performing string length encoding and decoding. You will have to write a function for each of those.

Encoding
For this part, your function will take in a string input and return another string that keeps a count of the consecutive characters in the string in the following manner.
For e.g., "hhaaabbxwww" will be encoded as "h2a3b2x1w3". As you can see, the character count is appended next to the character. Another example: "jjjkrrjjwww" will be encoded as "j3k1r2j2w3". Notice that j occurs consecutively twice in different parts of the string and is thus handled twice.
Decoding
For this part, the input and output will be strings just like the previous function. This function will do the opposite. For e.g., "h2a3b2x1w3" will be decoded to "hhaaabbxwww".
Note: For decoding, you can assume that the number next to a character will be a single digit. You can also attempt the more general scenario where a character could occur more than 9 times in sequence, so the number following it is multi-digit.
'''

'''
Use a hashset? 
`. Keep track of the number of times a character is repeated in the sequence, until
'''

def encoding():
    encode_input = input("Enter content to be encoded: ")
    

def decoding():
    decode_input = input("Enter content to be decoded: ")
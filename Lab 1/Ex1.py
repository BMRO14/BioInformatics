# 1. Design an application which is able to find the alphabet of a given sequence.
# The alphabet means the unique symbols from which the sequence is made
# Eg. sequence S="ATTGCCCCGAAT" find the alphabet of the sequence.

def find_alphabet(sequence):
    alphabet = [];
    for char in sequence:
        if char not in alphabet:
            alphabet.append(char)
    return alphabet

sequence = "ATTGCCCCGAAT"
alphabet = find_alphabet(sequence)

print("Alphabet:", alphabet)
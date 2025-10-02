# 2. Design an application which is able to calculate the relative frequencies 
# of each symbol from the alphabet of the sequence. Use the same sequence as before

def find_alphabet(sequence):
    alphabet = [];
    for char in sequence:
        if char not in alphabet:
            alphabet.append(char)
    return alphabet

sequence = "AACCCABBB"
alphabet = find_alphabet(sequence)

def calculate_frequency(sequence, alphabet):
    frequencies = {}
    length= len(sequence)
    for char in alphabet:
        count = sequence.count(char)
        relative_frequency = (count / length) * 100
        frequencies[char] = relative_frequency
    return frequencies

frequencies = calculate_frequency(sequence, alphabet)    

print("Alphabet:", alphabet)
print("Relative Frequencies:")
for char, freq in frequencies.items():
    print(f" {char}: {freq:.2f}%")
#!/usr/bin/env python
import math
from caesar import encrypt

letter_frequencies = {
            'a': 0.082,
            'b': 0.015,
            'c': 0.027,
            'd': 0.047,
            'e': 0.13,
            'f': 0.022,
            'g': 0.02,
            'h': 0.062,
            'i': 0.069,
            'j': 0.0016,
            'k': 0.0081,
            'l': 0.04,
            'm': 0.027,
            'n': 0.067,
            'o': 0.078,
            'p': 0.019,
            'q': 0.0011,
            'r': 0.059,
            's': 0.062,
            't': 0.096,
            'u': 0.027,
            'v': 0.0097,
            'w': 0.024,
            'x': 0.0015,
            'y': 0.02,
            'z': 0.00078,
    }

def shift_dict(dic, shift):
    dic_len = len(dic)
    shift = shift % dic_len
    list_dic = [(k,v) for k, v in dic.items()]
    shifted = {
        list_dic[x][0]: list_dic[ (x - shift) % dic_len ][1]
        for x in range(dic_len)
    }
    return shifted

def chi_sqaure_decrpyt(ciphertext: str, shift: int):
    ciphertext = ciphertext.lower()
    letters = [chr(i) for i in range(97, 123)]
    shifted_letter_frequencies = shift_dict(letter_frequencies, shift)
    chi_squared_statistic_values = {}
    letters_expected_count = {}
    total_count = len(ciphertext)
    for letter in letters:
        expected_count = total_count*shifted_letter_frequencies[letter]
        letters_expected_count[letter] = expected_count
    letters_obtained_count = {}
    for letter in letters:
        letters_obtained_count[letter] = ciphertext.count(letter)
    for letter in letters:
        chi_square_value = math.pow(letters_obtained_count[letter] - letters_expected_count[letter],2)/letters_expected_count[letter]
        chi_squared_statistic_values[letter] = chi_square_value
    obtained_value = sum(chi_squared_statistic_values.values())
    return obtained_value

def main():
    cipher_text = input("Cipher text: ")
    shifted_chi_square = []
    for i in range(26):
        shifted_chi_square.append(chi_sqaure_decrpyt(cipher_text,i))
    min_chi_square_value = min(shifted_chi_square)
    print("Got the min of Chi-square value while Caesar key is ", 26 - shifted_chi_square.index(min_chi_square_value))
    print("Decrpty with this key:")
    print(encrypt(cipher_text,26 - shifted_chi_square.index(min_chi_square_value)))

if __name__ == "__main__":
    main()

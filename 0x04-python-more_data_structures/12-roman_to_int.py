#!/usr/bin/python3
def roman_to_int(roman_string):
    suma = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) == str:
        for i in range(len(roman_string) - 1):
            if roman_string[i] == 'I' and roman_string[i + 1] in ['V', 'X']:
                suma -= 1
            elif roman_string[i] == 'X' and roman_string[i + 1] in ['L', 'C']:
                suma -= 10
            elif roman_string[i] == 'C' and roman_string[i + 1] in ['D', 'M']:
                suma -= 100
            else:
                suma += roman[roman_string[i]]
        suma += roman[roman_string[-1]]
        return suma
    else:
        return 0

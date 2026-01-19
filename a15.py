# Write a Python program to input a string and count the number of vowels, consonants, digits, and space
text = input("Enter a string: ")
vowels = 0
consonants = 0
digits = 0
spaces = 0
vowel_set = "aeiouAEIOU"
for ch in text:
    if ch in vowel_set:
        vowels += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    elif ch.isalpha():
        consonants += 1
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
print("Number of digits:", digits)
print("Number of spaces:", spaces)

#user input
string = input(str('Please enter a sentence: '))

#reverser
palindrome_string = string[::-1]
print('Revers sentences : ' + str(palindrome_string))

#palindrome
def palindrome(s):
    if s == palindrome_string:
        print(True, ' : This is a palindrome!')
    else:
        print(False, ' : This is not a palindrome!')
print(palindrome(string))

#number of numbers
count1 = 0
for i in string:
    if (i.isdigit()):
        count1 = count1 + 1
print('The number of numbers in a sentence : ' + str(count1))

#number of crypts
count2 = 0
for i in string:
    if (i.split()):
        count2 = count2 + 1
print('The number of crypts in a sentence is : ' + str(count2))

#number of words
words = string.split()
numberOfwords = len(words)
print('The number of words in a sentence is : ' + str(numberOfwords))

#average word length
avgWordsLen = count2 / numberOfwords
print('The average word length is : ' + str(avgWordsLen))

#the number of vowels in a sentence
stringVowels = string.lower()
vowels = 0
listVowels = ['a', 'e', 'i', 'o', 'u']
for char in stringVowels:
    if char in listVowels:
        vowels = vowels + 1
print('The number of vowels in the sentence is : ' + str(vowels))

#the number of consonants in the sentence
stringConsonant = string.lower()
consonant = 0
listConsonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z']
for char in stringConsonant:
    if char in listConsonant:
        consonant = consonant + 1
print('The number of consonants in the sentence is : ' + str(consonant))

#uppercase and lowercase letters
def string_ul(s):
    count_ul = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    for x in s:
        if x.isupper():
            count_ul["UPPER_CASE"] += 1
        elif x.islower():
            count_ul["LOWER_CASE"] += 1
        else:
            pass
    print("Uppercase letters are : ", count_ul["UPPER_CASE"], " and lowercase letters are : ", count_ul["LOWER_CASE"])
print(string_ul(string))

#total characters
print('Lenght of sentence is : ' + str(len(string)) + ' characters.')

# Sara is participating in a writing contest, and one of the rules requires that each word in her text has a maximum character limit.

# Help Sara by creating a function that receives a word and displays the number of characters.


# THIS WAS MY SOLUTION:

# def character_counter():
#    return f'The word {typed_word} has {number_of_characters} characters.'

# typed_word = input('Enter the word to be counted: ')
# number_of_characters = len(typed_word)

# print(character_counter())

# THE PROBLEM HERE IS THAT A FUNCTION WITHOUT PARAMETERS IS LESS INDEPENDENT AND REUSABLE, BECAUSE IT DEPENDS ON EXTERNAL VARIABLES;
# IT IS LIMITED TO A PRE-DEFINED MESSAGE THAT IS RESTRICTED TO A SINGLE USE;
# IT WOULD BE HARD TO USE IN AN EXERCISE WHERE IT IS NECESSARY TO COUNT THE CHARACTERS OF MORE THAN ONE WORD AT A TIME

# LESS IS MOOOOORE!!!


def count_characters(word):
    return len(word)

text = input('Enter a word to be counted: ')
print(f'The word {text} has {count_characters(text)} characters.')
searched_word = "his_father_is_the_prof"


# Manual function
def get_Index(character, word):
    for i in range(0, len(word)):
        if(word[i] == character):
            return i


print(get_Index('h', searched_word))


# Builtin functions

print(searched_word.find('h'))

print(searched_word.index('h'))
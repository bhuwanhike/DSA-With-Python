word_1 = "MARK"
word_2 = "TWAIN"


# Manual function

def get_concatenate(word_1, word_2):

    merged_words = ""

    for i in range(0, len(word_1)):
        merged_words+= word_1[i]

    for i in range(0, len(word_2)):
        merged_words+= word_2[i]

    return merged_words

print(get_concatenate(word_1, word_2))


# Inbuilt function

print(word_1+word_2)
print(''.join([word_1, word_2]))


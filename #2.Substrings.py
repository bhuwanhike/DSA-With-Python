word_Str = "To_be_or_not_to_be"


# Manual Implementation

def get_subString(word, start, end):
    substr = ""
    if end > len(word):
        return "Ending value is out of range!"
    for i in range(start, end):
        substr += word[i]
    
    return substr


print(get_subString(word_Str, 0, 19))          


# Inbuilt method

print(word_Str[2:9])

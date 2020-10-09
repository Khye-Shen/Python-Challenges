

def main():
    word = input('Enter Phrase : ')
    final_word = rovarspraket(word)
    print(final_word)

def is_vowel(letter):
    VOWELS = ['A', 'E', 'I', 'O', 'U']
    if str.upper(letter) in VOWELS:
        return True
    else:
        return False

def rovarspraket(word):
    new_word = []
    for character in word:
        if character.isalpha() and not is_vowel(character):
            new_word.append(character + 'o' + str.lower(character))
        else:
            new_word.append(character)
    return ''.join(new_word)


main()

def get_VowelsAndConsonants(word):
    w_number = 0
    c_number = 0
    forb_chars = '0123456789!"£$%^&*()_+=¬`\|<>,./?''#~}{[]'
    w_chars = 'AEIOU'

    for letter in word:
        upper_letter = letter.upper()
        if upper_letter in forb_chars:
            print('ERROR: Please enter a valid word')
            return
        if upper_letter in w_chars:
            w_number += 1 
        else:
            c_number += 1
    
    print()
    print(str(w_number), 'vowels')
    print(str(c_number), 'consonants')


if __name__ == '__main__':
    word = input('Enter your word: ')
    get_VowelsAndConsonants(word)

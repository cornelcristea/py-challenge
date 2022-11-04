# exercice 4
# please see the README.md file

def get_NmberOfVowelsAndConsonants(word):
    w_number = 0
    c_number = 0
    n_list = '0123456789'
    w_list = 'aeiou'

    for letter in word:
        if letter in n_list:
            print('ERROR: Please enter a valid word')
            return
        elif letter in w_list:
            w_number += 1 
        else:
            c_number += 1
        
    print(str(w_number), 'vowels')
    print(str(c_number), 'consonants')

if __name__ == '__main__':
    word = input('Enter your word: ')
    get_NmberOfVowelsAndConsonants(word)

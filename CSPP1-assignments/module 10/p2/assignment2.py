import random
import string

wordlist_filename = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    in_file = open(wordlist_filename, 'r')
    # line: string
    each_line = in_file.readline()
    # wordlist: list of strings
    word_list = each_line.split()
    print("  ", len(word_list), "words loaded.")
    return word_list

def choose_word(word_list):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    random_word = random.choice(word_list)
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is "+str(len(random_word))+" letters long.")
    print("---------")
    return random_word

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
word_list = load_words()

def get_available_letters(letters_guessed):
    '''
    :param letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    avaiable_letters = ""
    for i_iterator in string.ascii_lowercase:
        if i_iterator not in letters_guessed:
            avaiable_letters += i_iterator
    return avaiable_letters

def print_log(no_of_guesses, available_letters):
    '''print log'''
    print("You have "+str(no_of_guesses)+" guesses left.")
    print("Available letters: "+available_letters)
    user_input = input("Please guess a letter: ")
    return user_input.lower()

def is_guess_right(user_input, secret_word, available_letters, letters_guessed):
    '''is guess right'''
    if user_input in secret_word:
        available_letters = get_available_letters(letters_guessed)
        return (True, available_letters)
    return (False , available_letters)

def replace_by(secret_word, secret_word_copy):
    ''' in replace '''
    #print(secret_word)
    for each_item in secret_word_copy:
        loc_letter = secret_word.index(each_item)
        secret_word.remove(each_item)
        secret_word.insert(loc_letter, '_')
    #print(secret_word)
    return secret_word

def convert_list_to_string(secret_word):
    ''' in convert list to string'''
    str_1 = ''.join(str(e_i) for e_i in secret_word)
    return str_1

def get_guessed_word(secret_word, letters_guessed):
    '''
    in get guesses word
    '''
    # FILL IN YOUR CODE HERE...
    secret_word = list(secret_word)
    secret_word_copy = secret_word[:]
    secret_word1 = secret_word[:]
    i_iterator = ""
    for i_iterator in letters_guessed:
        if i_iterator in secret_word:
            secret_word_copy = list(filter(lambda
                lambda_param:
                                           lambda_param != i_iterator, secret_word))
            secret_word = list(filter(lambda
                lambda_param:
                                      lambda_param != i_iterator, secret_word))
        if not secret_word:
            return convert_list_to_string(secret_word1)
    if secret_word:
        secret_word_copy = replace_by(secret_word1, secret_word_copy)
        #print(secret_word_copy)
        return convert_list_to_string(secret_word_copy)
    return ""

def play_hangman(secret_word):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    no_of_guesses = 8
    available_letters = string.ascii_lowercase
    user_input = ""
    letters_guessed = []
    result_of_guess = "".join('_' for each_word in secret_word)

    while no_of_guesses >= 1:
        user_input = print_log(no_of_guesses, available_letters)
        is_right = is_guess_right(user_input, secret_word, available_letters, letters_guessed)
        available_letters = is_right[1]
        if user_input in letters_guessed:
            letters_guessed.append(user_input)
            available_letters = get_available_letters(letters_guessed)
            print("Oops! You've already guessed that letter: "+ result_of_guess)
            print("---------")
        elif is_right[0] is True:
            letters_guessed.append(user_input)
            available_letters = get_available_letters(letters_guessed)
            result_of_guess = get_guessed_word(secret_word, letters_guessed)
            print("Good guess: "+result_of_guess)
            print("---------")
        else:
            letters_guessed.append(user_input)
            available_letters = get_available_letters(letters_guessed)
            no_of_guesses = no_of_guesses - 1
            print("Oops! That letter is not in my word: "+result_of_guess)
            print("---------")
        if result_of_guess == secret_word:
            print("Congratulations, you won!")
            break
    if no_of_guesses < 1:
        print("Sorry, you ran out of guesses. The word was "+secret_word+".")

def main():
    '''
    Main function for the given program
    
    When you've completed your hangman function, uncomment these two lines
    and run this file to test! (hint: you might want to pick your own
    secretWord while you're testing)
    '''
    secret_word = choose_word(word_list).lower()
    #secretWord = "apple"
    play_hangman(secret_word)


if __name__ == "__main__":
    main()

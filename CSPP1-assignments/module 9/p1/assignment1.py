def is_word_guessed(secret_word, letters_guessed):
    '''
    in is_word_guessed function
    '''
    # FILL IN YOUR CODE HERE...
    secret_word = list(secret_word)
    secret_letter = ""
    for secret_letter in letters_guessed:
        if secret_letter in secret_word:
            lambda_solution = filter(lambda lambda_params:
                                     lambda_params != secret_letter, secret_word)
            secret_word = list(lambda_solution)
        if not secret_word:
            return "True"
    if not secret_word:
        return "True"
    return "False"
def main():
    '''
    Main function for the program
    '''
    user_input = input()
    if user_input:
        data = user_input.split()
        secret_word = data[0]
    else:
        data = []
        secret_word = ""
    list1 = []
    for j in range(1, len(data)):
        list1.append(data[j][0])
    print(is_word_guessed(secret_word, list1))

if __name__ == "__main__":
    main()

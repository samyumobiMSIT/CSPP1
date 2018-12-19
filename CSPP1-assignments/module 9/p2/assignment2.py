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

def main():
    '''
    Main function for current assignment
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
    print(get_guessed_word(secret_word, list1))

if __name__ == "__main__":
    main()

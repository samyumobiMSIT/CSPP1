def is_validword(input_word, player_hand, word_list):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    is_in_hand = False
    is_in_wordlist = False
    check_flag = 0
    for each_word in input_word:
        if each_word not in player_hand:
            check_flag = 1
    if not check_flag:
        is_in_hand = True
    if input_word in word_list:
        is_in_wordlist = True

    if is_in_hand and is_in_wordlist:
        return True
    return False

def main():
    '''in main function'''
    input_word = input()
    test_cases = int(input())
    a_dict = {}
    for i in range(test_cases):
        da_ta = input()
        l_1 = da_ta.split()
        a_dict[l_1[0]] = int(l_1[1])
        i = i + 1
    l_2 = input().split()
    print(is_validword(input_word, a_dict, l_2))


if __name__ == "__main__":
    main()

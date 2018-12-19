

def update_hand(player_hand, input_word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
    for each_word in input_word:
        #print(i)
        if each_word in list(player_hand.keys()):
            #print(hand[i])
            player_hand[each_word] -= 1
    return player_hand

def main():
    '''in main funtion'''
    no_test_cases = input()
    a_dict = {}
    for i_iterator in range(int(no_test_cases)):
        da_ta = input()
        l_data = da_ta.split()
        a_dict[l_data[0]] = int(l_data[1])
        i_iterator += 1
    input_word = input()
    print(update_hand(a_dict, input_word))


if __name__ == "__main__":
    main()

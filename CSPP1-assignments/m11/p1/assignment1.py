
def get_word_word_score(input_word, word_length):
    """
    Returns the word_score for a word. Assumes the word is a valid word.

    The word_score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are word_scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # TO DO ... <-- Remove this comment when you code this function
    scrabble_letter_values = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
        'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
        's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}

    word_score = 0
    for i in input_word:
        word_score += scrabble_letter_values[i]

    word_score *= len(input_word)
    if len(input_word) >= word_length:
        word_score = word_score + 50
    return word_score


def main():
    '''
    Main function for the given problem
    '''
    data = input()
    data = data.split()
    print(get_word_word_score(data[0], int(data[1])))


if __name__ == "__main__":
    main()

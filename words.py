def print_upper_words(words, must_start_with):
    """Print each word in the words list in uppercase and on a newline

    Args:
        words (list): list of strings
        must_start_with (set): set of letters
    """
    for word in words:
        first_letter = word.lower()[0]
        for char in must_start_with:
            if first_letter == char:
                print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})
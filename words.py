def print_upper_words(words):
    """Print each word in the words list in uppercase and on a newline

    Args:
        words (list): list of strings
    """
    for word in words:
        if word[0] == 'e' or word[0] == 'E':
            print(word.upper())
        
        
print_upper_words(['fish', 'cat','dog','duck', 'eagle'])
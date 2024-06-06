# this should print "HELLO", "HEY", "YO", and "YES"

def print_upper_words(words, must_start_with):
    """Print each word in the list on a separate line in uppercase,
    but only if the word starts with one of the specified letters.
    
    Args:
    words (list of str): List of words to be printed in uppercase.
    must_start_with (set of str): Set of letters that the words must start with.
    """
    for word in words:
        if word[0].lower() in must_start_with:
            print(word.upper())

# Test the function
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], {'h', 'y'})

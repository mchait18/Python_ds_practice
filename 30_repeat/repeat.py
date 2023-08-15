def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
    newPhrase = ''
    if isinstance(num, int) and num >= 0:
        for i in range(num):
            newPhrase += phrase
        return newPhrase
    return None
    
    
    #return[phrase += phrase for i in range(num) if is_integer(num)]
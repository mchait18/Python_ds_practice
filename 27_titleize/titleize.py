def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    # newStr = ''
    # separate_words = phrase.split(" ")
    
    # for word in separate_words:
    #     newStr += f"{word.capitalize()} "
    # return newStr.strip()

    return " ".join([word.capitalize() for word in phrase.split(" ")]) 



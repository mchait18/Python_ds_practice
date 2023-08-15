def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    # list1 = str(num1)
    # list2 = str(num2)

    for dig in str(num1):
        if str(num1).count(dig) != str(num2).count(dig):
            return False
    return True    

    
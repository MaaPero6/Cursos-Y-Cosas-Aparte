def number_pattern(n):
    pattern = ""

    if type(n) is not int:
        return "Argument must be an integer value."

    if n<1:
        return "Argument must be an integer greater than 0."

    for number in range(1, n+1):
        pattern += str(number) + " "
    
    return pattern.strip()
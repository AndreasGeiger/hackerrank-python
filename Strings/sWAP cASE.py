def swap_case(s):
    returnString = ""

    for character in s:
        if character.islower():
            returnString += character.upper()
        else:
            returnString += character.lower()

    return returnString

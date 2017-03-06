if __name__ == '__main__':
    s = input()
    isalphanum = False
    isalpha = False
    isdigit = False
    islower = False
    isupper = False

    for char in s:
        if char.isalnum():
            isalphanum = True
        if char.isalpha():
            isalpha = True
        if char.isdigit():
            isdigit = True
        if char.islower():
            islower = True
        if char.isupper():
            isupper = True

    print(isalphanum)
    print(isalpha)
    print(isdigit)
    print(islower)
    print(isupper)

def capitalize(string):
    return ' '.join(map(str.capitalize, string.split(' ')))


if __name__ == '__main__':
    #string = input()
    capitalized_string = capitalize("hello world")
    print(capitalized_string)

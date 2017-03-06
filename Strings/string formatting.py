def print_formatted(number):
    width = len(str(bin(n)))-2
    for i in range(1, number + 1 ):
        decimal = i
        octal = oct(i)
        hexadecimal = hex(i)
        binary = bin(i)

        print(str(decimal).rjust(width), octal[1:].rjust(width), hexadecimal[2:].upper().rjust(width), binary[2:].rjust(width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)



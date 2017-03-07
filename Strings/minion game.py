def minion_game(string):
    string = string.lower()
    scoreStuart = 0
    scoreKevin = 0
    vowels = 'aeiou'
    for j, i in enumerate(string):
        if i not in vowels:
            scoreStuart += len(string) - j
        if i in vowels:
            scoreKevin += len(string) - j
    if scoreStuart > scoreKevin:
        print('Stuart', scoreStuart)
    elif scoreKevin > scoreStuart:
        print('Kevin', scoreKevin)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)

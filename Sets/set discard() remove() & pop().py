amountNumbers = int(input())
arrNumbers = set(map(int, input().split()))
amountCommands = int(input())


for i in range(amountCommands):
    command = input().split()

    if command[0] == "pop":
        arrNumbers.pop()
    elif command[0] == "remove":
        if int(command[1]) in arrNumbers:
            arrNumbers.remove(int(command[1]))
    elif command[0] == "discard":
        if int(command[1]) in arrNumbers:
            arrNumbers.discard(int(command[1]))

print(sum(arrNumbers))

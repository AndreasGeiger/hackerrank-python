amountCommands = int(input())

testList = []

#read 'amountCommands' the user input and do the command
for i in range(amountCommands):
    userInput = input()
    userInput = userInput.split()

    command = userInput[0]
    
    if command == "insert":
        testList.insert(int(userInput[1]), int(userInput[2]))
    elif command == "print":
        print(testList)
    elif command == "remove":
        testList.remove(int(userInput[1]))
    elif command == "append":
        testList.append(int(userInput[1]))
    elif command == "sort":
        testList.sort()
    elif command == "pop":
        testList.pop()
    else:
        testList.reverse()
        
    

    
    

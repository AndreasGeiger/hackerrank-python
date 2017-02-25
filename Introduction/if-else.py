userInput = int(input())

if userInput%2 == 0 and ((userInput >= 2 and userInput <= 5) or userInput > 20):
    print("Not Weird")
else:
    print("Weird")

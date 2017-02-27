#read three coordinates and the number
x = int(input())
y = int(input())
z = int(input())
number = int(input())

listCoordinates = []

#save the possibilities as list into the listCoordinates
for i in range(x+1):
    for j in range(y+1):
        for l in range(z+1):
            if i+j+l != number:
                listCoordinates.append([i,j,l])

print(listCoordinates)
            


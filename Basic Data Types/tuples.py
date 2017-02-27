#input
amountNumbers = int(input())

#numbers seperated by spaces into list
integer_list = map(int, input().split())

#list to tuple
tuple_list = tuple(integer_list)

print(hash(tuple_list))
    

# item_list = [1, 2, 3, 4, [5, 6, 7], 8]

item_list = eval(input("enter the list "))

sum = 0

for item in item_list:
    if type(item) == list:
        for i in item:
            sum = sum + i
    else:
        sum = sum + item


print(item_list)
print(sum)
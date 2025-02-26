#Tuple = collection which is ordered and unchangeable
            #used to group together related data
            
# my_tuple = (10, 20, 30, 40, 50)

# print(my_tuple[2])


# numbers = (5, 10, 15, 20, 25)
# slice = numbers[2:5]
# print(slice)

# my_list = [1, 2, 3, 4, 5]
# my_list[0] = 10
# print(my_list)  

fruits = ("orange","banana","apple")
fruit_list = list(fruits)

fruit_list.append("mango")

fruits = tuple(fruit_list)
print(fruits)
my_list = [] # empty list

for i in range(1, 5): # loop from 1 to 4 to append values to the list
    my_list.append(i * 10)

my_list[1] = 15 # change the second element to 15

another_list = [50, 60, 70] # another list with three elements
my_list.extend(another_list) # extend my_list with another_list

my_list.remove(my_list[-1]) # remove the last element from my_list

my_list.sort() # sort the final list

index_of_30 = my_list.index(30) # find the index of the value 30
print(index_of_30) # print the index of the value 30

print(my_list) # print the final list
# APPEND
fruit = ['orange', 'apple', 'banana']
fruit.append('grape')
print(fruit)

#CLEAR
fruit = ['orange', 'apple', 'banana']
fruit.clear()
print(fruit)


#POPPING
my_list = [1, 2, 3, 4]
print(my_list.pop()) 
  # Output: 3
print(my_list)         # Output: [1, 2]

my_list = [1, 2, True, "a"]
index = my_list.index("a")
print(index)  # Output: 1


my_list = [3, 1, 2]
n = sorted(reverse=True)
# n.reverse()
print(n)  # Output: [1, 2, 3]

original_list = [1, 2, 3]
copied_list = original_list.copy()
print(copied_list)  # Output: [1, 2, 3]


my_list = 1, 2, 3, 4, 5
print(type(my_list))









import random

names = names_string.split(", ")

length_of_names = len(names)
first_name_index = names.index(names[0])
last_name_index = names.index(names[length_of_names - 1]) 

random_name_index = random.randint(first_name_index, last_name_index)
random_name = names[random_name_index]

print(f"{random_name} is going to buy the meal today!")

# Optimized Code
# names = names_string.split(", ")

# # Get the total number of items in list.
# num_items = len(names)
# # Generate random numbers between 0 and the last index. 
# random_choice = random.randint(0, num_items - 1)
# # Choose and print a random name.
# print(names[random_choice])
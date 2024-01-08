# Our Version
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
name = name1 + " " + name2
name_in_capital = name.upper()
count_of_t = name_in_capital.count("T")
count_of_r = name_in_capital.count("R")
count_of_u = name_in_capital.count("U")
count_of_e = name_in_capital.count("E")

count_of_l = name_in_capital.count("L")
count_of_o = name_in_capital.count("O")
count_of_v = name_in_capital.count("V")
count_of_e = name_in_capital.count("E")

total_count_of_true = count_of_t + count_of_r + count_of_u + count_of_e
total_count_of_love = count_of_l + count_of_o + count_of_v + count_of_e

true_count_in_str = str(total_count_of_true)
love_count_in_str = str(total_count_of_love)

love_score = true_count_in_str + love_count_in_str
love_score = int(love_score)

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")


# Optimized Version
print("The Love Calculator is calculating your score...")
name1 = input()
name2 = input()

combined_names = (name1 + name2).upper()

count_of_true = combined_names.count("T") + combined_names.count("R") + combined_names.count("U") + combined_names.count("E")
count_of_love = combined_names.count("L") + combined_names.count("O") + combined_names.count("V") + combined_names.count("E")

love_score = int(str(count_of_true) + str(count_of_love))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

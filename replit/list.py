# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num_count=len(names)
ran_num=random.randint(0,num_count-1)
bill_pay=names[ran_num]
print(f"The bill to be paid by {bill_pay}")
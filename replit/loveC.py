# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
new_name=name1+name2
lower_string=new_name.lower()
t=lower_string.count("t")
r=lower_string.count("r")
u=lower_string.count("u")
e=lower_string.count("e")
true=t+r+u+e
l=lower_string.count("l")
o=lower_string.count("o")
v=lower_string.count("v")
e=lower_string.count("e")
love=l+o+v+e
result=int(str(true)+str(love))
if (result < 10) or (result > 90):
    print(f"your score is {result},you go together like coke and mentos")
elif (result > 40) and (result < 50):
    print(f"your score is {result},you are alright together")
else:
    print(f"your score is {result}.")




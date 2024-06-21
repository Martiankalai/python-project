rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
game=["rock","paper","scissors"]
print(game)
choice=input("Enter your choice")
if choice=="rock":
  print(rock)
elif choice=="paper":
  print(paper)
else:
  print(scissors)
ran_num=random.randint(0,2)
if ran_num==0:
  comp_choose="rock"
  print(f"Computer choose {rock}")
elif ran_num==1:
  comp_choose="paper"
  print(f"Computer choose{paper}")
else:
  comp_choose="scissors"
  print(f"Computer choose{scissors}")
if choice==comp_choose:
  print("Tie")
elif choice=="rock" and comp_choose=="scissors":
  print("You Win")
elif choice=="rock" and comp_choose=="paper":
  print("You lose")



  



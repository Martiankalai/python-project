# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum_heights=0
f=len(student_heights)
for n in student_heights:
    sum_heights+=n
print(sum_heights)
avg=sum_heights/f
print(round(avg))




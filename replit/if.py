#Write your code below this row 👇
for i in range(1,101):
    if i % 3==0 and i % 5==0:
        i="fizzbuzz"
        print(i)
    elif i % 5==0:
        i="buzz"
        print(i)
    elif i % 3==0:
        i="fizz"
        print(i)
    else:
        print(i)
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

combined=name1+name2
tolower=combined.lower()

t=tolower.count("t")
u=tolower.count("u")
r=tolower.count("r")
e=tolower.count("e")
num1=10*(t+r+u+e)

l=tolower.count("l")
o=tolower.count("o")
v=tolower.count("v")
e=tolower.count("e")
num2=l+o+v+e

final=num1+num2
if final<10 or final>90:
  print(f"Your score is {final}, you go together like coke and mentos.")
elif final>40 and final<50:
  print(f"Your score is {final}, you are alright together.")
else:
  print(f"Your score is {final}.")
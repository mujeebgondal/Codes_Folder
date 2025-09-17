import random
q=input("Ask Question: ")
n=random.randint(1, 9)
if n == 1:
  print("Yes - definitely.")
elif n == 2:
  print("It is decidedly so.")
elif n == 3:
  print("Without a doubt")
elif n == 4:
  print("Reply hazy , try again")
elif n == 5:
  print("Ask again later")
elif n == 6:
  print("Better not tell yoy now")
elif n == 7:
  print("My source say no")
elif n == 8:
  print("Outlook not so good")
else :
  print("Very doubtful")

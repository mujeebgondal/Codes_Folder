import random
q=input("Question: ")
n=random.randint(1, 9)
if n == 1:
  ans='Yes - definitely.'
elif n == 2:
  ans='It is decidedly so.'
elif n == 3:
  ans='Without a doubt.'
elif n == 4:
  ans='Reply hazy , try again.'
elif n == 5:
  ans='Ask again later.'
elif n == 6:
  ans='Better not tell yoy now.'
elif n == 7:
  ans='My source say no.'
elif n == 8:
  ans='Outlook not so good.'
elif n == 9:
  ans='Very doubtful.'
else :
  ans='error'
print("majic 8 ball", ans)


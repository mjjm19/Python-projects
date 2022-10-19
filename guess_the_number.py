import random

def guess(x):
  randomno=random.randint(1,x)
  guess=0
  while(guess!=randomno):
      guess=int(input('Guess a number between 1 and {}: '.format(x)))
      if(guess>randomno):
            print('Sorry, too high. Try again')
      elif(guess<randomno):
            print('Sorry, too low. Try again')
      else:
          print('Yaay, congrats you have guessed it right')


def comp_guess(x):
  low=1
  high=x
  feedback=''
  while(feedback!='c'):
    if(low!=high):
      guess=random.randint(low,high)
    else:
      guess=low
    feedback=input('Is {} too high (h) or too low (l) or correct (c)?'.format(guess))
    if(feedback=='h'):
      high=guess-1
    elif(feedback=='l'):
      low=guess+1
  print('Yaay comp, you have guessed it right')


#guess(10)
comp_guess(100)
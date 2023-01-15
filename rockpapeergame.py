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
select=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
list1=[rock,paper,scissors] #rock paper scissor ko ek list mae save taki randomly generate kr ske
try:
    print(list1[select])
    computerChoice=random.randint(0,2)
    print(list1[computerChoice])
    if computerChoice==2 and select==0:
        print("You win")
    elif select>computerChoice:
        print("You win")
    elif select==computerChoice:
        print("it's a Draw")
    else:
        print("You loose")
except:
    if select<0 or select>2:
        print("invalid input Hence you loose")



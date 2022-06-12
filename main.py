import  random

def rock(user, computer):
    if user == computer:
        print ('player: ', 'rock')
        print ('computer: ', 'rock')
        print("Tie")
        play('','')
    elif computer == 'S' :
        print ('player: ', 'rock')
        print ('computer: ', 'scissors')
        print ('You Win')
    elif computer == 'P':
        print ('player: ', 'rock')
        print ('computer: ', 'papper')
        print ('Sorry, you lose :(')
    else:
        print('unknown Error')

def papper(user, computer): 
    if user == computer:
        print ('player: ', 'papper')
        print ('computer: ', 'papper')
        print("Tie")
        play('','')
    elif computer == 'R' :
        print ('player: ', 'papper')
        print ('computer: ', 'rock')
        print ('You Win')
    elif computer == 'S':
        print ('player: ', 'papper')
        print ('computer: ', 'Scissors')
        print ('Sorry, you lose :(')
    else:
        print('unknown Error')
   

def scissors(user, computer):  
    if user == computer:
        print ('player: ', 'scissors')
        print ('computer: ', 'scissors')
        print("Tie")
        play('','')
    elif computer == 'P':
        print ('player: ', 'scissors')
        print ('computer: ', 'papper')
        print ('You Win')
    elif computer == 'R':
        print ('player: ', 'scissors')
        print ('computer: ', 'rock')
        print ('Sorry, you lose :(')
    else:
        print('unknown Error')


def play (user, computer):
    print('Game of rock, papper, scissors. :)')
    print('R for rock')
    print('P for papper')
    print ('S for scissors')
    user = input('Enter either R, S or P: ')
    list = ['R', 'P', 'S']
    computer = random.choice(list)
   
    if user ==  list[0]:       
        rock(user,computer)
    elif user  == list[1]:
        papper(user,computer)
    elif user == list[2]:     
        scissors(user,computer)
    else:
        print ('Invalid Input, Try again')
        play('','')
    
play('','')




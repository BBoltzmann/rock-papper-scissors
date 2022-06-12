# import random

# def play():
#     user = input("please pick an option between R, P or S :} : ") 

#     computer = random.choice(['R','P','S'])

#     if user == computer:
#         return  "you: {}, Computer: {} \n Its a Tie".format(computer)
    
#     # R>S, S>P,  P>R
#     if  isWin(user, computer):
#         return  "you: {}, Computer: {} \n You Win!!".format(user,computer)

#     return "you: {}, Computer: {} \n You Lose :(".format(user,computer)


# def isWin(player,opponent):
#     # return  true if player wins
#     if (player == 'R' and opponent  == 'S') or (player == 'S' and opponent == 'P') or (player == 'P' and opponent=='S'):
#         return True
#     return False

# if __name__ == '__main__':
#     print(play())

#     # if (player=='R'  and opponent == 'S') or (player == "S" and  opponent ==  'P') or (player == 'P' and  opponent 'R'):
#     #     return True  
#     # return False



# def user(user):
#     if user == list[0]:
#         user = 'R'   
#         print (user)
#     elif user==  list[1]:
#         user = 'S' 
#         print (user)
#     elif user ==  list[2]:
#         user = 'P' 
#         print (user)
#     else:
#         print ('invalid input')
#     return user

# user('')


# i = 0
# for i in list:
#     if i == 'R':
#         print ('R')
#     elif i == 'S':
#         print('S')
#     elif i == 'P':
#         print('P')
    
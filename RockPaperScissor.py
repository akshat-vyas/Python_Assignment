#script of rock,paper,scissor game
print("Remember the rules:")
print("rock beats scissors")
print("scissors beats paper")
print("paper beats rock")
user1=input("enter your choice: ")
user2=input("enter your choice: ")
if user1==user2:
 print("it is a tie!!")
elif user1=="rock" and user2=="paper":
 print("user2 wins")
elif user1=="rock" and user2=="scissor":
 print("user1 wins")
elif user1=="paper" and user2=="rock":
 print("user1 wins")
elif user1=="paper" and user2=="scissor":
 print("user2 wins")
elif user1=="scissor" and user2=="paper":
 print("user1 wins")
elif user1=="scissor" and user2=="rock":
 print("user2 wins")
else:
 print("invalid choice!!please choose rock,paper,scissor")

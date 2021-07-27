import random

def random1():
    take_stick = random.randint(1,2)
    return take_stick

def get_name():
    name = input("What is your name: ")
    return name

def python(take_stick):
    take_stick = 3 - take_stick
    print("I. smart computer, take", take_stick )
    return take_stick

def p1take(sticks):
    if (sticks + 2)%3 == 0 :
       take_stick = random1()               
    if (sticks + 2)%3 == 1 :
       take_stick = 1 
    if (sticks + 2)%3 == 2 :
       take_stick = 2 
    print("I, smart computer, take", take_stick ) 
    return take_stick
    
def main():
  player_turn = 1
  name = get_name()
  print("Player1 : Python" ,"\n" "Player2 : " + str(name),"\n")
  sticks = int(input("How many sticks in the pile: "))
  print("There are", sticks, "sticks in the pile.")
  
  if (sticks + 2)%3 != 0 :
     while True:
         if sticks > 1 :  
              print("Turn: Player", player_turn)
              if player_turn == 1:
                  take_stick = p1take(sticks)
              if player_turn == 2:  
                  take_stick = int(input(str(name) + ", How many sticks do you want to take? (1 or 2): "))
                  if take_stick < 1 or take_stick > 2:
                      print("Sorry, that's not a valid number.")
                      continue
              sticks -= take_stick 
              print("There are", sticks, "sticks in the pile.")
              player_turn += 1
              if player_turn == 3:
                  player_turn -= 2

         if sticks <= 1:
             print("Turn: Player", player_turn)
             if player_turn == 1:
                 take_stick = 1
                 print("I, smart computer, takes the last stick.", "\n")
                 print(str(name) + ", wins! (I, smart computer, am sad ;---;)") 
             if player_turn == 2:     
                 take_stick = int(input(str(name) + ", How many sticks do you want to take? (1 or 2): "))       
                 if take_stick < 1 or take_stick > 1:
                     print("Sorry, that's not a valid number.", "\n")
                     continue
                 print(str(name) + ", takes the last stick.", "\n")
                 print("I, smart computer, wins! >-<")             
             break        
         
  else :
     while True:
         if sticks > 1 :  
              print("Turn: Player", player_turn)
              if player_turn == 1:
                  take_stick = p1take(sticks)
              if player_turn == 2:  
                  take_stick = int(input(str(name) + ", How many sticks do you want to take? (1 or 2): "))
              if take_stick < 1 or take_stick > 2:
                  print("Sorry, that's not a valid number.")
                  continue
              sticks -= take_stick 
              print("There are", sticks, "sticks in the pile.")
              player_turn += 1
              if player_turn == 3:
                  player_turn -= 2
                  
         if sticks <= 1:
             print("Turn: Player", player_turn)
             if player_turn == 1:
                 take_stick = 1
                 print("I, smart computer, takes the last stick.", "\n")
                 print(str(name) + ", wins! (I, smart computer, am sad ;---;)") 
             if player_turn == 2:     
                 take_stick = int(input(str(name) + ", How many sticks do you want to take? (1 or 2): "))       
                 if take_stick < 1 or take_stick > 1:
                     print("Sorry, that's not a valid number.", "\n")
                     continue
                 print(str(name) + ", takes the last stick.", "\n")
                 print("I, smart computer, wins! >-<")             
             break 

main()

"""
How the computer (Python) should think?
    Ans. max taken is 2 so n = 2 -> (sticks + 2)%3 != 0 and the reminder will be the number of python taken.
         [(sticks + n)%(n+1) ; n is maximun number of stick taken.]

Is it true that: If the computer (Python) does the first move, she will always win.
    Ans. Yes, she will always win if (sticks + 2)%3 not equal to 0.

What if the number of sticks change to any number, will AI the strategy change?
    Ans. It doesn't have to change strategy if want to change the number of sticks, 
         unless you want to change min or max number of stick taken.
         example take 1 or 3 then n = 3 magic number is 3 + 1 = 4 so change (sticks + 2)%3 to (sticks + 3)%4

"""

import random

def get_name():
    return input("What is you name : ")


def start(sticks):
    print("There are", sticks, "sticks in the pile.")


def main():
    name = get_name()
    print("Player1 : " + str(name) ,"\n" "Player2 : Python" "\n")
    sticks = 20
    start(20)
 
    while True:
        sticks = sticks
        if sticks > 3 :
            sticks_taken = int(input(str(name) + ", How many you will take (1 or 2): "))
            sticks = sticks - sticks_taken
            print("There are", sticks, "sticks in the pile.")
            python_take = 3 - sticks_taken
            sticks = sticks - python_take
            print( "I, python, take" , python_take,)
            print("There are", sticks, "sticks in the pile.")
        elif sticks <= 3 and sticks >= 2  :
            sticks_taken = int(input(str(name) + ", How many you will take (1 or 2): "))
            sticks = sticks - sticks_taken
            print("There are", sticks, "sticks in the pile.")
            python_take = 1
            sticks = sticks - python_take
            print( "I, python, take" , python_take,)
            print("There are", sticks, "sticks in the pile.")            
        elif sticks == 1 or sticks <= 0:
            print ("You take the last stick")
            print("Python won!")
            break
        if sticks_taken >2 or sticks_taken <1:
            print( "Wrong choice")
            continue    

        
main()
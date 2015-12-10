import time
import random

# game function
def game():

print ("*****************")
print ("Cave of the Void!")
print ("*****************")

time.sleep(3)

print ("You enter a dark cavern out of curiosity. All that is around you is a feeling of nothingness. You try and reach for a wall, but something touches you. You scream and turn around, its only a small stick.")
ch1 = str(input("Do you take it? yes or no? "))

# STICK TAKEN
if ch1 in ['Yes', 'YES', 'yes']:
    print("You have pulled the stick out of the wall.")
    time.sleep(2)
    stick = 1

# STICK NOT TAKEN
else:
    print("You have left the stick in the wall for some reason.")
    stick = 0

print ("As you wander in the darkness you see a faint glow off in the distance.")
ch2 = str(input("Do you approach the glow? yes or no?"))

# APPROACH THE GLOW
if ch2 in ['Yes', 'YES', 'yes']:
    print ("You went towards the light...")
    time.sleep(2)
    print ("As you draw closer, the source starts to become clear to you.")
    time.sleep(1)
    print ("The glow is coming from the torch held by a guardian knight of a vast treasure!")
    ch3 = str(input("The urge of fight or flight comes to you. Do you fight for your life and the gold? yes or no?"))

    # FIGHT THE KNIGHT
    if ch3 in ['Yes', 'YES', 'yes']:

        # WITH STICK
        if stick == 1:
            print ("You only have a stick to fight with! The knight has a long sword. This doesn't look good.")
            print ("You quickly jab the knight in it's eye and gain an advantage")
            time.sleep(2)
            print ("************************************************")
            print ("                  Fighting                      ")
            print ("   YOU MUST HIT ABOVE A 5 TO KILL THE Knight    ")
            print ("IF THE Knight HITS HIGHER THAN YOU, YOU WILL DIE")
            print ("************************************************")
            time.sleep(2)
            fdmg1 = int(random.randint(3, 10))
            edmg1 = int(random.randint(1, 5))
            print ("you hit a", fdmg1)
            print ("the Knight hits a", edmg1)
            time.sleep(2)

            if edmg1 > fdmg1:
                print ("The Knight has dealt more damage than you! The Knight leaves you bleeding on the floor.")
                complete = 0
                return complete

            elif fdmg1 < 5:
                print ("You didn't do enough damage to kill the Knight, what a shock, but you manage to escape from the Knight's impaired vision.")
                complete = 1
                return complete

            else:
                print ("By some grace of the divines you manage to knock the Knight out by hitting it on the head! You grab some gold and run.")
                complete = 1
                return complete

        # WITHOUT STICK
        else:
            print ("You don't have anything to fight with!")
            time.sleep(2)
            print ("                  Fighting...                   ")
            print ("   YOU MUST HIT ABOVE A 5 TO KILL THE Knight    ")
            print ("IF THE Knight HITS HIGHER THAN YOU, YOU WILL DIE")
            print ("************************************************")
            time.sleep(2)
            fdmg1 = int(random.randint(1, 7))
            edmg1 = int(random.randint(1, 5))
            print ("you hit a", fdmg1)
            print ("the Knight hits a", edmg1)
            time.sleep(2)

            if edmg1 > fdmg1:
                print ("The Knight has run you through with his sword. Damaging you for more!")
                complete = 0
                return complete

            elif fdmg1 < 5:
                print ("You didn't do enough damage to kill the Knight, but you are quicker than he is and manage to escape")
                complete = 1
                return complete

            else:
                print ("With sight of you defending yourself with no weapon the Knight laughed so hard he fell over and hit his head on a rock. go figure! ")
                complete = 1
                return complete

    #DON'T FIGHT THE KNIGHT
    print ("You choose not to fight the Knight and leave the gold alone.")
    time.sleep(1)
    print ("As you turn away, the Knight shoots an arrow and hits you in the knee.")
    complete = 0
    return complete

# DON'T APPROACH Knight
else:
        print ("You turn away from the glowing object, and attempt to leave the cave...")
        time.sleep(1)
        print ("But something won't let you, the glow calls to you.")
        time.sleep(2)
        complete = 0
        return complete

# game loop
alive = True
while alive:

complete = game()
if complete == 1:
    alive = input('You managed to escape the cave alive! Would you like to play again? yes or no? ')
    if alive in ['YES', 'yes', 'Yes',]:
        alive

    else:
        break

else:
    alive = input('The void has come calling and has taken your life. You have died! Would you like to play again? yes or no. ')
    if alive in ['YES', 'yes', 'Yes',]:
        alive

    else:
        break

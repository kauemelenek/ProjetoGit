print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')
print('Welcome to Treasure Island.')
print('Your mission is to find te treasure.')

path = input('Choose a path: left or right?\n ').lower()
if path == 'right':
    print('You found several starving lions. You died.')

elif path == 'left':
    print('You choose left. After some walk you found a lake.')
while path != 'right' and path != 'left':
    print('Invalid answer, please try again...')
    input('Choose a path: left or right?:\n ').lower()


lake = input('After some time, you discovered a path across the lake, do you wanna wait or swim?:\n ').lower()
if lake == 'swim':
    print('You swimed for so long that you died of starvation.')
elif lake == 'wait':
    print('You waited and the lake dried, opening a way for you to across it. ')
    print('After across the lake, you found the entrance of a house. The house has 3 doors: blue, red and yellow.')
while lake != 'wait' and lake != 'swim':
    print('Invalid answer, please try again...')
    input('swim or wait?:\n ').lower()

door = (input('Wich door do you choose?:\n ')).lower()
if door == 'blue':
    print('There was a viper snake in the room, she attacked you and you died.')
elif door == 'red':
    print('There was a fire demon behind the door, He attacked you and you burned to death.')
elif door == 'yellow':
    print('There was a giant treasure chest waiting for you.')
    print('CONGRATS! YOOU FOUND THE TREASURE!!!')
while door != 'red' and door != 'blue' and door != 'yellow':
    print('Please, choose the right color for the door...')
    input('Wich door do you choose?:\n ').lower()



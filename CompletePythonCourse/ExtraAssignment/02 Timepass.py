# # Band name generator
# print('Welcome to the Band Name Generator.')
# city_name = input('What\'s name of the city you grew in?\n')
# pet_name = input('What\'s your pet\'s name?\n')
# print('Your band name could be ' + city_name + ' ' + pet_name)
# print(6.0-0)

# # Bill Split and Tip Calculator: If the bill was $124.56, split between 7 people, with 12% tip.
# # Output Each person should pay: $19.93
# print('Welcome to the tip calculator!')
# bill = float(input('What was the total bill? $'))
# tip = int(input('How much tip would you like to give? 10, 12, or 15? '))
# people = int(input('How many people to split the bill? '))
#
# total_bill = bill + round((bill * tip) / 100, 2)
# per_person = total_bill / people
# print(f'Each person should pay: ${per_person}')

# # leap year
# year = int(input("Which year do you want to check? "))
# if year % 4 == 0:
#     if year % 100 == 0 and year % 400 != 0:
#         print('Not leap year.')
#     else:
#         print('Leap year.')
# else:
#     print('Not leap year.')

# # Count no of occurance of letters of 'TRUE' and 'LOVE' occurs in names
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
#
# true_count = 0
# love_count = 0
# names = name1.lower() + name2.lower()
#
# for char in "true":
#     true_count += names.count(char)
# for char in "love":
#     love_count += names.count(char)
#
# score = true_count * 10 + love_count
#
# if 90 < score or score < 10:
#     print(f'Your score is {score}, you go together like coke and mentos.')
# elif 40 < score < 50:
#     print(f'Your score is {score}, you are alright together.')
# else:
#     print(f'Your score is {score}')

# Tresure Island

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

choice = input('You\'re at a cross road. Where do you want to go "left" / "right"? ')
if choice.lower() != 'left':
    print('You end up in road full of poisonous snake... GAME OVER!')
    print('''
    ---_ ......._-_--.
      (|\ /      / /| \  
      /  /     .'  -=-'   `.
     /  /    .'             )
   _/  /   .'        _.)   /
  / o   o        _.-' /  .'
  \          _.-'    / .'*|
   \______.-'//    .'.' \*|
    \|  \ | //   .'.' _ |*|
     `   \|//  .'.'_ _ _|*|
      .  .// .'.' | _ _ \*|
      \`-|\_/ /    \ _ _ \*
       `/'\__/      \ _ _ \*
      /^|            \ _ _ \*
     '  `             \ _ _ \* 
                       \ _ _ \*
                        \ _ _ \*
    ''')

else:
    choice = input('You\'re near river now. There is an house on the other side. Do you wanna "wait" for boat / "swim"?')
    if choice.lower() != 'wait':
        print('You drown into river with bunch of hungry crocodiles... GAME OVER!')
        print('''
                            .-._   _ _ _ _ _ _ _ _
         .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
         '.___ '    .   .--_'-' '-' '-' _'-' '._
          V: V 'vv-'   '_   '.       .'  _..' '.'.
            '=.____.=_.--'   :_.__.__:_   '.   : :
                    (((____.-'        '-.  /   : :
                                      (((-'\ .' /
                                    _____..'  .'
                                   '-._____.-'
          ''')
    else:
        choice = input('You crossed river and arrived near house with 3 doors. Choose one "red" / "black" / "blue"?')
        if choice.lower() == 'red':
            print('You burnt in deadly fire... GAME OVER!')
            print('''
                           (  .      )
                       )           (              )
                             .  '   .   '  .  '  .
                    (    , )       (.   )  (   ',    )
                     .' ) ( . )    ,  ( ,     )   ( .
                  ). , ( .   (  ) ( , ')  .' (  ,    )
                 (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            ''')
        elif choice.lower() == 'black' or choice.lower() != 'blue':
            print('You eaten by hungry tiger... GAME OVER!')
            print('''
                      __,,,,_
          _ __..-;''`--/'/ /.',-`-.
      (`/' ` |  \ \ \\ / / / / .-'/`,_
     /'`\ \   |  \ | \| // // / -.,/_,'-,
    /<7' ;  \ \  | ; ||/ /| | \/    |`-/,/-.,_,/')
   /  _.-, `,-\,__|  _-| / \ \/|_/  |    '-/.;.\'
   `-`  f/ ;      / __/ \__ `/ |__/ |
        `-'      |  -| =|\_  \  |-' |
              __/   /_..-' `  ),'  //
             ((__.-'((___..-'' \__.'
            ''')
        else:
            print('You found the treasure, you are RICH... YOU WIN!')

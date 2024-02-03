#!/usr/bin/env python3
print('''
#######                     #                                                            #                                                           
   #    #    # ######      # #   #       ####  #    # ###### #    # #  ####  #####      # #   #####  #    # ###### #    # ##### #    # #####  ###### 
   #    #    # #          #   #  #      #    # #    # #      ##  ## # #        #       #   #  #    # #    # #      ##   #   #   #    # #    # #      
   #    ###### #####     #     # #      #      ###### #####  # ## # #  ####    #      #     # #    # #    # #####  # #  #   #   #    # #    # #####  
   #    #    # #         ####### #      #      #    # #      #    # #      #   #      ####### #    # #    # #      #  # #   #   #    # #####  #      
   #    #    # #         #     # #      #    # #    # #      #    # # #    #   #      #     # #    #  #  #  #      #   ##   #   #    # #   #  #      
   #    #    # ######    #     # ######  ####  #    # ###### #    # #  ####    #      #     # #####    ##   ###### #    #   #    ####  #    # ###### 
       ''')
print("A Daroc Production\n")

print('''
              _{\ _{\{\/}/}/}__
             {/{/\}{/{/\}(\}{/\} _
            {/{/\}{/{/\}(_)\}{/{/\}  _
         {\{/(\}\}{/{/\}\}{/){/\}\} /\}
        {/{/(_)/}{\{/)\}{\(_){/}/}/}/}
       _{\{/{/{\{/{/(_)/}/}/}{\(/}/}/}
      {/{/{\{\{\(/}{\{\/}/}{\}(_){\/}\}
      _{\{/{\{/(_)\}/}{/{/{/\}\})\}{/\}
     {/{/{\{\(/}{/{\{\{\/})/}{\(_)/}/}\}
      {\{\/}(_){\{\{\/}/}(_){\/}{\/}/})/}
       {/{\{\/}{/{\{\{\/}/}{\{\/}/}\}(_)
      {/{\{\/}{/){\{\{\/}/}{\{\(/}/}\}/}
       {/{\{\/}(_){\{\{\(/}/}{\(_)/}/}\}
         {/({/{\{/{\{\/}(_){\/}/}\}/}(\}
          (_){/{\/}{\{\/}/}{\{\)/}/}(_)
            {/{/{\{\/}{/{\{\{\(_)/}
             {/{\{\{\/}/}{\{\\}/}
              {){/ {\/}{\/} \}\}
              (_)  \.-'.-/
          __...--- |'-.-'| --...__
   _...--"   .-'   |'-.-'|  ' -.  ""--..__
 -"    ' .  . '    |.'-._| '  . .  '   
 .  '-  '    .--'  | '-.'|    .  '  . '
          ' ..     |'-_.-|
  .  '  .       _.-|-._ -|-._  .  '  .
              .'   |'- .-|   '.
  ..-'   ' .  '.   `-._.-😴  .'  '  - .
   .-' '        '-._______.-'     '  .
\n''')
# Intro to the game
print("You are sleeping under a Sycamore tree on the outskirts of the small settlement of Andalusia.")
print("You're having a wonderful dream of pyramids in Egypt and great treasure!\n")
print("One of your sheep wakes you up. They are frightened by a strange man walking towards you.")
print("You calm the herd and approach the man.")
print('''\n
           _{\ _{\{\/}/}/}__
             {/{/\}{/{/\}(\}{/\} _
            {/{/\}{/{/\}(_)\}{/{/\}  _
         {\{/(\}\}{/{/\}\}{/){/\}\} /\}
        {/{/(_)/}{\{/)\}{\(_){/}/}/}/}
       _{\{/{/{\{/{/(_)/}/}/}{\(/}/}/}
      {/{/{\{\{\(/}{\{\/}/}{\}(_){\/}\}
      _{\{/{\{/(_)\}/}{/{/{/\}\})\}{/\}
     {/{/{\{\(/}{/{\{\{\/})/}{\(_)/}/}\}
      {\{\/}(_){\{\{\/}/}(_){\/}{\/}/})/}
       {/{\{\/}{/{\{\{\/}/}{\{\/}/}\}(_)
      {/{\{\/}{/){\{\{\/}/}{\{\(/}/}\}/}
       {/{\{\/}(_){\{\{\(/}/}{\(_)/}/}\}
         {/({/{\{/{\{\/}(_){\/}/}\}/}(\}
          (_){/{\/}{\{\/}/}{\{\)/}/}(_)
            {/{/{\{\/}{/{\{\{\(_)/}
             {/{\{\{\/}/}{\{\\}/}
              {){/ {\/}{\/} \}\}
              (_)  \.-'.-/
          __...--- |'-.-'| --...__
   _...--"   .-'   |'-.-'|  ' -.  ""--..__
 -"    ' .  . '    |.'-._| '  . .  '   
 .  '-  '    .--'  | '-.'|    .  '  . '
          ' ..     |'-_.-|
  .  '  .       _.-|-._ -|-._  .  '  .
              .'   |'- .-|   '.
  ..-'   ' .  '.   `-._.-😳🐑🐑🐑 🧓   .'  '  - .
   .-' '        '-._______.-'     '  .
\n
''')
# Name variable and input function which will give a game RPG feel.
# Allows the user to input their actual name in the story.
name = input("Strange man: What is your name, young shepherd?\n ")
print(f"\nKing Musa: Hello {name}. I am King Musa.")
print("You both converse for a while, and you tell him about your dream.")

print(f"King Musa: {name}, you must follow your Personal Legend. To do that,\nyou must leave Andalusia and the life of a shepherd behind.\n")

# First choice variable with input function and "lower" function so that the user can type the input in any case.
choice1 = input('Days go by. You shepherd your herd while thinking about the conversation with King Musa. \nYou are now at a crossroads. Will you stay in Andalusia and keep your flock?\nOr will you sell your flock and travel to Egypt in search of your Personal Legend?\nWhat will you do? Type "leave" or "stay".\n').lower()

if choice1 == "leave":
  print("You sold your flock. It was tough because you've known those sheep all their life,\nbut you now have enough money to sail the seas to Egypt!")
  print('''\n###################################################################
                      \|/
                      -o-                              |
                      /|\                             ( )_
             |                                       /\ | |
            (_)             |      |   __         |  ||-| |-[]|  \|/  \|
 ___|___   _| |____   |    (_)_  _( )_|[]|     __(_)_|| |     |_~(|)~~(|
(_)__)__|_| []|[]  |_(_)_  |[]|_|_[]__|__|  __| |[]|__| | []|___|_|____|
| |__| [] |   |[]  |  | |  |    | []  |  | |  | |   |||_|    [][]      |
😃                                                   👳‍♂️👳‍♂️👳‍♂️

the city of Tangier,
___________________________________________________________________
################################################################### 
          \n''')
  #2nd choice variable
  choice2 = input('You made it to the city of Tangier in Egypt!\n You\'ve never been away from home before and you are amazed by the city as you walk around.\n Out of nowhere, 3 men surround you, beat you up and take all your money!.\nWill you work for the funds to get to the pyramids of Egypt or will you go home?\nType "work" to get a job or "quit" to give up and go home.\n').lower()
  if choice2 == "work":
    print("You decide to find a job to earn the money needed to continue your journey to the pyramids of Egypt.\nYou find employment working for a crystal merchant.")
    print("\nMonths go by working for the crystal merchant you've earned enough money to travel the desert and make it to the pyramids!\n")
    print("You leave the crystal merchant and set towards the pyramids. You buy a camel and as your leaving Tangier you see King Musa!\n")
    print('''\n
                                         //^\\ #
   q_/\/\   q_/\/\    q_/\/\   q_/\/\      #   #
🫅  ||||`   /|/|` 🫠 <\<\`    |\|\`     #   #
%*%*%**%**%**%*%*%**%**%**%****%*%**%**%**%*%*%**%**%**% 
              \n''')
    #3rd print variable
    choice3 = input(f'\n King Musa has been great company after days of traveling the desert together, you awake one night to see that King Musa is gone!\n what will you do now {name}? Type "give up" or "march on" \n ').lower()
    if choice3 == "march on": 
        print("\nYou used all you've learned from King Musa and confronted death!\nYour instincts and wisdom got you through the harsh desert and to an oasis not too far from the pyramids! You can see it from here!")
        print("You've been at the oasis to rest for a few days and find a lover. The love of your life, what an amazing thing! ")

        print('''\n😍 🥰\n''' )
        #4th choice varaible
        choice4 = input(f'Lover: Please {name} stay here with me forever screw that personal legend!\nYour lover wants you to stay but your so close to your personal legend. what will you do?\nType "leave"or type "stay"\n').lower()
        if choice4 == "leave":
          print(f"{name}: I have to go my love. My personal legend awaits")
          print("Your lover and you are both heartbroken but your lover understands you must pursue your personal legend.\nYou leave to the pyramids")
          print('''\n             __ -                                                   
        /     __   \                                               
          /   _ -    |                                             
      | '  | (_)  |                        _L/L                    
         |  __  /   /                    _LT/l_L_                  
        \ \  __  /                     _LLl/L_T_lL_                
            -      _T/L              _LT|L/_|__L_|_L_              
                 _Ll/l_L_          _TL|_T/_L_|__T__|_l_            
               _TLl/T_l|_L_      _LL|_Tl/_|__l___L__L_|L_          
             _LT_L/L_|_L_l_L_  _'|_|_|T/_L_l__T _ l__|__|L_        
           _Tl_L|/_|__|_|__T _LlT_|_Ll/_l_ _|__[ ]__|__|_l_L_      
  _ ___ _LT_l_l/|__|__l_T _T_L|_|_|l/___|_ _|__l__|__|__T_l_  __
        . ";;:;.;;:;.;;;;_Ll_|__|_l_/__|___l__|__|___l__L_|_l_LL_  
          .  .:::.:::..:::.";;;;:;;:.;.;;;;,;;:,;;;.;:,;;,;::;:".' 
              . ,::.:::.:..:.: ::.::::;..:,:::,::::.::::.:;:.:..   
                 . .:.:::.:::.:::: .::.::. :::.::::..::..:.::. . . 
                   . ::.:.: :. .:::  ::::.::.:::.::...:. .:::. .   
                       .:. ..   . ::.. .: ::. ::::.:: ::::::.   .  
   🤯                    .  :.         .. :::.::: ::.::::. ::. .     
                         . .           .:. :.. :::. ::..: :.       
                              . . .:. . : .        
                            ' "``                  . :. .          
                                                    .   .          
                                                       \n''')
          #Final choice variable
          choice5 = input(f'You make it to the pyramids {name}, your so close to your treasure you can feel it.\nAs you enter the pyramids you find looters! They knock you out and leave you for dead.\nWhen you awake you gather what strength you can to find your treasure but it\s all been looted\n You cry out of depression. After all who can blame you after all you have been through. What now? Type "give up" or "think"\n').lower()
          if choice5 == "think":
            print("You realize where the treasure is!\nYou go home and find your lover awaiting your arrival next to the Sycamore tree where it all started!\n As you reflect you realize that the true treasure was the journey.\nYou live a happy fulfilled life!")
            print('''\n*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/____The End!
******************************************************************************* ''')
          #all the following else statements end the game.

          #This else statement is for the final choice variable
          else:          
            print("You couldn't believe you came all this way for nothing! You gave up on life and passed from your injuries in the pyramid!\n**** Game over!****")
        
        #This else statement is for the 4th choice variable
        else:
          print(f"\n{name} stayed, got married and started a family after a while.\nYou love your family dearly but on your deathbed you couldn't help but think of your personal legend.\n****Game Over!****")

    #This else statement is for the 3rd choice variable
    else:
      print(f"{name} gave up all hope. As a result you died of dehydration and the harsh desert environment\n****Game Over****")
  
  #This else statement is for the 2nd choice variable
  else:
    print(f"{name}: This is too much! All this for a stupid dream. I'm going home!\n You found the journey too hard and went back to herding sheep.\n****Game Over****")

#This else statement is for the 1st choice variable
else:
  print("\nYou lived your life in Andalusia as a shepherd.")
  print("You died never forgetting the dream of treasure and the great pyramids of Egypt.\n****Game Over!****")
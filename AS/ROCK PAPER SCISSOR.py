
import random



print("""************************************************************
Welcome to Rock Paper Scissors
************************************************************
""")

user_choice = raw_input("Please choose (R) Rock, (P) Paper, or (S) Scissors: ").upper()


random_number = random.randint(1,3)


if random_number == 1:
	computer_choice = "R"

elif random_number == 2:
	computer_choice = "P"

elif random_number == 3:
	computer_choice = "S"


if computer_choice == "R":
	print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

The computer chose rock.""")

elif computer_choice == "P":
	print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

The computer chose paper.""")

elif computer_choice == "S":
	print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

The computer chose scissors.""")

print("")


if (computer_choice == "R" and user_choice == "P") or \
	(computer_choice == "P" and user_choice == "S") or \
	computer_choice == "S" and user_choice == "R":
	print("You win!")
	print(""" 
	$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'               `$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  
	$$$$$$$$$$$$$$$$$$$$$$$$$$$$'                   `$$$$$$$$$$$$$$$$$$$$$$$$$$$$
	$$$'`$$$$$$$$$$$$$'`$$$$$$!                       !$$$$$$'`$$$$$$$$$$$$$'`$$$
	$$$$  $$$$$$$$$$$  $$$$$$$                         $$$$$$$  $$$$$$$$$$$  $$$$
	$$$$. `$' \' \$`  $$$$$$$!                         !$$$$$$$  '$/ `/ `$' .$$$$
	$$$$$. !\  i  i .$$$$$$$$                           $$$$$$$$. i  i  /! .$$$$$
	$$$$$$   `--`--.$$$$$$$$$                           $$$$$$$$$.--'--'   $$$$$$
	$$$$$$L        `$$$$$^^$$                           $$^^$$$$$'        J$$$$$$
	$$$$$$$.   .'   ""~   $$$    $.                 .$  $$$   ~""   `.   .$$$$$$$
	$$$$$$$$.  ;      .e$$$$$!    $$.             .$$  !$$$$$e,      ;  .$$$$$$$$
	$$$$$$$$$   `.$$$$$$$$$$$$     $$$.         .$$$   $$$$$$$$$$$$.'   $$$$$$$$$
	$$$$$$$$    .$$$$$$$$$$$$$!     $$`$$$$$$$$'$$    !$$$$$$$$$$$$$.    $$$$$$$$
	$JT&yd$     $$$$$$$$$$$$$$$$.    $    $$    $   .$$$$$$$$$$$$$$$$     $by&TL$
	                                 $    $$    $
	                                 $.   $$   .$
	                                 `$        $'
	                                  `$$$$$$$$' """)


elif (computer_choice == "R" and user_choice == "S") or \
	(computer_choice == "P" and user_choice == "R") or \
	(computer_choice == "S" and user_choice == "P"):
	print("You lose!")


elif computer_choice == user_choice:
	print("Tie!")

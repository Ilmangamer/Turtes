
# Making an adventure game



# exit(0) means you exit with zero error -1 means that you leave one error.
print("Welcome to my adventure game.")
print( 'Do you wanna play? [y/n?]')


play = input()


if play == 'no':
	print("Maybe another time?")
	print('Session has ENded')
if play == 'no':
	exit(-1)

elif play == 'yes':
	print("You are welcome")
	print('First question')
	print('You are going to the beach, with youre friend')
	print('The beach is at the left, but then youre friend decides to go to the right. \n will you join him?[y/n]')



Yes_Or_No = input()


if Yes_Or_No == 'no':
	print('So you went to the beach alone is this a wise decison?')


#Beachmonster

dec = input()
if dec == 'wise':
	print('You encounter a scary beach monster, will you attack [y/n]?')
you_attack = input()

if you_attack == 'yes':
	print('You are attacking the monster, but it killed you')
	print('You Lose')
	print('Game has ENded')
  

elif you_attack == 'no':
	print('Well that\'s sad, anyways done is done.')
	print('You encounter a scary beach monster, will you attack? [a/n.attack]?')


encounter = input()

if encounter == 'attack':
	print('You are attacking the monster, but it killed you')
	print('You Lose')
	print('Game has ENded')
  

elif encounter == 'not attack':
	print('You are a wimpy')
	print('.....')
	print('\n \n \n \n You Lose! ha!')

if encounter:
	exit(0)

# The equaliser

   

#Friend

chrush = input('You and youre friend are encoutring youre chrush [Ok/Not OK]')
chrush.lower().strip()

if chrush == 'OK':
	print('Youre bestfriend is kissing youre chrush, still [Ok/Not Ok]')
chrush.lower().strip()
still_okay = input()



if still_okay == 'Ok':
	print('Congratulations you are a freaking \n LOOSER')
	print('Game Over')


elif still_okay == 'Not Ok':
	print(' Will you fight youre bestfriend? or run? [f/r]')

run = input()

if run == 'run':
	print('You Lose')
	print('Game Over')

elif run == 'fight':
	print('You win the fight. \n youre chrush loves you.')
	print('Congratulations, You win the game!')



	
adventure_game = False
exit()

	


# Aftermath
# I have an issue
# I want the computer to understand that the first input yes or no
# Then i want the computer to go on with my script.
# I can change this by saying simple words like run and go

# 1 problem left
# I need to end the game session when I say I lose.












































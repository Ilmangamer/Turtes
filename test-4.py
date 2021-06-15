









# Making an adventure game



# exit(0) means you exit with zero error -1 means that you leave one error.

# 'repr' shows what play clmpares to. 

# welcome

import time

print("Welcome to my adventure game.")
print( 'Do you wanna play? [y/n?]')
running = True

def play():
	play = input()
	if play == 'yes':
			print('You are welcome \n First question \n You are going to the beach, with youre friend \n The beach is at the left, but then youre friend decides to go to the right. \n will you join him?[y/n], \n [if yes, type yes and hit enter 4 times.]')
	else:
		print('Maybe another time')
			


play()


print('What are you trying to say?')
def cleaninput(message):
	if message.strip().lower() == "no":
		print('So you went to the beach alone is this a wise decison?, [wise]/[not wise]')
	else:
		print('Invalid syntax')
		exit(0)

message = input() 
cleaninput(message)

def chrush():
	if chrush.strip().lower() == 'Not Ok':
		print("You and youre friend are encoutring youre chrush (type Ok/Not Ok) and (hit enter twice), 'type here--->'  ")
	
chrush()
	

 


message = input('Please enter something:   ')
cleaninput(message)





def van(va):
	if va.lower().strip() == 'wise':
		print('You encounter a scary beach monster, will you attack [y/n]?')
	elif va.lower().strip() == 'not wise':
		print('You encounter a scary beach monster, will you attack [y/n]?')
	else:
		print('Invalid syntax')


va = input()
van(va)







#Beachmonster


#Error


#Error
def you(attack):
	if attack.lower().strip() == 'yes':
		print('You are attacking the monster, but it killed you')
		print('You Lose')
		print('Game has ENded')
		exit(-1)  
	elif attack.lower().strip() == 'no':
		print("Well that\'s sad, anyways done is done.")
		print('You encounter a scary beach monster, will you attack? [attack/not attack]?')

attack = input()
you(attack)



def encounter(ena):
	if ena == 'attack':
		print('You are attacking the monster, but it killed you')
		print('You Lose')
		print('Game has ENded')

	elif ena == 'not attack':
		print('You are a wimpy')
		time.sleep(3)
		print('.....')

	else: 
		time.sleep(3)
		print('\n \n \n \n You Lose! ha!')

ena = input()
encounter(ena)



#encounter = input()
#encounter(ena)



#if encounter:
	#exit(0)




# The equaliser
#if encounter:
	#exit(-1)



   

#Friend



	




def stay(run):
	if run.lower().strip() == 'run':
		print('You Lose, game over!')
		exit(0)
	else:
		print('Invalid syntax')

run = input()
stay(run)






def run(stay):
	if stay.lower().strip() == 'stay':
		print('Youre bestfriend is kissing youre chrush, still [Ok/not ok]')
	elif stay.lower().strip() == 'ok':
		print('Youre bestfriend is kissing youre chrush, still [ok/not ok]')
	else:
		print('Invalid syntax')
		exit(0)

stay = input()
run(stay)








def still(okay):
	if okay.lower().strip() == 'ok':
		print('Congratulations you are a freaking \n LOOSER')
		print('Game Over')
	elif okay.lower().strip() == 'not ok':
		print(' Will you fight youre bestfriend? or run? [f/r]')

	else:
		print('Invald syntax')
		exit(0)

still_okay = input()   
still(okay)



def r(run):
	if run.lower().strip() == 'run':
		print('You Lose')
		print('Game Over')
	elif run.lower().strip() == 'fight':
		print('You win the fight. \n youre chrush loves you.')
		print('Congratulations, You win the game!')
	else:
		print('Invalid syntax')
		exit()

run = input()
r(run)



	

	


# Aftermath
# I have an issue
# I want the computer to understand that the first input yes or no
# Then i want the computer to go on with my script.
# I can change this by saying simple words like run and go

# 1 problem left
# I need to end the game session when I say I lose.






# Version 2 is supposed to be way better than verison 1. Let us focus on three main things that we want to fix. 


# Improvements

# 1. We want to add neccassary information in the strings.
# 2. We want to lower the 'ok'.
# 3. We want to modify or lower.strip a string.
# finally we want to make the exit excellent. 





# facts about strings.
# Strings are immutable you can't change them.
# The first string you put at the top remains immutable the string you put under stays unaffected.


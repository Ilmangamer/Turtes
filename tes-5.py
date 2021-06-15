

def c(hrush):
    if hrush.lower().strip() == 'not ok':
    	print('will you run or stay from the situation?')
    elif hrush.lower().strip() == 'ok':
    	print("will you run or stay from the situation?")

hrush = input("You and youre friend are encoutring youre chrush (type Ok/Not Ok) and (hit enter twice), 'type here--->'  ")
c(hrush)


	




def stay(run):
	if run.lower().strip() == 'run':
		print('You Lose, game over!')
		exit(0)
	else:
		print('Invalid syntax')

run = input()
stay(run)




























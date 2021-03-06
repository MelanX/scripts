import random
import time

lap = 0
total_fail = 0
best_fail = int(2000000000)
best_lap = int(2000000000)
worst_fail = int(0)
worst_lap = int(0)

print("""   _____                       _   _            _   _                 _               
  / ____|                     | | | |          | \ | |               | |              
 | |  __ _   _  ___  ___ ___  | |_| |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \ | |_| | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/  \__|_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
							Fun for the whole family\n\n\n""")

time.sleep(1)
k = 0
print('Difficulty:\neasy   (0 - 100) \nnormal (0 - 1000)\nhard   (0 - 10000)\ncustom (0 - whatever you want)')
while True:
	difficulty = input('Please type in which difficulty you choose: ').strip()
	if difficulty == 'easy':
		k = 100
		break
	elif difficulty == 'normal':
		k = 1000
		break
	elif difficulty == 'hard':
		k = 10000
		break
	elif difficulty == 'custom':
		while ( k <= 9 or k >= 2000000000 ):
			k = input('What should be the highest number? ').strip()
			if not k.isdigit():
				print('Please type in a real number.')
			else:
				k = int(k)
			if k <= 9:
				print(f'{k} is too low. Please choose a higher number!')
			if k >= 2000000000:
				print(f'{k} is too high. Please choose a lower number!')
		break
	elif difficulty != 'easy' and 'normal' and 'hard' and 'custom':
		print('\n\nPlease type in \'easy\', \'normal\', \'hard\' or \'custom\'')

while True:
	chance = 0
	i = random.randint(0, k)
	guess = k + 1
	fail = 0
	while guess != i:
		while True:
			guess = input('\nGuess the number: ')
			if not guess.isdigit():
				print (f'\'{guess}\' is no number. Please type in a number from 0-{k}.')
			else:
				guess = int(guess)
				break
		if guess > k:
			print('This is higher than the highest number!')
			chance = chance + 1
			if chance == 3:
				print("Okay, you don't want to play normal. Game Over!")
				time.sleep(5)
				exit()
		elif guess > i:
			print(f'{guess} is too high. Try a lower number! ')
			fail += 1
		elif guess < i:
			print(f'{guess} is too low. Try a higher number!')
			fail += 1
		elif guess == i:
			print(f'The number was {i}.\n')
	if fail == 0:
		print(f'That was too easy for you. Or you\'re just the best player in the whole world!')
	elif fail == 1:
		print(f'You\'re the best player EU west! You just failed {fail} time.')
	elif ( fail < 5 ):
		print(f'You\'re the best player EU west! You just failed {fail} times.')
	elif ( fail < 20 ):
		print(f'That was really nice! You failed only {fail} times.')
	elif ( fail < 50 ):
		print(f'Oh boy/girl, you failed {fail} times. Next time you have more luck, haven\'t you?')
	elif ( fail < 100 ):
		print(f'{fail} times failed. Please make it a bit better.')
	else:
		print(f'You need more luck. You failed {fail} times!')
	lap += 1
	total_fail += fail
	if fail < best_fail:
		best_fail = fail
		best_lap = lap
	if fail > worst_fail:
		worst_fail = fail
		worst_lap = lap
	while True:
		again = input('Do you wanna play again (y/n)? ')
		if again == 'y':
			print(f'\nYour difficulty is still {difficulty} with the highest number {k}.')
			break
		elif again == 'n':
			break
		elif again != 'y' and again != 'n':
			print('Please answer with \'y\' or \'n\'.')
	if again == 'n':
		break

if difficulty == "custom":
	cstm = f' ({k})'
else:
	cstm = ''
if lap == 1:
	if total_fail == 1:
		print(f'\nYou totally failed {total_fail} time in {lap} {difficulty}{cstm} round. You failed {total_fail / lap} times on average.')
	else:
		print(f'\nYou totally failed {total_fail} times in {lap} {difficulty}{cstm} round. You failed {total_fail / lap} times on average.')
else:
	if total_fail == 1:
		print(f'\nYou totally failed {total_fail} time in {lap} {difficulty}{cstm} rounds. You failed {total_fail / lap} times on average.')
	else:
		print(f'\nYou totally failed {total_fail} times in {lap} {difficulty}{cstm} rounds. You failed {total_fail / lap} times on average.')
if best_fail == 1:
	print(f'Your best try was number {best_lap} with only {best_fail} fail!')
else:
	print(f'Your best try was number {best_lap} with only {best_fail} fails!')
if worst_fail == 1:
	print(f'Your worst try was number {worst_lap} with {worst_fail} fail!')
else:
	print(f'Your worst try was number {worst_lap} with {worst_fail} fails!')
# print(f'Please give me feedback on discord: \'MelanX#7949\'')
time.sleep(1)
input(f'\nPress enter to end this program...')
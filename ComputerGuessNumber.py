#This program will guess what number you think of with only 7 questions or less
#Note that you can change the Low and High values to -1 and 101 to guess from 1 to 100

#Heading
#----------------------------------------------------------------------------------------
print('What is your name?')
name = input()
print('Hello ' + name + ' and welcome to the guessing program!')
print('Please pick an interger number between 0 to 100 in your mind!')
print('Now the program is going to guess what your number is with only 7 questions or less!')
print('Ok lets start!')
low = 1
high = 100
guess = 50
i=0
from sys import exit

#Functions
#----------------------------------------------------------------------------------------

#Guess program
def fguess():
	global i,guess,high,low
	while i<7:
		print('Is it Higher or Lower:')
		test_ans3()
		if ans == 'Higher':
			low = guess
		elif ans == 'Lower':
			high = guess

		guess = (high + low) // 2

		print('Is ' + str(guess) + ' your number?\nYes or No')
		test_ans2()
		if ans == 'Yes':
			break
		elif ans =='No':
			print('Hmm')
		i+=1



#Test input program No.1
def test_ans1():
	global ans1
	ans1 = None
	while ans1 != 'Yes' or ans1 != 'No' :
		ans1 = input()
		if ans1 == 'Yes' or ans1 == 'No':
			break
		try:
			print('You did not enter a valid value, please try again!')
			continue
		except:
			print('You did not enter a valid value, please try again!')
			continue
		else:
			break

#Test input program No.2
def test_ans2():
	global ans
	ans = None
	while ans != 'Yes' or ans != 'No' :
		ans = input()
		if ans == 'Yes' or ans == 'No':
			break
		try:
			print('You did not enter a valid value, please try again!')
			continue
		except:
			print('You did not enter a valid value, please try again!')
			continue
		else:
			break

#Test input program No.3
def test_ans3():
	global ans
	ans = None
	while ans != 'Higher' or ans != 'Lower' :
		ans = input()
		if ans == 'Higher' or ans == 'Lower':
			break
		try:
			print('You did not enter a valid value, please try again!')
			continue
		except:
			print('You did not enter a valid value, please try again!')
			continue
		else:
			break

#Body
#----------------------------------------------------------------------------------------

print('First i must ask, is 50 your number?\nYes or No')
test_ans1()
if ans1 == 'Yes':
	print('The number you think of is: 50')
	exit()
elif ans1 == 'No':
	fguess()
	
#End
#----------------------------------------------------------------------------------------
if ans == 'No' and i == 7:
		print('Your number is not between 0 to 100!')
		exit()
print('The number you think of is: ' + str(guess))
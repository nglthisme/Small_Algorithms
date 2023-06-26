print('This tells you whether the input is a prime or not.')

n = int(input('Input a positive number: '))

test = 2
num_factors = 0

while test * test <= n:
	if n % test == 0:
		num_factors = num_factors + 1
	
	test = test + 1

if num_factors > 0:
	print('n is not a prime')
	
else:
	print('n is a prime!')

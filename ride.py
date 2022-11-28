from random import randint, shuffle
import string

#this function is the function that generates reference numbers
def ref_number():
	x = ''

	size = string.ascii_uppercase
	s = string.digits
	for i in range(3):
		j = randint(0,25)
		k = randint(0,9)
		x = x + s[k]
		x = x + size[j]

	return x
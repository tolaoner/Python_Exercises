'''Create a sequence of numbers and determine whether 
all the numbers of it are different from each other'''
import random
list_numbers=[]
different=True
for i in range(5):
	list_numbers.append(random.randrange(1,10,1))
	print(list_numbers[i])
for i in range(5):
	for j in range(5):
		if i==j:
			continue 
		if list_numbers[i]==list_numbers[j]:
			different=False
print('All numbers are different!'if different else 'There are same numbers!')

'''Correct solution.
Better Solution:
with set() method! set() sorts the iterables and removes repeating
elements! In dictionary, only keys remain after conversion!'''
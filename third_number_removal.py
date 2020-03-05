'''Write a Python program to remove and print every third number 
from a list of numbers until the list becomes empty.'''
def remove_third_nums(number_list):
	index=0
	while len(number_list)>0:
		index=(index+2)%len(number_list)
		print(number_list[index])
		number_list.pop(index)
remove_third_nums([1,2,3,4,5,6,7,8,9])



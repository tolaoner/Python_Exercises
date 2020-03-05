'''Write a Python program to find unique triplets whose three 
elements gives the sum of zero from an array of n integers.'''
import itertools
def unique_triplets(integer_list):
	all_triplets=list(itertools.permutations(integer_list,3))
	result=[]
	for i in range(len(all_triplets)):
		element=all_triplets[i]
		decider=sum(element)
		if decider==0:
			result.append(all_triplets[i])
		else:continue
	return result
int_list=[1,-6,4,2,-1,2,0,-2,0]
print(unique_triplets(int_list))


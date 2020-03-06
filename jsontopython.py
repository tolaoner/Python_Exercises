'''Write a Python program to convert JSON data to Python object.'''
import json
def jsondata_to_python(file_dir):
	with open(file_dir) as json_file:
		data=json.load(json_file)
		print(data[0]['Data'][0]['ID'])
		return data
#a=jsondata_to_python(r'C:\Users\tolao\OneDrive\Documents\GitHub\Hiwi_Job_Sahin\DEU_Merging_Interaction1.json')
def python_to_json(filename,data):
	with open(f'{filename}.txt','w') as jsonfile:
		json.dump(data,jsonfile)
#python_to_json('jasonshow',a)
complex_obj=json.dumps(2+3j)
print(complex_obj)

import os


folder = 'tub - original - copia'
inicio = 59600
fin    = 61119


def del_img_json():
    dirCheckpoint = os.path.join(os.getcwd(), folder)
    aux = []
    for root, dirs, files in os.walk(dirCheckpoint):
        for file_name in files:
            indexstr = file_name.find('_')
            if not (indexstr.__eq__(-1)): # si es diferente de -1
            	#print(file_name[:indexstr])
            	n = int(file_name[:indexstr]) 
            	#print(n)
            	if n in range(inicio, fin):
	            	print(file_name[:indexstr])
	            	#print(indexstr)
	            	path = os.path.join(dirCheckpoint, file_name)
	            	print(path)
	            	os.remove(path)
	            	print()

	               
def del_img_json2():
    dirCheckpoint = os.path.join(os.getcwd(), folder)
    aux = []
    for root, dirs, files in os.walk(dirCheckpoint):
        for file_name in files:
            indexstr = file_name.find('_')
            if not (indexstr.__eq__(-1)): # si es diferente de -1
            	if file_name.endswith('.json'):
	            	file = file_name[indexstr+1:]
	            	indexstr = file.find('.')
	            	file = file[:indexstr]
	            	n = int(file) 
	            	if n in range(inicio, fin):
	            		jsonpath = os.path.join(dirCheckpoint, 'record_{}.json'.format(n))
	            		print(jsonpath)
	            		os.remove(jsonpath)
	           





def main():
	del_img_json()


if __name__ == '__main__':
	main()
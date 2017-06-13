import numpy as np
import csv
   #  training_data = np.array(x1).astype("float")
   #  for row in irisreader:
     #        print(str(row))

#training_data = np.matrix('1 -1 -1 1; 1 -1 1 1; 1 1 1 -1;1 1 1 -1');#NOR gate

def testFunction(testvector=[]):
	wt1 = w.transpose()
	print(w)
	z = np.matrix(testvector)
	print(testvector)
	t = z * wt1
	act = t[0,0]
	print(t)
	print(act)
	if(act < 0):
		act = -1
		species = "iris-versicolor"
	else:
		act = 1
		species = "iris-virginica"
	print(species)


training_data = np.loadtxt("/home/kunal/iris_data.csv", delimiter=',', usecols=range(0,5))
desired_data = np.loadtxt("/home/kunal/iris_data.csv", delimiter=',', usecols=range(5,6))


#print(training_data)
#print(desired_data)
des = np.matrix(desired_data) 
#print(des)
w = np.matrix('0 0 0 0 0')
classified_count = 0
number_of_iterations_required = 0;
cur_run_len=0
best_run_len=0
pocket = w
dw = w
print("\n\n")

while(classified_count<=(len(training_data)-1) ):
	for i in range(len(training_data)):
		desired = 0
		x = training_data[i,0:5] 
		print("input Vector ",x)
		d1 = des[0,i] 
		d = np.matrix(d1)
		wt = w.transpose()
		classified = False
	        print("Weights ",w)
		y = x * wt
		act = y[0,0]

		if(act < 0):
			act = -1
		else:
			act = 1
		print("actual value %d" % act)
		print("desired value %d" % d[0,0])
		desired = d[0,0]



		
		if(act==desired):
			print("Classified")
			classified = True
			classified_count+=1
			cur_run_len+=1
			
		else:

			print("Not Classified")
			if(act>desired):
			        print("hello...")
				dw = np.negative(x)
				#print(dw)
			else:
				dw =  x
				#print(dw)
			w = w + dw
			if(best_run_len<cur_run_len):
				best_run_len = cur_run_len
				pocket = w
			classified_count = 0
		#print(w)
		number_of_iterations_required+=1
		print(classified_count)
		if(classified_count > len(training_data)-1 or number_of_iterations_required>500):
			break;
	if(number_of_iterations_required>500):
		break;	
		#print("\n\n\n")
print("best_run_len %d" % best_run_len)
print("pocket")
print(pocket)		
print("Total number of iterations required %d" % number_of_iterations_required)
testvector = input('enter test data: ')
print(testvector)
testFunction(testvector)


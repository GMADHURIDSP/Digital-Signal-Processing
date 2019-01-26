def matrix_mul (matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			print (matrix[i][j])
	for x in matrix:
		print (x)
		#print("\n")
#def main ():
a=int( input("rows of the first matrix:"))
b= int( input("columns of the first matrix:"))
c=int( input("rows of the second matrix:"))
d=int( input("columns of the second matrix:"))
if (b!= c):
	print ("matrix multiplication does not exist")
	exit();
array1= [[0 for j in range (0,b)] for i in range (0,a)]
array2= [[0 for j in range (0,d)] for i in range (0,c)]
result= [[0 for j in range (0,d)] for i in range (0,a)]
print ("enter first matrix elements:")
for i in range (0,a):
	for j in range (0,b):
		array1[i][j]=int (input("enter the element"))
print ("enter the elements of second matrix:")
for i in range (0,c):
	for j in range (0,d):
		array2[i][j]=int (input("enter the element"))
print("first matrix")
matrix_mul(array1)
print ("second matrix")
matrix_mul(array2)

for i in range(0,a):
	for j in range (0,d):
		for k in range(0,b):
			result[i][j] +=array1[i][k] * array2[k][j]

print ("multiplication of matrices:")
matrix_mul(result)



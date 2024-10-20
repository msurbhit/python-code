MAX = 100

def printDiagonalSums(mat, n):

	principal = 0
	secondary = 0;
	for i in range(0, n): 
		for j in range(0, n): 

			if (i == j):
				principal += mat[i][j]

			if ((i + j + 1) == (n - 1)):
				secondary += mat[i][j]
		
	print("Principal Diagonal:", principal)
	print("Secondary Diagonal:", secondary)


a = [[ 1, 2, 3, 4 ],
	[ 5, 6, 7, 8 ], 
	[ 1, 2, 3, 4 ],
	[ 5, 6, 7, 8 ]]
printDiagonalSums(a, 4)

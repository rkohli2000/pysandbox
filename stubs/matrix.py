'''
Return the indices of the target number or [-1, -1] if not found
matrix = [
	[1, 4, 7, 12, 15, 1000],
	[2, 5, 19, 31, 32, 1001],
	[3, 8, 24, 33, 35, 1002],
	[40, 41, 42, 44, 45, 1003],
	[99, 100, 103, 106, 128, 1004],
], 44

Answer = [3,3]

'''

# Time  O(n + m) Space: O(1)
def searchInSortedMatrix(matrix, tgt):
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] > tgt:
            col-=1
        elif matrix[row][col] < tgt:
            row+=1
        else:
            return [row, col]
    return [-1,-1]


if __name__ == "__main__":


    m =  [
        [1, 4, 7, 12, 15, 1000],
        [2, 5, 19, 31, 32, 1001],
        [3, 8, 24, 33, 35, 1002],
        [40, 41, 42, 44, 45, 1003],
        [99, 100, 103, 106, 128, 1004],
    ]

    print (m)
    print('indices for 44 are', searchInSortedMatrix(m, 44))

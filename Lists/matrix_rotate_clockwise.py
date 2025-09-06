matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def clockwise(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        row = []
        for row_length in range(len(matrix[0])):
            row.insert(0,matrix[row_length][i])

        new_matrix.append(row)
    return new_matrix

print(clockwise(matrix))

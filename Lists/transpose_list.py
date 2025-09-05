# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
mat = [[1, 1, 1, 1],[2, 2, 2, 2],[3, 3, 3, 3], [4, 4, 4, 4]]
def transpose(matrix: list[list[int]]):
    new_matrix = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            row.append(matrix[j][i])
        new_matrix.append(row)
    return new_matrix

print(transpose(mat))

class Matrix:
    """
    This class is here only as a note for possible future use.
    Further comments will be added, if the class is utilized.

    Attributes:
        n: number of rows.
        m: number of columns.
    """
    def __init__(self, n, m):
        self.matrix = self.build(n, m)

    def build(self, n, m):
        num = 0
        matrix = [[None for j in range(m)] for i in range(n)]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = num
                num += 1
        return matrix

    def __str__(self):
        def stringify(matrix):
            strings = []
            for row in matrix:
                strings.append(str(row))
            return '\n'.join(strings)

        return stringify(self.matrix)

    def __len__(self):
        return len(self.matrix)

    def __getitem__(self, item):
        return self.matrix[item]

    def get_element(self, i, j):
        return self.matrix[i-1][j-1]

    def set_element(self, i, j, element):
        self.matrix[i-1][j-1] = element

if __name__ == "__main__":
    mtx = Matrix(12, 11)
    print(mtx)

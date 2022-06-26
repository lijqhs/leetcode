class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        numPattern = 2 * (numRows - 1)      # repeat pattern substring

        matrix = []
        for k in range(numRows):
            matrix.append([])
            
        for i in range(len(s)):
            row = i % numPattern
            if row >= numRows:
                row = numPattern - row
            matrix[row].append(s[i])
        
        matrix = sum(matrix, [])
        newStr = ''.join(matrix)
        return newStr


if __name__ == '__main__':
    s = "PAYPALISHIRING"
    solution = Solution()
    print(solution.convert(s, 4))


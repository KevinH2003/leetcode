class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 0:
            return [[]]

        rows = [[1]]

        for i in (range(0, numRows - 1)):
            prevrow = rows[i]
            nextrow = []
            nextrow.append(1)
            for j in (range(i)):
                nextrow.append(prevrow[j] + prevrow[j + 1])
            nextrow.append(1)
            rows.append(nextrow)
        
        return rows
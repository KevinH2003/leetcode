class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [0] * (rowIndex + 1)
        row[0] = 1
        
        for i in range(rowIndex + 1):
            prev = 0
            print(row)
            for j in range(i + 1):
                temp = row[j]
                row[j] += prev
                prev = temp
        
        return row
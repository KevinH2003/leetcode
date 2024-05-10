class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [[set() for i in range(3)] for j in range(3)]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                element = board[i][j]
                
                if element == '.':
                    continue
                        
                if element in rows[i]:
                    return False
                if element in cols[j]:
                    return False
                if element in boxes[i // 3][j // 3]:
                    return False
                    
                rows[i].add(element)
                cols[j].add(element)
                
                boxes[i // 3][j // 3].add(element)
                    
        return True
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        neighbor = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def isInBound(r, c):
            return 0 <= r < n and 0 <= c < m

        def bt(i, j, idx):
            if idx == len(word):
                return True

            if not isInBound(i, j) or board[i][j] != word[idx]:
                return False

            temp = board[i][j]
            board[i][j] = '#'  # Mark the cell as visited

            for r, c in neighbor:
                if bt(i + r, j + c, idx + 1):
                    return True

            board[i][j] = temp  # Restore the cell

            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and bt(i, j, 0):
                    return True

        return False

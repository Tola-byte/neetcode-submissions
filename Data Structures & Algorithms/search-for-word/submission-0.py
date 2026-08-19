class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        

        # how do we solve this?
        # use the brute force approach, specify row and column, start at the first tile, 
        # check around it for the next character using dfs
        # specify the path and store the characters in it if seen and remove after
        # if none, count is as visited so users can't come back to count it again return false.


        # if seen return true

        # now specifiying row and column

        rows , columns = len(board) , len(board[0])
        path = set()

        # specifying a dfs function

        def dfs(r,c,i): # where r , c and i stands for row, column and character we searching for
            # then we check for conditions if not out of bounds, if there is we are not repeating
            # a character, and if the character we are using isn't in the word we searching for.
            if i == len(word):
                return True


            if( r < 0 or c < 0 or r >= rows or c >= columns 
            or word[i] != board[r][c] or (r,c) in path):
               return False

            
            path.add((r,c))

            res = (dfs(r,c+1,i+1) or
                dfs(r+1,c,i+1) or
                dfs(r-1,c, i+1) or
                dfs(r, c-1, i+1))
             
            path.remove((r,c))
            return res

        for r in range(rows):
            for c in range(columns):
                if dfs(r,c,0):
                    return True
        return False




        
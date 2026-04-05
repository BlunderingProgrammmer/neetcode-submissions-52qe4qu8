class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        #create a running hash for each row and each col 
        self.row_hash = collections.defaultdict(int)
        self.col_hash = collections.defaultdict(int)
        self.main_diagnoal = 0
        self.reverse_diagonal = 0

    def move(self, row: int, col: int, player: int) -> int:#no need of loops since it can be calculated movewise
        move_value = 1 if player == 1 else -1
        self.row_hash[row] += move_value
        self.col_hash[col] += move_value
        #check if its a  main_diagnoal
        if row == col:
            self.main_diagnoal += move_value
        #use if instead of elif cuz eg (1,1) can be both in main diagonal as well as reverse diagonal
        if row + col == self.n -1:
            self.reverse_diagonal += move_value
        #now check for absolute move_value 
        #check and comparing max reduce lines of code
        if max(abs(self.row_hash[row]),abs(self.col_hash[col]),abs(self.main_diagnoal),abs(self.reverse_diagonal)) == self.n:
            return player
        return 0 



# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

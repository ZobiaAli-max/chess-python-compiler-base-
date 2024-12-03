class ChessGame:
    def __init__(self):
        self.board = self.create_board()
        self.current_player = 'white'

    def create_board(self):
        board = []
        for _ in range(8):
            row = [' '] * 8
            board.append(row)
        for i in range(8):
            board[1][i] = 'wp'
            board[6][i] = 'bp'
        board[0] = ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
        board[7] = ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR']
        return board

    def print_board(self):
        for row in self.board:
            print(" ".join(row))
        print()

    def move_piece(self, start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        piece = self.board[start_row][start_col]
        if piece == ' ':
            print("No piece at that position!")
            return False
        elif (self.current_player == 'white' and piece[0] != 'w') or \
             (self.current_player == 'black' and piece[0] != 'b'):
            print("It's not your turn!")
            return False

        # Simple move validation
        # Add more complex move validation for specific pieces (e.g., knight, bishop, etc.)
        if self.board[end_row][end_col] != ' ':
            print("Invalid move! Destination already occupied.")
            return False
        self.board[end_row][end_col] = piece
        self.board[start_row][start_col] = ' '
        self.current_player = 'black' if self.current_player == 'white' else 'white'
        return True

    def play(self):
        while True:
            self.print_board()
            print(f"It's {self.current_player}'s turn.")
            start_pos = tuple(map(int, input("Enter start position (row, col): ").split(',')))
            end_pos = tuple(map(int, input("Enter end position (row, col): ").split(',')))
            if self.move_piece(start_pos, end_pos):
                print("Move successful!")
            else:
                print("Invalid move. Try again.")


if __name__ == "__main__":
    game = ChessGame()
    game.play()

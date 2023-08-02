class ChessPiece:
    def __init__(self, color):
        self.color = color
        self.is_alive = True

    def kill(self):
        self.is_alive = False

    def __repr__(self):
        return self.color + " Chess Piece"

class Pawn(ChessPiece):
    def __init__(self, color):
        super().__init__(color)

    def move(self):
        print("Moving Pawn")

class Knight(ChessPiece):
    def __init__(self, color):
        super().__init__(color)

    def move(self):
        print("Moving Knight")

class Bishop(ChessPiece):
    def __init__(self, color):
        super().__init__(color)

    def move(self):
        print("Moving Bishop")

class Rook(ChessPiece):
    def __init__(self, color):
        super().__init__(color)

    def move(self):
        print("Moving Rook")

class Queen(ChessPiece):
    def __init__(self, color):
        super().__init__(color)

    def move(self):
        print("Moving Queen")

class King(ChessPiece):
    def __init__(self, color):
        super().__init__(color)

    def move(self):
        print("Moving King")

class ChessBoard:
    def __init__(self):
        self.board = [
            [Rook("White"), Knight("White"), Bishop("White"), Queen("White"), King("White"), Bishop("White"), Knight("White"), Rook("White")],
            [Pawn("White"), Pawn("White"), Pawn("White"), Pawn("White"), Pawn("White"), Pawn("White"), Pawn("White"), Pawn("White")],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [Pawn("Black"), Pawn("Black"), Pawn("Black"), Pawn("Black"), Pawn("Black"), Pawn("Black"), Pawn("Black"), Pawn("Black")],
            [Rook("Black"), Knight("Black"), Bishop("Black"), Queen("Black"), King("Black"), Bishop("Black"), Knight("Black"), Rook("Black")],
        ]

    def print_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(self.board[i][j], end=" ")
            print()

    def move_piece(self, from_row, from_col, to_row, to_col):
        piece = self.board[from_row][from_col]
        if piece != " ":
            if piece.is_alive:
                piece.move()
                self.board[to_row][to_col] = piece
                self.board[from_row][from_col] = " "
            else:
                print("This piece is dead.")
        else:
            print("No piece found.")

chess_board = ChessBoard()
chess_board.print_board()
chess_board.move_piece(1, 0, 3, 0)
chess_board.print_board()
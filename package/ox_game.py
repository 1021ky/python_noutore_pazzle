class Board:
    MARU = "○"
    BATSU = "☓"
    DEFAULT = "　"

    def __init__(self) -> None:
        self._cells = [
            [Board.DEFAULT, Board.DEFAULT, Board.DEFAULT],
            [Board.DEFAULT, Board.DEFAULT, Board.DEFAULT],
            [Board.DEFAULT, Board.DEFAULT, Board.DEFAULT],
        ]

    @property
    def cells(self):
        return self._cells

    @cells.setter
    def cells(self, x, y, value):
        self._cells[x][y] = value


class BoardViewer:
    def __init__(self, board) -> None:
        self._board = board

    def print(self):
        for rows in self._board.cells:
            for cell in rows:
                print("|" + cell, end="")
            else:
                print("|")


def main():
    board = Board()
    viewer = BoardViewer(board)
    viewer.print()


if __name__ == "__main__":
    main()

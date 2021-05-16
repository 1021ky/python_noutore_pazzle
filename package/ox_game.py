from itertools import chain


class Board:
    MARU = "o"
    BATSU = "x"
    DEFAULT = " "

    def __init__(self) -> None:
        self._cells = [
            [Board.DEFAULT, Board.DEFAULT, Board.DEFAULT],
            [Board.DEFAULT, Board.DEFAULT, Board.DEFAULT],
            [Board.DEFAULT, Board.DEFAULT, Board.DEFAULT],
        ]

    @property
    def cells(self):
        return self._cells

    def update_cell(self, x, y, value):
        self._cells[x][y] = value


class BoardViewer:
    def __init__(self, board) -> None:
        self._board = board

    def print(self):
        for row in self._board.cells:
            for cell in row:
                print("|" + cell, end="")
            else:
                print("|")


class Referee:
    def __init__(self, board: Board) -> None:
        self._turn_count = 0
        self._board = board

    @property
    def turn_count(self):
        return self._turn_count

    @turn_count.setter
    def turn_count(self):
        self._turn_count = self._turn_count + 1

    def judge_victory(self):
        cells = self._board.cells
        lines = [
            # horizontal
            [cells[0][0], cells[0][1], cells[0][2]],
            [cells[1][0], cells[1][1], cells[1][2]],
            [cells[2][0], cells[2][1], cells[2][2]],
            # verticals
            [cells[0][0], cells[1][0], cells[2][0]],
            [cells[0][1], cells[1][1], cells[2][1]],
            [cells[0][2], cells[1][2], cells[2][2]],
            # diagonals
            [cells[0][0], cells[1][1], cells[2][2]],
            [cells[2][0], cells[1][1], cells[0][2]],
        ]
        for line in lines:
            not_empties = list(
                filter(lambda cell: cell in [Board.MARU, Board.BATSU], line)
            )
            if len(not_empties) == 3 and len(set(not_empties)) == 1:
                return not_empties.pop()
        return None


def main():
    board = Board()
    viewer = BoardViewer(board)
    referee = Referee(board)
    viewer.print()
    board.update_cell(0, 0, Board.MARU)
    viewer.print()
    print(referee.judge_victory())
    board.update_cell(0, 2, Board.BATSU)
    viewer.print()
    print(referee.judge_victory())
    board.update_cell(1, 1, Board.MARU)
    viewer.print()
    print(referee.judge_victory())
    board.update_cell(1, 2, Board.BATSU)
    viewer.print()
    print(referee.judge_victory())
    board.update_cell(2, 2, Board.MARU)
    viewer.print()
    print(referee.judge_victory())


if __name__ == "__main__":
    main()

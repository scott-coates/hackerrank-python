class MyGameBoard:
    def __init__(self):
        # this could also replace the `new_game` method
        pass

    def new_game(self, height, width):
        self.current_player = 1
        self.game_ongoing = True

        self.game_board = {}

        self.height = height
        self.width = width

        # create an internal repr of the board based on h X w

        # for each column, create a list/stack of counters

        for n in range(1, width + 1):
            self.game_board[n] = []

    def drop_piece(self, col):
        if self.game_ongoing:
            # based on the turn, that is the type of (X or O) that will no be placed on top of that column
            ret_val = False
            # print which player wins
            self.game_board[col].append(self.current_player)

            # after each drop, check to see if someone has scored vert, horz, or diag
            # check rows within index of 3
            col_len = len(self.game_board[col])

            if col_len >= 4:
                if all(x == self.current_player for x in self.game_board[col][-4:]):
                    ret_val = True

            row_counter = 0

            for col_index in range(1, self.width):

                game_board_col = self.game_board[col_index]

                try:
                    if game_board_col[col_len - 1] == self.current_player:
                        row_counter += 1
                    else:
                        row_counter = 0
                except:
                    row_counter = 0

                if row_counter >= 4:
                    break
            if row_counter >= 4:
                ret_val = True

            # check diaag
            # look at column, look at len for this column
            # look in

            if ret_val:
                print(self.current_player, 'won!')
                self.game_ongoing = False
            else:
                # check same column within 3
                # check within diag
                if self.current_player == 1:
                    self.current_player = 2
                else:
                    self.current_player = 1


game = MyGameBoard()
game.new_game(8, 8)

# win vert
# game.drop_piece(1)
# game.drop_piece(2)
# game.drop_piece(1)
# game.drop_piece(2)
# game.drop_piece(1)
#
# # player 2 blocks on col 1
# game.drop_piece(1)
# game.drop_piece(1)
#
# # player 2 continues
# game.drop_piece(2)
# game.drop_piece(1)
# game.drop_piece(2)

# wins horz
game.drop_piece(1)

# player 2 blocks
game.drop_piece(1)

game.drop_piece(2)
game.drop_piece(1)
game.drop_piece(3)
game.drop_piece(1)
game.drop_piece(4)

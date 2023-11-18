# Aditya Durbha
# 7/29/2023
# cli tictactoe
class Board:
    
    def __init__(self):
        self.invalid_move = False
        self.grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def print_board(self):
        print(f" {self.grid[0][0]} | {self.grid[0][1]} | {self.grid[0][2]} ")
        print("___|___|___")
        print(f" {self.grid[1][0]} | {self.grid[1][1]} | {self.grid[1][2]} ")
        print("___|___|___")
        print(f" {self.grid[2][0]} | {self.grid[2][1]} | {self.grid[2][2]} ")

#board wont update if another player chose that spot already
    def update(self, location, player):
        # if the location is not occupied, run cases
        self.invalid_move = False
        match location:
            case "1":
                if self.grid[2][0] == " " :
                    self.grid[2][0] = player
                else :
                    print("Invalid Move.")
                    self.invalid_move = True
            case "2":
                if self.grid[2][1] == " " :
                    self.grid[2][1] = player
                else :
                    print("Invalid Move.")
                    self.invalid_move = True
            case "3":
                if self.grid[2][2] == " " :
                    self.grid[2][2] = player
                else :
                    print("Invalid Move.")
                    self.invalid_move = True
            case "4":
                if self.grid[1][0] == " " :
                    self.grid[1][0] = player
                else :
                    print("Invalid Move.")
                    self.invalid_move = True
            case "5":
                if self.grid[1][1] == " " :
                    self.grid[1][1] = player
                else :
                    print("Invalid Move.")
                    self.invalid_move = True
            case "6":
                if self.grid[1][2] == " " :
                    self.grid[1][2] = player
                else :
                    print("Invalid Move.")
                    self.invalid_move = True
            case "7":
                if self.grid[0][0] == " " :
                    self.grid[0][0] = player
                else :
                    print("Invalid Move.")
                    self.invalid_move = True
            case "8":
                if self.grid[0][1] == " " :
                    self.grid[0][1] = player
                else :
                    print("Invalid Move.")
                    self.invalid_move = True
            case "9":
                if self.grid[0][2] == " " :
                    self.grid[0][2] = player
                else :
                    print("Invalid Move.")
                    self.invalid_move = True
        
        
    def game_over(self) :
        #check vertical, horzontal, diagonal
        #horizontal
        for row in range(3):
            if self.grid[row][0] == self.grid[row][1] and self.grid[row][1] == self.grid[row][2] and self.grid[row][0] != " ":
                return True
            #vertical
        for col in range(3):
            if self.grid[0][col] == self.grid[1][col] and self.grid[1][col] == self.grid[2][col] and self.grid[0][col] != " ":
                return True
            #diagonal
        if self.grid[0][0] == self.grid[1][1] and self.grid[1][1] == self.grid[2][2] and self.grid[1][1] != " ":
            return True
        if self.grid[2][0] == self.grid[1][1] and self.grid[1][1] == self.grid[0][2] and self.grid[1][1] != " ":
            return True
        #hey if every cell has been filled then game is over
        for row in range(3):
            for col in range(3):
                if self.grid[row][col] == " ":
                    return False
        return True

    
def main():
    board1 = Board()
    board1.print_board()
    player = "X"
    while not board1.game_over():
        select = input("Select 1-9 on the numpad")
        board1.update(select, player)
        if player == "X" and not board1.invalid_move:
            player = "O"
        elif player == "O" and not board1.invalid_move:
            player = "X"
        board1.print_board()
    print("you win. the transitive property never fails")
    quit()
    # None | None | None
    # None | None | None
    # None | None | None
if __name__ == "__main__":
    main()
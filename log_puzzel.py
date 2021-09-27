import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class homescreen:

    def __init__(self):
        self.selected_level = 1
        self.levels_avalible = 1

        self.top =    [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ],
                       [" ", " ", " ", " ", " ", "L", "O", "G", " ", " ", "R", "O", "L", "L", "E", "R", " ", " ", " ", " ", " ", ],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ]]
        self.middle = [[" ", "-", "-", "-", " ", "#", "#", "#", " ", "#", "#", "#", " ", "#", "#", "#", " ", "#", "#", "#", " ", ],
                       [" ", "|", "1", "|", " ", "#", "#", "#", " ", "#", "#", "#", " ", "#", "#", "#", " ", "#", "#", "#", " ", ],
                       [" ", "-", "-", "-", " ", "#", "#", "#", " ", "#", "#", "#", " ", "#", "#", "#", " ", "#", "#", "#", " ", ]]
        self.bottom = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ],
                       [" ", " ", " ", " ", " ", " ", " ", "P", "R", "E", "S", "S", " ", "S", " ", " ", " ", " ", " ", " ", " ", ],
                       [" ", " ", " ", " ", " ", " ", "T", "O", " ", " ", "S", "T", "A", "R", "T", " ", " ", " ", " ", " ", " ", ],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ],
                       [" ", " ", " ", " ", " ", " ", " ", "P", "R", "E", "S", "S", " ", "Q", " ", " ", " ", " ", " ", " ", " ", ],
                       [" ", " ", " ", " ", " ", " ", " ", "T", "O", " ", "E", "X", "I", "T", " ", " ", " ", " ", " ", " ", " ", ],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ]]

    def print_homescreen(self):
        self.change_middle()

        for i in range(13):
            for j in range(21):
                if i <= 2:
                    print(f"{self.top[i][j]}", end= " ")
                elif i > 2 and i < 6:
                    print(f"{self.middle[i - 3][j]}", end= " ")
                else:
                    print(f"{self.bottom[i - 6][j]}", end= " ")
            print()

    def check_input(self, input):
        if input.lower() == "a" or input.lower() == "d":
            self.change_selected_level(input)
            return False
        elif input.lower() == "s":
            lvl.update_selected_level(self.selected_level)
            return True
    
    def change_selected_level(self, input):
        if input.lower() == "a" and self.selected_level - 1 >= 1:
            self.selected_level -= 1
        elif input.lower() == "d" and self.selected_level + 1 <= self.levels_avalible:
            self.selected_level += 1

    def change_middle(self):

        # changing avalible

        if self.levels_avalible == 1:
            self.middle[1][2] = "1"
            for i in range(6, 19, 4):
                self.middle[1][i] = "#"

        elif self.levels_avalible == 2:
            self.middle[1][2] = "1"
            self.middle[1][6] = "2"
            for i in range(10, 19, 4):
                self.middle[1][i] = "#"

        elif self.levels_avalible == 3:
            self.middle[1][2] = "1"
            self.middle[1][6] = "2"
            self.middle[1][10] = "3"
            for i in range(14, 19, 4):
                self.middle[1][i] = "#"

        elif self.levels_avalible == 4:
            self.middle[1][2] = "1"
            self.middle[1][6] = "2"
            self.middle[1][10] = "3"
            self.middle[1][14] = "4"
            self.middle[1][18] = "#"

        elif self.levels_avalible == 5:
            self.middle[1][2] = "1"
            self.middle[1][6] = "2"
            self.middle[1][10] = "3"
            self.middle[1][14] = "4"
            self.middle[1][18] = "5"

        # changing selected

        if self.selected_level == 1:
            for i in range(0, 3, 2):
                for j in range(1, 4):
                    self.middle[i][j] = "-"
            for i in range(1, 4, 2):
                self.middle[1][i] = "|"

            for i in range(0, 3, 2):
                for j in range(5, 8):
                    self.middle[i][j] = "#"
            for i in range(5, 8, 2):
                self.middle[1][i] = "#"

            for i in range(0, 3, 2):
                for j in range(9, 12):
                    self.middle[i][j] = "#"
            for i in range(9, 12, 2):
                self.middle[1][i] = "#"

            for i in range(0, 3, 2):
                for j in range(13, 16):
                    self.middle[i][j] = "#"
            for i in range(13, 16, 2):
                self.middle[1][i] = "#"

            for i in range(0, 3, 2):
                for j in range(17, 20):
                    self.middle[i][j] = "#"
            for i in range(17, 20, 2):
                self.middle[1][i] = "#"

        elif self.selected_level == 2:
            for i in range(0, 3, 2):
                for j in range(1, 4):
                    self.middle[i][j] = "#"
            for i in range(1, 4, 2):
                self.middle[1][i] = "#"

            for i in range(0, 3, 2):
                for j in range(5, 8):
                    self.middle[i][j] = "-"
            for i in range(5, 8, 2):
                self.middle[1][i] = "|"

            for i in range(0, 3, 2):
                for j in range(9, 12):
                    self.middle[i][j] = "#"
            for i in range(9, 12, 2):
                self.middle[1][i] = "#"

            for i in range(0, 3, 2):
                for j in range(13, 16):
                    self.middle[i][j] = "#"
            for i in range(13, 16, 2):
                self.middle[1][i] = "#"

            for i in range(0, 3, 2):
                for j in range(17, 20):
                    self.middle[i][j] = "#"
            for i in range(17, 20, 2):
                self.middle[1][i] = "#"

        elif self.selected_level == 3:
            for i in range(0, 3, 2):
                for j in range(1, 4):
                    self.middle[i][j] = "#"
            for i in range(1, 4, 2):
                self.middle[1][i] = "#"

            for i in range(0, 3, 2):
                for j in range(5, 8):
                    self.middle[i][j] = "#"
            for i in range(5, 8, 2):
                self.middle[1][i] = "#"

            for i in range(0, 3, 2):
                for j in range(9, 12):
                    self.middle[i][j] = "-"
            for i in range(9, 12, 2):
                self.middle[1][i] = "|"

            for i in range(0, 3, 2):
                for j in range(13, 16):
                    self.middle[i][j] = "#"
            for i in range(13, 16, 2):
                self.middle[1][i] = "#"

            for i in range(0, 3, 2):
                for j in range(17, 20):
                    self.middle[i][j] = "#"
            for i in range(17, 20, 2):
                self.middle[1][i] = "#"

        elif self.selected_level == 4:
            for i in range(0, 3, 2):
                for j in range(1, 4):
                    self.middle[i][j] = "#"
            for i in range(1, 4, 2):
                self.middle[1][i] = "#"

            for i in range(0, 3, 2):
                for j in range(5, 8):
                    self.middle[i][j] = "#"
            for i in range(5, 8, 2):
                self.middle[1][i] = "#"

            for i in range(0, 3, 2):
                for j in range(9, 12):
                    self.middle[i][j] = "#"
            for i in range(9, 12, 2):
                self.middle[1][i] = "#"

            for i in range(0, 3, 2):
                for j in range(13, 16):
                    self.middle[i][j] = "-"
            for i in range(13, 16, 2):
                self.middle[1][i] = "|"

            for i in range(0, 3, 2):
                for j in range(17, 20):
                    self.middle[i][j] = "#"
            for i in range(17, 20, 2):
                self.middle[1][i] = "#"
            
        elif self.selected_level == 5:
            for i in range(0, 3, 2):
                for j in range(1, 4):
                    self.middle[i][j] = "#"
            for i in range(1, 4, 2):
                self.middle[1][i] = "#"

            for i in range(0, 3, 2):
                for j in range(5, 8):
                    self.middle[i][j] = "#"
            for i in range(5, 8, 2):
                self.middle[1][i] = "#"

            for i in range(0, 3, 2):
                for j in range(9, 12):
                    self.middle[i][j] = "#"
            for i in range(9, 12, 2):
                self.middle[1][i] = "#"

            for i in range(0, 3, 2):
                for j in range(13, 16):
                    self.middle[i][j] = "#"
            for i in range(13, 16, 2):
                self.middle[1][i] = "#"

            for i in range(0, 3, 2):
                for j in range(17, 20):
                    self.middle[i][j] = "-"
            for i in range(17, 20, 2):
                self.middle[1][i] = "|"

    def update_avalible_levels(self):
        if self.levels_avalible <= 4 and self.levels_avalible < self.selected_level + 1:
            self.levels_avalible = self.selected_level + 1

class level:
    
    def __init__(self):
        self.current_level = 1
        self.level = []
        self.log_pos = [[8], [0]]
        self.start_pos = [[8], [0]]
        self.end_pos = [[0], [8]]

        self.top = [[" ", " ", " ", " ", " ", " ", " ", "L", "E", "V", "E", "L", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                    [" ", " ", " ", " ", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", " ", " ", " ", " "]]

        self.bottom = [[" ", " ", " ", " ", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", " ", " ", " ", " "],
                       [" ", "R", "E", "S", "T", "A", "R", "T", " ", "R", " ", " ", " ", " ", "E", "X", "I", "T", " ", "Q", " "]]

        self.bottom_win = [[" ", " ", " ", " ", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", " ", " ", " ", " "],
                           [" ", "Y", "O", "U", " ", "W", "O", "N", " ", " ", " ", "P", "R", "E", "S", "S", " ", "R", "/", "Q", " "]]    

    def update_selected_level(self, selected):
        self.current_level = selected
        self.level_info()
    
    def level_info(self):
        if self.current_level == 1:
            self.start_pos = [[8], [0]]
            self.end_pos = [[0], [8]]
            self.log_pos = [[8], [0]] 
            self.top[0][13] = "1"

        elif self.current_level == 2:
            self.start_pos = [[8], [4]]
            self.end_pos = [[4], [4]]
            self.log_pos = [[8], [4]]
            self.top[0][13] = "2"   
            
        elif self.current_level == 3:
            self.start_pos = [[8], [0]]
            self.end_pos = [[0], [4]]
            self.log_pos = [[8], [0]]
            self.top[0][13] = "3" 

        elif self.current_level == 4:
            self.start_pos = [[8], [0]]
            self.end_pos = [[3], [4]]
            self.log_pos = [[8], [0]] 
            self.top[0][13] = "4"

        elif self.current_level == 5:
            self.start_pos = [[2], [2]]
            self.end_pos = [[6], [6]]
            self.log_pos = [[2], [2]] 
            self.top[0][13] = "5"

    def update_level(self):
        if self.current_level == 1:
            self.level = [[" ", " ", " ", " ", " ", " ", " ", " ", "+",],
                         [" ", " ", " ", " ", " ", " ", "#", "#", "#",],
                         ["#", "#", "#", "#", "#", " ", " ", " ", " ",],
                         [" ", " ", " ", " ", "#", " ", " ", " ", " ",],
                         [" ", " ", " ", " ", "#", " ", " ", " ", " ",],
                         [" ", "#", " ", " ", " ", "#", "#", "#", " ",],
                         [" ", "#", " ", " ", " ", " ", " ", " ", " ",],
                         [" ", "#", "#", "#", "#", "#", "#", "#", " ",],
                         ["-", "#", " ", " ", " ", " ", " ", " ", " ",],]

        elif self.current_level == 2:
            self.level = [[" ", " ", " ", " ", "#", " ", " ", "#", " ",],
                         [" ", " ", " ", " ", " ", " ", " ", "#", " ",],
                         [" ", " ", " ", "#", "#", "#", " ", "#", " ",],
                         [" ", " ", "#", " ", " ", " ", " ", " ", " ",],
                         [" ", " ", " ", " ", "+", " ", " ", " ", "#",],
                         [" ", " ", "#", "#", "#", " ", " ", " ", " ",],
                         [" ", " ", "#", " ", " ", "#", "#", "#", " ",],
                         ["#", " ", "#", " ", " ", " ", " ", " ", " ",],
                         [" ", " ", " ", " ", "-", " ", " ", " ", " ",],]

        elif self.current_level == 3:
            self.level = [[" ", " ", "#", " ", "+", "#", " ", " ", " ",],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ",],
                         [" ", " ", "#", "#", " ", " ", "#", " ", " ",],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ",],
                         [" ", "#", " ", " ", "#", " ", " ", " ", " ",],
                         [" ", " ", " ", "#", " ", " ", " ", " ", " ",],
                         [" ", " ", " ", " ", " ", " ", "#", " ", "#",],
                         [" ", "#", " ", " ", "#", " ", " ", " ", " ",],
                         ["-", " ", " ", " ", " ", " ", " ", " ", " ",],]

        elif self.current_level == 4:
            self.level = [[" ", " ", "#", " ", " ", " ", " ", " ", " ",],
                         [" ", " ", " ", " ", " ", "#", " ", " ", " ",],
                         [" ", "#", " ", "#", "#", "#", " ", " ", "#",],
                         [" ", " ", " ", " ", "+", " ", "#", " ", " ",],
                         [" ", " ", "#", " ", " ", " ", " ", " ", " ",],
                         ["#", " ", " ", " ", " ", "#", " ", " ", "#",],
                         [" ", " ", "#", " ", " ", " ", " ", " ", " ",],
                         [" ", " ", " ", " ", "#", " ", "#", " ", " ",],
                         ["-", " ", " ", " ", " ", " ", " ", " ", " ",],]

        elif self.current_level == 5:
            self.level = [[" ", " ", " ", " ", " ", " ", " ", "#", "#",],
                         [" ", "#", " ", " ", "#", " ", " ", " ", " ",],
                         [" ", " ", "-", " ", " ", "#", " ", " ", " ",],
                         [" ", "#", " ", " ", " ", " ", " ", "#", " ",],
                         [" ", " ", " ", " ", " ", "#", " ", " ", " ",],
                         [" ", "#", "#", "#", " ", " ", " ", " ", "#",],
                         [" ", " ", " ", " ", "#", "#", "+", " ", " ",],
                         [" ", " ", " ", " ", " ", " ", " ", " ", " ",],
                         [" ", "#", "#", " ", " ", " ", "#", " ", " ",],]

    def move_log(self, input): 
        if input.lower() == "w":
            
            if (len(self.log_pos[0]) == 1 and len(self.log_pos[1]) == 1):
                self.log_pos[0][0] -= 2
                self.log_pos[0].append(self.log_pos[0][0] + 1)

                if self.log_pos[0][0] <= -1:
                    self.log_pos[0][0] += 2
                    self.log_pos[0].pop()
                elif self.level[self.log_pos[0][0]][self.log_pos[1][0]] == "#": 
                    self.log_pos[0][0] += 2
                    self.log_pos[0].pop()
                elif self.level[self.log_pos[0][1]][self.log_pos[1][0]] == "#":
                    self.log_pos[0][0] += 2
                    self.log_pos[0].pop()
            
            elif len(self.log_pos[1]) == 2 and len(self.log_pos[0]) == 1:
                self.log_pos[0][0] -= 1

                if self.log_pos[0][0] <= -1:
                    self.log_pos[0][0] += 1
                elif self.level[self.log_pos[0][0]][self.log_pos[1][0]] == "#": 
                    self.log_pos[0][0] += 1
                elif self.level[self.log_pos[0][0]][self.log_pos[1][1]] == "#": 
                    self.log_pos[0][0] += 1

            elif len(self.log_pos[1]) == 1 and len(self.log_pos[0]) == 2:
                self.log_pos[0][0] -= 1
                self.log_pos[0].pop()

                if self.log_pos[0][0] <= -1:
                    self.log_pos[0][0] += 1
                    self.log_pos[0].append(self.log_pos[0][0] + 1)
                elif self.level[self.log_pos[0][0]][self.log_pos[1][0]] == "#": 
                    self.log_pos[0][0] += 1
                    self.log_pos[0].append(self.log_pos[0][0] + 1)

        elif input.lower() == "a":
            if (len(self.log_pos[1]) == 1 and len(self.log_pos[0]) == 1):
                self.log_pos[1][0] -= 2
                self.log_pos[1].append(self.log_pos[1][0] + 1)

                if self.log_pos[1][0] <= -1:
                    self.log_pos[1][0] += 2
                    self.log_pos[1].pop()
                elif self.level[self.log_pos[0][0]][self.log_pos[1][0]] == "#": 
                    self.log_pos[1][0] += 2
                    self.log_pos[1].pop()
                elif self.level[self.log_pos[0][0]][self.log_pos[1][1]] == "#":
                    self.log_pos[1][0] += 2
                    self.log_pos[1].pop()

            elif len(self.log_pos[1]) == 2 and len(self.log_pos[0]) == 1:
                self.log_pos[1][0] -= 1
                self.log_pos[1].pop()

                if self.log_pos[1][0] <= -1 :
                    self.log_pos[1][0] += 1
                    self.log_pos[1].append(self.log_pos[1][0] + 1)
                elif self.level[self.log_pos[0][0]][self.log_pos[1][0]] == "#": 
                    self.log_pos[1][0] += 1
                    self.log_pos[1].append(self.log_pos[1][0] + 1)

            elif len(self.log_pos[1]) == 1 and len(self.log_pos[0]) == 2:
                self.log_pos[1][0] -= 1

                if self.log_pos[1][0] <= -1 :
                    self.log_pos[1][0] += 1
                elif self.level[self.log_pos[0][0]][self.log_pos[1][0]] == "#": 
                    self.log_pos[1][0] += 1
                elif self.level[self.log_pos[0][1]][self.log_pos[1][0]] == "#": 
                    self.log_pos[1][0] += 1

        elif input.lower() == "s":
            if (len(self.log_pos[1]) == 1 and len(self.log_pos[0]) == 1):
                self.log_pos[0][0] += 1
                self.log_pos[0].append(self.log_pos[0][0] + 1)

                if self.log_pos[0][1] >= 9:
                    self.log_pos[0][0] -= 1
                    self.log_pos[0].pop()
                elif self.level[self.log_pos[0][0]][self.log_pos[1][0]] == "#": 
                    self.log_pos[0][0] -= 1
                    self.log_pos[0].pop()
                elif self.level[self.log_pos[0][1]][self.log_pos[1][0]] == "#":
                    self.log_pos[0][0] -= 1
                    self.log_pos[0].pop()

            elif len(self.log_pos[0]) == 1 and len(self.log_pos[1]) == 2:
                self.log_pos[0][0] += 1

                if self.log_pos[0][0] >= 9:
                    self.log_pos[0][0] -= 1
                elif self.level[self.log_pos[0][0]][self.log_pos[1][0]] == "#": 
                    self.log_pos[0][0] -= 1
                elif self.level[self.log_pos[0][0]][self.log_pos[1][1]] == "#": 
                    self.log_pos[0][0] -= 1

            elif len(self.log_pos[0]) == 2 and len(self.log_pos[1]) == 1:
                self.log_pos[0][0] += 2
                self.log_pos[0].pop()

                if self.log_pos[0][0] >= 9:
                    self.log_pos[0][0] -= 2
                    self.log_pos[0].append(self.log_pos[0][0] + 1)
                elif self.level[self.log_pos[0][0]][self.log_pos[1][0]] == "#": 
                    self.log_pos[0][0] -= 2
                    self.log_pos[0].append(self.log_pos[0][0] + 1)

        elif input.lower() == "d":
            if (len(self.log_pos[0]) == 1 and len(self.log_pos[1]) == 1):
                self.log_pos[1][0] += 1
                self.log_pos[1].append(self.log_pos[1][0] + 1)

                if self.log_pos[1][1] >= 9:
                    self.log_pos[1][0] -= 1
                    self.log_pos[1].pop()
                elif self.level[self.log_pos[0][0]][self.log_pos[1][0]] == "#": 
                    self.log_pos[1][0] -= 1
                    self.log_pos[1].pop()
                elif self.level[self.log_pos[0][0]][self.log_pos[1][1]] == "#":
                    self.log_pos[1][0] -= 1
                    self.log_pos[1].pop()

            elif len(self.log_pos[1]) == 2 and len(self.log_pos[0]) == 1:
                self.log_pos[1][0] += 2
                self.log_pos[1].pop()

                if self.log_pos[1][0] >= 9:
                    self.log_pos[1][0] -= 2
                    self.log_pos[1].append(self.log_pos[1][0] + 1)
                elif self.level[self.log_pos[0][0]][self.log_pos[1][0]] == "#": 
                    self.log_pos[1][0] -= 2
                    self.log_pos[1].append(self.log_pos[1][0] + 1)

            elif len(self.log_pos[1]) == 1 and len(self.log_pos[0]) == 2:
                self.log_pos[1][0] += 1

                if self.log_pos[1][0] >= 9 :
                    self.log_pos[1][0] -= 1
                elif self.level[self.log_pos[0][0]][self.log_pos[1][0]] == "#": 
                    self.log_pos[1][0] -= 1
                elif self.level[self.log_pos[0][1]][self.log_pos[1][0]] == "#": 
                    self.log_pos[1][0] -= 1

        elif input.lower() == "r":
            self.level_info()

    def check_win(self):
        if self.log_pos == self.end_pos:
            clear_screen()
            for i in range(13):
                for j in range(21):
                    if i <= 1:
                        print(f"{self.top[i][j]}", end= " ")
                    elif i >= 2 and i <= 10 and j >= 6 and j <= 14:
                        print(f"{self.level[i - 2][j - 6]}", end= " ")
                    elif i >= 11:
                        print(f"{self.bottom_win[i - 11][j]}", end= " ")
                    elif i >= 2 and i <= 10 and (j == 5 or j == 15):
                        print("#", end= " ")
                    else:
                        print(" ", end= " ")
                print()
            hs.update_avalible_levels()
            return True
        else:
            return False

    def print_level(self):
            self.update_level()
            for i in range(len(self.log_pos[0])):
                for j in range(len(self.log_pos[1])):
                    self.level[self.log_pos[0][i]][self.log_pos[1][j]] = "@"
            
            for i in range(13):
                for j in range(21):
                    if i <= 1:
                        print(f"{self.top[i][j]}", end= " ")
                    elif i >= 2 and i <= 10 and j >= 6 and j <= 14:
                        print(f"{self.level[i - 2][j - 6]}", end= " ")
                    elif i >= 11:
                        print(f"{self.bottom[i - 11][j]}", end= " ")
                    elif i >= 2 and i <= 10 and (j == 5 or j == 15):
                        print("#", end= " ")
                    else:
                        print(" ", end= " ")
                print()



def main():
    on = True
    playing = False
    won = False

    while on:
        clear_screen()
        if not playing:   
            hs.print_homescreen()
            user_input = input("")
            if user_input.lower() == "q":
                on = False
            else:
                playing = hs.check_input(user_input)
            
        elif playing:
            lvl.print_level()
            won = lvl.check_win()
            if won:
                user_input = input("")
                if user_input.lower() == "r":
                    won = False
                    playing = True
                    lvl.level_info()
                elif user_input.lower()  == "q":
                    won = False
                    playing = False
            else:
                user_input = input("")
                if user_input == "q":
                    playing = False
                else:
                    lvl.move_log(user_input)


hs = homescreen()
lvl = level()

main()
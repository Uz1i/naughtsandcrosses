import os

class Game:
    def __init__(self):
        self.game = [
                0, 0, 0,
                0, 0, 0,
                0, 0, 0
            ]

    def render(self):
        rendered = ""
        for i, cell in enumerate(self.game):
            if cell == 1:
                rendered+="o"
            elif cell == 2:
                rendered+="x"
            else:
                rendered+="_"
            if i in (0, 1, 3, 4, 6, 7):
                rendered+="|"

            if i == 2:
                rendered+="\n"
            if i == 5:
                rendered+="\n"


        return rendered

    def parseInput(self):
        inp = input("\n? ")
        if inp == "q":
            quit()
        if inp == "r":
            self.game = [
                    0, 0, 0,
                    0, 0, 0,
                    0, 0, 0
                         ]
        try:
            pos = int(inp[0])-1

            playerType = inp[1]
            if self.game[pos] == 0:
                if playerType == "o":
                    self.game[pos] = 1
                elif playerType == "x":
                    self.game[pos] = 2
        except:
            print("There was an error when handling player input.")

g = Game()
while True:
    print(g.render())
    g.parseInput()
    os.system('cls' if os.name == 'nt' else 'clear')

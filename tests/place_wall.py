class Player:
    def __init__(self, x, y, color, idy):
        self.id = idy
        self.x = x
        self.y = y
        self.color = color
        self.walls = []
    
    def move_from_path(self, s):
        print("Im moving from a path!", s)

    def think_greedy(self, s):
        print("Im thinking...")
        self.move_from_path(s)

initState = [[0, 8, 'royalblue'], [16,8,'limegreen'], 
                 [8, 0, 'gold'],     [8, 16, 'deeppink']]

players = []

nop = 4

for i in range(nop):
    pl = Player(initState[i][0], initState[i][1], initState[i][2], i+1)
    players.append(pl)



def place_wall_ai():
    for p in players:
        print(p.id, p.x, p.y, p.color)
        p.think_greedy("hello")

place_wall_ai()
import os

def map_update():
    earth = []
    N = 20
    for i in range(N):
        line = []
        for j in range(N):
            line.append(None)
        earth.append(line)

    for i in creatures:
        x = i.pos_x
        y = i.pos_y
        earth[y][x] = i

    return earth

def prt_earth():
    for i in earth:
        for j in i:
            print(f"{j.__str__():<10}",end=" ")
        print()

class cell:
    def __init__(self, size, speed, sence, pos):
        self.size = size
        self.speed = speed
        self.sence = sence

        self.pos = pos
        self.pos_x = pos[0]
        self.pos_y = pos[1]
    
    def __str__(self):
        return f"{self.size}, {self.speed}, {self.sence}"

    def sencer(self):
        self.sence_map = []
        for i in range(2*self.sence+1):
            line = []
            for j in range(2*self.sence+1):
                try:
                    it = earth[self.pos_y - self.sence + i][self.pos_x - self.sence + j]
                    if it != None:
                        line.append(self.size-it.size)
                    else: line.append(0)
                except:
                    pass
            self.sence_map.append(line)
    
    def analyze(self):
        k = []
        for i in range(len(self.sence_map)):
            k.append(self.sence_map[i].copy())
        self.point_map = k

        for i in range(len(self.point_map)):
            for j in range(len(self.point_map[i])):
                if (i,j) != (self.sence,self.sence):
                    try:
                        self.point_map[i][j] = 10/self.point_map[i][j] * 1/(abs(self.sence - i) + abs(self.sence - j))
                    except:
                        pass

    def move(self):
        self.destination = [0,0]
        most = -1000
        for i in self.point_map:
            for j in i:
                if j > most:
                    most = j
                    self.destination[0] = i.index(j) - self.sence
                    self.destination[1] = self.point_map.index(i) - self.sence
        self.target = earth[self.pos_y+self.destination[1]][self.pos_x+self.destination[0]]

        for i in range(self.speed):
            if self.destination[0] > 0:
                if earth[self.pos_x + 1][self.pos_y] == None or self.destination == [1,0]:
                    self.pos_x += 1
                    self.destination[0] -= 1
                    map_update()
                    print()
                    prt_earth()
                    continue
            if self.destination[0] < 0:
                if earth[self.pos_x - 1][self.pos_y] == None or self.destination == [-1,0]:
                    self.pos_x -= 1
                    self.destination[0] += 1
                    map_update()
                    print()
                    prt_earth()
                    continue
            if self.destination[1] < 0:
                if earth[self.pos_x][self.pos_y - 1] == None or self.destination == [0,-1]:
                    self.pos_x -= 1
                    self.destination[1] += 1
                    map_update()
                    print()
                    prt_earth()
                    continue
            if self.destination[1] > 0:
                if earth[self.pos_x][self.pos_y + 1] == None or self.destination == [0,1]:
                    self.pos_x += 1
                    self.destination[1] -= 1
                    map_update()
                    print()
                    prt_earth()
                    continue
            break
        map_update()
        print()
        prt_earth()
        print()
 

creatures = []
creatures.append(cell(5,2,2,(4,4)))

creatures.append(cell(1,3,2,(2,4)))
creatures.append(cell(3,3,2,(4,2)))
creatures.append(cell(7,3,2,(6,4)))
creatures.append(cell(9,3,2,(4,6)))


while True:
    os.system("cls")
    earth = map_update()

    prt_earth()

    for i in creatures:
        i.sencer()
        i.analyze()

    i = creatures[0]
    i.move()

    input()
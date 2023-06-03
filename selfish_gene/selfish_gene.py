import random as rd
import os
sunE = 3
earth = 70

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def fight(a,b):
    fight = [None,None]

    if a != "None" and b != "None":
        if (a.type, b.type) == ("producer","producer"):
            fight[0] = sunE * a.height / (a.height + b.height)
            fight[1] = sunE * b.height / (a.height + b.height)
        elif (a.type, b.type) == ("producer","fst_consumer"):
            b.eat(a.eaten())
        elif (a.type, b.type) == ("fst_consumer","producer"):
            a.eat(b.eaten())
        elif (a.type, b.type) == ("fst_consumer","scd_consumer"):
            b.hunt()
            a.run()
            b.eat(a.eaten())
        elif (a.type, b.type) == ("scd_consumer","fst_consumer"):
            a.hunt()
            b.run()
            a.eat(b.eaten())
        elif (a.type, b.type) == ("fst_consumer","fst_consumer"):
            a.eaten()
        elif (a.type, b.type) == ("scd_consumer","scd_consumer"):
            a.hunt()
            b.hunt()
            if rd.random() < a.height / (a.height+b.height):
                a.eat(b.eaten())
            else:
                b.eat(a.eaten())

    elif a != "None":
        if a.type == "producer":
            fight[0] = sunE
    elif b != "None":
        if b.type == "producer":
            fight[1] = sunE
    return fight

class organism:
    def __init__(self, species, energy,type,body):
        self. species = species
        self. type = type
        self. energy = energy
        self. body_energy = body
        self. height = 1
        self. useage = 0.1
        self. enghE = 1
    
    def __str__(self):
        if self.type == "producer":
            color = bcolors.OKGREEN
        elif self.type == "fst_consumer":
            color = bcolors.OKBLUE
        elif self.type == "scd_consumer":
            color = bcolors.WARNING
        profile = color + f"{self.species} ({self.type}): {round(self.energy,1)},{self.height}" + bcolors().ENDC
        return profile

    def eat(self,food):
        self.energy += food

    def eaten(self):
        nature.remove(self)
        return self.energy + self.body_energy*self.height
    
    def grow(self):
        pass

    def reproduce(self):
        pass

    def update(self):
        self.energy -= self.useage * self.height
        self.enghE = self.useage * self.height * 4
        if self.energy > self.height + self.enghE and rd.random() < 1/4:
            self.grow()
        if self.energy <= 0:
            if self in nature:
                self.eaten()
        if self.energy > self.enghE + self.body_energy + 5 and rd.random() < 4/5:
            if len(nature) < 2*earth:
                self.reproduce()

class producer(organism):

    def __init__(self, species, energy, body):
        super().__init__(species, energy, "producer", body)
        self.useage = 0.02

    def grow(self):
        self.height += 1
        self.energy -= 2

    def reproduce(self):
        nature.append(producer(self.species, 2, self.body_energy))
        self.energy -= self.body_energy + 2

class fst_consumer(organism):
    def __init__(self, species, energy,  body):
        super().__init__(species, energy, "fst_consumer", body)
        self.useage = 0.3

    def grow(self):
        self.height += 1
        self.energy -= self.height
    
    def run(self):
        self.energy -= 2
        
    def reproduce(self):
        nature.append(fst_consumer(self.species, 5, self.body_energy))
        self.energy -= self.body_energy + 5
        
class scd_consumer(organism):
    def __init__(self, species, energy,  body):
        super().__init__(species, energy, "scd_consumer", body)
        self.useage = 0.3
        self.height += 3

    def grow(self):
        self.height += 1
        self.energy -= self.height - 3
    
    def hunt(self):
        self.energy -= 2
        
    def reproduce(self):
        nature.append(scd_consumer(self.species, 5, self.body_energy))
        self.energy -= self.body_energy + 6


nature = []
nature.append(producer("Grass",2,0.5))
nature.append(fst_consumer("bunny", 5, 2))
nature.append(scd_consumer("wolf", 7, 3))

while True:
    os.system("cls")
    world = []
    for i in range(earth):
        world.append(["None","None"])
    for k in nature.copy():
        while True:
            m = rd.randrange(earth)
            n = rd.randrange(2)
            if world[m][n] == "None":
                world[m][n] = k
                break
    
    for i in world:
        print(f"{i[0].__str__():<35} {i[1].__str__()}")

    for i in world.copy():
        k = fight(i[0],i[1])
        if k[0] != None:
            i[0].eat(k[0])
        if k[1] != None:
            i[1].eat(k[1])
        for j in i:
            if j != "None":
                j.update()

    command = input()
    if command == "grass":
        new = producer("Grass",2,0.5)
    elif command == "bunny":
        new = fst_consumer("bunny", 5, 2)
    elif command == "wolf":
        new = scd_consumer("wolf", 7, 3)
    else:
        new = None
    
    if new != None:
        if len(nature) == 0:
            nature.append(new)
        else:
            nature[rd.randrange(len(nature))] = new
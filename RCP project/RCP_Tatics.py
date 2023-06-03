import random
count = 1
RCP = ['rock', 'scissor', 'paper']
people= []
delete_list = []
append_list = []

def rcp(a,b):
    
    # print(f"{a} : {b}")
    pl1 = RCP.index(a)
    pl2 = RCP.index(b)
    if  pl1 == pl2:
        return 'draw'
    elif pl1-pl2 in [-1,2]:
        return 'win'
    else:
        return 'lose'


class person:
    def __init__(self, id, static, gen):
        self.id = id
        self.static = static
        self.point = 0
        for i in range(len(self.static)):
            if self.static[i] <0:
                self.static[i] = 0;
        self.generation = gen

    def __str__(self):
        return f'ID : {self.id:<7}  | STATIC : {self.static[0]:<3} / {self.static[1]:<3} / {self.static[2]:<3}  | GEN {self.generation}   POINT : {self.point}'
    
    def __lt__(self,other):
        return self.point > other.point
    
    def play(self):
        total = self.static[0]+self.static[1]+self.static[2]+3
        self.choices = random.randrange(total)
        if self.choices < self.static[0]+1:
            return 'rock'
        elif self.choices < self.static[0]+self.static[1]+2:
            return 'scissor'
        else:
            return 'paper'


    def replicate (self):
        self.newstatic = [self.static[0] + random.randrange(-2,2,1), self.static[1]+ random.randrange(-2,2,1), self.static[2]+ random.randrange(-2,2,1)]
        return person(count,self.newstatic,self.generation+1)

for i in range(100):
    people.append(person(count,[100+ random.randrange(-100,100,5),100+ random.randrange(-100,100,5),100+ random.randrange(-100,100,5)],1))
    count +=1

for i in people:
    print(i)
print('-----------------------------------------------------------------------------------')
for i in range(400):
    # One game to survive
    # random.shuffle(people)
    # for j in range(50):
    #     while True:
    #         result = rcp(people[j].play(),people[j+50].play())

    #         if result == 'draw':
    #             continue
    #         elif result == 'win':
    #             append_list.append(people[j].replicate())
    #             count += 1
    #             delete_list.append(j+50)
    #         elif result == 'win':
    #             append_list.append(people[j+50].replicate())
    #             count += 1
    #             delete_list.append(j)
    #         break
    # for j in range(len(delete_list)):
    #     people[delete_list[j]] = append_list[j]
        

# Several games to survive
    for j in people:
        j.point = 0
    for j in range(len(people)):
        for k in range(len(people)):
            if k != j:
                result = rcp(people[j].play(),people[k].play())
                if result == 'draw':
                    pass
                elif result == 'win':
                    people[j].point += 1
                    people[k].point -= 1
                elif result == 'lose':
                    people[j].point -= 1
                    people[k].point += 1

    people.sort()
    for j in range(50):
        people[j+50] = people[j].replicate()
        count += 1

for j in people:
    j.point = 0
for j in range(len(people)):
    for k in range(len(people)):
        if k != j:
            result = rcp(people[j].play(),people[k].play())
            if result == 'draw':
                pass
            elif result == 'win':
                people[j].point += 1
                people[k].point -= 1
            elif result == 'lose':
                people[j].point -= 1
                people[k].point += 1

people.sort()
for i in people:
    print(i)
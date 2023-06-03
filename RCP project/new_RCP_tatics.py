import random
count = 1
RCP = ['rock', 'scissor', 'paper']
people= []
delete_list = []
append_list = []

def rcp(a,b):
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
        for i in range(len(self.static)):
            if self.static[i] <0:
                self.static[i] = 0;
        self.generation = gen
        self.point = 0

    def __str__(self):
        return f'ID : {self.id:<7}  | STATIC : {self.static[0]:<3} / {self.static[1]:<3} / {self.static[2]:<3}  | GEN {self.generation}'
    
    def play(self):
        self.choices = []
        for i in range(self.static[0]):
            self.choices.append('rock')
        for i in range(self.static[1]):
            self.choices.append('scissor')
        for i in range(self.static[2]):
            self.choices.append('paper')

        return random.choice(self.choices)

    def replicate (self):
        self.newstatic = [self.static[0] + random.randrange(-3,3,1), self.static[1]+ random.randrange(-3,3,1), self.static[2]+ random.randrange(-3,3,1)]
        return person(count,self.newstatic,self.generation+1)

for i in range(100):
    people.append(person(count,[100+ random.randrange(-50,50,5)+ random.randrange(-50,50,5),100+ random.randrange(-50,50,5)+ random.randrange(-50,50,5),100+ random.randrange(-50,50,5)+ random.randrange(-50,50,5)],1))
    count +=1


for i in range(5):
    print(f'gen{i}')
    delete_list = []
    for j in range(len(people)):
        for k in range(len(people)):
            if j != k:
                result = rcp(people[j].play(), people[k].play())
                if result == 'draw':
                    pass
                elif result == 'win':
                    people[j].point += 1
                    people[k].point -= 1
                elif result == 'lose':
                    people[j].point -= 1
                    people[k].point += 1
    

    for j in people:
        if j.point < 0:
            delete_list.append(people.index(j))

    delete_list.reverse()
    for j in delete_list:
        people.remove(people[j])
    for j in people:
        append_list.append(j.replicate())
    people += append_list

for i in people:
    print(i)
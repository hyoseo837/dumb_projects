import math
baam = ['1','2','3','4']
coice = '0'
GC = 6.67*(10**-11)

def ask(a):
    m1,m2,r,F = 0,0,0,0
    if a != '1':
        m1 = float(input('what is value of m1 : '))
    if a != '2':
        m2 = float(input('what is value of m2 : '))
    if a != '3':
        r = float(input('what is value of r : '))
    if a != '4':
        F = float(input('what is value of F : '))
    a = int(a)
    result = [m1,m2,r,F]
    result.remove(result[a-1])
    return result


print('what do you want to get ?')
print('1. Mass of 1st object (kg)')
print('2. Mass of 2nd object (kg)')
print('3. distance between two object (m)')
print('4. Force between two object (N)')

while coice not in baam:
    coice = input(': ')

if coice == '1':
    numbers = ask(coice)
    m2 = numbers[0]
    r = numbers[1]
    F = numbers[2]
    m1 = F*r*r/(GC*m2)
    print(f'mass of 1st object is {m1} kg')
elif coice == '2':
    numbers = ask(coice)
    m1 = numbers[0]
    r = numbers[1]
    F = numbers[2]
    m2 = F*r*r/(GC*m1)
    print(f'mass of 2nd object is {m2} kg')
elif coice == '3':
    numbers = ask(coice)
    m1 = numbers[0]
    m2 = numbers[1]
    F = numbers[2]
    r = m1*m2*GC/F
    r = math.sqrt(r)
    print(f'distance between two object is {r} m')
elif coice == '3':
    numbers = ask(coice)
    m1 = numbers[0]
    m2 = numbers[1]
    r = numbers[2]
    F = m1*m2*GC/(r*r)
    print(f'Force between two object is {F} N')
import random
import os

nameing_1 = ["연습용 막대기","목검","철검","사무라이검","요검","마검","신검"]
nameing_2 = ["쓸만한","묵직한","쓸데없이 큰","전통의","강력한","무한한","용의"]
sword_level = 0
sword_name = ""
money = 0

def name_sword(level):
    name = f"{nameing_2[level%7]} {nameing_1[(level%49)//7]}" 
    return name

while True:
    print()
    print()
    print(f"성공 확률 : {100 - sword_level}%")
    print(f"파괴 확률 : {sword_level/10}%")    
    print()
    if input("강화!") == "n":
        break
    else:
        os.system("cls")
        if random.random() > sword_level/100:
            print()
            print()
            print()
            print(f"{name_sword(sword_level)} => {name_sword(sword_level+1)}")
            print()
            print("강화 성공!")
            sword_level += 1
        elif random.random() < sword_level/1000:
            print()
            print()
            print()
            print("파괴됨!")
            print()
            print()
            print()

            sword_level = 0
        else:
            if sword_level > 10:
                print()
                print()
                print()
                print(f"{name_sword(sword_level)} => {name_sword(sword_level-1)}")
                print()
                print("강화 실패!")
                sword_level -= 1
            else:
                pass
                print()
                print()
                print()
                print(f"{name_sword(sword_level)} => {name_sword(sword_level)}")
                print()
                print("강화 실패!")

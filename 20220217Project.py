"""
import random
rand_num = random.randrange(1, 100)
input_num = 0
def getinput() :
    number = input("1이상 100미만의 수를 입력하세요 : ")
    return number

def compare(recieve) :
    if recieve > rand_num :
        return 1
    if recieve < rand_num :
        return 2
    if recieve == rand_num :
        return 3

def print(answer) :
    if answer == 1 :
        print("숫자를 더 내리세요 : ")
    if answer == 2 :
        print("숫자를 더 올리세요 : ")
    if answer == 3 :
        print("숫자가 같습니다.")


while input_num != rand_num :
    input_num = getinput()
    A = compare(input_num)
    print(A)
    """
import random
rand1, rand2, rand3 = random.randrange(1, 9)
count = 0
win = False

def comparenum(first, second, third):
    st = 0
    ba = 0
    if rand1 == first:
        st += 1
    if rand2 == second:
        st += 1
    if rand3 == third:
        st += 1
    if (rand1 == third) or (rand1 == second) :
        ba += 1
    if (rand2 == second) or (rand2 == third) :
        ba += 1
    if (rand3 == first) or (rand3 == second) :
        ba += 1
    return st, ba


def get_input() :
    Fnum, Snum, Tnum = input("숫자를 입력하세요 : ").split()
    return Fnum, Snum, Tnum

while (count==9) or (win == True) :

    A, B, C = get_input()
    strike, ball = compare(A, B, C)
    print(strike, "스트라이크,", ball, "볼")
    if strike == 3 :
        print("승리하셨습니다.")
        win = True
    if count == 9:
        print("패배하셨습니다.")
    count += 1
    strike = 0
    ball = 0




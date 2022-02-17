"""
A, B = input("두 정수를 입력하세요 : ").split()
A, B = int(A), int(B)
C = A//B
D = A%B
print(C, D)
"""

"""
x, y = input("좌표를 입력하세요")
if (x>0 and y>0)
    print("1사분면에 속합니다.")
if (x<0 and y>0)
    print("2사분면에 속합니다.")
if (x<0 and y<0)
    print("3사분면에 속합니다.")
if (x>0 and y<0)
    print("4사분면에 속합니다.")
"""
"""
x1, y1 = input("X1과 Y1을 입력하세요 : ")
x2, y2 = input("x2와 y2를 입력하세요 : ")
x1, y1 = int(x1), int(y1)
x2, y2 = int(x2), int(y2)
m1 = (y2-y1)/(x2-x1)
x3, y3 = input("X3과 Y3을 입력하세요 : ")
x4, y4 = input("x4와 y4를 입력하세요 : ")
x3, y3 = int(x3), int(y3)
x4, y4 = int(x4), int(y4)
m2 = (y4-y3)/(x4-x3)

if m1 == m2 :
    print("평행합니다.")
else :
    print("평행하지 않습니다.")
    """

"""
x, y = input("숫자를 입력하세요 : ").split()
x, y = int(x), int(y)
x2, y2 = x, y
num = 1
for i in range(2, x) :
    if (x2 % i ==0) and (y2 % i ==0) :
        num = num * i
        x2, y2 = x2/i, y2/i
        if(x2<i) or (y2<i):
            i = x

print(num)

"""
"""
num = int(input("정수를 입력하세요 : "))
i = 10
aa = 0
while i == 10*10:
     aa = num//i
     num = 
    if(aa != 0):
        print(aa, end="")
    i = i/10
"""
import random

def comparenum(k, r, l) :
    if k==r:
        if r==l :
            if(k ==7) :
                return 5
            else :
                return 2
        else :
            return 1
    if k == l :
        return 1
    if r==l :
        return 1
    else :
        return 0

num = 1
while 1 :
    a, b, c = random.randint(0, 9)
    print(a, b, c)
    score = comparenum(a, b, c)
    print(score)
    ch = input("더 하시겠습니까?")
    if ch=="n" :
        break;
    else :
        num += 1
print (score, num)



















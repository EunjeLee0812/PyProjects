"""my_list = ["가위", "바위", "보"]
a = int(input("첫 번째 사람을 입력하시오 : "))
b = int(input("두 번째 사람을 입력하시오 : "))
print("첫 번째 사람 :", my_list[a])
print("두 번째 사람 :", my_list[b])

if my_list[a] == my_list[b]:
    print("비겼습니다.")

else:
    if (a == 1 and b == 2) or (a == 0 and b == 1) or (a == 2 and b == 0):
        print("두 번째 사람이 이겼습니다.")

    else:
        print("첫 번째 사람이 이겼습니다.")"""

"""my_list = [""]
game_continue = 1

def last_check_wrong(word):


def print_words():
    i = 0
    for i in range(len(my_list)):
        print(my_list[i], "->")


print("끝말잇기 게임을 시작합니다.\n 첫 단어를 말해주세요 : ",end = "")
aa = input()
my_list.append(aa)
print_words()
num = 0

while game_continue == 1:
    if last_check_wrong(my_list[num]):
        print("끝말이 일치하지 않습니다!")"""

"""my_list = []
a = int(input("숫자를 입력하세요 : "))
for j in range(a):
    my_list.append(str(a-j))

num = 0

for i in range(a):
    for k in range(len(my_list[i])):
        if my_list[i][k] == "1":
            num += 1


print(num)"""

"""num = input("숫자를 입력하세요").split()
my_list = []
for i in range(len(num)):
    my_list.append(num[i])

for i in range(5):
    j = 0
    if my_list[i] == str(i):
        j += 1
    if j != 1:
        print("숫자는 쌍둥이가 아니며 포함되지 않은 숫자는", my_list[i], "입니다.")
    """

"""my_list = []
my_second_list = []
for i in range(99999):
    my_list.append(i+1)

for i in range(2, 50000):
    for j in range(99999):
        if j % i == 0:
            my_second_list.append(i)

for i in range(len(my_second_list)):
    for j in range(99999):
        if my_list[j] == my_second_list[i]:
            my_list.remove(j)


print("소수의 개수는 모두", len(my_list), "개 입니다.")"""

"""num = input("숫자를 입력하세요 : ")
my_list = []
for i in range(len(num)):
    my_list.append(num[len(num)-i])
c = 0
for i in range(len(num)):
    c = c + int(my_list[i])*10**i

print(c + int(num))"""

"""num = int(input("숫자를 입력하세요 : "))
my_list = []
for i in range(num-1):
    for j in range(num-1):"""




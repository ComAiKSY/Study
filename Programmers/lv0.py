"[PCCE 기출문제] 1번 / 문자 출력"
message = "Let's go"
print("3\n2\n1")
print(message)

"[PCCE 기출문제] 2번 / 각도 합치기"
angle1 = int(input())
angle2 = int(input())

sum_angle = (angle1 + angle2)%360

print(sum_angle)

"[PCCE 기출문제] 3번 / 수 나누기"
number = int(input())

answer = 0

while number > 0:
    answer += number % 100
    number //= 100

print(answer)

"[PCCE 기출문제] 4번 / 병과분류"
code = input()
last_four_words = code[-4:]

if last_four_words == "_eye":
    print("Ophthalmologyc")
elif last_four_words == "head":
    print("Neurosurgery")
elif last_four_words == "infi":
    print("Orthopedics")
elif last_four_words == "skin":
    print("Dermatology")
else:
    print("direct recommendation")

def solution(cpr):
    answer = []
    basic_order = ["check", "call", "pressure", "respiration", "repeat"]
    for action in cpr:
        for i in range(len(basic_order)):
            if action == basic_order[i]:
                answer.append(i + 1)
    return answer


def solution(storage, usage, change):
    total_usage = 0
    for i in range(len(change)):
        usage = int(usage * (100 + change[i]) / 100)
        total_usage += usage
        if total_usage > storage:
            return i

    return -1

def solution(seat, passengers):
    cur = 0
    for station in passengers:
        cur = func1(cur - func3(station))
        board = min(seat - cur, station.count("On"))
        cur += board
    return func1(seat - cur)

def solution(nickname):
    answer = ""
    for letter in nickname:
        if letter == "l":
            answer += "I"
        elif letter == "w":
            answer += "vv"
        elif letter == "W":
            answer += "VV"
        elif letter == "O":
            answer += "0"
        else:
            answer += letter
    if len(answer) < 4:   # ← 여기만 수정
        answer += "o"
    if len(answer) > 8:
        answer = answer[:8]
    return answer


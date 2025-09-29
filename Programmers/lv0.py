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
    for action in cpr:                     # 주어진 cpr 리스트에서 하나씩 확인
        for i in range(len(basic_order)):  # 기본 순서와 비교
            if action == basic_order[i]:
                answer.append(i + 1)       # 단계 번호(1부터 시작)를 추가
    return answer


def solution(storage, usage, change):
    total_usage = 0
    for i in range(len(change)):
        usage = int(usage * (100 + change[i]) / 100)  # ← 수정된 한 줄
        total_usage += usage
        if total_usage > storage:
            return i

    return -1

def solution(seat, passengers):
    cur = 0  # 현재 탑승 인원
    for station in passengers:
        # 하차(음수 방지)
        cur = func1(cur - func3(station))
        # 승차(좌석 한도 적용)
        board = min(seat - cur, station.count("On"))  # ← 핵심 한 줄
        cur += board
    # 영진이가 타려는 순간의 빈 좌석 수(영진이 착석 전 기준)
    return func1(seat - cur)
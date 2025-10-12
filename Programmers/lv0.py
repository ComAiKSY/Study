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
    if len(answer) < 4:
        answer += "o"
    if len(answer) > 8:
        answer = answer[:8]
    return answer

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
    if len(answer) < 4:
        answer += "o"
    if len(answer) > 8:
        answer = answer[:8]
    return answer

def solution(mats, park):
    R = len(park)
    C = len(park[0]) if R > 0 else 0


    bin_grid = [[1 if park[i][j] == "-1" else 0 for j in range(C)] for i in range(R)]

    # 최대 정사각형 DP
    dp = [[0] * C for _ in range(R)]
    max_sq = 0
    for i in range(R):
        for j in range(C):
            if bin_grid[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                if dp[i][j] > max_sq:
                    max_sq = dp[i][j]

    mats_set = set(mats)

    best = -1

    for k in sorted(mats_set, reverse=True):
        if k <= max_sq:
            best = k
            break

    return best

def solution(video_len, pos, op_start, op_end, commands):
    def to_sec(t):
        m, s = map(int, t.split(":"))
        return m * 60 + s

    def to_mmss(x):
        m = x // 60
        s = x % 60
        return f"{m:02d}:{s:02d}"

    L = to_sec(video_len)
    p = to_sec(pos)
    op_s = to_sec(op_start)
    op_e = to_sec(op_end)

    # 오프닝 건너뛰기: 초기 위치에 대해 우선 적용
    if op_s <= p <= op_e:
        p = op_e

    for cmd in commands:
        if cmd == "prev":
            p = max(0, p - 10)
        elif cmd == "next":
            p = min(L, p + 10)

        # 오프닝 구간이면 즉시 op_end로 이동
        if op_s <= p <= op_e:
            p = op_e

    return to_mmss(p)

def solution(data, ext, val_ext, sort_by):

    col_idx = {"code": 0, "date": 1, "maximum": 2, "remain": 3}

    # 기준 열 인덱스 추출
    ext_idx = col_idx[ext]
    sort_idx = col_idx[sort_by]

    # 조건(ext < val_ext) 필터링
    filtered = [row for row in data if row[ext_idx] < val_ext]

    filtered.sort(key=lambda row: row[sort_idx])

    return filtered
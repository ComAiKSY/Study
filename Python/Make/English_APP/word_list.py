import tkinter as tk
from tkinter import messagebox
import manage_work

# 단어 검색 시 이벤트
def enter(event=None):
    entered_text = answer.get()
    print(f"입력된 단어: {entered_text}")

# 이전 페이지 이동
def left():
    print("이전 페이지")

# 다음 페이지 이동
def right():
    print("다음 페이지")

# 메인 메뉴로 이동
def goToMenu():
    root2.destroy()
    manage_work.run()

# 모듈화된 GUI 함수
def run():
    global root2, answer
    root2 = tk.Tk()
    root2.title("영단어 학습 프로그램 - 단어 목록")
    root2.geometry("800x700")

    # 저장해놓은 단어 버튼
    btn_word = tk.Button(root2, text="저장한 단어", command=goToMenu, width=10)
    btn_word.place(relx=0.075, rely=0.03, anchor="w", x=-30)

    # 처음으로 버튼
    btn_home = tk.Button(root2, text="처음으로", command=goToMenu, width=10)
    btn_home.place(relx=1.0, rely=0.03, anchor="e", x=-30)

    # 상단 입력 영역
    frame_top = tk.Frame(root2)
    frame_top.pack(pady=10)

    label_search = tk.Label(frame_top, text="단어 검색", font=("Arial", 14))
    label_search.pack(side="left", padx=10)

    answer = tk.Entry(frame_top)
    answer.pack(side="left", padx=10)
    answer.bind("<Return>", enter)

    submit_button = tk.Button(frame_top, text="검색", command=enter)
    submit_button.pack(side="left")

    # 단어 목록 헤더
    frame_header = tk.Frame(root2)
    frame_header.pack(pady=10)

    headers = ["ID", "단어", "해석", "틀린 횟수"]
    for i, text in enumerate(headers):
        tk.Label(frame_header, text=text, font=("Arial", 14, "bold"), width=15, bg="#FFE4B5").grid(row=0, column=i, padx=7, pady=10)

    # 단어 목록 표시
    frame_words = tk.Frame(root2)
    frame_words.pack(pady=10)

    for i in range(1, 11):
        tk.Label(frame_words, text=i, font=("Arial", 14), width=15, bg="#FFE4B5").grid(row=i, column=0, padx=15, pady=10)
        tk.Label(frame_words, text=f"super{i}", font=("Arial", 14), width=15).grid(row=i, column=1, padx=15, pady=10)
        tk.Label(frame_words, text=f"안녕하세요{i}", font=("Arial", 14), width=15).grid(row=i, column=2, padx=15, pady=10)
        tk.Label(frame_words, text="123", font=("Arial", 14), width=15).grid(row=i, column=3, padx=15, pady=10)

    # 하단 네비게이션 버튼
    frame_nav = tk.Frame(root2)
    frame_nav.pack(pady=10)

    tk.Button(frame_nav, text="이전", command=left, width=20).pack(side="left", padx=15)
    tk.Label(frame_nav, text="2/236", font=("Arial", 14), width=15).pack(side="left", padx=15)
    tk.Button(frame_nav, text="다음", command=right, width=20).pack(side="left", padx=15)

    root2.mainloop()

# 직접 실행 시 (테스트 용)
if __name__ == '__main__':
    run()

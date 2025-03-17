import tkinter as tk
import test, word_list

def run():
    root = tk.Tk()
    root.title("영단어 학습 프로그램")
    root.geometry("300x250")

    tk.Label(root, text="📌 메뉴를 선택하세요", font=("Arial", 14)).pack(pady=10)

    # 단어 테스트 버튼 클릭 시
    def start_test():
        root.destroy()
        test.run()

    # 단어 목록 버튼 클릭 시
    def show_word_list():
        root.destroy()
        word_list.run()

    # 단어 관리 버튼 (기능 추가 예정)
    def manage_words():
        tk.messagebox.showinfo("단어 관리", "단어 관리 기능은 준비중입니다.")

    tk.Button(root, text="1. 단어 테스트 하기", command=start_test, width=20).pack(pady=5)
    tk.Button(root, text="2. 단어 목록 보기", command=show_word_list, width=20).pack(pady=5)
    tk.Button(root, text="3. 단어 관리", command=manage_words, width=20).pack(pady=5)
    tk.Button(root, text="4. 종료", command=root.quit, width=20).pack(pady=5)

    root.mainloop()

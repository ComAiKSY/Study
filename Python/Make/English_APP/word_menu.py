import tkinter as tk
import test, word_list, manage_work

def run():
    global root
    root = tk.Tk()
    root.title("영단어 학습 프로그램")
    root.geometry("400x300")

    # 버튼 클릭 시
    def test_click():
        root.destroy()
        test.run()

    def word_list_click():
        root.destroy()
        word_list.run()

    def manage_work_click():
        root.destroy()
        manage_work.run()

    tk.Label(root, text="📌 메뉴를 선택하세요", font=("Arial", 14)).pack(pady=10)
    tk.Button(root, text="1. 단어 테스트 하기", command=test_click, width=40).pack(pady=10)
    tk.Button(root, text="2. 단어 목록 보기", command=word_list_click, width=40).pack(pady=10)
    tk.Button(root, text="3. 단어 관리", command=manage_work_click, width=40).pack(pady=10)
    tk.Button(root, text="4. 종료", command=root.quit, width=40).pack(pady=10)

    root.mainloop()

if __name__ == '__main__':
    run()
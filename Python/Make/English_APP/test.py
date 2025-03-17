import tkinter as tk
from tkinter import messagebox

current_index = 0


def run():
    global root1, answer, count_word, word_label, current_index
    current_index = 0

    def save_word():
        messagebox.showinfo("", "단어가 저장되었습니다!")

    def enter(event=None):
        entered_text = answer.get()
        if entered_text == "cold":
            messagebox.showinfo("", "정답입니다!")
        else:
            response = messagebox.askquestion("오답!", "오답입니다! 단어를 저장하시겠습니까?")
            if response == "yes":
                save_word()
        next_word()

    def next_word():
        global current_index
        current_index += 1
        if current_index == 3:
            messagebox.showinfo("", "모든 단어를 완료했습니다!")
            root1.destroy()
            import manage_work
            manage_work.run()
        else:
            word_label.config(text=f"cold{current_index}")
            count_word.config(text=f"남은 단어 갯수: {current_index}")

    root1 = tk.Tk()
    root1.title("단어 테스트")
    root1.geometry("500x400")

    tk.Label(root1, text="정답을 입력하세요", font=("Arial", 14)).pack(pady=20)
    word_label = tk.Label(root1, text=f"cold{current_index}", font=("Arial", 25))
    word_label.pack(pady=20)

    answer = tk.Entry(root1)
    answer.place(relx=0.5, rely=0.5, anchor="center", width=200, height=25)

    submit_button = tk.Button(root1, text="입력", command=enter)
    submit_button.place(relx=0.8, rely=0.5, anchor="e", width=40)
    answer.bind("<Return>", enter)

    count_word = tk.Label(root1, text=f"남은 단어 갯수: {current_index}", font=("Arial", 14))
    count_word.pack(side="bottom", pady=10)

    root1.mainloop()


if __name__ == '__main__':
    run()

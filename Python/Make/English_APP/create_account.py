import tkinter as tk
from tkinter import messagebox
import test, manage_work, word_list

import tkinter as tk
from tkinter import messagebox
import test, manage_work, word_list


def enter(event=None):
    entered_id = answer_id.get()
    entered_password = answer_password.get()
    entered_name = answer_name.get()
    entered_number = answer_number.get()

    print(entered_id + " 1")
    print(entered_password + " 2")
    print(entered_name + " 3")
    print(entered_number+ " 4")

def register():
    print("임시")
    #레지스터 py로 이동
    root1.destroy()

#id관련
def on_focus_in_id(event):
    if answer_id.get() == "ID":  #현재 ID가 입력되어 있다면 (즉 사용자가 아무것도 이용하지 않은 상태)
        font_color = answer_id.cget("fg")
        if font_color == "gray":
            answer_id.delete(0, tk.END) #입력되어있던 ID를 삭제함
            answer_id.config(fg="black")

def on_focus_out_id(event):
    if answer_id.get() == "":  #사용자가 무언가를 입력했다가 지워서 비워졌다면
        answer_id.insert(0, "ID")  #안에 ID를 입력하고 회색으로 글자를 바꿈
        answer_id.config(fg="gray")

#패스워드
def on_focus_in_password(event):
    if answer_password.get() == "Password":  #현재 password가 입력되어 있다면 (즉 사용자가 아무것도 이용하지 않은 상태)
        font_color = answer_password.cget("fg")
        if font_color == "gray":
            answer_password.delete(0, tk.END) #입력되어있던 passwrod를 삭제함
            answer_password.config(fg="black")

def on_focus_out_password(event):
    if answer_password.get() == "":  #사용자가 무언가를 입력했다가 지워서 비워졌다면
        answer_password.insert(0, "Password")  #안에 password를 입력하고 회색으로 글자를 바꿈
        answer_password.config(fg="gray")

#이름
def on_focus_in_name(event):
    if answer_name.get() == "이름":  #현재 가 입력되어 있다면 (즉 사용자가 아무것도 이용하지 않은 상태)
        font_color = answer_name.cget("fg")
        if font_color == "gray":
            answer_name.delete(0, tk.END) #입력되어있던 를 삭제함
            answer_name.config(fg="black")

def on_focus_out_name(event):
    if answer_name.get() == "":  #사용자가 무언가를 입력했다가 지워서 비워졌다면
        answer_name.insert(0, "이름")  #안에 를 입력하고 회색으로 글자를 바꿈
        answer_name.config(fg="gray")

#전화번호
def on_focus_in_number(event):
    if answer_number.get() == "전화번호":  #현재 가 입력되어 있다면 (즉 사용자가 아무것도 이용하지 않은 상태)
        font_color = answer_number.cget("fg")
        if font_color == "gray":
            answer_number.delete(0, tk.END) #입력되어있던 를 삭제함
            answer_number.config(fg="black")

def on_focus_out_number(event):
    if answer_number.get() == "":  #사용자가 무언가를 입력했다가 지워서 비워졌다면
        answer_number.insert(0, "전화번호")  #안에 를 입력하고 회색으로 글자를 바꿈
        answer_number.config(fg="gray")

# Tkinter 윈도우 생성
#def menuPro():
global root1
root1 = tk.Tk()
root1.title("영단어 학습 프로그램")
root1.geometry("400x400")

# 버튼 생성
tk.Label(root1, text="회원가입", font=("Arial", 14)).pack(pady=10)

#id입력
answer_id = tk.Entry(root1, font=("Arial", 16), fg = "gray")
answer_id.insert(0, "ID")
answer_id.bind("<FocusIn>", on_focus_in_id)
answer_id.bind("<FocusOut>", on_focus_out_id)
answer_id.pack(pady = 10, ipady = 7)

#패스워드
answer_password = tk.Entry(root1, font=("Arial", 16), fg = "gray")
answer_password.insert(0, "Password")
answer_password.bind("<FocusIn>", on_focus_in_password)
answer_password.bind("<FocusOut>", on_focus_out_password)
answer_password.pack(pady = 10, ipady = 7)

#이름
answer_name = tk.Entry(root1, font=("Arial", 16), fg = "gray")
answer_name.insert(0, "이름")
answer_name.bind("<FocusIn>", on_focus_in_name)
answer_name.bind("<FocusOut>", on_focus_out_name)
answer_name.pack(pady = 10, ipady = 7)

#전화번호
answer_number = tk.Entry(root1, font=("Arial", 16), fg = "gray")
answer_number.insert(0, "전화번호")
answer_number.bind("<FocusIn>", on_focus_in_number)
answer_number.bind("<FocusOut>", on_focus_out_number)
answer_number.pack(pady = 10, ipady = 7)

answer_id.bind("<Return>", enter)
answer_password.bind("<Return>", enter)
answer_name.bind("<Return>", enter)
answer_number.bind("<Return>", enter)

tk.Button(root1, text="회원가입", command= enter, width = 25).pack(side="bottom", pady = 20)
#tk.Button(root1, text="4. 종료", command=root1.quit, width=15).pack(side="bottom", pady = 20)

# 실행
root1.mainloop()
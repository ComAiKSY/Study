import tkinter as tk
from tkinter import messagebox
#from test import testPro

def word_inter():
    root.destroy()
    #testPro()

def inter_word():
    root.destroy()

def any1():
    root.destroy()
    
def any2():
    root.destroy()
    

# Tkinter 윈도우 생성
#def menuPro():
global root
root = tk.Tk()
root.title("영단어 학습 프로그램")
root.geometry("400x300")

# 버튼 생성
tk.Button(root, text="1. 단어 -> 해석", command=word_inter, width=40).pack(pady=15, ipady = 10)
tk.Button(root, text="2. 해석 -> 단어", command=inter_word, width=40).pack(pady=15, ipady = 10)
tk.Button(root, text="3. 기타1", command=any1, width=40).pack(pady=15, ipady = 10)
tk.Button(root, text="4. 기타2", command=any2, width=40).pack(pady=15, ipady = 10)

# 실행
root.mainloop()
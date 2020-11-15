# -*- coding: utf-8 -*-

from tkinter import *
import pandas as pd

dat = pd.read_excel("data.xlsx")

def click():
    # 01 entry에 적은 단어를 기억한다.
    # 02 뜻을 출력할 output(텍스트상자)를 초기화한다.
    # 03 우리가 입력한 단어로 뜻을 찾는다.
    # 04 해당되는 뜻을 넣는다.
    global dat
    
    word = entry.get()
    output.delete(0.0, END)
    try:
        def_word = dat.loc[dat["단어"] == word, "뜻"].values[0]
    except:
        def_word = "단어의 뜻을 찾을 수 없습니다"
    output.insert(END, def_word)
    
window = Tk()
window.title("My Dictionary")

label = Label(window, text = "검색할 단어를 입력한 후, 뜻 확인 버튼을 눌러주세요")
label.grid(row = 0, column = 0, sticky = W)

entry = Entry(window, width = 15, bg = "light green")
entry.grid(row = 1, column = 0, sticky = W)

btn = Button(window, text = "뜻 확인", width = 5, command = click)
btn.grid(row = 2, column = 0, sticky = W)

# columnspan은 위젯이 한 칼럼 이상의 공간을 차지하도록 하는 데 사용.
# columnspan : 위젯점유가 얼마나 컬럼을 차지할 것인가. 기본값 1
output = Text(window, width = 50, height = 6, wrap = WORD, background = "light green")
output.grid(row = 3, column = 0, columnspan = 2, sticky = W)

window.mainloop()
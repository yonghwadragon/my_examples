""" 
GUI 관련 예제 코드 
"""
import tkinter as tk

def example_1():
    """간단한 윈도우 창 만들기"""
    window = tk.Tk()
    window.title("My First GUI")
    window.geometry("300x200")
    window.mainloop()

def example_2():
    """버튼 추가하기"""
    def on_click():
        print("Button Clicked!")
    window = tk.Tk()
    window.title("Button Example")
    button = tk.Button(window, text="Click Me!", command=on_click)
    button.pack()
    window.mainloop()

def example_3():
    """텍스트 입력 창과 출력"""
    def display_text():
        user_input = entry.get()
        label.config(text=f"입력한 값: {user_input}")
    window = tk.Tk()
    window.title("Input Example")
    entry = tk.Entry(window)
    entry.pack()
    button = tk.Button(window, text="확인", command=display_text)
    button.pack()
    label = tk.Label(window, text="여기에 출력됨")
    label.pack()
    window.mainloop()

def example_4():
    """간단한 계산기"""
    def calculate():
        try:
            result = eval(entry.get())  # 입력된 수식 계산
            label.config(text=f"결과: {result}")
        except Exception as e:
            label.config(text="오류: 잘못된 수식")

    window = tk.Tk()
    window.title("Calculator")

    entry = tk.Entry(window)
    entry.pack()

    button = tk.Button(window, text="계산", command=calculate)
    button.pack()

    label = tk.Label(window, text="결과가 여기에 표시됨")
    label.pack()

    window.mainloop()

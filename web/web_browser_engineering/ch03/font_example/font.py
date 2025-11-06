from tkinter import font
import tkinter
window = tkinter.Tk()
bi_times = font.Font(
    family="Times",
    size=16,
    weight="bold",
    slant="italic",
)

print(bi_times.metrics())
print(bi_times.measure("Hello World!"))

font1 = font.Font(family="Times", size=16)
font2 = font.Font(family="Helvetica", size=16, slant="italic")

x, y = 200, 200
canvas = tkinter.Canvas(window, width=400, height=400)
canvas.create_text(x, y, text="Hello", font=font1, anchor="nw")
x += font1.measure("Hello")
canvas.create_text(x, y, text=" World!", font=font2, anchor="nw")
canvas.pack()  # 캔버스를 윈도우에 표시
window.mainloop()  # 메인 이벤트 루프 실행

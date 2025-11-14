import tkinter.font

window = tkinter.Tk()
bi_times = tkinter.font.Font(
    family = "Times",
    size = 16,
    weight="bold",
    slant="italic"
)

canvas = tkinter.Canvas(window, width=400, height=400)
canvas.create_text(200, 100, text="Hello World", font=bi_times)
canvas.pack()
tkinter.mainloop()
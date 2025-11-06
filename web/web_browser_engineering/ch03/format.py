import tkinter
import tkinter.font
from ch01 import telnet
WIDTH, HEIGHT = 800, 600
HSTEP, VSTEP = 13, 18
SCROLL_STEP = 30

class Browser:
    def __init__(self):
        self.window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.window, width=WIDTH, height=HEIGHT)

        self.canvas.pack()
        self.scroll = 0
        self.window.bind("<Down>", self.scrolldown)
        self.window.bind("<Up>", self.scrollup)
        self.window.bind("<MouseWheel>", self.scrollwheel)
        self.window.bind("<Configure>", self.expand)

    def load(self, url):
        body = url.request()
        tokens = lex(body)
        self.tokens = tokens
        self.text = body
        self.display_list = Layout(tokens).display_list
        self.draw()

    def draw(self):
        self.canvas.delete("all")
        for x, y, c, f in self.display_list:
            if y > self.scroll + HEIGHT: continue
            if y + VSTEP < self.scroll: continue
            self.canvas.create_text(x, y - self.scroll, text=c, font=f, anchor="nw")

    def scrolldown(self, e):
        self.scroll += SCROLL_STEP
        self.draw()

    def scrollup(self, e):
        self.scroll -= SCROLL_STEP
        self.draw()

    def scrollwheel(self, e):
        self.scroll -= e.delta
        self.draw()

    def expand(self, e):
        global WIDTH, HEIGHT
        WIDTH = e.width
        HEIGHT = e.height
        self.display_list = Layout(self.tokens).display_list
        self.draw()

class Text:
    def __init__(self, text):
        self.text = text

class Tag:
    def __init__(self, tag):
        self.tag = tag

class Layout:
    def __init__(self, tokens):
        self.display_list = []
        self.cursor_x = HSTEP
        self.cursor_y = VSTEP
        self.weight = "normal"
        self.style = "roman"
        self.size = 12

        for tok in tokens:
            self.token(tok)

    def token(self, tok):
        if isinstance(tok, Text):
            for word in tok.text.split('\n'):
                self.word(word)
        elif tok.tag == "i":
            self.style = "italic"
        elif tok.tag == "/i":
            self.style = "roman"
        elif tok.tag == "b":
            self.weight = "bold"
        elif tok.tag == "/b":
            self.weight = "normal"
        elif tok.tag == "small":
            self.size -= 2
        elif tok.tag == "/small":
            self.size += 2
        elif tok.tag == "big":
            self.size += 4
        elif tok.tag == "/big":
            self.size -= 4

    def word(self, word):
        font = tkinter.font.Font(
            size=16,
            weight=self.weight,
            slant=self.style,
        )
        w = font.measure(word)
        if word == "\n":
            self.cursor_x = HSTEP
            self.cursor_y += VSTEP
            return
        self.display_list.append((self.cursor_x, self.cursor_y, word, font))
        self.cursor_x += w + font.measure(" ")
        if self.cursor_x + w >= WIDTH - HSTEP:
            self.cursor_y += font.metrics("linespace") * 1.25
            self.cursor_x = HSTEP

def lex(body):
    out = []
    buffer = ""
    in_tag = False
    for c in body:
        if c == "<":
            if buffer: out.append(Text(buffer))
            buffer = ""
            in_tag = True
        elif c == ">":
            out.append(Tag(buffer))
            buffer = ""
            in_tag = False
        elif not in_tag:
            buffer += c
    if not in_tag and buffer: out.append(Text(buffer))
    return out


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        Browser().load(telnet.URL("http://browser.engineering/examples/xiyouji.html"))
    else: Browser().load(telnet.URL(sys.argv[1]))

    tkinter.mainloop()

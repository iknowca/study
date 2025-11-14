import tkinter
import tkinter.font
from ch01 import telnet

WIDTH, HEIGHT = 800, 600
HSTEP, VSTEP = 13, 18
SCROLL_STEP = 30

FONTS = {}
def get_font(size, weight, style):
    key = (size, weight, style)
    if key not in FONTS:
        font = tkinter.font.Font(size=size, weight=weight, slant=style)
        label = tkinter.Label(font=font)
        FONTS[key] = (font, label)
    return FONTS[key][0]

class Browser:
    def __init__(self):
        self.display_list = None
        self.text = None
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
        text = lex(body)
        self.text = text
        self.display_list = Layout(text).display_list
        # self.display_list = layout(text)
        self.draw()

    def load_txt(self, txt):
        self.text = lex(txt)
        self.display_list = Layout(self.text).display_list
        self.draw()

    def draw(self):
        self.canvas.delete("all")
        for x, y, word, f in self.display_list:
            if y > self.scroll + HEIGHT: continue
            if y + f.metrics("linespace") * 1.25 < self.scroll: continue
            self.canvas.create_text(x, y - self.scroll, text=word, anchor="nw", font=f)

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
        self.display_list = Layout(self.text).display_list
        self.draw()

class Layout:
    def __init__(self, tokens):
        self.display_list = []
        self.cursor_x = HSTEP
        self.cursor_y = VSTEP
        self.weight = "normal"
        self.style = "roman"
        self.size =12
        self.line = []

        for tok in tokens:
            self.token(tok)
        self.flush()

    def token(self, tok):
        if isinstance(tok, Text):
            for w in tok.text.split():
                self.word(w)
        elif tok.tag == "i":
            self.style = "italic"
        elif tok.tag == "/i":
            self.style = "roman"
        elif tok.tag == "b":
            self.weight = "bold"
        elif tok.tag == "/b":
            self.weight = "normal"
        elif tok.tag == "big":
            self.size += 4
        elif tok.tag == "/big":
            self.size -= 4
        elif tok.tag == "small":
            self.size -= 2
        elif tok.tag == "/small":
            self.size += 2
        elif tok.tag == "br":
            self.flush()
        elif tok.tag == "/p":
            self.flush()
            self.cursor_y += VSTEP

    def word(self, word):
        font = get_font(self.size, self.weight, self.style)
        w = font.measure(word)
        if self.cursor_x + w >= WIDTH - HSTEP:
            self.flush()
        self.line.append((self.cursor_x, word, font))
        self.cursor_x += w + font.measure(" ")

    def flush(self):
        if not self.line: return
        metrics = [font.metrics() for x, word, font in self.line]
        max_ascent = max([metric["ascent"] for metric in metrics])
        baseline = self.cursor_y + 1.25 * max_ascent
        for x, word, font in self.line:
            y = baseline - font.metrics("ascent")
            self.display_list.append((x, y, word, font))
        max_descent = max([metric["descent"] for metric in metrics])
        self.cursor_y = baseline + 1.25 * max_descent
        self.cursor_x = HSTEP
        self.line = []


def lex(body):
    out = []
    buf = ""
    in_tag = False
    for c in body:
        if c == "<":
            in_tag = True
            if buf: out.append(Text(buf))
            buf = ""
        elif c == ">":
            in_tag = False
            out.append(Tag(buf))
            buf = ""
        else:
            buf += c
    if not in_tag and buf: out.append(Text(buf))
    return out

class Text:
    def __init__(self, text):
        self.text = text

class Tag:
    def __init__(self, tag):
        self.tag = tag

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        Browser().load(telnet.URL("http://browser.engineering/text.html"))
    else: Browser().load(telnet.URL(sys.argv[1]))
    # Browser().load_txt("<small>a</small><big>A</big><i>i</i><b>b</b>")
    tkinter.mainloop()

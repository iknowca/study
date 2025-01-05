from manim import *

class main(Scene):
    def construct(self):
        X = VGroup()
        W = VGroup()
        Y = VGroup()
        
        for i in range(2):
            X.add(Circle(radius=0.3))
        
        for i in range(3):
            Y.add(Circle(radius=0.3))
        
        X.arrange(UP, buff=1)
        Y.arrange(UP, buff=1)
        

        nodes = VGroup(X, Y).arrange(RIGHT, buff=3).shift(LEFT*4)
        for i in X:
            for j in Y:
                W.add(Arrow(i.get_center(), j.get_center(), buff=0.5))
                
        self.add(X, W, Y)
        
        eq = VGroup()
        eqeq = Tex(r"$=$")
        eqx = Tex(r"$X$").scale(1.5)
        
        eqwv = Tex(r"""$\begin{pmatrix}
                    w_{00}&w_{01}&w_{02}\\
                    w_{10}&w_{11}&w_{12}
                    \end{pmatrix}
                    $""").scale(0.7)
        eqw = Tex(r"$W$").scale(1.5)
        eqxv = Tex(r"""$\begin{pmatrix}
                    x_{00}&
                    x_{10}
                    \end{pmatrix}
                    $""").scale(0.7)
        
        eqy = Tex(r"$Y$").scale(1.5)
        eqyv = Tex(r"""$\begin{pmatrix}
                    y_{00}&
                    y_{10}&
                    y_{20}
                    \end{pmatrix}
                    $""").scale(0.7)
        vals = VGroup(eqxv, eqwv,eqeq, eqyv).arrange(RIGHT).shift(RIGHT*3)
        eq.add(eqx, eqw, eqy)
        eqx.next_to(eqxv, UP)
        eqw.next_to(eqwv, UP)
        eqy.next_to(eqyv, UP)
        eqx.align_to(eqw, DOWN)
        eqy.align_to(eqw, DOWN)
        self.add(eq, vals)
        
        x_brace = Brace(eqxv, DOWN)
        w_brace = Brace(eqwv, DOWN)
        y_brace = Brace(eqyv, DOWN)
        
        x_brace.align_to(w_brace, DOWN)
        y_brace.align_to(w_brace, DOWN)
        
        x_brace_text = x_brace.get_text(r"$1\times 2$")
        w_brace_text = w_brace.get_text(r"$2\times 3$")
        y_brace_text = y_brace.get_text(r"$1\times 3$")
        self.add(x_brace, w_brace, y_brace, x_brace_text, w_brace_text, y_brace_text)
        
        
        Y_label = eqy.copy().next_to(Y, UP)
        X_label = eqx.copy().next_to(X, UP).align_to(Y_label, DOWN)
        W_label = eqw.copy().next_to(W, UP).align_to(Y_label, DOWN)

        self.add(Y_label, X_label, W_label)
        
        
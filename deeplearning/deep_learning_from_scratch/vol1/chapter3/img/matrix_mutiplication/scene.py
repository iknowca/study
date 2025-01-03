from manim import *

class main(Scene):
    
    def make_equation(self, A, B, C, i, j):
        
        lbox = SurroundingRectangle(A.get_rows()[i], buff = .1)
        rbox = SurroundingRectangle(B.get_columns()[j], buff = .1, color=ORANGE)
        self.play(Create(lbox))
        self.play(Create(rbox))
        
        a = A.get_rows()[i].copy()
        a0 = a[0].copy()
        a1 = a[1].copy()
        a2 = a[2].copy()
        
        b = B.get_columns()[j].copy()
        b0 = b[0].copy()
        b1 = b[1].copy()
        b2 = b[2].copy()
        
        c = C.get_rows()[i].copy()
        
        plus = MathTex(r"+")
        plus0 = plus.copy()
        plus1 = plus.copy()
        
        equal = MathTex(r"=")
        
        eq = VGroup()
        
        eq.add(a0, b0, plus0)
        
        self.play(a0.animate.move_to(DOWN*2 + LEFT*3))
        self.play(b0.animate.next_to(a0, RIGHT))
        self.play(Create(plus0.next_to(b0, RIGHT)))
        
        eq.add(a1, b1, plus1)
        
        self.play(a1.animate.next_to(plus0, RIGHT))
        self.play(b1.animate.next_to(a1, RIGHT))
        self.play(Create(plus1.next_to(b1, RIGHT)))
        
        eq.add(a2, b2)
        
        self.play(a2.animate.next_to(plus1, RIGHT))
        self.play(b2.animate.next_to(a2, RIGHT))
        self.play(Create(equal.next_to(b2, RIGHT)))
        
        ce = MathTex(r"c_{%d%d}" % (i+1, j+1)).next_to(equal, RIGHT)
        eq.add(ce, equal)
        self.play(Create(ce))
        
        self.play(ce.animate.move_to(c[j].get_center()))
        
        cbox = SurroundingRectangle(c[j], buff = .1, color=GREEN)
        self.play(Create(cbox))
        self.wait(1)
        self.play(FadeOut(eq))
        self.play(FadeOut(lbox), FadeOut(rbox), FadeOut(cbox))
    
    def construct(self):
        title = Text("Matrix Multiplication").shift(3*UP)
        self.add(title)
        
        matrix_A = Matrix(
            [["a_{11}", "a_{12}", "a_{13}"],
            ["a_{21}", "a_{22}", "a_{23}"]]
        )
        matrix_A.shift(4*LEFT)
        matrix_A_label = MathTex(r"A").next_to(matrix_A, UP)
        matmul = MathTex(r"\times").next_to(matrix_A, RIGHT)
        matrix_B = Matrix(
            [["b_{11}", "b_{12}"],
            ["b_{21}", "b_{22}"],
            ["b_{31}", "b_{32}"]]
        )
        matrix_B_label = MathTex(r"B").next_to(matrix_B, UP)
        equal = MathTex(r"=").next_to(matrix_B, RIGHT)
        matrix_C = Matrix(
            [["c_{11}", "c_{12}"],
            ["c_{21}", "c_{22}"]]
        ).next_to(equal, RIGHT)
        matrix_C_label = MathTex(r"C").next_to(matrix_C, UP)
        
        
        self.play(Create(matrix_A), Write(matrix_A_label))
        self.play(Create(matmul))
        self.play(Create(matrix_B), Write(matrix_B_label))
        self.play(Create(equal))
        self.play(Create(matrix_C), Write(matrix_C_label))
        self.wait(1)
        
        for i in range(2):
            for j in range(2):
                self.make_equation(matrix_A, matrix_B, matrix_C, i, j)
                self.wait(1)
                
        self.play(FadeOut(matrix_A), FadeOut(matrix_A_label), FadeOut(matmul), FadeOut(matrix_B), FadeOut(matrix_B_label), FadeOut(equal), FadeOut(matrix_C), FadeOut(matrix_C_label))
        


        
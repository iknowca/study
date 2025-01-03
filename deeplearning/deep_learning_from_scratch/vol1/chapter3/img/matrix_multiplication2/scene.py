from manim import *

class main(Scene):
    def make_matrix(self, c, m, n):
        return Matrix([[r"{%c}_{%d%d}" % (c, i+1, j+1) for j in range(n)] for i in range(m)])
    
    def construct(self):
        title = Text("Matrix Multiplication").shift(3*UP)
        self.add(title)
        
        matrix_A = self.make_matrix("a", 2, 3)
        matrix_A.shift(4*LEFT)
        matrix_A_label = MathTex(r"A").next_to(matrix_A, UP)
        matmul = MathTex(r"\times").next_to(matrix_A, RIGHT)
        matrix_B = self.make_matrix("b", 3, 2)
        matrix_B_label = MathTex(r"B").next_to(matrix_B, UP)
        equal = MathTex(r"=").next_to(matrix_B, RIGHT)
        matrix_C = self.make_matrix("c", 2, 2).next_to(equal, RIGHT)
        matrix_C_label = MathTex(r"C").next_to(matrix_C, UP)
        
        eq = VGroup()
        a = Text("2 X 3").next_to(matrix_A, DOWN).shift(DOWN*2).set_color(YELLOW)
        b = Text("3 X 2").next_to(matrix_B, DOWN).align_to(a, UP).set_color(ORANGE)
        c = Text("2 X 2").next_to(matrix_C, DOWN).align_to(b, UP).set_color(RED)
        eq.add(a, b, c)
        
        self.play(Create(matrix_A), Write(matrix_A_label))
        self.play(Create(matmul))
        self.play(Create(matrix_B), Write(matrix_B_label))
        self.play(Create(equal))
        self.play(Create(matrix_C), Write(matrix_C_label))
        self.play(Write(eq))
        self.wait(1)
        
        self.play(*(self.transform_matrix(matrix_A, 4, 3, matrix_A_label, a)), *(self.transform_matrix(matrix_C, 4, 2, matrix_C_label, c)))
        self.play(*(self.transform_matrix(matrix_B, 3, 1, matrix_B_label, b)), *(self.transform_matrix(matrix_C, 4, 1, matrix_C_label, c)))
        self.play(*(self.transform_matrix(matrix_A, 2, 2, matrix_A_label, a)), *(self.transform_matrix(matrix_C, 2, 2, matrix_C_label, c)), *(self.transform_matrix(matrix_B, 2, 2, matrix_B_label, b)))

        self.play(FadeOut(matrix_A), FadeOut(matrix_A_label), FadeOut(matmul), FadeOut(matrix_B), FadeOut(matrix_B_label), FadeOut(equal), FadeOut(matrix_C), FadeOut(matrix_C_label), FadeOut(eq))
        
    def transform_matrix(self, matrix, m, n, matrix_label, mn):
        new_matrix = self.make_matrix(matrix_label.get_tex_string()[0], m, n).next_to(matrix.get_center(), 0)
        new_mn = Text(f"{m} X {n}").move_to(mn.get_center()).set_color(mn.get_color())
        return Transform(matrix, new_matrix), matrix_label.animate.next_to(new_matrix, UP), Transform(mn, new_mn)

        
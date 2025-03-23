from manim import *

class StepByStepInputs(Scene):
    def construct(self):

        # ========================
        # 1) DEFINITIONS & POSITIONS
        # ========================

        # -- Top row: x0 -> w0 --
        x0_pos = [-4, 2, 0]
        w0_pos = [-1, 2, 0]
        
        x0_label = MathTex("x_0").move_to(x0_pos)
        line_x0_w0 = Line(start=[-3.4,2,0], end=[-2,2,0], color=WHITE)
        w0_circle = Circle(radius=0.3, color=TEAL).move_to(w0_pos)
        w0_label  = MathTex("w_0").move_to(w0_circle.get_center())

        # -- Middle row: x1 -> w1 --
        x1_pos = [-4, 0, 0]
        w1_pos = [-1, 0, 0]
        
        x1_label = MathTex("x_1").move_to(x1_pos)
        line_x1_w1 = Line(start=[-3.4,0,0], end=[-2,0,0], color=WHITE)
        w1_circle = Circle(radius=0.3, color=TEAL).move_to(w1_pos)
        w1_label  = MathTex("w_1").move_to(w1_circle.get_center())

        # -- Bottom row: x2 -> w2 --
        x2_pos = [-4, -2, 0]
        w2_pos = [-1, -2, 0]

        x2_label = MathTex("x_2").move_to(x2_pos)
        line_x2_w2 = Line(start=[-3.4,-2,0], end=[-2,-2,0], color=WHITE)
        w2_circle = Circle(radius=0.3, color=TEAL).move_to(w2_pos)
        w2_label  = MathTex("w_2").move_to(w2_circle.get_center())

        # ========================
        # 2) ANIMATION STEPS
        # ========================

        # (1) Show x0
        self.play(Write(x0_label))
        self.wait(0.5)

        # (2) Draw line from x0 to w0
        self.play(Create(line_x0_w0))
        self.wait(0.5)

        # (3) Show w0 circle
        self.play(Create(w0_circle), Write(w0_label))
        self.wait(1)

        # (4) Show x1
        self.play(Write(x1_label))
        self.wait(0.5)

        # (5) Draw line from x1 to w1
        self.play(Create(line_x1_w1))
        self.wait(0.5)

        # (6) Show w1 circle
        self.play(Create(w1_circle), Write(w1_label))
        self.wait(1)

        # (7) Show x2
        self.play(Write(x2_label))
        self.wait(0.5)

        # (8) Draw line from x2 to w2
        self.play(Create(line_x2_w2))
        self.wait(0.5)

        # (9) Show w2 circle
        self.play(Create(w2_circle), Write(w2_label))
        self.wait(2)

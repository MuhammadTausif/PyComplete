from manim import *

class SingleNeuronDiagram(Scene):
    def construct(self):
        # ---------------------------
        # 1) CREATE INPUT CIRCLES
        # ---------------------------
        # Positions for each input circle (left to right or top to bottom)
        input_positions = [
            [-4,  2, 0],
            [-4,  0, 0],
            [-4, -2, 0],
            [-4, -4, 0],
        ]
        # Labels for each circle (e.g., "x_0", "x_1", "x_2", "x_3")
        input_labels = [r"x_0", r"x_1", r"x_2", r"x_3"]
        # Weights for each arrow (e.g., "w_0", "w_1", "w_2", "w_3")
        weight_labels = [r"w_0", r"w_1", r"w_2", r"w_3"]

        input_nodes = VGroup()
        input_node_labels = VGroup()
        for pos, label_text in zip(input_positions, input_labels):
            circle = Circle(radius=0.3, color=BLUE).move_to(pos)
            text   = MathTex(label_text).move_to(pos)
            input_nodes.add(circle)
            input_node_labels.add(text)

        # Animate the appearance of input circles
        self.play(Create(input_nodes))
        self.play(Write(input_node_labels))
        self.wait(1)

        # ---------------------------
        # 2) CREATE SUM (SIGMA) CIRCLE
        # ---------------------------
        sum_circle = Circle(radius=0.4, color=ORANGE).move_to([-1, -1, 0])
        sum_label  = MathTex(r"\Sigma").move_to(sum_circle.get_center())

        self.play(Create(sum_circle))
        self.play(Write(sum_label))
        self.wait(1)

        # -------------------------------------------------
        # 3) ARROWS FROM INPUTS TO SUM, LABELED WITH w_i
        # -------------------------------------------------
        arrows_input_to_sum = VGroup()
        weight_texts = VGroup()
        for i, (circle, w_label) in enumerate(zip(input_nodes, weight_labels)):
            arrow = Arrow(
                start=circle.get_right(), 
                end=sum_circle.get_left(), 
                buff=0.1, 
                stroke_width=2
            )
            # Position the weight label near the midpoint of the arrow
            midpoint = 0.5*(arrow.get_start() + arrow.get_end())
            w_text = MathTex(w_label).move_to(midpoint + UP*0.3)
            
            arrows_input_to_sum.add(arrow)
            weight_texts.add(w_text)

        self.play(
            *[Create(arrow) for arrow in arrows_input_to_sum],
            *[Write(wt) for wt in weight_texts]
        )
        self.wait(1)

        # --------------------------------------
        # 4) CREATE SIGMOID (ACTIVATION) CIRCLE
        # --------------------------------------
        sigmoid_circle = Circle(radius=0.4, color=YELLOW).move_to([2, -1, 0])
        sigmoid_label  = MathTex(r"\sigma").move_to(sigmoid_circle.get_center())

        self.play(Create(sigmoid_circle))
        self.play(Write(sigmoid_label))
        self.wait(1)

        # --------------------------------------------------
        # 5) ARROW FROM SUM (SIGMA) CIRCLE TO SIGMOID CIRCLE
        # --------------------------------------------------
        arrow_sum_to_sigmoid = Arrow(
            start=sum_circle.get_right(), 
            end=sigmoid_circle.get_left(), 
            buff=0.1, 
            stroke_width=2,
            color=RED
        )
        self.play(Create(arrow_sum_to_sigmoid))
        self.wait(1)

        # ----------------------------------
        # 6) CREATE OUTPUT CIRCLE (y-hat)
        # ----------------------------------
        output_circle = Circle(radius=0.3, color=PURPLE).move_to([4, -1, 0])
        output_label  = MathTex(r"\hat{y}").move_to(output_circle.get_center())

        self.play(Create(output_circle))
        self.play(Write(output_label))
        self.wait(1)

        # --------------------------------------
        # 7) ARROW FROM SIGMOID TO OUTPUT CIRCLE
        # --------------------------------------
        arrow_sigmoid_to_output = Arrow(
            start=sigmoid_circle.get_right(),
            end=output_circle.get_left(),
            buff=0.1,
            stroke_width=2,
            color=RED
        )
        self.play(Create(arrow_sigmoid_to_output))
        self.wait(2)

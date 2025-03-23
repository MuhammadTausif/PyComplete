from manim import *

class SingleNeuronDiagram(Scene):
    def construct(self):

        # ---------------------------
        # DEFINE INPUT CIRCLES
        # ---------------------------
        input_positions = [
            [-4,  3, 0],
            [-4,  1, 0],
            [-4, -1, 0],
            [-4, -3, 0],
        ]
        input_labels = [r"x_0", r"x_1", r"x_2", r"x_3"]
        weight_labels = [r"w_0", r"w_1", r"w_2", r"w_3"]

        # Create Mobjects but do NOT animate them yet
        input_nodes = VGroup()
        input_node_labels = VGroup()
        for pos, label_text in zip(input_positions, input_labels):
            circle = Circle(radius=0.3, color=BLUE).move_to(pos)
            text   = MathTex(label_text).move_to(pos)
            input_nodes.add(circle)
            input_node_labels.add(text)

        # ---------------------------
        # DEFINE SUM (SIGMA) CIRCLE
        # ---------------------------
        sum_circle = Circle(radius=0.4, color=ORANGE).move_to([-1, 0, 0])
        sum_label  = MathTex(r"\Sigma").move_to(sum_circle.get_center())

        # ---------------------------------
        # DEFINE ARROWS FROM INPUTS TO SUM
        # ---------------------------------
        arrows_input_to_sum = []
        weight_texts = []
        for circle, w_label in zip(input_nodes, weight_labels):
            arrow = Arrow(
                start=circle.get_right(),
                end=sum_circle.get_left(),
                buff=0.1,
                stroke_width=2
            )
            # Position the weight label near the midpoint
            midpoint = 0.5 * (arrow.get_start() + arrow.get_end())
            w_text = MathTex(w_label).move_to(midpoint + UP * 0.3)

            arrows_input_to_sum.append(arrow)
            weight_texts.append(w_text)

        # -------------------------------------
        # DEFINE SIGMOID (ACTIVATION) CIRCLE
        # -------------------------------------
        sigmoid_circle = Circle(radius=0.4, color=YELLOW).move_to([2, 0, 0])
        sigmoid_label  = MathTex(r"\sigma").move_to(sigmoid_circle.get_center())

        # ------------------------------------------------
        # DEFINE ARROW FROM SUM (SIGMA) CIRCLE TO SIGMOID
        # ------------------------------------------------
        arrow_sum_to_sigmoid = Arrow(
            start=sum_circle.get_right(),
            end=sigmoid_circle.get_left(),
            buff=0.1,
            stroke_width=2,
            color=RED
        )

        # ----------------------------------
        # DEFINE OUTPUT CIRCLE (y-hat)
        # ----------------------------------
        output_circle = Circle(radius=0.3, color=PURPLE).move_to([4, 0, 0])
        output_label  = MathTex(r"\hat{y}").move_to(output_circle.get_center())

        # --------------------------------------------
        # DEFINE ARROW FROM SIGMOID TO OUTPUT CIRCLE
        # --------------------------------------------
        arrow_sigmoid_to_output = Arrow(
            start=sigmoid_circle.get_right(),
            end=output_circle.get_left(),
            buff=0.1,
            stroke_width=2,
            color=RED
        )

        # ==========================
        # ANIMATION IN SPECIFIC ORDER
        # ==========================

        # 1) All input circles appear
        self.play(Create(input_nodes), Write(input_node_labels))
        self.wait(0.5)

        # 2) Arrow x_0 to sum (top arrow)
        self.play(Create(arrows_input_to_sum[0]), Write(weight_texts[0]))
        self.wait(0.5)

        # 3) Arrow x_1 to sum
        self.play(Create(arrows_input_to_sum[1]), Write(weight_texts[1]))
        self.wait(0.5)

        # 4) Arrow x_2 to sum
        self.play(Create(arrows_input_to_sum[2]), Write(weight_texts[2]))
        self.wait(0.5)

        # 5) Arrow x_3 to sum (bottom arrow)
        self.play(Create(arrows_input_to_sum[3]), Write(weight_texts[3]))
        self.wait(0.5)

        # 6) Summation circle appears
        self.play(Create(sum_circle), Write(sum_label))
        self.wait(0.5)

        # 7) Arrow from sum to sigmoid
        self.play(Create(arrow_sum_to_sigmoid))
        self.wait(0.5)

        # 8) Sigmoid circle appears
        self.play(Create(sigmoid_circle), Write(sigmoid_label))
        self.wait(0.5)

        # 9) Arrow from sigmoid to output
        self.play(Create(arrow_sigmoid_to_output))
        self.wait(0.5)

        # 10) Output circle appears
        self.play(Create(output_circle), Write(output_label))
        self.wait(2)

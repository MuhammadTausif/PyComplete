from manim import *

class SingleNeuronDiagram(Scene):
    def construct(self):

        # ---------------------------
        # 1) DEFINE INPUT CIRCLES
        # ---------------------------
        # Positions for each input circle
        input_positions = [
            [-4,  2, 0],
            [-4,  0, 0],
            [-4, -2, 0],
        ]
        input_labels = [r"x_0", r"x_1", r"x_2"]
        weight_labels = [r"w_0", r"w_1", r"w_2"]

        # Create input circles and their labels (label on the LEFT)
        input_nodes = VGroup()
        input_node_labels = VGroup()
        inputs_lines = VGroup()
        input_weights = VGroup()
        for pos, label_text, weight in zip(input_positions, input_labels, weight_labels):
            circle = Circle(radius=0.5, color=BLUE).move_to(pos)
            label  = MathTex(label_text).next_to(circle, LEFT * 3, buff=0.4)
            weight_label   = MathTex(weight).move_to(pos)
            input_nodes.add(circle)
            input_node_labels.add(label)
            line = Line(label.get_right() + RIGHT * 0.1 , circle.get_left(),  color=WHITE)
            inputs_lines.add(line)
            input_weights.add(weight_label)
            

        # Animate the appearance of the three input circles
        self.play(Create(input_nodes))
        self.play(Write(input_node_labels))
        self.play(Write(inputs_lines))
        self.play(Write(input_weights))
        self.wait(0.5)
        
        
        # ---------------------------
        # 3) DEFINE SUM (SIGMA) CIRCLE
        # ---------------------------
        sum_circle = Circle(radius=0.6, color=ORANGE).move_to([-1, 0, 0])
        sum_label  = MathTex(r"\Sigma").move_to(sum_circle.get_center())


        # -------------------------
        # 3) ARROWS & LABELS
        # -------------------------
        # We'll give each arrow a slight angle so they land on different points
        # around the summation circle. We'll also place a label (e.g., x_0 w_0) on each arrow.

        # Angles (in degrees) to offset each arrow around the summation circle
        # from the circle's center
        angles = [-20 * DEGREES, 0 * DEGREES, 20 * DEGREES]

        # Example arrow labels, e.g., x_0 w_0, x_1 w_1, x_2 w_2
        arrow_labels = [r"x_0 w_0", r"x_1 w_1", r"x_2 w_2"]

        arrows = VGroup()
        arrow_label_texts = VGroup()

        for i in range(len(input_nodes)):
            # 1) Compute a point on the summation circle's boundary at a given angle
            center = sum_circle.get_center()
            radius = sum_circle.radius
            angle  = angles[i]
            end_x  = center[0] - radius * np.cos(angle)
            end_y  = center[1] - radius * np.sin(angle)
            end_point = np.array([end_x, end_y, 0])

            # 2) Create an arrow from input node to that point on the summation circle
            start_point = input_nodes[i].get_right()  # right edge of the circle
            arrow = Arrow(
                start=start_point,
                end=end_point,
                buff=0.1,
                stroke_width=3,
                color=WHITE
            )

            # 3) Create a label for the arrow (e.g., "x_0 w_0")
            label_tex = MathTex(arrow_labels[i])
            # Place it near the midpoint of the arrow, offset slightly above
            label_tex.move_to(arrow.point_from_proportion(0.5))
            # We can offset it perpendicular to the arrow direction:
            
            # direction = arrow.get_unit_vector()
            # # Rotate direction by 90 degrees (PI/2) to get a perpendicular
            # perpendicular = np.array([
            #     -direction[1],
            #     direction[0],
            #     0
            # ])
            # label_tex.shift(perpendicular * 0.3)


            # 1) Rotate label to match arrow's angle
            arrow_angle = arrow.get_angle()  
            label_tex.rotate(arrow_angle, about_point=label_tex.get_center())

            # 2) Shift label slightly "above" the arrow
            #    (in global coords) using a perpendicular direction
            direction = arrow.get_unit_vector()
            perpendicular = np.array([-direction[1], direction[0], 0])
            label_tex.shift(perpendicular * 0.2)
            
            # Alternatively, you could do:
            # label_tex.next_to(arrow, UP, buff=0.2)

            arrows.add(arrow)
            arrow_label_texts.add(label_tex)

        # Summation circle appears
        self.play(Create(sum_circle), Write(sum_label))
        self.wait(0.5)

        # Animate the arrows and labels
        for arrow, label_tex in zip(arrows, arrow_label_texts):
            self.play(Create(arrow), Write(label_tex))
            self.wait(0.5)
            

            
        # -------------------------------------
        # 2) SHOW THE EQUATION FOR THE NEURON
        # -------------------------------------
        # Example equation: y = w0*x0 + w1*x1 + w2*x2 + b
        equation = MathTex(
            r"y = w_0 x_0 + w_1 x_1 + w_2 x_2 + b"
        ).scale(0.8).to_edge(DOWN)

        self.play(Write(equation))
        self.wait(1)
            

        # # ---------------------------------
        # # DEFINE ARROWS FROM INPUTS TO SUM
        # # ---------------------------------
        # arrows_input_to_sum = []
        # weight_texts = []
        # for circle, w_label in zip(input_nodes, weight_labels):
        #     arrow = Arrow(
        #         start=circle.get_right(),
        #         end=sum_circle.get_left(),
        #         buff=0.1,
        #         stroke_width=2
        #     )
        #     # Position the weight label near the midpoint of the arrow
        #     midpoint = 0.5 * (arrow.get_start() + arrow.get_end())
        #     w_text = MathTex(w_label).move_to(midpoint + UP * 0.3)

        #     arrows_input_to_sum.append(arrow)
        #     weight_texts.append(w_text)

        # -------------------------------------
        # 4) DEFINE SIGMOID (ACTIVATION) CIRCLE
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

        # # Arrows from inputs to sum (one by one)
        # for arrow, w_text in zip(arrows_input_to_sum, weight_texts):
        #     self.play(Create(arrow), Write(w_text))
        #     self.wait(0.5)


        # Arrow from sum to sigmoid
        self.play(Create(arrow_sum_to_sigmoid))
        self.wait(0.5)

        # Sigmoid circle appears
        self.play(Create(sigmoid_circle), Write(sigmoid_label))
        self.wait(0.5)

        # Arrow from sigmoid to output
        self.play(Create(arrow_sigmoid_to_output))
        self.wait(0.5)

        # Output circle appears
        self.play(Create(output_circle), Write(output_label))
        self.wait(2)

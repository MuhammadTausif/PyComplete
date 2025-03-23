from manim import *
import numpy as np

class PerceptronArrows(Scene):
    def construct(self):
        # -------------------------
        # 1) INPUT NODES
        # -------------------------
        # We'll create 3 input circles labeled x_0, x_1, x_2
        input_positions = [
            [-4,  1.5, 0],  # x_0
            [-4,  0.0, 0],  # x_1
            [-4, -1.5, 0],  # x_2
        ]
        input_labels = [r"x_0", r"x_1", r"x_2"]

        input_nodes = VGroup()
        input_node_labels = VGroup()
        for pos, label in zip(input_positions, input_labels):
            circle = Circle(radius=0.4, color=BLUE).move_to(pos)
            text   = MathTex(label).move_to(pos)
            input_nodes.add(circle)
            input_node_labels.add(text)

        # Animate creation of input nodes
        self.play(Create(input_nodes))
        self.play(Write(input_node_labels))
        self.wait(1)

        # -------------------------
        # 2) SUMMATION CIRCLE
        # -------------------------
        sum_circle = Circle(radius=0.5, color=ORANGE).move_to([2, 0, 0])
        sum_label  = MathTex(r"\Sigma").move_to(sum_circle.get_center())

        self.play(Create(sum_circle), Write(sum_label))
        self.wait(1)

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
            direction = arrow.get_unit_vector()
            # Rotate direction by 90 degrees (PI/2) to get a perpendicular
            perpendicular = np.array([
                -direction[1],
                direction[0],
                0
            ])
            label_tex.shift(perpendicular * 0.3)

            # Alternatively, you could do:
            # label_tex.next_to(arrow, UP, buff=0.2)

            arrows.add(arrow)
            arrow_label_texts.add(label_tex)

        # Animate the arrows and labels
        for arrow, label_tex in zip(arrows, arrow_label_texts):
            self.play(Create(arrow), Write(label_tex))
            self.wait(0.5)

        self.wait(2)

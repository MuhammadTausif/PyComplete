from manim import *

class SingleNeuronScene(Scene):
    def construct(self):
        # Title
        title = Text("Single Neuron").to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Draw neuron body (circle)
        neuron_body = Circle(radius=1, color=BLUE).shift(RIGHT*2)
        self.play(Create(neuron_body))
        self.wait(0.5)

        # Create input arrows and labels
        input_texts = ["x₁", "x₂", "x₃"]
        inputs = VGroup()
        for i, txt in enumerate(input_texts):
            # Calculate vertical offset for each input arrow
            offset = (i - 1) * 1.5  
            arrow = Arrow(
                start=LEFT*3 + UP*offset, 
                end=neuron_body.get_left(), # + UP*offset, 
                buff=0.1
            )
            label = Text(txt, font_size=24).next_to(arrow.get_start(), LEFT)
            self.play(Create(arrow), Write(label))
            self.wait(0.5)

        # Draw output arrow and label
        output_arrow = Arrow(
            start=neuron_body.get_right(), 
            end=RIGHT*3, 
            buff=0.1, 
            color=GREEN
        )
        output_label = Text("y", font_size=24).next_to(output_arrow.get_end(), RIGHT)
        self.play(Create(output_arrow), Write(output_label))
        self.wait(0.5)

        # Write the neuron equation below the neuron
        equation = MathTex(
            "y", "=", "\\sigma(", "w_1 x_1", "+", "w_2 x_2", "+", "w_3 x_3", "+", "b", ")"
        ).scale(0.8)
        equation.next_to(neuron_body, DOWN, buff=1)
        self.play(Write(equation))
        self.wait(2)

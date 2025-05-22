from manim import *

class ThreeLayerNetwork(Scene):
    def construct(self):
        # ----------------------
        # 1) CREATE INPUT LAYER
        # ----------------------
        input_nodes = VGroup(
            Circle(radius=0.2, color=RED).move_to([-4,  2, 0]),
            Circle(radius=0.2, color=RED).move_to([-4,  0, 0]),
            Circle(radius=0.2, color=RED).move_to([-4, -2, 0]),
        )
        input_label = Text("Input Layer", font_size=28).next_to(input_nodes, UP, buff=1)
        
        # Animate the creation of input nodes and label
        self.play(Create(input_nodes))
        self.play(Write(input_label))
        self.wait(1)

        # ----------------------
        # 2) CREATE HIDDEN LAYER
        # ----------------------
        hidden_nodes = VGroup(
            Circle(radius=0.2, color=BLUE).move_to([0,  3, 0]),
            Circle(radius=0.2, color=BLUE).move_to([0,  1, 0]),
            Circle(radius=0.2, color=BLUE).move_to([0, -1, 0]),
            Circle(radius=0.2, color=BLUE).move_to([0, -3, 0]),
        )
        hidden_label = Text("Hidden Layer", font_size=28).next_to(hidden_nodes, UP, buff=1)
        
        # Animate the creation of hidden nodes
        self.play(Create(hidden_nodes))
        self.play(Write(hidden_label))
        self.wait(1)

        # ---------------------------------------------------
        # 3) DRAW ARROWS FROM INPUT LAYER TO HIDDEN LAYER
        # ---------------------------------------------------
        arrows_input_hidden = VGroup()
        for inp_node in input_nodes:
            for hid_node in hidden_nodes:
                arrow = Arrow(
                    start=inp_node.get_right(), 
                    end=hid_node.get_left(),
                    buff=0.1,
                    stroke_width=2
                )
                arrows_input_hidden.add(arrow)
        
        self.play(Create(arrows_input_hidden))
        self.wait(1)

        # -----------------------
        # 4) CREATE OUTPUT LAYER
        # -----------------------
        output_nodes = VGroup(
            Circle(radius=0.2, color=GREEN).move_to([4,  1, 0]),
            Circle(radius=0.2, color=GREEN).move_to([4, -1, 0]),
        )
        output_label = Text("Output Layer", font_size=28).next_to(output_nodes, UP, buff=1)
        
        # Animate the creation of output nodes
        self.play(Create(output_nodes))
        self.play(Write(output_label))
        self.wait(1)

        # ----------------------------------------------------
        # 5) DRAW ARROWS FROM HIDDEN LAYER TO OUTPUT LAYER
        # ----------------------------------------------------
        arrows_hidden_output = VGroup()
        for hid_node in hidden_nodes:
            for out_node in output_nodes:
                arrow = Arrow(
                    start=hid_node.get_right(), 
                    end=out_node.get_left(),
                    buff=0.1,
                    stroke_width=2
                )
                arrows_hidden_output.add(arrow)
        
        self.play(Create(arrows_hidden_output))
        self.wait(2)

from manim import *

class ZoomToSumCircle(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        
        # Example: Summation circle
        sum_circle = Circle(radius=0.5, color=ORANGE).move_to([2, 0, 0])
        sum_label  = MathTex(r"\Sigma").move_to(sum_circle.get_center())
        self.play(Create(sum_circle), Write(sum_label))
        self.wait()

        # Zoom in on sum_circle
        #  - move_to(...) centers the camera on the object
        #  - set(width=...) shrinks the camera frame width => more zoomed in
        # self.play(
        #     self.camera.frame.animate
        #         .move_to(sum_circle.get_center())
        #         .set(width=2)  
        # )
        
        self.play(self.camera.frame.animate.scale(0.5).move_to(sum_circle.get_center()))
        self.wait(2)

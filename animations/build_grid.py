from manim import *

# Optional: Configure for vertical (portrait) output
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

class BuildGridFromTopLeft(Scene):
    def construct(self):
        # Grid size
        Nx, Ny = 4, 4  # 4 columns, 4 rows
        side = 1       # each square side length
        buff = 0.1     # spacing between squares
        margin = 0.5   # margin from screen edge

        # Calculate a "top-left" corner for the first square
        # (so it won't be off-screen)
        x0 = -config.frame_width/2 + side/2 + margin
        y0 =  config.frame_height/2 - side/2 - margin

        # Create a list to hold all squares
        squares = []

        # Build squares row by row (top to bottom),
        # placing them left to right in each row.
        for row in range(Ny):
            for col in range(Nx):
                sq = Square(side_length=side).set_stroke(BLUE, 2)
                # Compute position for this square
                x = x0 + col * (side + buff)
                y = y0 - row * (side + buff)
                sq.move_to([x, y, 0])
                squares.append(sq)

        # Animate the creation of each square, one by one
        for sq in squares:
            self.play(Create(sq))
            # self.wait(0.05)

        self.wait(1)

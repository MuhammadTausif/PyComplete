from manim import *
import numpy as np

# Configure for a vertical (portrait) video (9:16 aspect ratio)
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

class GridOnCat(Scene):
    def construct(self):
        # 1. Load and display the cat image
        cat_image = ImageMobject("cat.jpg")
        cat_image.scale_to_fit_width(6)  # Adjust to your desired size
        cat_image.move_to(ORIGIN)
        self.add(cat_image)  # Add image as background
        self.wait(1)
        
        # 2. Determine grid parameters
        Nx, Ny = 4, 4      # 4 columns and 4 rows (16 boxes)
        side = 1           # Side length for each square
        buff = 0.1         # Spacing between squares
        margin = 0.01       # Extra margin from the image edge

        # Get the top-left corner of the cat image
        # UL corner gives a point at the top-left of the image's bounding box
        top_left = cat_image.get_corner(UL)
        
        # For a square, its center should be offset from the top-left by (side/2, -side/2)
        x0 = top_left[0] + side/2 + margin
        y0 = top_left[1] - side/2 - margin

        # 3. Create and animate each square one by one,
        # starting at the computed top-left and proceeding row by row.
        squares = []
        for row in range(Ny):
            for col in range(Nx):
                # Create a square and set its stroke (color & width)
                sq = Square(side_length=side).set_stroke(WHITE, 2)
                # Compute the center for this square
                x = x0 + col * (side + buff)
                y = y0 - row * (side + buff)
                sq.move_to(np.array([x, y, 0]))
                squares.append(sq)
        
        # Animate drawing each square sequentially
        for sq in squares:
            # self.play(Create(sq))
            self.add(sq)
            self.wait(0.1)
            
        self.wait(1)

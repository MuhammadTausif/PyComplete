from manim import *

# 1) Configure for a vertical (portrait) video (9:16)
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

class GridExactlyOverImage(Scene):
    def construct(self):
        # 2) Load the cat image
        cat_image = ImageMobject("cat.jpg")
        # Scale to fit your desired width (adjust as needed)
        cat_image.scale_to_fit_width(6)
        cat_image.move_to(ORIGIN)
        self.add(cat_image)  # Add the image to the scene

        self.wait(1)

        # 3) We want a 4×4 grid that covers the entire image
        Nx, Ny = 4, 4  # columns × rows

        # Get the bounding box of the image
        # width & height of the cat image in Manim units
        w = cat_image.width
        h = cat_image.height

        # The top-left corner of the image
        top_left = cat_image.get_corner(UL)

        # 4) Create each cell so that the 4×4 grid *exactly* covers the image
        #    That means each cell is (w/Nx) wide and (h/Ny) tall.
        cells = []
        for row in range(Ny):
            for col in range(Nx):
                # Create a rectangle cell
                cell_width = w / Nx
                cell_height = h / Ny
                cell = Rectangle(
                    width=cell_width, 
                    height=cell_height,
                    stroke_color=WHITE, 
                    stroke_width=5
                )
                
                # Compute the center of this cell
                #   - x is offset from left by (col + 0.5)*cell_width
                #   - y is offset from top by (row + 0.5)*cell_height
                x_center = top_left[0] + (col + 0.5) * cell_width
                y_center = top_left[1] - (row + 0.5) * cell_height
                cell.move_to([x_center, y_center, 0])
                
                cells.append(cell)

        # 5) Animate each cell appearing in sequence
        for cell in cells:
            # self.play(Create(cell))
            self.add(cell)
            self.wait(0.1)

        self.wait(1)

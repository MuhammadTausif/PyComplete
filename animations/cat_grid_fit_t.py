from manim import *

# Configure for a vertical (portrait) video (9:16)
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

class GridExactlyOverImage(Scene):
    def construct(self):
        # 1) Load & display the cat image
        cat_image = ImageMobject("cat.jpg")
        cat_image.scale_to_fit_width(6)  # Adjust as needed
        cat_image.move_to(ORIGIN)
        self.add(cat_image)
        self.wait(1)

        # 2) Define grid parameters
        Nx, Ny = 4, 4  # 4 columns × 4 rows
        w = cat_image.width
        h = cat_image.height
        top_left = cat_image.get_corner(UL)

        # 3) Create the 4×4 grid cells so they exactly cover the image
        cells = []
        for row in range(Ny):
            for col in range(Nx):
                cell_width = w / Nx
                cell_height = h / Ny
                cell = Rectangle(
                    width=cell_width, 
                    height=cell_height,
                    stroke_color=RED, 
                    stroke_width=2
                )
                # Center of this cell
                x_center = top_left[0] + (col + 0.5) * cell_width
                y_center = top_left[1] - (row + 0.5) * cell_height
                cell.move_to([x_center, y_center, 0])
                cells.append(cell)

        # 4) Animate drawing each cell over the cat image
        for cell in cells:
            # self.play(Create(cell))
            self.add(cell)
            self.wait(0.1)
        self.wait(1)

        # 5) Hide the cat picture before transforming the cells
        self.play(FadeOut(cat_image))

        # 6) Transform each cell into a smaller, solid blue rectangle
        #    (Adjust the scale factors as you like.)
        transforms = []
        for cell in cells:
            new_rect = Rectangle(
                width=cell.width * 0.4,  # narrower
                height=cell.height * 0.8, # slightly shorter
                fill_color=BLUE,
                fill_opacity=1,
                stroke_width=0
            )
            new_rect.move_to(cell.get_center())
            transforms.append(Transform(cell, new_rect))

        # Animate all transforms simultaneously
        self.play(*transforms)
        self.wait(2)

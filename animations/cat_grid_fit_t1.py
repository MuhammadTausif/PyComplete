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

        # 3) Create the 4×4 grid cells exactly covering the image
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
                # Position this cell
                x_center = top_left[0] + (col + 0.5) * cell_width
                y_center = top_left[1] - (row + 0.5) * cell_height
                cell.move_to([x_center, y_center, 0])
                cells.append(cell)

        # 4) Display each cell over the cat image
        #    (using .add() so there's no "draw" animation)
        for cell in cells:
            self.add(cell)
            self.wait(0.1)

        self.wait(1)

        # 5) Hide the cat picture
        self.play(FadeOut(cat_image))

        # 6) Instead of transforming (which removes the original),
        #    we'll create new blue rectangles on top, leaving the base squares visible.
        new_rects = []
        for cell in cells:
            new_rect = Rectangle(
                width=cell.width * 0.15,  # narrower
                height=cell.height * 0.6, # slightly shorter
                fill_color=BLUE,
                fill_opacity=1,
                stroke_width=0
            )
            # Place the new rectangle at the same center as the original cell
            new_rect.move_to(cell.get_center())
            new_rects.append(new_rect)

        # Animate the appearance of all blue rectangles
        # e.g., all at once, or with a slight lag
        self.play(LaggedStart(*[FadeIn(rect) for rect in new_rects], lag_ratio=0.1))
        self.wait(2)

from manim import *

# Configure for a vertical (portrait) video (9:16)
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

class MoveTopLeftRectangle(Scene):
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
                    stroke_color=WHITE, 
                    stroke_width=3
                )
                # Center of this cell
                x_center = top_left[0] + (col + 0.5) * cell_width
                y_center = top_left[1] - (row + 0.5) * cell_height
                cell.move_to([x_center, y_center, 0])
                cells.append(cell)

        # 4) Animate drawing each cell over the cat image
        for cell in cells:
            self.play(Create(cell), run_time=0.3)
        self.wait(1)

        # 5) Fade out the cat image
        self.play(FadeOut(cat_image))

        # 6) Create new rectangles from each square WITHOUT removing the original
        #    We'll store them in new_rects so we can move one of them later
        new_rects = []
        transforms = []
        for cell in cells:
            # A new, smaller blue rectangle
            new_rect = Rectangle(
                width=cell.width * 0.4,
                height=cell.height * 0.8,
                fill_color=BLUE,
                fill_opacity=1,
                stroke_width=0
            )
            new_rect.move_to(cell.get_center())

            # TransformFromCopy keeps the original cell on screen
            transforms.append(TransformFromCopy(cell, new_rect))
            new_rects.append(new_rect)

        # Animate all rectangles appearing
        self.play(*transforms, run_time=2)
        self.wait(1)

        # 7) Move the top-left rectangle to the top-middle
        #    while all other blue rectangles fade out
        top_left_rect = new_rects[0]
        others = [r for r in new_rects if r is not top_left_rect]

        top_center = [0, config.frame_height/2 - 1, 0]  # slightly below top edge
        self.play(
            top_left_rect.animate.move_to(top_center),
            *[FadeOut(cell) for cell in cells],
            *[FadeOut(rect) for rect in others],
            run_time=2
        )

        self.wait(2)

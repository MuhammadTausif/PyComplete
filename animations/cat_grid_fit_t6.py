from manim import *

# Configure for a vertical (portrait) video (9:16)
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

class TransformRectangleToVector(Scene):
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

        # 3) Create the 4×4 grid cells (white squares) covering the image
        cells = []
        for row in range(Ny):
            for col in range(Nx):
                cell_width = w / Nx
                cell_height = h / Ny
                cell = Rectangle(
                    width=cell_width, 
                    height=cell_height,
                    stroke_color=WHITE, 
                    stroke_width=2
                )
                # Position each cell
                x_center = top_left[0] + (col + 0.5) * cell_width
                y_center = top_left[1] - (row + 0.5) * cell_height
                cell.move_to([x_center, y_center, 0])
                cells.append(cell)

        # 4) Animate drawing each white cell
        for cell in cells:
            # self.play(Create(cell), run_time=0.3)
            self.add(cell)
            self.wait(0.1)
        self.wait(1)

        # 5) Fade out the cat image
        self.play(FadeOut(cat_image))

        # 6) Transform each white square -> smaller blue rectangle (but keep the squares)
        new_rects = []
        transforms = []
        for cell in cells:
            blue_rect = Rectangle(
                width=cell.width * 0.15,
                height=cell.height * 0.6,
                fill_color=BLUE,
                fill_opacity=1,
                stroke_width=0
            )
            blue_rect.move_to(cell.get_center())

            # Use TransformFromCopy so the white square remains
            transforms.append(TransformFromCopy(cell, blue_rect))
            new_rects.append(blue_rect)

        # Animate all blue rectangles appearing
        self.play(*transforms, run_time=2)
        self.wait(1)

        # 7) Move the top-left blue rectangle to the top-middle
        top_left_rect = new_rects[0]  # first new rect
        others = [r for r in new_rects if r is not top_left_rect]

        top_center = [0, config.frame_height / 2 - 1, 0]  # near top
        self.play(
            top_left_rect.animate.move_to(top_center),
            *[FadeOut(cell) for cell in cells],  # fade out original squares
            *[FadeOut(rect) for rect in others],  # fade out other blue rectangles
            run_time=2
        )
        self.wait(1)

        # 8) Transform that top rectangle into a "vector" of numbers with square brackets
        #    We'll use TransformFromCopy again, but properly size the brackets.

        # Example vector data
        data_values = [12, 45, 78, 34, 56, 89, 23, 67, 90, 123, 45, 67, 89, 23, 101, 145]

        # Create a vertical list of numbers
        lines = VGroup()
        for val in data_values:
            t = Text(str(val), font_size=30, color=WHITE)
            lines.add(t)
        lines.arrange(DOWN, buff=0.15)

        # Create square brackets as Text objects
        left_bracket = Text("[", font_size=18, color=WHITE)
        right_bracket = Text("]", font_size=18, color=WHITE)

        # Stretch each bracket to match the total height of the lines (plus a little padding)
        desired_height = lines.height * 1.1
        left_bracket.stretch_to_fit_height(desired_height)
        right_bracket.stretch_to_fit_height(desired_height)

        # Position brackets around the lines
        left_bracket.next_to(lines, LEFT, buff=0.2)
        right_bracket.next_to(lines, RIGHT, buff=0.2)

        # Group everything into one vector-like object
        vector_group = VGroup(left_bracket, lines, right_bracket)

        # Position the vector group below the rectangle (or wherever you prefer)
        vector_group.next_to(top_left_rect, DOWN, buff=1)

        # Animate: a copy of the rectangle "turns into" the bracketed vector
        self.play(TransformFromCopy(top_left_rect, vector_group), run_time=2)

        # The original rectangle remains on screen
        self.wait(2)

from manim import *
import numpy as np

# 1) Configure output for a 9:16 portrait video (e.g., YouTube Shorts, TikTok)
config.pixel_width = 1080     # output width in pixels
config.pixel_height = 1920    # output height in pixels
config.frame_width = 9        # coordinate system width
config.frame_height = 16      # coordinate system height

class VisionTransformerShort(Scene):
    def construct(self):
        # 2) Create the title text in the center
        title_text = Text(
            "Vision Transformer (ViT)", 
            font_size=32, 
            color=BLUE
        ).move_to(ORIGIN)

        # Fade in the title
        self.play(FadeIn(title_text))
        self.wait(1)

        # 3) Prepare the cat image
        # Make sure "cat.jpg" is in the same folder as this script
        cat_image = ImageMobject("cat.jpg")
        # Scale so it fits nicely within the 9x16 frame
        cat_image.scale_to_fit_width(6)  # Adjust as needed

        # We'll move the cat image slightly down for the final position
        cat_image.move_to(DOWN * 1.5)

        # 4) Animate the text moving up while the cat image fades in
        new_title_position = title_text.get_center() + UP * 4  # shift text upward
        self.play(
            title_text.animate.move_to(new_title_position),
            FadeIn(cat_image, shift=DOWN)
        )
        self.wait(1)

        # 5) Draw a grid of boxes on top of the cat image
        #    Let's create a 4x4 grid (so 5 vertical & 5 horizontal lines)
        Nx, Ny = 4, 4
        w, h = cat_image.width, cat_image.height

        grid_lines = VGroup()
        # Vertical lines
        for i in range(Nx + 1):
            x_pos = -w/2 + i * (w / Nx)
            line = Line([x_pos, -h/2, 0], [x_pos, h/2, 0], color=WHITE, stroke_width=1)
            grid_lines.add(line)
        # Horizontal lines
        for j in range(Ny + 1):
            y_pos = -h/2 + j * (h / Ny)
            line = Line([-w/2, y_pos, 0], [w/2, y_pos, 0], color=WHITE, stroke_width=1)
            grid_lines.add(line)

        # Move the entire grid to the cat image's center
        grid_lines.move_to(cat_image.get_center())

        # Animate the creation of the grid
        self.play(Create(grid_lines))
        self.wait(2)

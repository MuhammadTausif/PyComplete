from manim import config, Scene, Text, FadeIn, FadeOut, BLUE

# --- 1. Configure for Vertical (9:16) Output ---
config.pixel_width = 1080     # Width in pixels
config.pixel_height = 1920    # Height in pixels
config.frame_width = 9        # Frame "units" wide
config.frame_height = 16      # Frame "units" tall

class VerticalShort(Scene):
    def construct(self):
        # 2) Example content for your vertical scene
        text = Text("Hello Shorts!", color=BLUE, font_size=100)
        self.play(FadeIn(text))
        self.wait(1)
        self.play(FadeOut(text))
        self.wait(1)

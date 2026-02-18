from manim import *

class AddWithRunTimeScene(Scene):
    def construct(self):
        # A 5x5 grid of circles
        circles = VGroup(
            *[Circle(radius=0.5) for _ in range(5)]
        ).arrange_in_grid(1, 5)

        self.play(
            Succession(
                # Add a run_time of 0.2 to wait for 0.2 seconds after
                # adding the circle, instead of using Wait(0.2) after Add!
                *[Add(circle, run_time=0.9) for circle in circles],
                rate_func=smooth,
            )
        )
        self.wait()

if __name__ == "__main__":
    scene = AddWithRunTimeScene()
    scene.render()
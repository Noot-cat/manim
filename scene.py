from manim import *
import math

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(BLUE, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen
        square = Square()
        self.play(Create(square))

class MovingFrameBox(Scene):
    def construct(self):
        text=MathTex(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff = .1)
        framebox2 = SurroundingRectangle(text[3], buff = .1)
        self.play(
            Create(framebox1),
        )
        self.wait()
        self.play(
            ReplacementTransform(framebox1,framebox2),
        )
        self.wait()

class SectionalQuadrature(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 6],
            y_range=[0, 12],
            tips=False,
        )
        labels = ax.get_axis_labels()
        dxrange = 1
        curve_1 = ax.plot(lambda x: (1/3)*x**3-3*x**2+8*x, x_range=[0, 6], color=BLUE_C)
        riemann_area = ax.get_riemann_rectangles(curve_1, x_range=[0, 6], dx=dxrange, color=BLUE, fill_opacity=0.5)
        self.play(
            Create(ax),
            Create(labels),
        )
        self.wait()
        self.play(
            Create(curve_1),
            Create(riemann_area)
        )
        self.wait()
        while (dxrange > 0.0625):
            self.play(
                FadeOut(riemann_area)
            )
            dxrange = (1/2)*dxrange
            riemann_area = ax.get_riemann_rectangles(curve_1, x_range=[0, 6], dx=dxrange, color=BLUE, fill_opacity=0.5)
            self.play(
                Create(riemann_area)
                )
            self.wait(0.25)
        self.play(
            FadeOut(riemann_area)
        )
        area = ax.get_area(graph=curve_1, x_range=(0,6), color=BLUE, fill_opacity=0.5)
        self.play(FadeIn(area))
        self.wait()
        group = VGroup(ax,area,curve_1,labels)
        self.play(group.animate.scale(0.25).move_to(LEFT * 5 + UP * 2.5))
        self.wait()
        text=MathTex(
            "\\lim_{n \\to \\infty} \\sum_{k = 1}^{n} f\\left ( \\frac{k}{n} \\right ) \\frac{1}{n}  = \\int_{0}^{1} f(x) \\,dx"
        )
        self.play(Write(text))
        self.wait(2)

class DifferentiationOfTrigonometricFunctions(Scene):
    def construct(self):
        r = 2.5
        theta = 1/3
        ax = Axes(x_range=([-6,6,r]),y_range=([-3,3,r]),tips=False)
        labels = ax.get_axis_labels(x_label="x", y_label="y")
        cos = math.cos(theta*PI)
        sin = math.sin(theta*PI)
        line_cos = Line(start=([0,0,0]),end=([r*cos,0,0]), color=BLUE_C)
        line_sin = Line(start=([r*cos,r*sin,0]),end=([r*cos,0,0]), color=TEAL_C)
        line_little = Line(start=([r,0,0]),end=([r*cos,0,0]))
        circle = Circle(color=BLUE, radius=r)
        # circle_up = ax.plot(lambda x: math.sqrt(1-x**2), x_range=[-1,1,0.01], color=BLUE_C)
        # circle_down = ax.plot(lambda x: - math.sqrt(1-x**2), x_range=[-1,1,0.01], color=BLUE_C)
        self.play(
            Create(ax)      
        )
        self.wait()
        self.play(
            Create(circle)      
        )
        line = Line(start=([0,0,0]), end=([r,0,0]))
        line_moved = Line(start=([0,0,0]), end=([r*cos,r*sin,0]))
        
        a = Angle(line, line_moved, radius=0.5, other_angle=False)
        tex = MathTex(r"\theta").move_to(
            Angle(
                line, line_moved, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
            )
        )
        self.play(Rotate(mobject=line,angle=theta*PI,about_point=([0,0,0])))
        self.wait()
        self.play(
            Create(a),
            Create(tex),
            Create(line_sin),
            Create(line_cos)
        )
        self.wait()
        rectangle = Rectangle(height=0.5,width=1).to_corner(corner=UR)
        self.play(Create(rectangle))
        self.play(rectangle.animate.move_to(([r*cos,r*sin,0])))
        group = VGroup(ax,circle,a,tex,line,rectangle)
        self.wait()
        rectangle_zoom = Rectangle(height=3, width=5).to_corner(corner=UR)
        self.play(
            Create(rectangle_zoom)
        )
        self.wait()
        arc_zoom = Arc(radius=1).move_to(([0,0,0]))
        # rectangle_zoom.animate.
        self.wait()
        # self.play(
        #     group.animate.move_to([-6.6,-3.5,0])
        # )
        # self.play(group.animate.scale(5))
        # self.wait()
        # line2 = ax.plot(lambda x:((-cos/sin)*x)+((r*cos**2)/sin))
        # self.play(Create(line2))
        # self.wait(2)
        
class ComplementaryAngle(Scene):
    def construct(self):
        ax = Axes(x_range=[-4.4, 4.4], y_range=[-2.2, 2.2])
        labels = ax.get_axis_labels(x_label="x", y_label="y")
        circle_up = ax.plot(lambda x: math.sqrt(1-x**2), x_range=[-1,1,0.01], color=WHITE)
        circle_down = ax.plot(lambda x: - math.sqrt(1-x**2), x_range=[-1,1,0.01], color=WHITE)
        circle = Circle(color=WHITE, radius=1.35)
        self.play(
            Create(ax)      
        )
        self.wait()
        self.play(
            Create(circle)      
        )
        rotation_center = LEFT

        theta = 1/6
        line1 = Line(start=([0,0,0]), end=([1.35,0,0]))
        line_moved = Line(start=([0,0,0]), end=([1.169,0.675,0]))
        
        a = Angle(line1, line_moved, radius=0.5, other_angle=False)
        tex = MathTex(r"\theta").move_to(
            Angle(
                line1, line_moved, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
            )
        )
        cos = math.cos(theta*PI)
        sin = math.sin(theta*PI)
        line_cos = Line(start=([0,0,0]),end=([1.35*cos,0,0]), color=BLUE_C)
        line_sin = Line(start=([1.35*cos,1.35*sin,0]),end=([1.35*cos,0,0]), color=TEAL_C)
        line_little = Line(start=([1.35,0,0]),end=([1.35*cos,0,0]))

        self.play(
            Create(line_moved),
            Create(line_cos),
            Create(line_sin),
            Create(line_little)  
        )
        self.wait(0.25)
        self.play(
            Create(a),
            Create(tex)
        )
        self.wait()
        self.play(FadeOut(a,tex))
        group = VGroup(circle,line_moved,line_cos,line_sin,line_little)
        base_angle = 1/2
        self.play(
            Rotate(
                mobject=group, angle=(base_angle - theta)*PI
            )
        )
        a = Angle(line_cos, line_moved, radius=0.5, other_angle=False)
        tex = MathTex(r"\theta").move_to(
            Angle(
                line_cos, line_moved, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
            )
        )
        a_rotate = Angle(line1, line_cos, radius=0.5, other_angle=False)
        tex_rotate = MathTex(r"\frac{\pi}{2}-\theta").move_to(
            Angle(
                line1, line_cos, radius=1.4 + SMALL_BUFF, other_angle=False
            )
        )
        tex_rotate.move_to([1.25,0.5,0])
        self.play(
            Create(a),
            Create(tex),
            Create(a_rotate),
            Create(tex_rotate)
        )
        self.wait()

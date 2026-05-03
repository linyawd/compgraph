import numpy as np
from src.engine.model.Model import Model
from src.engine.model.SimplePolygon import SimplePolygon
from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.math.Vec4 import Vec4
from hw1_2.utils import *


class Tetrahedron(Model):

    def __init__(self,
                 alpha=1.0,
                 color="cyan",
                 edge_color="blue",
                 line_style="-",
                 line_width=1.0,
                 ):
        super().__init__()
        self.polygons = []

        vertices = [
            [0, 0, 0],
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
        ]

        faces = [
            [vertices[j] for j in [0, 1, 2]],
            [vertices[j] for j in [0, 1, 3]],
            [vertices[j] for j in [0, 2, 3]],
            [vertices[j] for j in [1, 2, 3]],  
        ]

        for face in faces:
            self.polygons.append(
                SimplePolygon(
                    *face,
                    color=color,
                    edgecolor=edge_color,
                    alpha=alpha,
                    line_width=line_width,
                    line_style=line_style,
                )
            )

    def draw_model(self, plt_axis):
        for polygon in self.polygons:
            polygon.transformation = self.transformation
            polygon.pivot(self._pivot)
            polygon.draw(plt_axis)

    def apply_transformation_to_geometry(self):
        super().apply_transformation_to_geometry()

        for polygon in self.polygons:
            polygon.apply_transformation_to_geometry()


obj = Tetrahedron(alpha=0.2)

tetra = tetra_points()

angle = np.random.uniform(10, 90)
axis = np.random.uniform(-1, 1, 3)
shift = np.random.uniform(-5, 5, 3)

R = rot_axis(angle, axis)
T = translate(*shift)

tr1 = apply(tetra, R)
print_points("Rotate", tr1)

tr2 = apply(tetra, compose(R, T))
print_points("Final", tr2)

animations = [
    RotationAnimation(end=np.radians(angle), axis=Vec4(*axis), channel="object"),
    TranslationAnimation(end=Vec4(*shift), channel="object")
]

run_animations(animations, "Task 5", obj)
import numpy as np

from src.engine.scene.AnimatedScene import AnimatedScene
from src.engine.model.Polygon import Polygon

FIGURE_ID = "rect"


# -------------------- SCENE --------------------

def create_rectangle_scene(pivot_point, **kwargs):
    scene = AnimatedScene(**kwargs)

    rect = Polygon(
        0, 0,
        1, 0,
        1, 1,
        0, 1
    )

    rect["color"] = "blue"
    rect["line_style"] = "-"
    rect.pivot(*pivot_point)
    rect.show_pivot()

    scene[FIGURE_ID] = rect
    return scene


def run_animation(transformations, title, pivot=(0, 0)):
    scene = create_rectangle_scene(
        pivot_point=pivot,
        image_size=(7, 7),
        coordinate_rect=(-1, -1, 6, 6),
        title=title,
        base_axis_show=False,
        axis_show=True,
        axis_color=("red", "green"),
        axis_line_width=2.0,
        axis_line_style="--",
        keep_aspect_ratio=True,
    )

    for t in transformations:
        scene.add_animation(t)

    scene.show()


# -------------------- GEOMETRY --------------------

def create_unit_square():
    return np.array([
        [0, 0, 1],
        [1, 0, 1],
        [1, 1, 1],
        [0, 1, 1]
    ])


# -------------------- TRANSFORMATIONS --------------------

def rotation_matrix(deg):
    rad = np.radians(deg)
    return np.array([
        [np.cos(rad), -np.sin(rad), 0],
        [np.sin(rad),  np.cos(rad), 0],
        [0, 0, 1]
    ])


def translation_matrix(dx, dy):
    return np.array([
        [1, 0, dx],
        [0, 1, dy],
        [0, 0, 1]
    ])


def scale_matrix(sx, sy):
    return np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])


def compose(*matrices):
    result = np.eye(3)
    for m in matrices:
        result = result @ m
    return result


def transform_points(points, matrix):
    return points @ matrix.T


# -------------------- PIVOT OPERATIONS --------------------

def around_point(matrix, pivot):
    px, py = pivot
    return compose(
        translation_matrix(px, py),
        matrix,
        translation_matrix(-px, -py)
    )


# -------------------- DEBUG --------------------

def log_points(label, points):
    print(f"\n{label}:")
    for p in points:
        coords = ", ".join(f"{v:.3f}" for v in p[:2])
        print(f"({coords})")
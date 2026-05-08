from hw1_3.utils import *

steps = 10

for i in range(steps + 1):
    t = i / steps

    ax = 90 * t
    ay = 90 * t
    az = 90 * t

    R = compose(rot_x(ax), rot_y(ay), rot_z(az))

    forward = np.array([0,0,1,1])
    transformed = R @ forward

    print(f"Step {i}: dir = {transformed[:3]}")
    print_points("matrix", R[:3])
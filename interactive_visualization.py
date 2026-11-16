import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button


VERTICES = np.array(
    [
        [-1, -1, -1],
        [ 1, -1, -1],
        [ 1,  1, -1],
        [-1,  1, -1],
        [-1, -1,  1],
        [ 1, -1,  1],
        [ 1,  1,  1],
        [-1,  1,  1],
    ],
    dtype=float,
)


EDGES = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7),
]


def rotation_matrix(x_degrees, y_degrees, z_degrees):

    x, y, z = np.radians([x_degrees, y_degrees, z_degrees])
    cx, sx = np.cos(x), np.sin(x)
    cy, sy = np.cos(y), np.sin(y)
    cz, sz = np.cos(z), np.sin(z)

    rx = np.array([
        [1, 0, 0],
        [0, cx, -sx],
        [0, sx, cx],
    ])
    ry = np.array([
        [cy, 0, sy],
        [0, 1, 0],
        [-sy, 0, cy],
    ])
    rz = np.array([
        [cz, -sz, 0],
        [sz, cz, 0],
        [0, 0, 1],
    ])
    return rz @ ry @ rx


def draw_edges(ax, points, color="royalblue", linewidth=2.0):

    for i, j in EDGES:
        ax.plot(
            [points[i, 0], points[j, 0]],
            [points[i, 1], points[j, 1]],
            [points[i, 2], points[j, 2]],
            color=color,
            linewidth=linewidth,
        )


def configure_3d_axes(ax, title):

    ax.set_title(title)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)
    ax.set_box_aspect((1, 1, 1))
    ax.grid(True)


def calculate_checks(matrix, rotated_vertices):

    orthogonality_error = np.linalg.norm(matrix.T @ matrix - np.eye(3))
    determinant = np.linalg.det(matrix)

    original_lengths = np.array([
        np.linalg.norm(VERTICES[i] - VERTICES[j]) for i, j in EDGES
    ])
    rotated_lengths = np.array([
        np.linalg.norm(rotated_vertices[i] - rotated_vertices[j])
        for i, j in EDGES
    ])
    max_edge_error = float(np.max(np.abs(original_lengths - rotated_lengths)))

    return orthogonality_error, determinant, max_edge_error, original_lengths[0]


def main():
    fig = plt.figure(figsize=(13, 8))
    fig.suptitle(
        "3D Object Rotation Using Orthogonal Matrices",
        fontsize=15,
        fontweight="bold",
    )

    ax_original = fig.add_axes([0.03, 0.32, 0.42, 0.58], projection="3d")
    ax_rotated = fig.add_axes([0.53, 0.32, 0.42, 0.58], projection="3d")
    configure_3d_axes(ax_original, "Original Cube")
    draw_edges(ax_original, VERTICES, color="gray")


    slider_ax_x = fig.add_axes([0.13, 0.235, 0.54, 0.025])
    slider_ax_y = fig.add_axes([0.13, 0.190, 0.54, 0.025])
    slider_ax_z = fig.add_axes([0.13, 0.145, 0.54, 0.025])
    slider_x = Slider(slider_ax_x, "X angle", 0, 360, valinit=0, valstep=1)
    slider_y = Slider(slider_ax_y, "Y angle", 0, 360, valinit=0, valstep=1)
    slider_z = Slider(slider_ax_z, "Z angle", 0, 360, valinit=0, valstep=1)


    reset_ax = fig.add_axes([0.73, 0.16, 0.13, 0.055])
    reset_button = Button(reset_ax, "Reset")


    matrix_text = fig.text(
        0.56, 0.19, "", fontsize=8.5, family="monospace",
        va="top", ha="left"
    )
    check_text = fig.text(
        0.56, 0.045, "", fontsize=9, family="monospace",
        va="bottom", ha="left"
    )

    def update(_value=None):
        x, y, z = slider_x.val, slider_y.val, slider_z.val
        matrix = rotation_matrix(x, y, z)

        rotated = VERTICES @ matrix.T

        ax_rotated.clear()
        configure_3d_axes(
            ax_rotated,
            f"Rotated Cube: X={x:.0f}°, Y={y:.0f}°, Z={z:.0f}°",
        )
        draw_edges(ax_rotated, rotated)

        orth_error, det, edge_error, edge_length = calculate_checks(matrix, rotated)
        matrix_text.set_text(
            "Combined rotation matrix R = Rz @ Ry @ Rx\n"
            f"[{matrix[0, 0]: 7.3f} {matrix[0, 1]: 7.3f} {matrix[0, 2]: 7.3f}]\n"
            f"[{matrix[1, 0]: 7.3f} {matrix[1, 1]: 7.3f} {matrix[1, 2]: 7.3f}]\n"
            f"[{matrix[2, 0]: 7.3f} {matrix[2, 1]: 7.3f} {matrix[2, 2]: 7.3f}]"
        )
        check_text.set_text(
            f"Orthogonality error ||RᵀR − I||: {orth_error:.2e}\n"
            f"Determinant det(R): {det:.6f}  (expected +1)\n"
            f"Original edge length: {edge_length:.6f}\n"
            f"Maximum edge-length error: {edge_error:.2e}"
        )
        fig.canvas.draw_idle()

    def reset(_event):
        slider_x.reset()
        slider_y.reset()
        slider_z.reset()

    slider_x.on_changed(update)
    slider_y.on_changed(update)
    slider_z.on_changed(update)
    reset_button.on_clicked(reset)

    update()
    plt.show()


if __name__ == "__main__":
    main()

import matplotlib.pyplot as plt


def draw_cube(ax, vertices, edges, title="Cube"):

    for i, j in edges:
        ax.plot(
            [vertices[i, 0], vertices[j, 0]],
            [vertices[i, 1], vertices[j, 1]],
            [vertices[i, 2], vertices[j, 2]],
            linewidth=2,
        )

    ax.set_title(title)
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.set_zlabel("Z axis")
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)
    ax.set_box_aspect((1, 1, 1))
    ax.grid(True)


def show_cubes(original_vertices, rotated_vertices, edges):

    fig = plt.figure(figsize=(12, 6))
    ax_original = fig.add_subplot(121, projection="3d")
    ax_rotated = fig.add_subplot(122, projection="3d")

    draw_cube(ax_original, original_vertices, edges, "Original Cube")
    draw_cube(ax_rotated, rotated_vertices, edges, "Rotated Cube")

    fig.suptitle("3D Object Rotation Using Orthogonal Matrices")
    fig.tight_layout()
    plt.show()

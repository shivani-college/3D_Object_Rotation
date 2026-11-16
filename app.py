import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(
    page_title="3D Cube Rotation Simulator",
    page_icon="🧊",
    layout="wide"
)

st.title("3D Cube Rotation Simulator")
st.write("Explore 3D rotations using orthogonal matrices.")

vertices = np.array([
    [-1, -1, -1],
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, 1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, 1, 1]
])

edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

def rotation_x(angle):
    theta = np.radians(angle)
    return np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta), np.cos(theta)]
    ])

def rotation_y(angle):
    theta = np.radians(angle)
    return np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])

def rotation_z(angle):
    theta = np.radians(angle)
    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])

st.sidebar.header("Rotation Controls")

preset = st.sidebar.selectbox(
    "Choose a preset",
    [
        "Custom",
        "Reset (0°, 0°, 0°)",
        "X Rotation (90°)",
        "Y Rotation (90°)",
        "Z Rotation (90°)",
        "Combined (30°, 45°, 60°)"
    ]
)

presets = {
    "Reset (0°, 0°, 0°)": (0, 0, 0),
    "X Rotation (90°)": (90, 0, 0),
    "Y Rotation (90°)": (0, 90, 0),
    "Z Rotation (90°)": (0, 0, 90),
    "Combined (30°, 45°, 60°)": (30, 45, 60)
}

default_angles = presets.get(preset, (0, 0, 0))
key_name = preset.replace(" ", "_").replace("°", "")

st.sidebar.subheader("Adjust Angles")

angle_x = st.sidebar.slider(
    "Rotation around X-axis",
    0, 360, default_angles[0],
    key=f"x_{key_name}"
)

angle_y = st.sidebar.slider(
    "Rotation around Y-axis",
    0, 360, default_angles[1],
    key=f"y_{key_name}"
)

angle_z = st.sidebar.slider(
    "Rotation around Z-axis",
    0, 360, default_angles[2],
    key=f"z_{key_name}"
)

Rx = rotation_x(angle_x)
Ry = rotation_y(angle_y)
Rz = rotation_z(angle_z)

R = Rz @ Ry @ Rx

rotated_vertices = vertices @ R.T

def draw_cube(points, title):
    fig = go.Figure()

    for start, end in edges:
        fig.add_trace(go.Scatter3d(
            x=[points[start, 0], points[end, 0]],
            y=[points[start, 1], points[end, 1]],
            z=[points[start, 2], points[end, 2]],
            mode="lines",
            line=dict(color="#2196F3", width=6),
            showlegend=False
        ))

    fig.add_trace(go.Scatter3d(
        x=points[:, 0],
        y=points[:, 1],
        z=points[:, 2],
        mode="markers+text",
        text=[f"P{i+1}" for i in range(8)],
        textposition="top center",
        marker=dict(size=6, color="#FF5722"),
        name="Vertices"
    ))

    fig.update_layout(
        title=title,
        height=500,
        margin=dict(l=0, r=0, b=0, t=40),
        scene=dict(
            xaxis_title="X",
            yaxis_title="Y",
            zaxis_title="Z",
            aspectmode="cube"
        )
    )

    return fig

col1, col2 = st.columns(2)

with col1:
    st.subheader("Original Cube")
    st.plotly_chart(
        draw_cube(vertices, "Before Rotation"),
        use_container_width=True
    )

with col2:
    st.subheader("Rotated Cube")
    st.plotly_chart(
        draw_cube(rotated_vertices, "After Rotation"),
        use_container_width=True
    )

st.divider()
st.header("Rotation Information")

c1, c2, c3 = st.columns(3)

c1.metric("X Rotation", f"{angle_x}°")
c2.metric("Y Rotation", f"{angle_y}°")
c3.metric("Z Rotation", f"{angle_z}°")

st.subheader("Combined Rotation Matrix")
st.write("R = Rz × Ry × Rx")
st.dataframe(np.round(R, 3), use_container_width=True)

st.subheader("Orthogonality Verification")

identity = np.eye(3)
check = R.T @ R
orthogonality_error = np.max(np.abs(check - identity))
determinant = np.linalg.det(R)

v1, v2 = st.columns(2)

with v1:
    st.metric("Orthogonality Error", f"{orthogonality_error:.2e}")

    if np.allclose(check, identity):
        st.success("Verified: RᵀR = I")
    else:
        st.error("Orthogonality check failed")

with v2:
    st.metric("Determinant", f"{determinant:.4f}")

    if np.isclose(determinant, 1):
        st.success("Verified: det(R) = +1")
    else:
        st.error("Determinant check failed")

st.divider()
st.subheader("Vertex Coordinate Comparison")

show_coordinates = st.checkbox(
    "Show original and rotated coordinates",
    value=True
)

if show_coordinates:
    coordinate_data = []

    for i in range(8):
        coordinate_data.append({
            "Vertex": f"P{i+1}",
            "Original Coordinates": np.round(vertices[i], 3),
            "Rotated Coordinates": np.round(rotated_vertices[i], 3)
        })

    st.dataframe(coordinate_data, use_container_width=True)

st.divider()

with st.expander("About this project"):
    st.write("""
    This project demonstrates how orthogonal matrices are used
    to rotate a 3D object.

    - A cube is represented using 8 vertices.
    - Rotation matrices are created for X, Y and Z axes.
    - The matrices are multiplied to create a combined rotation.
    - Cube vertices are transformed using the combined matrix.
    - Orthogonality is verified using R transpose multiplied by R.
    - The determinant of a proper rotation matrix is +1.

    Rotation preserves distances, angles and the shape of the cube.
    """)

st.caption(
    "Linear Algebra Project | 3D Object Rotation Using Orthogonal Matrices"
)

# 3D Object Rotation Using Orthogonal Matrices

## 1. Project Overview

This project demonstrates the rotation of a 3D object using orthogonal matrices. A cube is represented using eight vertices in 3D space. Rotation matrices are applied around the X, Y and Z axes to change the orientation of the cube.

The project uses Python to perform mathematical calculations and provides an interactive web interface to visualize the rotation.

## 2. Objectives

- Understand the concept of orthogonal matrices.
- Implement rotation matrices around the X, Y and Z axes.
- Perform combined 3D rotations.
- Visualize the original and rotated cube.
- Verify the orthogonality property of rotation matrices.
- Understand the practical applications of linear algebra in 3D graphics.

## 3. Technologies Used

- **Python:** Main programming language.
- **NumPy:** Matrix operations and mathematical calculations.
- **Streamlit:** Interactive user interface.
- **Plotly:** Interactive 3D visualization.

## 4. Mathematical Concepts

### Rotation Around X-axis

\[
R_x(\theta)=
\begin{bmatrix}
1&0&0\\
0&\cos\theta&-\sin\theta\\
0&\sin\theta&\cos\theta
\end{bmatrix}
\]

### Rotation Around Y-axis

\[
R_y(\theta)=
\begin{bmatrix}
\cos\theta&0&\sin\theta\\
0&1&0\\
-\sin\theta&0&\cos\theta
\end{bmatrix}
\]

### Rotation Around Z-axis

\[
R_z(\theta)=
\begin{bmatrix}
\cos\theta&-\sin\theta&0\\
\sin\theta&\cos\theta&0\\
0&0&1
\end{bmatrix}
\]

### Combined Rotation

The combined rotation matrix is:

\[
R=R_zR_yR_x
\]

The rotations are applied in the order X, Y and then Z.

The cube vertices are stored as row vectors in NumPy. Therefore, the transformation is:

\[
P'=PR^T
\]

Where:
- \(P\) represents the original cube coordinates.
- \(R\) represents the combined rotation matrix.
- \(P'\) represents the rotated cube coordinates.

### Orthogonality Property

A rotation matrix is orthogonal if:

\[
R^TR=I
\]

For a proper rotation matrix:

\[
\det(R)=+1
\]

Orthogonal rotation matrices preserve distances and angles.

## 5. Project Features

- Interactive 3D cube visualization.
- Original and rotated cube displayed side by side.
- Separate rotation controls for X, Y and Z axes.
- Preset rotation options.
- Combined rotation functionality.
- Display of the combined rotation matrix.
- Orthogonality verification.
- Determinant verification.
- Comparison of original and rotated vertex coordinates.

## 6. Installation and Setup

### Step 1: Install Python

Install Python 3 on your computer if it is not already installed.

### Step 2: Install Required Libraries

Open the terminal and execute:

bash
python3 -m pip install streamlit numpy plotly


### Step 3: Download or Clone the Project

Place the project files in a folder named:

text
3D_Rotation_Project/

The folder should contain:

```text
3D_Rotation_Project/
│
├── app.py
├── requirements.txt
└── README.md
```

### Step 4: Install Dependencies Using requirements.txt

```bash
python3 -m pip install -r requirements.txt
```

## 7. How to Run the Project

Open the terminal in the project folder and execute:

```bash
python3 -m streamlit run app.py
```

After execution, Streamlit will provide a local URL, usually:

```text
http://localhost:8501
```

Open this URL in your browser to access the interactive application.

## 8. How to Use the Application

1. Open the application in your browser.
2. Select a rotation preset or choose Custom.
3. Adjust the X-axis, Y-axis and Z-axis sliders.
4. Observe the original and rotated cubes.
5. View the combined rotation matrix.
6. Check the orthogonality error and determinant.
7. Enable the coordinate comparison to see how the vertices change.

## 9. Orthogonality Verification

The application verifies the orthogonality of the combined rotation matrix using:

```python
identity = np.eye(3)
check = R.T @ R

orthogonality_error = np.max(
    np.abs(check - identity)
)

determinant = np.linalg.det(R)
```

The orthogonality error should be close to zero, and the determinant should be close to +1.

Small numerical differences may occur due to floating-point precision.

## 10. Real-Life Applications

Orthogonal matrices and 3D rotation techniques are used in:

- **Robotics:** Controlling the orientation of robotic arms.
- **Computer Graphics:** Rotating 3D objects in animations and games.
- **Drones:** Representing and controlling drone orientation.
- **Medical Imaging:** Aligning and orienting 3D scan data.
- **Virtual Reality:** Updating the orientation of virtual objects.
- **Space Technology:** Controlling satellite and spacecraft orientation.

## 11. Limitations and Future Scope

### Limitations

- The project demonstrates rotation but does not implement translation or scaling.
- The cube is a simple 3D object.
- The visualization is intended for educational demonstration.
- Floating-point calculations may introduce very small numerical errors.

### Future Scope

- Add rotation animation.
- Support other 3D objects such as pyramids and spheres.
- Add translation and scaling transformations.
- Implement camera controls.
- Extend the project to demonstrate more complex 3D transformations.

## 12. Conclusion

This project demonstrates how orthogonal matrices can be used to rotate objects in three-dimensional space.

By implementing rotation matrices around the X, Y and Z axes, we can calculate new vertex coordinates and visualize the resulting object.

The orthogonality verification confirms that the rotation preserves the object's distances and angles.

The project connects fundamental linear algebra concepts with practical applications in computer graphics, robotics and other 3D technologies.

---

**Project Title:** 3D Object Rotation Using Orthogonal Matrices

**Programming Language:** Python

**Libraries:** NumPy, Streamlit and Plotly

**Project Domain:** Linear Algebra and 3D Visualization

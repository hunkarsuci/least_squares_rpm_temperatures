# Least Squares Estimation: Temperature-RPM Model

This project implements the **closed-form Least Squares (LS) estimation** to identify a linear relationship between temperature and RPM from noisy measurement data.  
It demonstrates model formulation, parameter estimation, validation, and visualization using Python.

---

## Problem Description

Given noisy measurements of temperature at different RPM values, the goal is to estimate the parameters of the linear model:

\[
y_i = x_1 r_i + x_2
\]

where:
- \( y_i \) is the measured temperature  
- \( r_i \) is the RPM  
- \( x_1 \) and \( x_2 \) are unknown constant parameters  

The estimation is performed using **batch Least Squares**.

---

## Least Squares Solution

The measurement model is written in matrix form:

\[
\mathbf{y} \approx \mathbf{H}\mathbf{x}
\]

with:

\[
\mathbf{H} =
\begin{bmatrix}
r_1 & 1 \\
r_2 & 1 \\
\vdots & \vdots \\
r_n & 1
\end{bmatrix},
\quad
\mathbf{x} =
\begin{bmatrix}
x_1 \\
x_2
\end{bmatrix}
\]

The closed-form Least Squares estimate is:

\[
\hat{\mathbf{x}} = (\mathbf{H}^T\mathbf{H})^{-1}\mathbf{H}^T\mathbf{y}
\]

---

## Project Structure


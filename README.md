# Least Squares Estimation of a Temperature–RPM Model

## Overview

This repository presents a **batch Least Squares (LS) estimation framework** for identifying a linear relationship between temperature and rotational speed (RPM) from noisy measurement data.  
The project focuses on **model formulation, estimation theory, numerical implementation, and validation**, and is intended as a concise demonstration of parameter estimation techniques commonly used in engineering systems.

The implementation is written in Python and follows a clear separation between:
- estimation algorithms,
- data generation, and
- evaluation / visualization.

---

## Problem Formulation

Given a set of noisy measurements:

\[
\mathcal{D} = \{(r_i, y_i)\}_{i=1}^{n}
\]

where:
- \( r_i \) denotes RPM,
- \( y_i \) denotes the measured temperature,

the goal is to estimate the parameters of the linear model:

\[
y_i = x_1 r_i + x_2 + v_i
\]

with:
- \( \mathbf{x} = [x_1 \;\; x_2]^T \) being unknown constant parameters,
- \( v_i \) representing measurement noise.

---

## Least Squares Estimation

The measurement model is written in matrix form as:

\[
\mathbf{y} \approx \mathbf{H}\mathbf{x}
\]

where:

\[
\mathbf{H} =
\begin{bmatrix}
r_1 & 1 \\
r_2 & 1 \\
\vdots & \vdots \\
r_n & 1
\end{bmatrix},
\quad
\mathbf{y} =
\begin{bmatrix}
y_1 \\
y_2 \\
\vdots \\
y_n
\end{bmatrix}
\]

The batch Least Squares solution is obtained by minimizing the squared residual norm:

\[
\hat{\mathbf{x}} = \arg\min_{\mathbf{x}} \|\mathbf{y} - \mathbf{H}\mathbf{x}\|^2
\]

which yields the closed-form estimator:

\[
\hat{\mathbf{x}} = (\mathbf{H}^T \mathbf{H})^{-1} \mathbf{H}^T \mathbf{y}
\]

This formulation assumes full column rank of \( \mathbf{H} \).

---

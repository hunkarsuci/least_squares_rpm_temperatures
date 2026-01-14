# Least Squares Estimation: Temperature–RPM Model

## Overview

This repository demonstrates a **batch Least Squares estimation** approach to identify a linear relationship between temperature and rotational speed (RPM) from noisy measurement data.  
The project focuses on clean implementation, reproducibility, and result validation, and is intended as a compact engineering example of parameter estimation.

The codebase is written in Python and organized to clearly separate:
- estimation logic,
- data generation, and
- evaluation and visualization.

---

## Problem Description

Given noisy temperature measurements recorded at different RPM values, the objective is to estimate the parameters of a linear model that best fits the data in a least-squares sense.

The estimated model represents:
- a proportional relationship between RPM and temperature, and
- a constant offset term.
- 
---

## Key Features

- Closed-form batch Least Squares estimator
- Reproducible synthetic dataset with realistic measurement noise
- Linear regression applied to RPM–temperature data
- Quantitative performance evaluation using RMSE
- Visualization of measurements and fitted model
- Modular and extensible code structure

---

## How to Run

### Install dependencies
```bash
pip install -r requirements.txt

import numpy as np
import matplotlib.pyplot as plt

from data import generate_rpm_temp_dataset
from least_squares import CalculateLineOfBestFitSolution

def rmse(y_true, y_pred):
    y_true = np.array(y_true, dtype=float)
    y_pred = np.array(y_pred, dtype=float)
    return float(np.sqrt(np.mean((y_true - y_pred) ** 2)))

if __name__ == "__main__":
    # 1) Create dataset
    dataset, meta = generate_rpm_temp_dataset(n=40, seed=7)

    # 2) Fit line y = a*r + b
    x_hat = CalculateLineOfBestFitSolution(dataset)
    a_hat, b_hat = float(x_hat[0]), float(x_hat[1])

    # 3) Prepare arrays for plotting + evaluation
    rpm = np.array([r for (t, r) in dataset], dtype=float)
    temp = np.array([t for (t, r) in dataset], dtype=float)
    temp_pred = a_hat * rpm + b_hat

    # 4) Print results
    print("True params:      a =", meta["a_true"], "b =", meta["b_true"])
    print("Estimated params: a =", a_hat, "b =", b_hat)
    print("RMSE (°C):", rmse(temp, temp_pred))
    print("Outlier indices:", meta["outlier_idx"], "seed:", meta["seed"])

    # 5) Plot scatter + fitted line
    # Sort by rpm for a clean line plot
    sort_idx = np.argsort(rpm)
    rpm_sorted = rpm[sort_idx]
    pred_sorted = temp_pred[sort_idx]

    plt.figure()
    plt.scatter(rpm, temp, label="Noisy measurements")
    plt.plot(rpm_sorted, pred_sorted, label="Least Squares fit")

    plt.xlabel("RPM")
    plt.ylabel("Temperature (°C)")
    plt.title("Temperature vs RPM — Least Squares Line Fit")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

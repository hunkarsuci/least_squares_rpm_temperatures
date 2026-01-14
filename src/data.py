import numpy as np 

def generate_rpm_temp_dataset(n = 40, seed = 7): 
    """
    Generates a reproducible RPM vs temperature dataset.
    - RPM range: 1000...6000
    - True model: T = a_true * rpm + b_true + noise
    - Adds a couple of outliers to mimic occasional sensor glitches (optional realism)
    """
    rng = np.random.default_rng(seed)

    rpm = np.linspace(1000,6000,n)

    # True underlying relationship 
    a_true = 0.012  # degC per RPM
    b_true = 35.0   # degC baseline

    noise = rng.normal(0.0, 2.0, size=n)  # 2�C measurement noise
    temp = a_true * rpm + b_true + noise

    # Optional realistic outliers (2 points)
    outlier_idx = rng.choice(n, size=2, replace=False)
    temp[outlier_idx] += rng.normal(0.0, 10.0, size=2)

    dataset = [[float(temp[i]), float(rpm[i])] for i in range(n)]
    meta = {
        "a_true": a_true,
        "b_true": b_true,
        "outlier_idx": outlier_idx.tolist(),
        "seed": seed,
        "n": n
    }
    return dataset, meta

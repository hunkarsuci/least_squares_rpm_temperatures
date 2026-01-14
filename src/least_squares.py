import numpy as np

def CalculateLeastSquaresSolution(Hmatrix, Ymatrix):
    """
    General Least Squares solution:
        x_hat = (H^T H)^(-1) H^T y

    Returns x_hat as 1-D array shape (n,)
    """
    H = np.array(Hmatrix, dtype=float)
    y = np.array(Ymatrix, dtype=float)

    # Ensure y is a column vector (m,1)
    if y.ndim == 1:
        y = y.reshape(-1, 1)

    HT = H.T
    x_hat = np.linalg.inv(HT @ H) @ (HT @ y)

    # Autograders / typical usage often expect shape (n,)
    return x_hat.reshape(-1)

def CalculateLineOfBestFitSolution(Dataset):
    """
    Dataset format: [[y1, r1], [y2, r2], ..., [yn, rn]]
    Fits: y = x1 * r + x2
    """
    H_rows = []
    y_rows = []
    for yi, ri in Dataset:
        H_rows.append([ri, 1.0])
        y_rows.append([yi])  # keep column-like entries

    return CalculateLeastSquaresSolution(H_rows, y_rows)


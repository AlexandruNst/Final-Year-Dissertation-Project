import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Code for generatin box charts for the test results

rmse_svd_whole = np.array([
    5.55, 5.64, 5.85, 6.38, 7.80, 6.36, 5.52, 6.40, 4.51, 6.26, 5.55, 5.64,
    5.85, 6.38, 7.80, 6.36, 5.52, 6.40, 4.51, 6.26, 5.55, 5.64, 5.85, 6.38,
    7.80, 6.36, 5.52, 6.40, 4.51, 6.26
])

rmse_icp_whole = np.array([
    5.97, 6.27, 6.57, 6.73, 7.23, 5.45, 5.50, 4.51, 4.74, 5.94, 5.97, 6.28,
    6.57, 6.72, 7.24, 5.46, 5.50, 4.50, 4.74, 5.95, 5.98, 6.17, 6.58, 6.72,
    7.23, 5.46, 5.50, 4.50, 4.74, 5.94
])

rmse_svd_top = np.array([
    5.15, 2.73, 2.76, 4.26, 4.88, 6.45, 5.19, 6.67, 4.80, 6.45, 5.15, 2.73,
    2.76, 4.26, 4.88, 6.45, 5.19, 6.67, 4.80, 6.45, 5.15, 2.73, 2.76, 4.26,
    4.88, 6.45, 5.19, 6.67, 4.80, 6.45
])

rmse_icp_top = np.array([
    3.28, 2.84, 3.08, 3.93, 4.77, 3.55, 3.40, 2.93, 3.53, 3.92, 3.29, 2.84,
    3.08, 3.93, 4.78, 3.56, 3.40, 2.93, 3.52, 3.92, 3.28, 2.83, 3.08, 3.94,
    4.77, 3.56, 3.40, 2.93, 3.52, 3.92
])

data_rmse = np.transpose(
    [rmse_svd_whole, rmse_icp_whole, rmse_svd_top, rmse_icp_top])

#########################

hausdorff_svd_whole = np.array([
    16.35, 17.13, 17.05, 20.50, 24.67, 16.52, 16.32, 15.40, 20.75, 34.35,
    16.35, 17.25, 17.05, 21.33, 24.67, 16.48, 16.32, 15.40, 20.72, 34.35,
    16.35, 16.95, 16.77, 20.50, 24.67, 16.48, 16.32, 15.40, 20.72, 34.35
])

hausdorff_icp_whole = np.array([
    26.04, 19.15, 18.28, 17.42, 17.95, 18.49, 20.16, 17.73, 25.60, 34.51,
    26.05, 19.17, 18.26, 16.99, 17.81, 18.52, 20.16, 17.73, 25.60, 34.50,
    26.06, 19.26, 18.26, 17.00, 17.90, 18.53, 20.17, 17.71, 25.62, 34.49
])

hausdorff_svd_top = np.array([
    11.37, 7.35, 8.93, 12.94, 12.69, 15.50, 10.89, 14.34, 11.72, 16.30, 11.37,
    7.48, 8.88, 12.94, 12.53, 15.50, 10.89, 14.34, 11.72, 16.36, 11.37, 7.32,
    8.88, 12.94, 12.55, 15.50, 10.88, 14.34, 11.72, 16.18
])

hausdorff_icp_top = np.array([
    9.94, 9.21, 7.76, 9.06, 14.25, 11.37, 15.79, 10.98, 8.62, 10.83, 9.83,
    8.96, 7.71, 9.24, 14.33, 11.46, 15.58, 10.99, 8.57, 10.83, 9.88, 9.93,
    8.97, 7.70, 9.03, 14.25, 11.47, 15.57, 10.99, 8.57
])

data_hausdorff = np.transpose([
    hausdorff_svd_whole, hausdorff_icp_whole, hausdorff_svd_top,
    hausdorff_icp_top
])

###############

volume_svd = np.array([
    0.8543, 0.8590, 0.8557, 0.8497, 0.8144, 0.8587, 0.8724, 0.8579, 0.8608,
    0.8110, 0.8503, 0.8588, 0.8576, 0.8483, 0.8172, 0.8593, 0.8716, 0.8583,
    0.8638, 0.8099, 0.8527, 0.8609, 0.8566, 0.8483, 0.8158, 0.8580, 0.8716,
    0.8595, 0.8647, 0.8091
])

volume_icp = np.array([
    0.8778, 0.9038, 0.9000, 0.8789, 0.8751, 0.8831, 0.9070, 0.9033, 0.8716,
    0.8169, 0.8776, 0.9040, 0.8981, 0.8790, 0.8756, 0.8873, 0.9063, 0.9018,
    0.8712, 0.8414, 0.8776, 0.9052, 0.8967, 0.8761, 0.8761, 0.8857, 0.9053,
    0.9026, 0.8674, 0.8417
])

data_volume = np.transpose([volume_svd, volume_icp])

df = pd.DataFrame(data_volume, columns=['SVD', 'ICP'])
df.plot.box()

plt.title('Volume overlap')
plt.xlabel('Evaluation method')
plt.ylabel('Volume overlap')
plt.show()
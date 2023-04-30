import numpy as np
from preprocess.point_cloud import subject_1_cp, subject_2_cp, subject_3_cp, subject_4_cp, subject_5_cp, subject_6_cp, subject_7_cp, subject_8_cp, subject_9_cp, subject_10_cp, atlas_cp

# Generate the top of the head isolations for the evaluation

rows = np.where(subject_1_cp[:, 2] > -10)
subject_1_top_of_head_cp = subject_1_cp[rows]

rows = np.where(subject_2_cp[:, 2] > -10)
subject_2_top_of_head_cp = subject_2_cp[rows]

rows = np.where(subject_3_cp[:, 2] > -10)
subject_3_top_of_head_cp = subject_3_cp[rows]

rows = np.where(subject_4_cp[:, 2] > -10)
subject_4_top_of_head_cp = subject_4_cp[rows]

rows = np.where(subject_5_cp[:, 2] > -10)
subject_5_top_of_head_cp = subject_5_cp[rows]

rows = np.where(subject_6_cp[:, 2] > -10)
subject_6_top_of_head_cp = subject_6_cp[rows]

rows = np.where(subject_7_cp[:, 2] > -10)
subject_7_top_of_head_cp = subject_7_cp[rows]

rows = np.where(subject_8_cp[:, 2] > -10)
subject_8_top_of_head_cp = subject_8_cp[rows]

rows = np.where(subject_9_cp[:, 2] > -10)
subject_9_top_of_head_cp = subject_9_cp[rows]

rows = np.where(subject_10_cp[:, 2] > -10)
subject_10_top_of_head_cp = subject_10_cp[rows]

rows = np.where(atlas_cp[:, 2] > -10)
atlas_top_of_head_cp = atlas_cp[rows]

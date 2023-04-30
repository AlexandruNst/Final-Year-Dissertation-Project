from scipy.spatial.distance import directed_hausdorff
import numpy as np


# Calculate the Hausdorff distance
def calculate_hausdorff_distance(subject, atlas):
    subject_len = len(subject)
    atlas_len = len(atlas)

    min_len = subject_len if subject_len < atlas_len else atlas_len

    rnd_indices = np.random.choice(len(subject), size=min_len, replace=False)
    subject = subject[rnd_indices]

    rnd_indices = np.random.choice(len(atlas), size=min_len, replace=False)
    atlas = atlas[rnd_indices]

    dist = directed_hausdorff(subject, atlas)[0]

    return dist

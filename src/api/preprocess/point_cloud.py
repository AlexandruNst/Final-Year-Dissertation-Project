import numpy as np
import pprint

# Read the point clouds

subject_1_cp = np.loadtxt("./data/subject1.txt", max_rows=1000000)
subject_2_cp = np.loadtxt("./data/subject2.txt", max_rows=1000000)
subject_3_cp = np.loadtxt("./data/subject3.txt", max_rows=1000000)
subject_4_cp = np.loadtxt("./data/subject4.txt", max_rows=1000000)
subject_5_cp = np.loadtxt("./data/subject5.txt", max_rows=1000000)
subject_6_cp = np.loadtxt("./data/subject6.txt", max_rows=1000000)
subject_7_cp = np.loadtxt("./data/subject7.txt", max_rows=1000000)
subject_8_cp = np.loadtxt("./data/subject8.txt", max_rows=1000000)
subject_9_cp = np.loadtxt("./data/subject9.txt", max_rows=1000000)
subject_10_cp = np.loadtxt("./data/subject10.txt", max_rows=1000000)
atlas_cp = np.loadtxt("./data/atlas.txt", max_rows=1000000)
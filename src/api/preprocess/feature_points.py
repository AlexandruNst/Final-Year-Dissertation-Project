import numpy as np
import pprint

# Read feature points

file_data_path = "./data/subject1_fp.txt"
subject_1_fp = np.loadtxt(file_data_path, max_rows=1000000, comments='#')

file_data_path = "./data/subject2_fp.txt"
subject_2_fp = np.loadtxt(file_data_path, max_rows=1000000, comments='#')

file_data_path = "./data/subject3_fp.txt"
subject_3_fp = np.loadtxt(file_data_path, max_rows=1000000, comments='#')

file_data_path = "./data/subject4_fp.txt"
subject_4_fp = np.loadtxt(file_data_path, max_rows=1000000, comments='#')

file_data_path = "./data/subject5_fp.txt"
subject_5_fp = np.loadtxt(file_data_path, max_rows=1000000, comments='#')

file_data_path = "./data/subject6_fp.txt"
subject_6_fp = np.loadtxt(file_data_path, max_rows=1000000, comments='#')

file_data_path = "./data/subject7_fp.txt"
subject_7_fp = np.loadtxt(file_data_path, max_rows=1000000, comments='#')

file_data_path = "./data/subject8_fp.txt"
subject_8_fp = np.loadtxt(file_data_path, max_rows=1000000, comments='#')

file_data_path = "./data/subject9_fp.txt"
subject_9_fp = np.loadtxt(file_data_path, max_rows=1000000, comments='#')

file_data_path = "./data/subject10_fp.txt"
subject_10_fp = np.loadtxt(file_data_path, max_rows=1000000, comments='#')

file_data_path = "./data/atlas_fp.txt"
atlas_fp = np.loadtxt(file_data_path, max_rows=1000000, comments='#')
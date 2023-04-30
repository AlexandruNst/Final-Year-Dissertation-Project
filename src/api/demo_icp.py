from render.render import render_point_cloud, render_two_point_clouds
from process.registration import registration
from process.icp import icp_quaternion as icp
from evaluation.hausdoff import calculate_hausdorff_distance
from evaluation.rms import calculate_rms_distance
from preprocess.point_cloud import subject_1_cp, subject_2_cp, subject_3_cp, subject_4_cp, subject_5_cp, subject_6_cp, subject_7_cp, subject_8_cp, subject_9_cp, subject_10_cp, atlas_cp
from preprocess.feature_points import subject_1_fp, subject_2_fp, subject_3_fp, subject_4_fp, subject_5_fp, subject_6_fp, subject_7_fp, subject_8_fp, subject_9_fp, subject_10_fp, atlas_fp
from preprocess.point_cloud_top_of_head import subject_1_top_of_head_cp, subject_2_top_of_head_cp, subject_3_top_of_head_cp, subject_4_top_of_head_cp, subject_5_top_of_head_cp, subject_6_top_of_head_cp, subject_7_top_of_head_cp, subject_8_top_of_head_cp, subject_9_top_of_head_cp, subject_10_top_of_head_cp, atlas_top_of_head_cp
from metrics_calc.calc_metrics import calc_metrics
from metrics_calc.calc_metrics_top_of_head import calc_metrics_top_head
import time
from evaluation.volume_points import calculate_volume_points_percentage
from stl_handling.stl import ben_head_reduced_cp, ben_reduced_cp
from process.rotate import rotate_to_match, rotate_to_face_front, rotate_to_match_bad
from ply_handling.handle_ply_input import get_point_cloud_from_user_input, get_top_of_head_from_user_input, write_registered_points

# Demo for the ICP method in action

render_two_point_clouds(subject_3_cp, atlas_cp)
transformed_top_head, transformed_whole_head = icp(subject_3_cp, subject_3_cp,
                                                   atlas_cp, subject_3_cp)
render_two_point_clouds(transformed_whole_head, atlas_cp)

print("//BEFORE//")
print("Hausdorff ditance: ", end="")
print(calculate_hausdorff_distance(subject_3_cp, atlas_cp))
print("RMSE: ", end="")
print(calculate_rms_distance(subject_3_cp, atlas_cp))
print("//AFTER//")
print("Hausdorff ditance: ", end="")
print(calculate_hausdorff_distance(transformed_whole_head, atlas_cp))
print("RMSE: ", end="")
print(calculate_rms_distance(transformed_whole_head, atlas_cp))
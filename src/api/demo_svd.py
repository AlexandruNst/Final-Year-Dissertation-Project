from render.render import render_point_cloud, render_two_point_clouds
from process.registration import registration
from evaluation.hausdoff import calculate_hausdorff_distance
from evaluation.rms import calculate_rms_distance
from preprocess.point_cloud import subject_1_cp, subject_2_cp, subject_3_cp, subject_4_cp, subject_5_cp, subject_6_cp, subject_7_cp, subject_8_cp, subject_9_cp, subject_10_cp, atlas_cp
from preprocess.feature_points import subject_1_fp, subject_2_fp, subject_3_fp, subject_4_fp, subject_5_fp, subject_6_fp, subject_7_fp, subject_8_fp, subject_9_fp, subject_10_fp, atlas_fp

# Demo for the SVD method in action

render_two_point_clouds(subject_3_cp, atlas_cp)
transformed_s3 = registration(subject_3_cp, subject_3_fp, atlas_fp)
render_two_point_clouds(transformed_s3, atlas_cp)
print("//BEFORE//")
print("Hausdorff ditance: ", end="")
print(calculate_hausdorff_distance(subject_3_cp, atlas_cp))
print("RMSE: ", end="")
print(calculate_rms_distance(subject_3_cp, atlas_cp))
print("//AFTER//")
print("Hausdorff ditance: ", end="")
print(calculate_hausdorff_distance(transformed_s3, atlas_cp))
print("RMSE: ", end="")
print(calculate_rms_distance(transformed_s3, atlas_cp))
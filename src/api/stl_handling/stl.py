from stl import mesh
import numpy as np

# Methods for reading the STL subject point clouds

stl_mesh = mesh.Mesh.from_file("./data/Ben_head.stl")
ben_head_pc = np.around(
    np.unique(stl_mesh.vectors.reshape([int(stl_mesh.vectors.size / 3), 3]),
              axis=0), 2)
rnd_indices = np.random.choice(len(ben_head_pc), size=30000, replace=False)
ben_head_reduced_cp = ben_head_pc[rnd_indices]

stl_mesh = mesh.Mesh.from_file("./data/Ben.stl")
ben_pc = np.around(
    np.unique(stl_mesh.vectors.reshape([int(stl_mesh.vectors.size / 3), 3]),
              axis=0), 2)
rnd_indices = np.random.choice(len(ben_pc), size=30000, replace=False)
ben_reduced_cp = ben_pc[rnd_indices]
import matplotlib.pyplot as plt

# Methods for rendering scatter plots


# Individual point cloud render
def render_point_cloud(pc):
    ax = plt.axes(projection='3d')
    ax.scatter(pc[:, 0], pc[:, 1], pc[:, 2], s=0.02)
    plt.show()


# Two point couds render
def render_two_point_clouds(pc1, pc2):
    ax = plt.axes(projection='3d')
    ax.scatter(pc1[:, 0], pc1[:, 1], pc1[:, 2], s=0.02)
    ax.scatter(pc2[:, 0], pc2[:, 1], pc2[:, 2], s=0.02)
    ax.view_init(0, 0)
    plt.show()

####################################################
### Matplotlibを利用し、結果の図を描く
####################################################
import main_stl as ms

import numpy as np
from stl import mesh
import math
from matplotlib import pyplot
from mpl_toolkits import mplot3d

## モデルを表示
def show(filename_bunny):
  figure = pyplot.figure()
  axes = mplot3d.Axes3D(figure)

  your_mesh = mesh.Mesh.from_file(filename_bunny)
  axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))
  # 大きさを自動調整
  scale = your_mesh.points.flatten(-1)
  axes.auto_scale_xyz(scale, scale, scale)

  volume, cog, inertia = your_mesh.get_mass_properties()
  print(volume)
  # 表示
  pyplot.rcParams["font.family"] = "IPAexGothic"
  axes.set_xlabel("x-axis")
  axes.set_ylabel("y-axis")
  axes.set_zlabel("z-axis")
  pyplot.show()

if __name__ == "__main__":
  filename_bunny = 'D:\\Python\\20190613\\stl_sample\\Bunny-LowPoly.stl'
  show(filename_bunny)

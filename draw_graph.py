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
def show(your_mesh):
  figure = pyplot.figure()
  axes = mplot3d.Axes3D(figure)
  axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))
  # 大きさを自動調整
  scale = your_mesh.points.flatten(-1)
  axes.auto_scale_xyz(scale, scale, scale)

  # 表示
  pyplot.show()
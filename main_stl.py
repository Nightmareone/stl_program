####################################################
###メインのSTLファイルの読み込み、サポートの起点を生成
####################################################
import program4support as p4s
import draw_graph as dg

import numpy as np
from stl import mesh
import math
import datetime
from matplotlib import pyplot
from mpl_toolkits import mplot3d

## 读入STL文件，模型的角度旋转实现，生成识别范围
def main_get_plane(filename):
  starttime = datetime.datetime.now() ##開始時間
  angle = 0
  your_mesh = mesh.Mesh.from_file(filename)
  print("ファセットの数は:{}".format(len(your_mesh)))

  while angle <= 360:
    your_mesh.rotate([0.0, 1.0, 0.0], math.radians(angle)) ## 限制模型沿着y轴进行旋转

    total_support = 0 ## サポートの総合長さ
    list_x = []
    list_y = []
    list_z = []
    
    for v in your_mesh.data:
      ## すべてのx軸座標を取得
      list_x.append(v[1][0][0])
      list_x.append(v[1][1][0])
      list_x.append(v[1][2][0])

      ## すべてのy軸座標を取得
      list_y.append(v[1][0][1])
      list_y.append(v[1][1][1])
      list_y.append(v[1][2][1])

    ##x軸とy軸の最小と最大の座標を取得、起点の選択範囲を確定
    min_x = min(list_x)
    max_x = max(list_x)
    min_y = min(list_y)
    max_y = max(list_y)

    gap = 2 ##起点と起点の距離 
    num_dot_x = int((max_x - min_x) / gap)
    num_dot_y = int((max_y - min_y) / gap)

    for x in range(num_dot_x):
      ini_x = min_x
      ini_x += gap * x
      for y in range(num_dot_y):
        ini_y = min_y
        ini_y += gap * y
        origin_point = [ini_x, ini_y] ##起点座標
        point_support = p4s.get_mesh(origin_point, your_mesh) ##サポートの計算関数に導入
        total_support += point_support
    
    print(total_support)
    angle += 5

  endtime = datetime.datetime.now() #終了時間
  lauchtime = endtime - starttime
  print("動く時間: " + str(lauchtime) + "秒")


if __name__ == "__main__":
  filename_triangle = 'D:\\Python\\20190613\\stl_sample\\triangle.stl'
  filename_cube = 'D:\\Python\\20190613\\stl_sample\\cube.stl'
  filename_bunny = 'D:\\Python\\20190613\\stl_sample\\Bunny-LowPoly.stl'
  
  ## file
  filename = filename_bunny
  main_get_plane(filename)


#def test_for_plane():
  # list_x = []
  # list_y = []
  # list_z = []
  
  # for v in your_mesh.data:
  #   ## すべてのx軸座標を取得
  #   list_x.append(v[1][0][0])
  #   list_x.append(v[1][1][0])
  #   list_x.append(v[1][2][0])

  #   ## すべてのy軸座標を取得
  #   list_y.append(v[1][0][1])
  #   list_y.append(v[1][1][1])
  #   list_y.append(v[1][2][1])

  # ##x軸とy軸の最小と最大の座標を取得、起点の選択範囲を確定
  # min_x = min(list_x)
  # max_x = max(list_x)
  # min_y = min(list_y)
  # max_y = max(list_y)

  # gap = 2 ##起点と起点の距離 
  # num_dot_x = int((max_x - min_x) / gap)
  # num_dot_y = int((max_y - min_y) / gap)

  # total_support = 0 ## サポートの総合長さ
  # for x in range(num_dot_x):
  #   ini_x = min_x
  #   ini_x += gap * x
  #   for y in range(num_dot_y):
  #     ini_y = min_y
  #     ini_y += gap * y
  #     origin_point = [ini_x, ini_y] ##起点座標
  #     point_support = p4s.get_mesh(origin_point, your_mesh) ##サポートの計算関数に導入
  #     total_support += point_support
  
  # print(total_support)
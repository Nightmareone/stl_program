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
  origin_mesh = mesh.Mesh.from_file(filename)
  print("ファセットの数は:{}".format(len(origin_mesh)))
  

  while abs(angle) <= 360:
    your_mesh = origin_mesh
    ## 每次旋转的模型不是原来的模型，是前一次旋转过的模型*****************
    ## 角度旋转有问题
    ##===========================================
    # 角度：90
    # max_x:30.0; min_x:0.0
    # max_y:0.0; min_y:-30.0
    # num_dot_x:30; num_dot_y:30

    total_support = 0 ## サポートの総合長さ
    list_x = []
    list_y = []
    list_z = []
    
    for v in your_mesh.data:
      ## 1. 首先生成在xy平面的投影，并且
      ## すべてのx軸座標を取得
      list_x.append(v[1][0][0])
      list_x.append(v[1][1][0])
      list_x.append(v[1][2][0])

      ## すべてのy軸座標を取得
      list_y.append(v[1][0][1])
      list_y.append(v[1][1][1])
      list_y.append(v[1][2][1])

    ##x軸とy軸の最小と最大の座標を取得、起点の選択範囲を確定 (由于坐标，无法判断旋转的是否正确)
    min_x = round(min(list_x), 4)
    max_x = round(max(list_x), 4)
    min_y = round(min(list_y), 4)
    max_y = round(max(list_y), 4)

    list_x.clear()
    list_y.clear()
    print('===========================================')
    print("角度：" + str(angle))

    print("max_x:" + str(max_x) + "; min_x:" + str(min_x))
    print("max_y:" + str(max_y) + "; min_y:" + str(min_y))

    gap = 1   ##起点と起点の距離 ( 不知道STL文件的单位是多少，长度是多少)
    num_dot_x = int((max_x - min_x) / gap)
    num_dot_y = int((max_y - min_y) / gap)
    print("num_dot_x:" + str(num_dot_x) + "; num_dot_y:" + str(num_dot_y))

    # for x in range(num_dot_x):
    #   ini_x = min_x
    #   ini_x += gap * x
    #   for y in range(num_dot_y):
    #     ini_y = min_y
    #     ini_y += gap * y
    #     origin_point = [ini_x, ini_y] ##起点座標
    #     point_support = p4s.get_mesh(origin_point, your_mesh) ##サポートの計算関数に導入(问题处)
    #     total_support += point_support
    
    # print("サポートの量：" + str(total_support))
    your_mesh.rotate([0.0, 0.0, 1.0], math.radians(45)) ## 限制模型沿着y轴进行旋转
    angle += 45

  endtime = datetime.datetime.now() #終了時間
  lauchtime = endtime - starttime
  print("動く時間: " + str(lauchtime) + "秒")


if __name__ == "__main__":
  filename_triangle = 'B:\\Python\\stl_master\\stl_sample\\triangle.stl'
  filename_cube = 'B:\\Python\\stl_master\\stl_sample\\cube.stl'
  filename_bunny = 'B:\\Python\\stl_master\\stl_sample\\Bunny-LowPoly.stl'
  
  ## Sphere_file
  filename_sphere_5000 = 'B:\\Python\\stl_master\\stl_sample\\5000_polygon_sphere_100mm.STL'
  filename_sphere_300 = 'B:\\Python\\stl_master\\stl_sample\\300_polygon_sphere_100mm.STL'
  filename_sphere = 'B:\\Python\\stl_master\\stl_sample\\Sphere.stl'
  
  ## panel file
  ## このパーネルのサイズは (L)30mm * (W)30mm * (H)10mm, 位置は (x)0 * (y)0 * (z)5
  filename_panel = 'B:\\Python\\stl_master\\stl_sample\\panel.stl'


  ## file
  main_get_plane(filename_panel)

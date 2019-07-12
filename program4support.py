####################################################
###サポートの長さの計算と生成処理
####################################################
import main_stl as ms

import numpy as np
from stl import mesh
import math
from matplotlib import pyplot
from mpl_toolkits import mplot3d

## 三角形の面積を計算の和により、点が三角形の内部にあるかどうか
def check_in_triangle(v0, v1, v2, point):
  all_triangle = calculate_area(v0, v1, v2)

  triangle1 = calculate_area(v0, v1, point)
  triangle2 = calculate_area(v0, v2, point)
  triangle3 = calculate_area(v1, v2, point)
  
  sum_triangle = triangle1 + triangle2 + triangle3
  trim = 0.0001 ## 精度を考える
  if(abs(sum_triangle - all_triangle) < trim):
    return True
  else:
    return False

## 三角形の面積を計算
def calculate_area(v0, v1, v2):
  v0v1 = v1 - v0
  v0v2 = v2 - v0
  s = abs(np.cross(v0v1, v0v2)/ 2)
  return s

## メッシュを取得
## サポートを追加が必要なところのファセットデータをリストに追加する
list_mesh01 = [] ## 生成的support的list
list_z = []
def get_mesh(p, your_mesh):
  origin_point = np.array(p) ## 平面の起点のX座標とY座標
  count = 0
  for i in range(len(your_mesh.data)):
    ## 获取原始数据
    v0 = your_mesh.v0[i]
    v1 = your_mesh.v1[i]
    v2 = your_mesh.v2[i]
    normal = your_mesh.normals[i]

    ## 进行数据切割
    a = v0[:2]
    b = v1[:2]
    c = v2[:2]
    result = check_in_triangle(a, b, c, origin_point)
    if result == False:
      continue
    else:
      ## 1. 三角形和点有相交，首先生成z轴数坐标，并将x, y值和z轴值放在一起，生成list1
      ## 2. 获取交点坐在的三角形的法向量，以及三角形三点坐标list2
      ## 3. 将获得的list1，list2合并成总list放入list_mesh01
      z_result = generate_z(origin_point, normal, v0)
      list_z.append(z_result)
      array_point = np.append(origin_point, z_result)
      list_point = array_point.tolist()
      list_main = [normal.tolist(), v0.tolist(), v1.tolist(), v2.tolist(), list_point] ## 2***
      list_mesh01.append(list_main) ## 3
      count += 1
  # print("三角形の数は:{}".format(count))
  result = generate_support(list_mesh01, list_z)
  return result


## z軸データの生成
def generate_z(point, normal, v0):
  ## normalとv0 
  a = v0[0]
  b = v0[1]
  c = v0[2]

  n1 = normal[0]
  n2 = normal[1]
  n3 = normal[2]

  if (n3 != 0):
    z = (n1 * (a - point[0]) + n2 * (b - point[1])) / n3 + c
    return z
  else:
    return 0.0 ##サポートがいらない

## サポートを生成する
#############################################
###[normal.tolist(), v0.tolist(), v1.tolist(), v2.tolist(), list_point]
# 1. 法線の方向
###(1) 向上为1
###(2) 向下为0     
###2. サポートの長さ
#############################################
def generate_support(list_mesh, list_z):
  main_list = []
  for list_total in list_mesh:
    normal_z = list_total[0][2] ## 法線を取得
    point_z = list_total[4][2] ## 交差点を取得
    check_updown = 0
    if(normal_z > 0):
      check_updown = 1
    check_list = [point_z, check_updown]
    main_list.append(check_list)
  main_dict = dict(main_list)

  sorted_key = sorted(main_dict.keys())
  list_result = []
  for x in sorted_key:
    value = main_dict[x]
    new_list = [x, value]
    list_result.append(new_list)
  # print(list_result)
  
  long_support = 0
  for x in range(len(list_result) - 1):
    if(list_result[x][1] != list_result[x + 1][1]):
      long_part = abs(list_result[x][0] - list_result[x + 1][0])
      long_support += long_part
    else:
      continue
  return long_support ### サポートの長さ

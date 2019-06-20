import numpy as np
from stl import mesh
from matplotlib import pyplot
from mpl_toolkits import mplot3d

## use for checking the points in the facets
## (a, b) in XOY 
## check (a, b, c) is in the facet or not
## 主要是通过射线穿过三角形来判断
## using the algorithm of this link
## 射线和三角形的相交检测（ray triangle intersection test）
## https://www.cnblogs.com/graphics/archive/2010/08/09/1795348.
## 对向量 (n行1列 或 1行n列) 定义有长度,即 各分量的平方和 开平方
## || (1,2)^T|| = √ (1+4) = √5
def check_in_facet(a, b, c, x):
  O = np.array([a, b, 0])
  D = np.array([0, 0, c])
  v0 = np.array(x[1][0])
  v1 = np.array(x[1][1])
  v2 = np.array(x[1][1])
  
  E1 = v1 - v0
  E2 = v2 - v0
  T = O - v0
  
  P = D * E2
  Q = T * E1

  denominator = np.dot(P, E1)

  if(denominator < 0.0001):
    return False

  u = np.dot(P, T) 
  if(u < 0.0 or u > denominator):
    return False
  
  v = np.dot(Q, D)
  if(v < 0.0 or u + v > denominator):
    return False
  
  t = np.dot(Q, E2) 
  
  findet = 1.0 / denominator
  t *= findet
  u *= findet
  v *= findet
  return True

## main function
def main(filename):
  your_mesh = mesh.Mesh.from_file(filename)


  list_x = []
  list_y = []
  list_z = []

  for v in your_mesh.data:
    ## append the x vector
    list_x.append(v[1][0][0])
    list_x.append(v[1][1][0])
    list_x.append(v[1][2][0])

    ## append the y vector
    list_y.append(v[1][0][1])
    list_y.append(v[1][1][1])
    list_y.append(v[1][2][1])

    ## append the z vector
    list_z.append(v[1][0][2])
    list_z.append(v[1][1][2])
    list_z.append(v[1][2][2])

  min_x = min(list_x)
  max_x = max(list_x)
  min_y = min(list_y)
  max_y = max(list_y)
  max_z = max(list_z)

  ## check the points
  num_dot_x = int((max_x - min_x) / 2)
  num_dot_y = int((max_y - min_y) / 2)
  ini_x = min_x
  ini_y = min_y
  # print(num_dot_x)
  # print(num_dot_y)
  print(len(your_mesh))
  facet_list = []
  # the loop of checking triangle
  count = 0
  for i in range(num_dot_x):
    ini_x += 2              ##  
    for j in range(num_dot_y):
      ini_y += 2              ##
      for x in your_mesh.data: 
        in_or_not = check_in_facet(ini_x, ini_y, max_z, x)
        if(in_or_not == True):
          facet_list.append(x)
          print(str(ini_x) + "," + str(ini_y) + "," + str(len(facet_list)))
        else:
          continue
      facet_list.clear()        


if __name__ == "__main__":
  filename_cube = 'D:\\Python\\20190613\\stl_sample\\cube.stl'
  filename_bunny = 'D:\\stl_project\\Bunny-LowPoly.stl'
  # main(filename_cube)
  main(filename_bunny)

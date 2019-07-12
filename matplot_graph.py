import numpy as np 
from matplotlib import pyplot as plt 
 
x = np.arange(120, 370, 30)

filename = 'D:\\Python\\20190613\\result_data\\X.txt'
y = []
with open(filename, 'r') as file_to_read:
  while True:
    lines = file_to_read.readline()
    if not lines:
      break
    else:
      y.append(float(lines))

print(x)
print(y)

plt.rcParams["font.family"] = "IPAexGothic"
plt.title("X軸で変換する結果") 
plt.xlabel("角度") 
plt.ylabel("サポートの長さ")

plt.xticks(x)
plt.plot(x,y) 
plt.show()
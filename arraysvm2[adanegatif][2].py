#%%
import numpy as np
import pandas as pd
import math as math

x1 = [0.159,0.238,0.477,0.477,0.238,0,0,0,0,0,0]
x2 = [0.159,0.238,0,0,0.238,0.477,0,0,0,0,0]
x3 = [0.159,0,0,0,0,0,0.477,0.477,0.477,0.477,0.477]

hasil_x1x1 = np.dot(x1,x1)
hasil_x1x2 = np.dot(x1,x2)
hasil_x1x3 = np.dot(x1,x3)
hasil_x2x1 = np.dot(x2,x1)
hasil_x2x2 = np.dot(x2,x2)
hasil_x2x3 = np.dot(x2,x3)
hasil_x3x1 = np.dot(x3,x1)
hasil_x3x2 = np.dot(x3,x2)
hasil_x3x3 = np.dot(x3,x3)

##hasil
hasil = [
hasil_x1x1,
hasil_x1x2,
hasil_x1x3,
hasil_x2x1,
hasil_x2x2,
hasil_x2x3,
hasil_x3x1,
hasil_x3x2,
hasil_x3x3,
]
data = pd.DataFrame(hasil)

data
# %%
xd1 = hasil_x1x1 + hasil_x1x2 + hasil_x1x3
xd2 = hasil_x2x1 + hasil_x2x2 + hasil_x2x3
xd3 = hasil_x3x1 + hasil_x3x2 + hasil_x3x3

hasilxd = [xd1,xd2,xd3]

tampilhasilxd = pd.DataFrame(hasilxd)

tampilhasilxd


# %%
#perhitungan y
ytiyj=[[1,1,-1],[1,1,-1],[-1,-1,1]]
ytiyj
#%%
import math as math

def hitung_trans(dx,dy):
    transD = math.sqrt(((dx ** 2)+(dy ** 2)))
    if transD > 2:
        transDX = math.sqrt((dx ** 2)+(dy ** 2)) - dx + abs(dx-dy)
        transDY = math.sqrt((dx ** 2)+(dy ** 2)) - dy + abs(dx-dy)
        transHasil = [transDX,transDY]
        print(abs(dx-dy))
        return transHasil
    else:
        return [dx,dy]

transformasi = [hitung_trans(xd1,1),hitung_trans(xd2,1),hitung_trans(xd3,-1)]
transformasi

# a=math.sqrt((xd1 ** 2)+(3 ** 2)) - xd1 + abs(xd1-1)
# a

# %%
for i in range(0,3,1):
    transformasi[i].append(1)

transformasi

# %%
listHasilArrayTrans = [
    np.dot(transformasi[0],transformasi[0]),
    np.dot(transformasi[0],transformasi[1]),
    np.dot(transformasi[0],transformasi[2]),
    np.dot(transformasi[1],transformasi[0]),
    np.dot(transformasi[1],transformasi[1]),
    np.dot(transformasi[1],transformasi[2]),
    np.dot(transformasi[2],transformasi[0]),
    np.dot(transformasi[2],transformasi[1]),
    np.dot(transformasi[2],transformasi[2])
    ]

listHasilArrayTrans
# for arr in transformasi enumerate:
#     for i in range(0,3,1):
#         np.dot(arr[i][0])
#         np.dot(arr[i][1])
#         np.dot(arr[i][2])

# %%
# a1 = 3.575
# a2 = -3.126
# a3 = 0.412

a1 = 1.535
a2 = -1.037
a3 = -0.502


w1 = np.multiply(a1,transformasi[0])
w2 = np.multiply(a2,transformasi[1])
w3 = np.multiply(a3,transformasi[2])

whasil = np.add(w1,w2,w3)
# whasil
# whasil = np.add(w1,w3)
# whasil

# w2
w1

# %%

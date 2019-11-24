#%%
import numpy as np
import pandas as pd
import math as math

x1 = [0.159,0.477,0.477,0.477,0,0,0,0,0,0,0,0,0]
x2 = [0.159,0,0,0,0.477,0.477,0.477,0.477,0,0,0,0,0]
x3 = [0.159,0,0,0,0,0,0,0,0.477,0.477,0.477,0.477,0.477]
x4 = [0.159,0,0.477,0.477,0,0.477,0.477,0,0,0,0,0,0]

hasil_x1x1 = np.dot(x1,x1)
hasil_x1x2 = np.dot(x1,x2)
hasil_x1x3 = np.dot(x1,x3)
hasil_x1x4 = np.dot(x1,x4)
hasil_x2x1 = np.dot(x2,x1)
hasil_x2x2 = np.dot(x2,x2)
hasil_x2x3 = np.dot(x2,x3)
hasil_x2x4 = np.dot(x2,x4)
hasil_x3x1 = np.dot(x3,x1)
hasil_x3x2 = np.dot(x3,x2)
hasil_x3x3 = np.dot(x3,x3)
hasil_x3x4 = np.dot(x3,x4)
hasil_x4x1 = np.dot(x4,x1)
hasil_x4x2 = np.dot(x4,x2)
hasil_x4x3 = np.dot(x4,x3)
hasil_x4x4 = np.dot(x4,x4)

##hasil
hasil = [
hasil_x1x1,
hasil_x1x2,
hasil_x1x3,
hasil_x1x4,
hasil_x2x1,
hasil_x2x2,
hasil_x2x3,
hasil_x2x4,
hasil_x3x1,
hasil_x3x2,
hasil_x3x3,
hasil_x3x4,
hasil_x4x1,
hasil_x4x2,
hasil_x4x3,
hasil_x4x4,
]
data = pd.DataFrame(hasil)

data
# %%
xd1 = hasil_x1x1 + hasil_x1x2 + hasil_x1x3 + hasil_x1x4
xd2 = hasil_x2x1 + hasil_x2x2 + hasil_x2x3 + hasil_x2x4
xd3 = hasil_x3x1 + hasil_x3x2 + hasil_x3x3 + hasil_x3x4
xd4 = hasil_x4x1 + hasil_x4x2 + hasil_x4x3 + hasil_x4x4

hasilxd = [xd1,xd2,xd3,xd4]

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

transformasi = [hitung_trans(xd1,1),hitung_trans(xd2,1),hitung_trans(xd3,-1),hitung_trans(xd4,0)]
transformasi

# a=math.sqrt((xd1 ** 2)+(3 ** 2)) - xd1 + abs(xd1-1)
# a
#%%
# [3.21134431, 3.163     , 3.987     ]
# hasil 2 = [0.9475066, 0.961    , 0.961    ]
# hasil 3 = [0.5986288, 0.501    , 0.501    ]
# w = [0.5986288, 0.501]
w = [0.947, 0.961]
tuji= [1.921, 0]

hasil = np.dot(w,tuji)
hasil



# %%

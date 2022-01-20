import os.path
from multiprocessing import Pool

import numpy as np

import matplotlib.animation as ani
import matplotlib.pyplot as plt
from matplotlib import animation

# %matplotlib
# パスの確認用
drname = os.getcwd()
print("現在地:{}".format(drname))

data_set = np.loadtxt(
    # numpyで読むからCSVにはstringを入れないでね
    # debugパス
    # fname="\contents\matplo"
    fname="g.csv",
    dtype="float32",
    delimiter=",",
)
print(type(data_set))
#描画するグラフの作成
fig = plt.figure()
fig.set_size_inches(3,3)
# x y軸の作成
plt.xlim(-1, 1)
plt.ylim(-1, 1)
# グラフを入れる配列
ims = []
imsAppend = ims.append
# for文で取得と描画を行う
print("csvのデータを読み込んでいます")
for data in data_set:
    # 描画領域の作成
    im = plt.plot(data[1], data[2], marker="o", color='r')
    imsAppend(im)
    plt.cla
    # name=str(data)+".png"
    # fig.savefig(name)

print("start saving")
ani = animation.ArtistAnimation(fig, ims,interval=1,repeat=False,blit=True)
plt.show()

# ani.save("test2.mp4", writer="ffmpeg")

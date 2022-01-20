import os.path

import numpy as np

import matplotlib.animation as ani
import matplotlib.pyplot as plt
from matplotlib import animation
from numba._dispatcher import jit
import numba

# パスの確認用
drname = os.getcwd()
print("現在地:{}".format(drname))


# 描画領域の作成
fig = plt.figure()
fig.set_size_inches(5,5)


@jit
def plot(frame):
    data_set = np.loadtxt(
    # numpyで読むからCSVにはstringを入れないでね
    fname="g.csv",
    dtype="float",
    delimiter=",",
    )
    print("csvを読み込んでいます")
    for data in data_set:
        # x y軸の作成
        plt.plot(data[1], data[2], marker="o", color='r')
        plt.cla()
    print("csvの読み込みが終了しました")

ani = animation.FuncAnimation(fig,plot(1),frames=1)

ani.save("test2.mp4", writer="ffmpeg")

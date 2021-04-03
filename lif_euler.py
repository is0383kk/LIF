# LIFモデルをオイラー法によりシミュレーションによって求めるプログラム
"""
Leaky Integrate-and-fire(LIF)モデル
-定義式
\tau_m * (dV/dt) = -(V-E_l) + I(t)
V->V_reset if V - V_th
-パラメータ
tau_m = 20 [ms]
E_L = -75 [mV]
V_th = -54 [mV]
V_reset = -70 [mV]
"""

import numpy as np
import matplotlib.pyplot as plt

duration = 70
dt = 0.1 # tの刻み幅
time = int(duration/dt)

# 条件
v_reset = -70 # 初期値
v_th = -54 # 閾値
el = -75 # ELの値
tau = 20 # \tau_mの値

t = 0.0 # 時間軸の初期値
v = v_reset 

t_ISI = 0 # 発火までの時間
f = 0 # 発火率
f_list = [] # 発火率を格納するリスト
I = np.arange(0, duration, dt) # 入力(0~durationをdt刻みにした入力値)
#print(len(I))
for input_i in range(time):
    # t=0 では v=v_reset
    t = 0.0 # 時間軸の初期値
    v = v_reset 
    count_spike = 0 # 最初の発火までの時間を計測するために使用する
    spike_flag = 0 # 発火したか否かのフラグ
    for i in range(1000):
        func = (-v + el + I[input_i])/tau # dv/dt = -(V -E_L - I(t)) / \tau_m = (-v -75 +I)/20
        v = v + func * dt # オイラー法
        t = t + dt # 時刻をdt進める
        if  v_th <= v:  # 閾値を超えたらv_resetに初期化
            v = v_reset
            if count_spike == 0: # 最初の発火までの時間を計測
                t_ISI = t # 発火までの時間
                f = 1/t_ISI # 発火率
                f_list.append(f)
                count_spike = count_spike + 1
                spike_flag = 1
    if spike_flag == 0: # 発火しなかった場合，発火率を0とする
        f_list.append(0)

# グラフ
plt.plot(I, f_list, label='Sim')
plt.xlabel('I') # 横軸
plt.ylabel('F') # 縦軸
plt.legend(loc='best') # 凡例
plt.show()

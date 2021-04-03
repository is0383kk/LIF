# LIFモデルのVとTの関係グラフ化するプログラム
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

n = 1000 # ステップ数
dt = 0.1 # tの刻み幅

# 初期条件
v_reset = -70 # 初期値
v_th = -54 # 閾値
el = -75 # E_Lの値
tau = 20 # \tau_mの値

# t, v の値を格納するリスト
t_list = []
v_list = []

t = 0.0 # 時間軸の初期値
v = v_reset 

# 値を格納するリスト
t_list.append(t)
v_list.append(v)

I = 21 # Iの値（定数）.I > V_th - EL
"""
Iの値を変えるとグラフに変化が現れる
"""
spike_trig = v_th - el # 発火に必要なI=21より上
for i in range(n):
    func = (-v + el + I) / tau # dv/dt = -(V -E_L - I(t)) / \tau_m = (-v -75 +I)/20
    v = v + func * dt # オイラー法
    t = t + dt # 時刻をdt進める
    if  v_th <= v:  # 閾値を超えたらV_resetに初期化
        v = v_reset
    # v, t の格納
    t_list.append(t)
    v_list.append(v)

# グラフ
plt.plot(t_list, v_list, label='Sim')
plt.xlabel('Time') # 横軸
plt.ylabel('V') # 縦軸
plt.legend(loc='best') # 凡例
plt.show()

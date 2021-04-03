# LIFモデルをシミュレーション，解析的，近似的に解くプログラム
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
import warnings

duration = 70
dt = 0.1 # tの刻み幅
time = int(duration/dt)
warnings.simplefilter('ignore', category=RuntimeWarning) # F_0における0割りを無視するため

# 条件
v_reset = -70 # 初期値
v_th = -54 # 閾値
el = -75 # ELの値
tau = 20 # \tau_mの値

t = 0.0 # 時間軸の初期値
v = v_reset 

t_ISI = 0 # 発火までの時間
f = 0 # 発火率
fsim_list = [] # 発火率を格納するリスト
f0_list = [] # 解析解を格納するリスト
f1_list = [] # 近似解を格納するリスト
I = np.arange(0, duration, dt) # 入力(0~durationをdt刻みにした入力値)
spike_trig = v_th - el # 発火に必要なI=21より上
#print(len(I))
for input_i in range(time):
    # t=0 では v=v_reset
    t = 0.0 # 時間軸の初期値
    v = v_reset 
    count_spike = 0 # 最初の発火までの時間を計測するために使用する
    spike_flag = 0 # 発火したか否かのフラグ
    
    # F_0（解析解）
    if np.isnan(1/(tau * np.log((5-I[input_i])/(21-I[input_i])))): # NaNのときは0
        f0_list.append(0)
    else:
        f0_list.append(1/(tau * np.log((5-I[input_i])/(21-I[input_i]))))
    
    # F_1（近似解）
    f1_list.append((I[input_i]-21)/320)
    
    # F_0（シミュレーション）
    for i in range(1000):
        func = (-v + el + I[input_i])/tau # dv/dt = -(V -E_L - I(t)) / \tau_m = (-v -75 +I)/20
        v = v + func * dt # オイラー法
        t = t + dt # 時刻をdt進める
        if  v_th <= v:  # 閾値を超えたらv_resetに初期化
            v = v_reset
            if count_spike == 0: # 最初の発火までの時間を計測
                t_ISI = t # 発火までの時間
                f = 1/t_ISI # 発火率
                fsim_list.append(f)
                count_spike = count_spike + 1
                spike_flag = 1
    if spike_flag == 0: # 発火しなかった場合，発火率を0とする
        fsim_list.append(0)

# グラフ
plt.ylim(0,0.2)
plt.plot(I, fsim_list, label='F_sim') # F_sim
plt.plot(I, f0_list, label='F_0',linestyle="dashed") # F_0について
plt.plot(I, f1_list, label='F_1',linestyle = "dotted") # F_1について
plt.xlabel('I') # 横軸
plt.ylabel('f') # 縦軸
plt.legend(loc='best') # 凡例
plt.show()

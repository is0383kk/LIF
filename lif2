import numpy as np
import matplotlib.pyplot as plt


def lif(currents, time: int, dt: float = 1.0, rest=-70, th=-54, ref=3, tc_decay=20):
    """ simple LIF neuron """
    time = int(time / dt)

    # initialize
    tlast = 0  # 最後に発火した時刻
    vpeak = -40  # 膜電位のピーク(最大値)
    spikes = np.zeros(time)
    v = rest  # 静止膜電位

    monitor = []  # monitor voltage
    tlast_list = [0]
    t_ISI_rev = []
    # Core of LIF
    for t in range(time):
        dv = ((dt * t) > (tlast + ref)) * (-v -54 + currents[t]) / tc_decay  # 微小膜電位増加量
        v = v + dt * dv  # 膜電位を計算

        tlast = tlast + (dt * t - tlast) * (v >= th)  # 発火したら発火時刻を記録
        tlast_list.append(tlast)
        tlast_list = sorted(set(tlast_list))
        #print(tlast_list)
        v = v + (vpeak - v) * (v >= th)  # 発火したら膜電位をピークへ
        monitor.append(v)
        spikes[t] = (v >= th) * 1  # スパイクをセット
        
        v = v + (rest - v) * (v >= th)  # 静止膜電位に戻す
    #print("spikes",spikes)
    
    return spikes, monitor


if __name__ == '__main__':
    duration = 100  # ms
    dt = 0.1  # time step

    time = int(duration / dt)

    # Input data
    input_data_1 = 10 * np.sin(0.1 * np.arange(0, duration, dt)) + 50
    input_data_2 = -10 * np.cos(0.05 * np.arange(0, duration, dt)) - 10

    # 足し合わせ
    input_data = input_data_1 + input_data_2
    
    spikes, voltage = lif(input_data, duration, dt)

    # Plot
    #plt.subplot(2, 2, 1)
    #plt.ylabel('Input 1')
    #plt.plot(np.arange(0, duration, dt), input_data_1)

    #plt.subplot(2, 2, 2)
    #plt.ylabel('Input 2')
    #plt.plot(np.arange(0, duration, dt), input_data_2)

    plt.plot()
    plt.ylabel('Membrane Voltage')
    plt.xlabel('time [ms]')
    plt.plot(np.arange(0, duration, dt), voltage)
    plt.show()

    plt.plot()
    plt.ylabel('Output')
    plt.xlabel('time [ms]')
    plt.plot(np.arange(0, duration, dt), spikes)
    plt.show()

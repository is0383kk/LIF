# Leaky Integrate-and-fire (LIF) model Example  
## LIFモデルの定義式

<div>
	<img src='/img/equation_lif.png' width="320px">
</div>

## 問題設定
1. 各パラメータの値  
\tau_m = 20 [ms]  
E_L = -75 [mV]  
V_th = -54 [mV]  
V_reset = -70 [mV]  
2. 発火率は閾値V_thに達してから次の閾値に達するまでの時間[s]の逆数  
3. 微分方程式の解法はオイラー法を使用する  

## LIFモデルに対し一定の入力（I）を与えたときの発火率をfとしたとき，入出力曲線f=F(i)を求める
1. LIFモデルの入出力曲線をシミュレーションによって求める（lif1.py） 
<div>
	<img src='/graph/Figure_1.png'>
</div>
2. LIFモデルの入出力曲線を解析的によって求める（lif2.py） 
<div>
	<img src='/graph/Figure_1.png'>
</div>
3. LIFモデルの入出力曲線を近似解を求める（lif3.py） 
<div>
	<img src='/graph/Figure_1.png'>
</div>

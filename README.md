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
発火に必要な入力はV_th - EL = -54 + 75 = 21 以上の値が必要になる．  
(a) I=21の時の入出力曲線  
発火の閾値V_th = -54 [mV]を超えず発火していないことが分かる．  
<div>
	<img src='/graph/lif1/Figure_1.png'width="420px">
</div>
(b) I=22の時の入出力曲線  
発火の閾値V_th = -54 [mV]を超えて発火していることが分かる．  
<div>
	<img src='/graph/lif1/Figure_2.png'width="420px">
</div>
2. LIFモデルの入出力曲線を解析的(手計算)によって求める（lif2.py） 
計算過程は省略．  
結果としてf = F(I) = 1 / (20 * \log(|5-I|/|21-I|))が得られる．  
<div>
	<img src='/graph/lif2/Figure_1.png'width="420px">
</div>
3. LIFモデルの入出力曲線を近似解を求める（lif3.py） 
<div>
	<img src='/graph/lif3/Figure_1.png'width="420px">
</div>

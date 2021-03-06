# Leaky Integrate-and-fire (LIF) model Example  
## LIFモデルの定義式
[詳しい内容はここにまとめてあります](https://qiita.com/is0383kk/items/94a3b4ec14448eb2f22a)

<div>
	<img src='/img/equation_lif.png' width="320px">
</div>

## 問題設定
1. 各パラメータの値  
時刻tでの膜電位：V [mV]  
時定数：\tau_m = 20 [ms]  
静止電位：E_L = -75 [mV]  
スパイク発射のための閾値：V_th = -54 [mV]  
リセット電位：V_reset = -70 [mV]  
2. 発火率は閾値V_thに達してから次の閾値に達するまでの時間[s]の逆数  
3. シミュレーションでの微分方程式の解法はオイラー法を使用する  

## LIFモデルに対し一定の入力（I）を与えたときの発火率をfとしたとき，入出力曲線f=F(i)を求める  
### 1. LIFモデルの入出力曲線をシミュレーションによって求める  
LIFモデルの定義式をオイラー法を用いて数値的に解き入出力曲線fをグラフ化すると以下のグラフが得られる．  
<div>
	<img src='/graph/f_sim.png'width="420px">
</div>

グラフの横軸（I）に着目すると，Iが21を超えると発火していることが分かる．  
その理由は，LIFモデルが発火するのは与えるIの値がI>V_th-E_Lを満たすときのみであるからだ．  
この場合，発火に必要な入力はV_th - EL = -54 + 75 = 21 となりIが21を超過した値が与えられると発火する．  
ここで，時間ステップtと膜電位Vの関係を見てみよう．  
(a) I=21の場合  
膜電位が発火の閾値V_th = -54 [mV]を超えず発火していないことが分かる．  
<div>
	<img src='/graph/Figure_1.png'width="420px">
</div>

(b) I=22の場合  
膜電位が発火の閾値V_th = -54 [mV]を超えて発火していることが分かる．  
発火後，膜電位は初期値に戻る．  
<div>
	<img src='/graph/Figure_2.png'width="420px">
</div>

### 2. LIFモデルの入出力曲線を解析的(手計算)によって求める  
計算過程は[ここ](https://qiita.com/is0383kk/items/94a3b4ec14448eb2f22a#lif%E3%83%A2%E3%83%87%E3%83%AB%E3%82%92%E8%A7%A3%E6%9E%90%E7%9A%84%E3%81%AB%E8%A7%A3%E3%81%8F)に記述．  
結果としてf = F(I) = 1 / (20 * \log(|5-I|/|21-I|))が得られ，これをグラフ化すると以下のグラフとなる．
<div>
	<img src='/graph/f_0.png'width="420px">
</div>

### 3. LIFモデルの入出力曲線を近似解を求める  
f = F(i)の解析解はIが十分大きい際，Iの一次関数として近似可能である．今回の場合は，I=21以上の際にLIFモデルが発火するため，I=21以上のIが与えられると近似可能である．  
近似後のfはf = F(I) = (I + E_L L V_th) / (\tau_m*(V_th-V_reset))として定義されることが知られている．

<div>
	<img src='/graph/f_1.png'width="420px">
</div>

### 各グラフを重ねて可視化した図  
F_simがシミュレーションでのグラフ．F_0が解析解でのグラフ．F_1が近似解でのグラフを表す．
<div>
	<img src='/graph/Figure_5.png'width="420px">
</div>

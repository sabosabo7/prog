#### 第3章　基本的なデータ分析

### ３．２　代表値（基本統計量）

# サンプルデータの生成
data <- c(1,1,2,3,4,5,5,5,6,6,6,7,7,7,7,7,8,9,10,10,80)

# 平均、中央値、最頻値
mean(data)     # 平均
median(data)   # 中央値
table(data)    # table関数で集計表を作成し、一番多いものが最頻値

# 分散、標準偏差
var(data)      # 分散（不偏分散）
sd(data)       # 標準偏差（不偏標準偏差）

# 最大値、最小値、範囲、合計
max(data)      # 最大値
min(data)      # 最小値
range(data)    # 範囲
sum(data)      # 合計

# クォンタイル点
quantile(data) # 四分位数の確認が可能
summary(data)  # 四分位数に加え、平均値も同時に確認可能


### ３．４　グラフの作成

## ▼Rを使用した棒グラフの作成
data=c(5,10,20,40,80)
barplot(data,main="BarPlot",xlab="name",ylab="value",col="darkblue",horiz=T, names.arg=c("a","b","c","d","e"))

# 店舗ごとの売上を、年代別に積み上げた棒グラフとして描画

s2 <- matrix(c(21, 20, 10, 5, 20, 18, 7, 3, 31, 25, 14, 8, 17, 12, 8, 2), ncol=4, nrow=4)
barplot(s2)

# 年代別の売上を、それぞれ棒グラフとして横に並べる

barplot(s2, beside=TRUE)

# 1列だけの行列を対象にすれば、帯グラフが描画可能

a <- c(21, 20, 10, 5)		# A店の売上を対象
s3 <- as.matrix(a / sum(a) * 100)	# 値を％に換算して行列に変換
barplot(s3, horiz=TRUE)		# 横向きの棒グラフ(帯グラフ)


## ▼Rを使用した折れ線グラフの作成

# データの生成
s <- ts(c(89, 102, 154, 182, 201, 173, 132, 179, 211, 249, 321, 372), start=1, end=12, frequency=1)

# グラフの描画
plot(s, xaxt="n", xaxp=c(1, 12, 11))       # X軸の目盛りを表示せず、X軸の両端の値を1、12にする
axis(side=1, at=1:12, labels=c(4:12, 1:3)) # X軸の1～12に、ラベル 4,5,6,...12,1,2,3 を割り当てる



## ▼Rを使用したヒストグラムの作成

# アメリカの都市の年間降水量のデータの先頭を確認
head(precip, n = 3) 

# ヒストグラムの描画
hist(precip,col="orange") 



## ▼Rを使用した散布図の作成

# carsデータの初めの3件を表示
head(cars,n=3)  
x <- cars[,1]　　# x軸用に車の速度を代入
y <- cars[,2]　　# y軸用に停止時間を代入

# plot関数で可視化
plot(x, y, xlab = "speed", ylab = "dist") 

# 下記でもOK
plot(cars)



## ▼Rを使用した円グラフの作成

# データの生成
s <- c("不可"=15, "可"=38, "良"=45, "優"=25)

# 円グラフの描画

# Macを使用していて日本語が化ける場合は下の行のコメントを外して実行してみてください。
# フォントは必要に応じて変更してください。
# 下記の""で囲まれたフォント名を　システム＞ライブラリ＞Fonts＞日本語のフォントを選択＞詳しい情報＞一般情報の中の「フルネーム」からコピー＆ペーストでOK
# 他のplotで文字化けした場合も、同じ対応をしてください。
# 毎回plotの文字化け対応をしたくない方は、インターネットで方法を調べてみましょう。

# par(family="Hiragino Kaku Gothic ProN W3")
pie(s)

# オプションを設定した円グラフの描画

# par(family="Hiragino Kaku Gothic ProN W3")
pie(s, clockwise=FALSE, init.angle=90, main="反時計回り 90度")




## ▼Rを使用した箱ひげ図の作成

# データのインポート、確認
#フォルダの格納場所に応じて、適宜変更してください。
setwd("c:/kda/text")
s <- read.table("score.csv", header=TRUE, sep=",",fileEncoding="SHIFT-JIS")
head(s, n=5)

# クラス１のみの箱ひげ図
s2 <- as.vector(s[s[,1] == 1, 2])	# クラス"1"の成績のみを抽出
boxplot(s2)

# 3クラス分同時に描画
# par(family="Hiragino Kaku Gothic ProN W3")
boxplot(成績 ~ クラス, data=s, boxwex=0.5,names=c("1クラス", "2クラス", "3クラス"), col=c("pink","skyblue","orange"))

# 【参考】beeswarmパッケージを使用すると、データの分布状況が確認可能
install.packages("beeswarm")
library(beeswarm)
beeswarm(成績 ~ クラス, data=s, add=TRUE, col="black")








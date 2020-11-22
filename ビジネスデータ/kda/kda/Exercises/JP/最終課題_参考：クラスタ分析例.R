# ■「訪日外国人消費動向調査」を使用したクラスター分析（例）■
# 簡易的な説明のためのクラスター分析スクリプトです。
# データや項目などを色々と変更して試行錯誤してみてください。

### 参考：クラスター分析

## 大項目での分析
# 階層的クラスター分析

# データのインポート
setwd("c:/kda/Exercises/JP")
jp <- read.csv("2018_国ごとの支出_大項目_T.csv",header=T,row.names=1,fileEncoding="SHIFT-JIS")

# 距離の算出
(y <- dist(jp))

# クラスタリング＆図示化
# par(family="Hiragino Kaku Gothic ProN W3") # Macの方用
plot(hclust(y,method="centroid"))

# 非階層的クラスター分析
jp <- read.csv("2018_国ごとの支出_大項目_T.csv",header=T,row.names=1,fileEncoding="SHIFT-JIS")

# クラスタリング(k-means法、クラスタ３）
c1 <- kmeans(jp,centers=3) 

# 棒グラフで可視化
barplot(c1$centers,beside=TRUE,col=c("blue","pink","orange"),legend=TRUE)



## 小項目での分析

# データのインポート
jp2 <- read.csv("2018_国ごとの支出_小項目_T.csv",header=T,row.names=1,fileEncoding="SHIFT-JIS")


(y <- dist(jp2))

plot(hclust(y,method="centroid"))

# 3クラスタ
jp2
(c2 <- kmeans(jp2,centers=3)) 

barplot(c2$centers,beside=TRUE,col=c("blue","pink","orange"),legend=TRUE)

# 5クラスタ
jp2
(c3 <- kmeans(jp2,centers=5)) 

barplot(c3$centers,beside=TRUE,col=c("blue","pink","orange","green","red"),legend=TRUE)




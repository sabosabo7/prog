#### 第3章　基本的なデータ分析　演習問題解答例

# データのインポート
setwd("c://kda/text")
x <- read.csv("prac3.csv",fileEncoding="SHIFT-JIS")

# データの概要確認
head(x)
dim(x)
 
# 代表値の確認
summary(x)
                   
range(x$プログラム);range(x$NW);range(x$DB);range(x$OS);range(x$統計)
colSums(x2<- x[,-1])  # 列値の合計
sd(x$プログラム);sd(x$NW);sd(x$DB);sd(x$OS);sd(x$統計)
var(x$プログラム);var(x$NW);var(x$DB);var(x$OS);var(x$統計)

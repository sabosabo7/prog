#### 第4章　相関分析　演習問題解答例

### ４．２　相関係数の算出

## １対１の関係性

# データの読み込み、確認
setwd("c:/kda/text")
x <- read.csv("prac4.csv",fileEncoding="SHIFT-JIS")
head(x)

# 必要部分のみを抽出、格納
x2 <- x[,c(2,3)]
head(x2)

# 相関係数の算出（列名を指定）
cor(x2$つぶやき数,x2$売上,method="pearson")

# 相関係数の算出（データフレームごと算出）
cor(x2)



## 多対多の関係性

# データの読み込み、確認
x <- read.csv("prac4-2.csv",fileEncoding="SHIFT-JIS")
head(x)

# x2にxの全行、1列目以外を代入
x2 <- x[,-1] 

# x2の全変数間で相関係数を算出
cor(x2) 

# pairs関数で散布図行列を作成することも可能
pairs(x2)   





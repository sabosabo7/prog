#### 第5章　回帰分析、判別分析　演習問題解答例

### ５．１　回帰分析

## データのインポート、確認
x <- read.csv("prac4.csv",fileEncoding="SHIFT-JIS")
head(x)

res<-lm(売上~つぶやき数,data=x)  # 変数resに分析結果を代入
summary(res)                     # summary関数で内容を確認

plot(x$つぶやき数,x$売上)
abline(res,col="red")



### オプション解答例

# データのインポート、確認
x <- read.csv("prac4-2.csv",fileEncoding="SHIFT-JIS")
head(x)

# x2にxの全行、1列目以外を代入
x2 <- x[,-1] 

# x2の全変数間で相関係数を算出
cor(x2) 

# pairs関数で散布図行列を作成することも可能
pairs(x2)   

# 関係性の強い変数を使ってモデルを作成
res <- lm(Sales~TW_Bigdata+AC_Bigdata+Age,data=x2)

# summary関数で内容を確認
summary(res)


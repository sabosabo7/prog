# ■「訪日外国人消費動向調査」を使用した相関分析（例）■
# 簡易的な説明のためのスクリプトです。
# データや項目などを色々と変更して試行錯誤してみてください。
# もちろん、相関分析以外の分析手法を使用していただいても構いません！

# ディレクトリの指定
setwd("c:/kda/Exercises/JP")
jp <- read.csv("2018_国ごとの支出_大項目_T.csv",header=T,fileEncoding="SHIFT-JIS")

# データの確認
head(jp)
nrow(jp)
ncol(jp)

# 相関係数の算出
(res <- cor(jp[,-1]))

# 出てきた相関係数から何が読み取れるか？
# 出てきた結果をアクションプランに反映できるか？
# 別データを使用してもっと深掘りできるか？


# 相関行列のプロットをしたい場合は、様々なパッケージが用意されているので
# 調べて使用しても良い。

### 今回の例でプロットを行う場合は下記のinstall.packages以降を実行
### ミラーサイトは適宜選択すること（不明点は質問してください）
## corrplot使用例
# install.packages("corrplot")
# library(corrplot)

# par(family="Hiragino Kaku Gothic ProN W3") # Macの方用
# corrplot(res, method="shade", shade.col=NA)

## psych使用例
# install.packages("psych")
# library(psych)
# par(family="Hiragino Kaku Gothic ProN W3") # Macの方用
# cor.plot(res)







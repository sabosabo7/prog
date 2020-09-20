# ■ECサイトのユーザー属性データを使用したロジスティック回帰分析（例）■
# 簡易的な説明のためのスクリプトです。
# 下記では「サブスクC契約有無」列を目的変数としてモデルを作成しています（精度はよくありません）
# 
# 目的変数を何に設定するか？指標の値を改善するためにはどうするか？試行錯誤してみてください。
# 本データにロジスティック回帰を使うことが正解、という訳でもありません。
# 何をしたいのか？という目的の設定から考えてみましょう。

# ディレクトリの指定
setwd("c:/kda/Exercises/EC")
EC <- read.csv("EC.csv",header=T,fileEncoding="SHIFT-JIS")

# データの確認
head(EC)
nrow(EC) # データ件数：2151件
ncol(EC) # 27列
colnames(EC)

# ランダムにサンプルを抽出
# set.seed(X)　←　Xの値を変えることにより、データ変更が可能
set.seed(7) ; s <- sample(1:2151,size=300) 

# ランダムに設定した値の確認
s

# 訓練用データセット「dt_m」の作成
dt_m <- EC[-s, ];nrow(dt_m) 
head(dt_m)
nrow(dt_m) # データ件数確認

# テスト用データセット「dt_p」の作成
dt_p <- EC[s, ];nrow(dt_p)
head(dt_p)
nrow(dt_p) # データ件数確認

# 下記では「サブスクC契約有無」列を目的変数としてモデルを作成する
# （演習時は必要に応じて列の追加や削除を行うこと）
judge.glm <- glm(サブスクC契約有無 ~.,family = binomial, data = dt_m)

# 分析結果の確認
summary(judge.glm)

# ステップワイズを使用して説明変数を探る場合
# 「目的変数~.」の「.」は、データセット中の目的変数以外、という指定方法
judge.glm <- step(judge.glm <- glm(サブスクC契約有無 ~ . , family = binomial, data = dt_m ))

# 分析結果の確認
summary(judge.glm)

# 上記で出てきた内容をベースに変数を検討するという考え方もあり


# 係数の対数変換
round(exp(judge.glm$coefficients),2)

# テストデータを使用し、結果を2値で予測
(res <- round(predict(judge.glm, newdata = dt_p, type="response")))

# テストデータを使用し、結果をパーセンテージで予測
(conf <- round(predict(judge.glm, newdata = dt_p, type="response")*100))

# テストデータに予測結果、パーセンテージを付与
(ALL <- transform(dt_p,PREDICT=res)) 
# サブスクC契約有無とPREDICT列のみ取り出し
(ALL <- ALL[c(13,28)])
# 上記にパーセンテージ列を追加
(ALL <- transform(ALL,パーセンテージ=conf))

# 混同行列の作成＆結果が見やすいように行列の入れ替え
(cm <- table(ALL$PREDICT,ALL$サブスクC契約有無)) # 行：予測値 / 列：正解値　
(cm2 <- cm[,c(2,1)])     # 列入れ替え
(cm3 <- cm2[c(2,1),])    # 行入れ替え

# 指標の計算
cm3.accuracy <- sum(diag(cm3)) / sum(cm3) # 正解率
cm3.recall <- cm3[1,1] / (cm3[1,1] + cm3[2,1]) # 再現率
cm3.precision <- cm3[1,1] / (cm3[1,1] + cm3[1,2]) # 適合率
cm3.Fnum <- (2 * cm3.recall * cm3.precision) /
(cm3.recall + cm3.precision)       # F値
(cm3.resall <- data.frame("指標" =c("正解率","再現率","適合率","F値"),"値"=c(cm3.accuracy,cm3.recall,cm3.precision,cm3.Fnum))) 

# 結果を確認し、分析結果が妥当かどうかを判断する。
# 指標の結果は？係数は？使用した説明変数は妥当か？（分析視点）
# 出てきた結果をアクションプランに反映できるか？（ビジネス視点）

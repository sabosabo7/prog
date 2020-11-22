#### 第5章　回帰分析、判別分析

### ５．１　回帰分析

## 単回帰分析
# データのインポート、確認
head(cars)
plot(cars)

# 単回帰分析を実行し、変数resに分析結果を代入
res<-lm(dist~speed,data=cars)  

# summary関数で内容を確認
summary(res)                     

# 分析結果の可視化

abline(res,col="red")


## 重回帰分析
# データの読み込み、確認
head(trees)

res <- lm(Volume ~ Girth + Height, data = trees)

summary(res)




### ５．２　判別分析（ロジスティック回帰分析）

# データのインポート、確認
setwd("c://kda/text")
judge <- read.table("judge.csv", header = T, sep = ",",fileEncoding="SHIFT-JIS")
head(judge)
dim(judge)

# 訓練データの生成の準備
set.seed(4); s <- sample(1:200, size = 150)

# ロジスティック回帰の実行
judge.glm <- glm(合否 ~ 国語 + 数学 + 英語 + 理科 + 社会 + 部活動 + 性別, 
family = binomial, 
data = judge[s, ])

# ステップワイズ法の実行
step(judge.glm)

judge.glm <- glm(合否 ~ 国語 + 数学 + 英語 + 社会 + 部活動 , family = binomial, data = judge[s, ])

# モデルの確認
summary(judge.glm)
judge.glm$coefficients

round(exp(judge.glm$coefficients),2)
(res <- round(predict(judge.glm, newdata = judge[-s,], type="response")))

# 予測結果の確認
judge.ALL <- transform(judge[-s,],PREDICT=res) 
head(judge.ALL)

# 混同行列の作成
(cm <- table(judge.ALL$PREDICT,judge.ALL$合否)) # 列：正解値　行：予測値
(cm2 <- cm[,c(2,1)])     # 列入れ替え
(cm3 <- cm2[c(2,1),])    # 行入れ替え

# 指標の計算
cm3.accuracy <- sum(diag(cm3)) / sum(cm3) # 正解率
cm3.recall <- cm3[1,1] / (cm3[1,1] + cm3[2,1]) # 再現率
cm3.precision <- cm3[1,1] / (cm3[1,1] + cm3[1,2]) # 適合率
cm3.Fnum <- (2 * cm3.recall * cm3.precision) /
(cm3.recall + cm3.precision)       # F値
(cm3.resall <- data.frame("指標" =c("正解率","再現率","適合率","F値"),
"値"=c(cm3.accuracy,cm3.recall,cm3.precision,cm3.Fnum))) 

﻿#### 第4章　相関分析

### ４．２　相関係数の算出

## １対１の関係性

# P53計算例と同データを使用した算出結果
# データフレームの定義
(df <- data.frame("アクセス数" = c(9,30,11,35,9,7,4,48,45), 
                  "販売数" = c(4,5,11,6,2,8,4,7,15)))

# 相関係数の算出
cor(df)

# P54 Rでの分析例
# データの読み込み、確認
head(cars)

# 相関係数の算出（列名を指定）
cor(cars$dist,cars$speed,method="pearson")

# 相関係数の算出（データフレームごと算出）
cor(cars)

# 散布図の描画
plot(cars)


## 多対多の関係性

# データの読み込み、確認
head(trees)

# treesの全変数間で相関係数を算出
cor(trees) 

# pairs関数で散布図行列を作成することも可能
pairs(trees)   





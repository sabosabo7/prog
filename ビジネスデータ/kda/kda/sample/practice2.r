﻿# データフレームの定義
(a <- data.frame("製品" = c("テレビ","冷蔵庫","洗濯機"), "単価" = c(20,10,15), "販売数" = c(1000, 400, 350)))

# 要素の参照
a[1, 1]   # 1行目、1列目のデータを取得する
a[ , 2]   # 全行、2列目のデータを取得する

# データフレームに新規列を追加する
(a <- data.frame("製品" = c("テレビ","冷蔵庫","洗濯機"), "単価" = c(20,10,15),"販売数" = c(1000, 400, 350)))
(b <- c("AAA","BBB","CCC"))
(c <- transform(a,"追加列"=b))

# 作業ディレクトリの変更、確認
setwd("c:/kda/sample/")  # 作業ディレクトリの設定
getwd()          # 作業ディレクトリの確認

# データフレーム内のファイル出力
write.table(c,file="output.txt",quote=F,sep=",",row.names = F,col.names = T)


### 下記、テキスト未掲載（オマケ）
# Windowsの場合は、下記のような形でクリップボードの中身を簡単にインポート可能
# Excelなどでザックリデータを準備して、そのままインポートして簡易分析をすることもできます。

x <- read.table("clipboard",header=T)

# Mac、Linuxの場合はやり方が変わってくるので、使いたい場合は調べてみてください。


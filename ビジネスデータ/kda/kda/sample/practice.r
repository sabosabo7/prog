#演習問題１

#作業ディレクトリの指定
#フォルダの格納場所に応じて、適宜変更してください。
setwd("C:\Users\sabosabo\Documents\prog\ビジネスデータ\kda\kda\sample")
getwd()

#ファイルの読み込み
ds<-read.csv("jinkou.csv",header=T,fileEncoding="SHIFT-JIS")

#データの確認
ds
head(ds)
tail(ds)

#年の範囲を確認
range(ds$year)

#男性の人口
male<-ds$tokyo_m+ds$aichi_m+ds$osaka_m+ds$fukuoka_m
male
#平均
mean(male)

#女性の人口
female<-ds$tokyo_f+ds$aichi_f+ds$osaka_f+ds$fukuoka_f
female
#平均
mean(female)

#男女の人口合計
t1<-male+female

#合計人口数の推移をプロット
plot(ds$year,t1,type="l",xlab="年",ylab="人口")



# Macを使用していて日本語が化ける場合は下の行（par～）のコメントを外して実行してみてください。
# フォントは必要に応じて変更してください。
# 下記の""で囲まれたフォント名を　システム＞ライブラリ＞Fonts＞日本語のフォントを選択＞詳しい情報＞一般情報の中の「フルネーム」からコピー＆ペーストでOK
# 他のplotで文字化けした場合も、同じ対応をしてください。
# 毎回plotの文字化け対応をしたくない方は、インターネットで方法を調べてみましょう。

# par(family="Hiragino Kaku Gothic ProN W3")
plot(ds$year,t1,type="l",xlab="年",ylab="人口")


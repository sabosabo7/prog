# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # ImageDataGeneratorを用いたデータ拡張
# https://keras.io/preprocessing/image/

# %%
import numpy as np
from PIL import Image
from keras.preprocessing.image import ImageDataGenerator
import os 

# %% [markdown]
# ## numpy形式の画像を拡張する場合

# %%
def onehot_to_str(label):
    """
    ワンホットベクトル形式のラベルをカタカナ文字に変換する
    """
    dic_katakana = {"a":0,"i":1,"u":2,"e":3,"o":4,"ka":5,"ki":6,"ku":7,"ke":8,"ko":9,"sa":10,"si":11,"su":12,"se":13,"so":14}
    label_int = np.argmax(label)
    for key, value in dic_katakana.items():
        if value==label_int:
            return key
    

# 画像読み込み
data = np.load("../../../../DAY1/DAY1_vr6_0_0/DAY1_vr6_0_0/4_kadai/1_data/train_data.npy")  # パスは適宜変更すること
data = data[:1]
label = np.load("../../../../DAY1/DAY1_vr6_0_0/DAY1_vr6_0_0/4_kadai/1_data/train_label.npy")  # パスは適宜変更すること
label = label[:1]
label = onehot_to_str(label)
        
# 軸をN,H,W,Cに入れ替え
data = data.transpose(0,2,3,1)

# ImageDataGeneratorのオブジェクト生成
datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

# 生成後枚数
num_image = 3

# 生成
g = datagen.flow(data, batch_size=1, save_to_dir="../1_data/imagedatagenerator/",
                 save_format='png', save_prefix='out_%s_from_npy_'%label)
for i in range(num_image):
        batches = g.next()
        print(batches.shape)

# %% [markdown]
# ## pngの画像を拡張する場合

# %%



# %%
# 元画像
fname = "../1_data/imagedatagenerator/a_201.png"
pixel = 28

# numpy形式に変換
num_image = 1 # 画像枚数
channel = 1 # グレースケール
data = np.empty((num_image, channel, pixel, pixel)) # 配列初期化

# 画像読み込み
img_ = Image.open(fname)
img_ = np.array(img_).astype(np.float32)
data[0, 0, :] = img_

# 軸をN,H,W,Cに入れ替え
data = data.transpose(0,2,3,1)

# ImageDataGeneratorのオブジェクト生成
datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

# 生成後枚数
num_image = 3

# 生成
g = datagen.flow(data, batch_size=1, save_to_dir="../1_data/imagedatagenerator/", save_format='png', save_prefix='out_a_from_png_')
for i in range(num_image):
        batches = g.next()
        print(batches.shape)


# %%

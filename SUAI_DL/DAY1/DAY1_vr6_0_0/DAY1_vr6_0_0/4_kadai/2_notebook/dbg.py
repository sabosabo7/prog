# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # 学習方法の例

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from common.layers import *
from sklearn.model_selection import train_test_split
from common.optimizer import *
import pickle
import sklearn.preprocessing as sp
from model import SimpleConvNet, TwoConvNet,DeepConvNet

# %% [markdown]
# ## データを読む1

# %%
raw_data = np.load("../1_data/train_data.npy")
raw_label = np.load("../1_data/train_label.npy")
raw_data = raw_data[:raw_data.shape[0]//1000*1000]
raw_label = raw_label[:raw_label.shape[0]//1000*1000]
print("raw_data.shape=", raw_data.shape)
print("raw_label.shape=", raw_label.shape)
# 正規化
raw_data = (raw_data - raw_data.min()) / raw_data.max()
raw_data = raw_data.astype('float32')


# %%
train_data = np.load("../1_data/integ_data7.npy")
train_label = np.load("../1_data/integ_label7.npy")
train_data = train_data[:train_data.shape[0]//1000*1000]
train_label = train_label[:train_label.shape[0]//1000*1000]
print("train_data.shape=", train_data.shape)
print("train_label.shape=", train_label.shape)

train_data = (train_data - train_data.min()) / train_data.max()
train_data = train_data.astype('float32')


# %%
# 配列形式変更
train_data = train_data.reshape(-1, 28*28)
print("train_data.shape=", train_data.shape)

# %% [markdown]
# ## trainとtestに分割する

# %%
X_train, X_test, y_train, y_test = train_test_split(train_data, train_label,test_size=0.3, random_state=1234, shuffle=True)

print(X_train.shape, X_test.shape)


# %%
X_train = X_train.reshape(-1,1,28,28)
X_test = X_test.reshape(-1,1,28,28)
train_data = train_data.reshape(-1,1, 28,28)


# %%
print(X_train.shape, X_test.shape)

# %% [markdown]
# ## 学習

# %%
def save_pickle(i):
    with open("katakana_modeltwo_d70_ep"+str(i)+"_w.pickle", "wb") as f:
        pickle.dump(tnet.params, f)

    c={
        "Batch1":[tnet.layers["Batch1"].moving_mean,tnet.layers["Batch1"].moving_var],
        "Batch2":[tnet.layers["Batch2"].moving_mean,tnet.layers["Batch2"].moving_var],
        "Batch3":[tnet.layers["Batch3"].moving_mean,tnet.layers["Batch3"].moving_var]
    }
    with open("katakana_modeltwo_d70_ep"+str(i)+"_c.pickle", "wb") as f:
        pickle.dump(c, f)


# %%
def calc_loss_acc(d,l,model): 
    data_size = len(d)
    batch_size = 1000
    minibatch_num = np.ceil( data_size / batch_size).astype(int) 
    li_loss = []
    li_accuracy = []
    li_num = []
    index = np.arange(data_size)
    
    for mn in range(minibatch_num):
        # print(mn)
        mask = index[batch_size*mn:batch_size*(mn+1)]        
        data = d[mask]
        label = l[mask]
        loss = model.loss(data, label,train_flg=False)
        accuracy=model.accuracy(data, label,batch_size=batch_size)
        # print(loss, accuracy)
        
        li_loss.append(loss)
        li_accuracy.append(accuracy)
        li_num.append(len(data))

    ave_loss = np.dot(li_loss, li_num) / np.sum(li_num)
    print('loss:', ave_loss)
    ave_accuracy = np.dot(li_accuracy, li_num) / np.sum(li_num)
    print('accuracy:', ave_accuracy)
    return ave_loss,ave_accuracy


# %%
tnet = DeepConvNet(input_dim=(1, 28, 28), hidden_size=100, output_size=15, weight_init_std=0.01)


# %%
for l in tnet.layers.keys():
    print(l)
print()
for p in tnet.params.keys():
    print(p+"\t "+str(tnet.params[p].shape))


# %%
train_loss = []
test_loss = []
train_accuracy = []
test_accuracy = []
optimizer = RMSProp(lr=0.01, rho=0.9)
epoch=0


# %%
# epochs = 10
batch_size = 100

# 繰り返し回数
xsize = X_train.shape[0]
iter_num = np.ceil(xsize / batch_size).astype(np.int)
# 2層NNのオブジェクト生成


epochs=1
while epoch<epochs:
    print("epoch=%s"%epoch)
    
    # シャッフル
    idx = np.arange(xsize)
    np.random.shuffle(idx)

    for it in range(iter_num):
        """
        ランダムなミニバッチを順番に取り出す
        """
        print("it=", it)
        mask = idx[batch_size*it : batch_size*(it+1)]
    
        # ミニバッチの生成
        x_ = X_train[mask]
        y_ = y_train[mask]
        
        # 勾配の計算
        grads = tnet.gradient(x_, y_)

        # パラメータの更新
        optimizer.update(tnet.params, grads)

    ## 学習経過の記録
    
  
    # # 訓練データにおけるloss,acc
    # print("###  train  ###")
    # loss,acc=calc_loss_acc(X_train,y_train,tnet)
    # train_loss.append(loss)
    # train_accuracy.append(acc)
    # print()
    # # テストデータにおけるloss,acc
    # print("###  test  ###")
    # loss,acc=calc_loss_acc(X_test,y_test,tnet)
    # test_loss.append(loss)
    # test_accuracy.append(acc)

    
    # save_pickle(epoch)
    
    if test_accuracy[-1]==1:
        break
    epoch+=1


# %%
plt.plot(test_loss,label="test")
plt.plot(train_loss,label="train")
plt.legend()
plt.ylim([0,0.2])


# %%
plt.plot(test_accuracy,label="test")
plt.plot(train_accuracy,label="train")
plt.legend()
plt.ylim([0.95,1])

# %% [markdown]
# ## 学習済みモデルの復元

# %%
with open("katakana_modeltwo_d50_ep6_w.pickle", "rb") as f:
    w=pickle.load(f)
with open("katakana_modeltwo_d50_ep6_c.pickle", "rb") as f:
    c=pickle.load(f)


# %%
tnet2=TwoConvNet(input_dim=(1, 28, 28),param=w,const=c)


# %%
tnet2.layers["Batch1"].moving_mean


# %%
def _check_fail(x,y,t,cnt):
    kana=["a","i","u","e","o","ka","ki","ku","ke","ko","sa","si","su","se","so"]
    for _x,_y,_t in zip(x,y,t):
        __t,__y=np.argmax(_t),np.argmax(_y)
        if __y!=__t:
            cnt+=1
            print("cnt:",cnt,"label:",kana[__t],"pre:",kana[__y])
            plt.imshow(_x[0,:,:],cmap="gray")
            plt.show()
    return cnt

def check_fail(x,t,m):
    index = np.arange(x.shape[0])
    cnt=0
    for i in range(x.shape[0]//1000):
        print("No.",i*1000,"~")
        mask=index[i*1000:(i+1)*1000]
        _x=x[mask]
        _t=t[mask]
        _pre_x=m.predict(_x,train_flg=False)
        cnt=_check_fail(_x,_pre_x,_t,cnt)
        if cnt>100:
            break


# %%
check_fail(train_data,train_label,tnet2)


# %%

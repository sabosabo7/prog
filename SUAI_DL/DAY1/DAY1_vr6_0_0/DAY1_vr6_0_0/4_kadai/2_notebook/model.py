import numpy as np
import cupy as cp
from common.layers import *
from sklearn.model_selection import train_test_split
from common.optimizer import *


class SimpleConvNet:
    def __init__(self, input_dim=(1, 28, 28), param=None,const={"Batch1":[None,None],"Batch2":[None,None]},
                 conv_param={'filter_num':30, 'filter_size':5, 'pad':0, 'stride':1},
                 pool_param={'pool_size':2, 'pad':0, 'stride':2},
                 hidden_size=100, output_size=15, weight_init_std=0.01):
        """
        input_size : tuple, 入力の配列形状(チャンネル数、画像の高さ、画像の幅)
        conv_param : dict, 畳み込みの条件
        pool_param : dict, プーリングの条件
        hidden_size : int, 隠れ層のノード数
        output_size : int, 出力層のノード数
        weight_init_std ： float, 重みWを初期化する際に用いる標準偏差
        """
                
        filter_num = conv_param['filter_num']
        filter_size = conv_param['filter_size']
        filter_pad = conv_param['pad']
        filter_stride = conv_param['stride']
        
        pool_size = pool_param['pool_size']
        pool_pad = pool_param['pad']
        pool_stride = pool_param['stride']
        
        input_size = input_dim[1]
        conv_output_size = (input_size + 2*filter_pad - filter_size) // filter_stride + 1 # 畳み込み後のサイズ(H,W共通)
        pool_output_size = (conv_output_size + 2*pool_pad - pool_size) // pool_stride + 1 # プーリング後のサイズ(H,W共通)
        pool_output_pixel = filter_num * pool_output_size * pool_output_size # プーリング後のピクセル総数
        
        # 重みの初期化
        if param==None:
            self.params = {}
            std = weight_init_std
            self.params['W1'] = std * cp.random.randn(filter_num, input_dim[0], filter_size, filter_size) # W1は畳み込みフィルターの重みになる
            self.params['b1'] = cp.zeros(filter_num) #b1は畳み込みフィルターのバイアスになる
            self.params['W2'] = std *  cp.random.randn(pool_output_pixel, hidden_size)
            self.params['b2'] = cp.zeros(hidden_size)
            self.params['W3'] = std *  cp.random.randn(hidden_size, output_size)
            self.params['b3'] = cp.zeros(output_size)
            self.params["gamma1"]=cp.ones(filter_num)
            self.params["beta1"]= cp.zeros(filter_num)
            self.params["gamma2"]=cp.ones(hidden_size)
            self.params["beta2"]= cp.zeros(hidden_size)
        else:
            self.params=param
    
        # レイヤの生成
        self.layers = OrderedDict()
        self.layers['Conv1'] = Convolution(self.params['W1'], self.params['b1'],
                                           conv_param['stride'], conv_param['pad']) # W1が畳み込みフィルターの重み, b1が畳み込みフィルターのバイアスになる
        self.layers["Batch1"] = BatchNormalization(self.params["gamma1"],self.params["beta1"],moving_mean=const["Batch1"][0],moving_var=const["Batch1"][1])
        self.layers['ReLU1'] = ReLU()
        self.layers['Pool1'] = MaxPooling(pool_h=pool_size, pool_w=pool_size, stride=pool_stride, pad=pool_pad)
        # self.layers["Drop1"]=Dropout(0.3)
        self.layers['Affine1'] = Affine(self.params['W2'], self.params['b2'])
        self.layers["Batch2"] = BatchNormalization(self.params["gamma2"],self.params["beta2"],moving_mean=const["Batch2"][0],moving_var=const["Batch2"][1])
        self.layers['ReLU2'] = ReLU()
        self.layers['Affine2'] = Affine(self.params['W3'], self.params['b3'])

        self.last_layer = SoftmaxWithLoss()

    def predict(self, x,train_flg):
        for layer in self.layers.values():
            x = layer.forward(x,train_flg)

        return x

    def loss(self, x, t,train_flg):
        """
        損失関数
        x : 入力データ
        t : 教師データ
        """
        y = self.predict(x,train_flg)
        return self.last_layer.forward(y, t)

    def accuracy(self, x, t):
        if t.ndim != 1 : t = cp.argmax(t, axis=1)
        
        y = self.predict(x,train_flg=False)
        y = cp.argmax(y, axis=1)
        acc = cp.sum(y == t)
        return acc / x.shape[0]

        # for i in range(int(x.shape[0] / batch_size)):
        #     tx = x[i*batch_size:(i+1)*batch_size]
        #     tt = t[i*batch_size:(i+1)*batch_size]
        #     y = self.predict(tx,train_flg=False)
        #     y = cp.argmax(y, axis=1)
        #     acc += cp.sum(y == tt) 
               
        # return acc / (x.shape[0] // batch_size*batch_size)

    def gradient(self, x, t):
        """勾配を求める（誤差逆伝播法）
        Parameters
        ----------
        x : 入力データ
        t : 教師データ
        Returns
        -------
        各層の勾配を持ったディクショナリ変数
            grads['W1']、grads['W2']、...は各層の重み
            grads['b1']、grads['b2']、...は各層のバイアス
        """
        # forward
        self.loss(x, t,train_flg=True)

        # backward
        dout = 1
        dout = self.last_layer.backward(dout)

        layers = list(self.layers.values())
        layers.reverse()
        for layer in layers:
            dout = layer.backward(dout)

        # 設定
        grads = {}
        grads['W1'], grads['b1'] = self.layers['Conv1'].dW, self.layers['Conv1'].db
        grads['W2'], grads['b2'] = self.layers['Conv2'].dW, self.layers['Conv2'].db
        grads['W3'], grads['b3'] = self.layers['Affine1'].dW, self.layers['Affine1'].db
        grads['W4'], grads['b4'] = self.layers['Affine2'].dW, self.layers['Affine2'].db
        grads["gamma1"],grads["beta1"] = self.layers["Batch1"].dgamma,self.layers["Batch1"].dbeta
        grads["gamma2"],grads["beta2"] = self.layers["Batch2"].dgamma,self.layers["Batch2"].dbeta


        return grads




class TwoConvNet:
    def __init__(self, input_dim=(1, 28, 28),             
                 hidden_size=100, output_size=15, weight_init_std=0.01,param=None,const={"Batch1":[None,None],"Batch2":[None,None],"Batch3":[None,None]}):
        """
        input_size : tuple, 入力の配列形状(チャンネル数、画像の高さ、画像の幅)
        conv_param : dict, 畳み込みの条件
        pool_param : dict, プーリングの条件
        hidden_size : int, 隠れ層のノード数
        output_size : int, 出力層のノード数
        weight_init_std ： float, 重みWを初期化する際に用いる標準偏差
        """
        self.params = {}
        std = weight_init_std

        conv1_param={"input_dim":input_dim[0],'filter_num':30, 'filter_size':3, 'pad':1, 'stride':1}
        batch1_param={"input_dim":conv1_param["filter_num"]}
        conv2_param={"input_dim":batch1_param["input_dim"],'filter_num':30, 'filter_size':3, 'pad':1, 'stride':1}
        batch2_param={"input_dim":conv2_param["filter_num"]}
        pool1_param={"input_dim":batch2_param["input_dim"],'pool_size':2, 'pad':0, 'stride':2} 
        affin1_param={"input_dim":(30,14,14)}
        batch3_param={"input_dim":hidden_size}
        affin2_param={"input_dim":hidden_size}


        if param==None:
            self.params['W1'] = std * cp.random.randn(conv1_param['filter_num'], conv1_param["input_dim"], conv1_param['filter_size'], conv1_param['filter_size']) # W1は畳み込みフィルターの重みになる
            self.params['b1'] = cp.zeros(conv1_param['filter_num']) #b1は畳み込みフィルターのバイアスになる

            self.params["gamma1"]=cp.ones(batch1_param["input_dim"])
            self.params["beta1"]= cp.zeros(batch1_param["input_dim"])

            self.params['W2'] = std * cp.random.randn(conv2_param['filter_num'], conv2_param["input_dim"], conv2_param['filter_size'], conv2_param['filter_size']) # W1は畳み込みフィルターの重みになる
            self.params['b2'] = cp.zeros(conv2_param['filter_num']) #b1は畳み込みフィルターのバイアスになる

            self.params["gamma2"]=cp.ones(batch2_param["input_dim"])
            self.params["beta2"]= cp.zeros(batch2_param["input_dim"])

            self.params['W3'] = std *  cp.random.randn(cp.prod(affin1_param["input_dim"]), hidden_size)
            self.params['b3'] = cp.zeros(hidden_size)

            self.params["gamma3"]=cp.ones(batch3_param["input_dim"])
            self.params["beta3"]= cp.zeros(batch3_param["input_dim"])

            self.params['W4'] = std *  cp.random.randn(affin2_param["input_dim"], output_size)
            self.params['b4'] = cp.zeros(output_size)

        else:
            self.params=param


        self.layers = OrderedDict()
        #conv1
        self.layers['Conv1'] = Convolution(self.params['W1'], self.params['b1'],
                                           conv1_param['stride'], conv1_param['pad']) 

        #batchnorm1
        self.layers["Batch1"] = BatchNormalization(self.params["gamma1"],self.params["beta1"],
                                                    moving_mean=const["Batch1"][0],moving_var=const["Batch1"][1])

        #Relu1
        self.layers['ReLU1'] = ReLU()

        #conv2
        self.layers['Conv2'] = Convolution(self.params['W2'], self.params['b2'],
                                           conv2_param['stride'], conv2_param['pad']) 

        #batchnorm2
        self.layers["Batch2"] = BatchNormalization(self.params["gamma2"],self.params["beta2"],
                                                    moving_mean=const["Batch2"][0],moving_var=const["Batch2"][1])

        #Relu2
        self.layers['ReLU2'] = ReLU()
        
        #Maxpooling1
        self.layers['Pool1'] = MaxPooling(pool_h=pool1_param["pool_size"], pool_w=pool1_param["pool_size"], stride=pool1_param["stride"], pad=pool1_param["pad"])


        #affin1

        self.layers['Affine1'] = Affine(self.params['W3'], self.params['b3'])

        #batchnorm3

        self.layers["Batch3"] = BatchNormalization(self.params["gamma3"],self.params["beta3"],
                                                    moving_mean=const["Batch3"][0],moving_var=const["Batch3"][1])

        #Relu3
        self.layers['ReLU3'] = ReLU()

        #affin2

        self.layers['Affine2'] = Affine(self.params['W4'], self.params['b4'])

        #softmax 
        self.last_layer = SoftmaxWithLoss()


    def predict(self, x,train_flg):
        for layer in self.layers.values():
            x = layer.forward(x,train_flg)

        return x

    def loss(self, x, t,train_flg):
        """
        損失関数
        x : 入力データ
        t : 教師データ
        """
        y = self.predict(x,train_flg)
        return self.last_layer.forward(y, t)

    def accuracy(self, x, t, batch_size=100):
        if t.ndim != 1 : t = cp.argmax(t, axis=1)
        
        y = self.predict(x,train_flg=False)
        y = cp.argmax(y, axis=1)
        acc = cp.sum(y == t)
        return acc / x.shape[0]


    def gradient(self, x, t):
        """勾配を求める（誤差逆伝播法）
        Parameters
        ----------
        x : 入力データ
        t : 教師データ
        Returns
        -------
        各層の勾配を持ったディクショナリ変数
            grads['W1']、grads['W2']、...は各層の重み
            grads['b1']、grads['b2']、...は各層のバイアス
        """
        # forward
        self.loss(x, t,train_flg=True)

        # backward
        dout = 1
        dout = self.last_layer.backward(dout)

        layers = list(self.layers.values())
        layers.reverse()
        for layer in layers:
            dout = layer.backward(dout)

        # 設定
        grads = {}
        grads['W1'], grads['b1'] = self.layers['Conv1'].dW, self.layers['Conv1'].db
        grads['W2'], grads['b2'] = self.layers['Conv2'].dW, self.layers['Conv2'].db
        grads['W3'], grads['b3'] = self.layers['Affine1'].dW, self.layers['Affine1'].db
        grads['W4'], grads['b4'] = self.layers['Affine2'].dW, self.layers['Affine2'].db
        grads["gamma1"],grads["beta1"] = self.layers["Batch1"].dgamma,self.layers["Batch1"].dbeta
        grads["gamma2"],grads["beta2"] = self.layers["Batch2"].dgamma,self.layers["Batch2"].dbeta
        grads["gamma3"],grads["beta3"] = self.layers["Batch3"].dgamma,self.layers["Batch3"].dbeta

        return grads



class TfConvNet:
    def __init__(self, input_dim=(1, 28, 28),             
                 hidden_size=100, output_size=15, weight_init_std=0.01,param=None,
                 const={"Batch_c1":[None,None],"Batch_c2":[None,None],"Batch_c3":[None,None],"Batch_c4":[None,None],"Batch_c5":[None,None],
                        "Batch_a1":[None,None]}
                ):
        """
        input_size : tuple, 入力の配列形状(チャンネル数、画像の高さ、画像の幅)
        conv_param : dict, 畳み込みの条件
        pool_param : dict, プーリングの条件
        hidden_size : int, 隠れ層のノード数
        output_size : int, 出力層のノード数
        weight_init_std ： float, 重みWを初期化する際に用いる標準偏差
        """
        self.params = {}
        std = weight_init_std

        conv1_param={"input_dim":input_dim[0],'filter_num':32, 'filter_size':3, 'pad':1, 'stride':1}
        batch_c1_param={"input_dim":conv1_param["filter_num"]}
        conv2_param={"input_dim":batch_c1_param["input_dim"],'filter_num':32, 'filter_size':3, 'pad':1, 'stride':1}
        batch_c2_param={"input_dim":conv2_param["filter_num"]}
        pool1_param={"input_dim":batch_c2_param["input_dim"],'pool_size':2, 'pad':0, 'stride':2} 

        conv3_param={"input_dim":pool1_param["input_dim"],'filter_num':64, 'filter_size':3, 'pad':1, 'stride':1}
        batch_c3_param={"input_dim":conv3_param["filter_num"]}
        conv4_param={"input_dim":batch_c3_param["input_dim"],'filter_num':64, 'filter_size':3, 'pad':1, 'stride':1}
        batch_c4_param={"input_dim":conv4_param["filter_num"]}
        pool2_param={"input_dim":batch_c4_param["input_dim"],'pool_size':2, 'pad':0, 'stride':2} 

        conv5_param={"input_dim":pool2_param["input_dim"],'filter_num':64, 'filter_size':3, 'pad':0, 'stride':1}
        batch_c5_param={"input_dim":conv5_param["filter_num"]}

        affin1_param={"input_dim":(64,5,5)}
        batch_a1_param={"input_dim":hidden_size}
        affin2_param={"input_dim":hidden_size}


        if param==None:
            self.params['W_c1'] = std * cp.random.randn(conv1_param['filter_num'], conv1_param["input_dim"], conv1_param['filter_size'], conv1_param['filter_size']) # W1は畳み込みフィルターの重みになる
            self.params['b_c1'] = cp.zeros(conv1_param['filter_num']) #b1は畳み込みフィルターのバイアスになる
            self.params["gamma_c1"]=cp.ones(batch_c1_param["input_dim"])
            self.params["beta_c1"]= cp.zeros(batch_c1_param["input_dim"])

            self.params['W_c2'] = std * cp.random.randn(conv2_param['filter_num'], conv2_param["input_dim"], conv2_param['filter_size'], conv2_param['filter_size']) # W1は畳み込みフィルターの重みになる
            self.params['b_c2'] = cp.zeros(conv2_param['filter_num']) #b1は畳み込みフィルターのバイアスになる
            self.params["gamma_c2"]=cp.ones(batch_c2_param["input_dim"])
            self.params["beta_c2"]= cp.zeros(batch_c2_param["input_dim"])

            self.params['W_c3'] = std * cp.random.randn(conv3_param['filter_num'], conv3_param["input_dim"], conv3_param['filter_size'], conv3_param['filter_size']) # W1は畳み込みフィルターの重みになる
            self.params['b_c3'] = cp.zeros(conv3_param['filter_num']) #b1は畳み込みフィルターのバイアスになる
            self.params["gamma_c3"]=cp.ones(batch_c3_param["input_dim"])
            self.params["beta_c3"]= cp.zeros(batch_c3_param["input_dim"])

            self.params['W_c4'] = std * cp.random.randn(conv4_param['filter_num'], conv4_param["input_dim"], conv4_param['filter_size'], conv4_param['filter_size']) # W1は畳み込みフィルターの重みになる
            self.params['b_c4'] = cp.zeros(conv4_param['filter_num']) #b1は畳み込みフィルターのバイアスになる
            self.params["gamma_c4"]=cp.ones(batch_c4_param["input_dim"])
            self.params["beta_c4"]= cp.zeros(batch_c4_param["input_dim"])

            self.params['W_c5'] = std * cp.random.randn(conv5_param['filter_num'], conv5_param["input_dim"], conv5_param['filter_size'], conv5_param['filter_size']) # W1は畳み込みフィルターの重みになる
            self.params['b_c5'] = cp.zeros(conv5_param['filter_num']) #b1は畳み込みフィルターのバイアスになる
            self.params["gamma_c5"]=cp.ones(batch_c5_param["input_dim"])
            self.params["beta_c5"]= cp.zeros(batch_c5_param["input_dim"])

            self.params['W_a1'] = std *  cp.random.randn(cp.prod(affin1_param["input_dim"]), hidden_size)
            self.params['b_a1'] = cp.zeros(hidden_size)
            self.params["gamma_a1"]=cp.ones(batch_a1_param["input_dim"])
            self.params["beta_a1"]= cp.zeros(batch_a1_param["input_dim"])

            self.params['W_a2'] = std *  cp.random.randn(affin2_param["input_dim"], output_size)
            self.params['b_a2'] = cp.zeros(output_size)

        else:
            self.params=param


        self.layers = OrderedDict()

        #conv1
        self.layers['Conv1'] = Convolution(self.params['W_c1'], self.params['b_c1'],
                                           conv1_param['stride'], conv1_param['pad']) 
        #batchnorm1
        self.layers["Batch_c1"] = BatchNormalization(self.params["gamma_c1"],self.params["beta_c1"],
                                                    moving_mean=const["Batch_c1"][0],moving_var=const["Batch_c1"][1])
        #Relu1
        self.layers['ReLU1'] = ReLU()

        #conv2
        self.layers['Conv2'] = Convolution(self.params['W_c2'], self.params['b_c2'],
                                           conv2_param['stride'], conv2_param['pad']) 
        #batchnorm2
        self.layers["Batch_c2"] = BatchNormalization(self.params["gamma_c2"],self.params["beta_c2"],
                                                    moving_mean=const["Batch_c2"][0],moving_var=const["Batch_c2"][1])
        #Relu2
        self.layers['ReLU2'] = ReLU()
        #Maxpooling1
        self.layers['Pool1'] = MaxPooling(pool_h=pool1_param["pool_size"], pool_w=pool1_param["pool_size"], stride=pool1_param["stride"], pad=pool1_param["pad"])


        #conv3
        self.layers['Conv3'] = Convolution(self.params['W_c3'], self.params['b_c3'],
                                           conv3_param['stride'], conv3_param['pad']) 
        #batchnorm3
        self.layers["Batch_c3"] = BatchNormalization(self.params["gamma_c3"],self.params["beta_c3"],
                                                    moving_mean=const["Batch_c3"][0],moving_var=const["Batch_c3"][1])
        #Relu3
        self.layers['ReLU3'] = ReLU()

        #conv4
        self.layers['Conv4'] = Convolution(self.params['W_c4'], self.params['b_c4'],
                                           conv4_param['stride'], conv4_param['pad']) 
        #batchnorm4
        self.layers["Batch_c4"] = BatchNormalization(self.params["gamma_c4"],self.params["beta_c4"],
                                                    moving_mean=const["Batch_c4"][0],moving_var=const["Batch_c4"][1])
        #Relu4
        self.layers['ReLU4'] = ReLU()
        #Maxpooling2
        self.layers['Pool2'] = MaxPooling(pool_h=pool2_param["pool_size"], pool_w=pool2_param["pool_size"], stride=pool2_param["stride"], pad=pool2_param["pad"])


        #conv5
        self.layers['Conv5'] = Convolution(self.params['W_c5'], self.params['b_c5'],
                                           conv5_param['stride'], conv5_param['pad']) 
        #batchnorm5
        self.layers["Batch_c5"] = BatchNormalization(self.params["gamma_c5"],self.params["beta_c5"],
                                                    moving_mean=const["Batch_c5"][0],moving_var=const["Batch_c5"][1])
        #Relu5
        self.layers['ReLU5'] = ReLU()



        #affin1
        self.layers['Affine1'] = Affine(self.params['W_a1'], self.params['b_a1'])
        #batchnorm5
        self.layers["Batch_a1"] = BatchNormalization(self.params["gamma_a1"],self.params["beta_a1"],
                                                    moving_mean=const["Batch_a1"][0],moving_var=const["Batch_a1"][1])
        #Relu5
        self.layers['ReLU5'] = ReLU()

        #affin2
        self.layers['Affine2'] = Affine(self.params['W_a2'], self.params['b_a2'])

        #softmax 
        self.last_layer = SoftmaxWithLoss()


    def predict(self, x,train_flg):
        for layer in self.layers.values():
            x = layer.forward(x,train_flg)

        return x

    def loss(self, x, t,train_flg):
        """
        損失関数
        x : 入力データ
        t : 教師データ
        """
        y = self.predict(x,train_flg)
        return self.last_layer.forward(y, t)

    def accuracy(self, x, t, batch_size=100):
        if t.ndim != 1 : t = cp.argmax(t, axis=1)
        
        y = self.predict(x,train_flg=False)
        y = cp.argmax(y, axis=1)
        acc = cp.sum(y == t)
        return acc / x.shape[0]


    def gradient(self, x, t):
        """勾配を求める（誤差逆伝播法）
        Parameters
        ----------
        x : 入力データ
        t : 教師データ
        Returns
        -------
        各層の勾配を持ったディクショナリ変数
            grads['W1']、grads['W2']、...は各層の重み
            grads['b1']、grads['b2']、...は各層のバイアス
        """
        # forward
        self.loss(x, t,train_flg=True)

        # backward
        dout = 1
        dout = self.last_layer.backward(dout)

        layers = list(self.layers.values())
        layers.reverse()
        for layer in layers:
            dout = layer.backward(dout)

        # 設定
        grads = {}
        grads['W_c1'], grads['b_c1'] = self.layers['Conv1'].dW, self.layers['Conv1'].db
        grads['W_c2'], grads['b_c2'] = self.layers['Conv2'].dW, self.layers['Conv2'].db
        grads['W_c3'], grads['b_c3'] = self.layers['Conv3'].dW, self.layers['Conv3'].db
        grads['W_c4'], grads['b_c4'] = self.layers['Conv4'].dW, self.layers['Conv4'].db
        grads['W_c5'], grads['b_c5'] = self.layers['Conv5'].dW, self.layers['Conv5'].db

        grads['W_a1'], grads['b_a1'] = self.layers['Affine1'].dW, self.layers['Affine1'].db
        grads['W_a2'], grads['b_a2'] = self.layers['Affine2'].dW, self.layers['Affine2'].db
        grads["gamma_c1"],grads["beta_c1"] = self.layers["Batch_c1"].dgamma,self.layers["Batch_c1"].dbeta
        grads["gamma_c2"],grads["beta_c2"] = self.layers["Batch_c2"].dgamma,self.layers["Batch_c2"].dbeta
        grads["gamma_c3"],grads["beta_c3"] = self.layers["Batch_c3"].dgamma,self.layers["Batch_c3"].dbeta
        grads["gamma_c4"],grads["beta_c4"] = self.layers["Batch_c4"].dgamma,self.layers["Batch_c4"].dbeta
        grads["gamma_c5"],grads["beta_c5"] = self.layers["Batch_c5"].dgamma,self.layers["Batch_c5"].dbeta
        grads["gamma_a1"],grads["beta_a1"] = self.layers["Batch_a1"].dgamma,self.layers["Batch_a1"].dbeta

        return grads


class TfsConvNet:
    def __init__(self, input_dim=(1, 28, 28),             
                 hidden_size=100, output_size=15, weight_init_std=0.01,param=None,
                 const={"Batch_c1":[None,None],"Batch_c2":[None,None],"Batch_c3":[None,None],"Batch_c4":[None,None],"Batch_c5":[None,None],
                        "Batch_a1":[None,None]}
                ):
        """
        input_size : tuple, 入力の配列形状(チャンネル数、画像の高さ、画像の幅)
        conv_param : dict, 畳み込みの条件
        pool_param : dict, プーリングの条件
        hidden_size : int, 隠れ層のノード数
        output_size : int, 出力層のノード数
        weight_init_std ： float, 重みWを初期化する際に用いる標準偏差
        """
        self.params = {}
        std = weight_init_std

        conv1_param={"input_dim":input_dim[0],'filter_num':32, 'filter_size':3, 'pad':1, 'stride':1}
        batch_c1_param={"input_dim":conv1_param["filter_num"]}
        # conv2_param={"input_dim":batch_c1_param["input_dim"],'filter_num':32, 'filter_size':3, 'pad':1, 'stride':1}
        # batch_c2_param={"input_dim":conv2_param["filter_num"]}
        pool1_param={"input_dim":batch_c1_param["input_dim"],'pool_size':2, 'pad':0, 'stride':2} 

        conv3_param={"input_dim":pool1_param["input_dim"],'filter_num':64, 'filter_size':3, 'pad':1, 'stride':1}
        batch_c3_param={"input_dim":conv3_param["filter_num"]}
        # conv4_param={"input_dim":batch_c3_param["input_dim"],'filter_num':64, 'filter_size':3, 'pad':1, 'stride':1}
        # batch_c4_param={"input_dim":conv4_param["filter_num"]}
        pool2_param={"input_dim":batch_c3_param["input_dim"],'pool_size':2, 'pad':0, 'stride':2} 

        conv5_param={"input_dim":pool2_param["input_dim"],'filter_num':64, 'filter_size':3, 'pad':0, 'stride':1}
        batch_c5_param={"input_dim":conv5_param["filter_num"]}

        affin1_param={"input_dim":(64,5,5)}
        batch_a1_param={"input_dim":hidden_size}
        affin2_param={"input_dim":hidden_size}


        if param==None:
            self.params['W_c1'] = std * cp.random.randn(conv1_param['filter_num'], conv1_param["input_dim"], conv1_param['filter_size'], conv1_param['filter_size']) # W1は畳み込みフィルターの重みになる
            self.params['b_c1'] = cp.zeros(conv1_param['filter_num']) #b1は畳み込みフィルターのバイアスになる
            self.params["gamma_c1"]=cp.ones(batch_c1_param["input_dim"])
            self.params["beta_c1"]= cp.zeros(batch_c1_param["input_dim"])

            # self.params['W_c2'] = std * cp.random.randn(conv2_param['filter_num'], conv2_param["input_dim"], conv2_param['filter_size'], conv2_param['filter_size']) # W1は畳み込みフィルターの重みになる
            # self.params['b_c2'] = cp.zeros(conv2_param['filter_num']) #b1は畳み込みフィルターのバイアスになる
            # self.params["gamma_c2"]=cp.ones(batch_c2_param["input_dim"])
            # self.params["beta_c2"]= cp.zeros(batch_c2_param["input_dim"])

            self.params['W_c3'] = std * cp.random.randn(conv3_param['filter_num'], conv3_param["input_dim"], conv3_param['filter_size'], conv3_param['filter_size']) # W1は畳み込みフィルターの重みになる
            self.params['b_c3'] = cp.zeros(conv3_param['filter_num']) #b1は畳み込みフィルターのバイアスになる
            self.params["gamma_c3"]=cp.ones(batch_c3_param["input_dim"])
            self.params["beta_c3"]= cp.zeros(batch_c3_param["input_dim"])

            # self.params['W_c4'] = std * cp.random.randn(conv4_param['filter_num'], conv4_param["input_dim"], conv4_param['filter_size'], conv4_param['filter_size']) # W1は畳み込みフィルターの重みになる
            # self.params['b_c4'] = cp.zeros(conv4_param['filter_num']) #b1は畳み込みフィルターのバイアスになる
            # self.params["gamma_c4"]=cp.ones(batch_c4_param["input_dim"])
            # self.params["beta_c4"]= cp.zeros(batch_c4_param["input_dim"])

            self.params['W_c5'] = std * cp.random.randn(conv5_param['filter_num'], conv5_param["input_dim"], conv5_param['filter_size'], conv5_param['filter_size']) # W1は畳み込みフィルターの重みになる
            self.params['b_c5'] = cp.zeros(conv5_param['filter_num']) #b1は畳み込みフィルターのバイアスになる
            self.params["gamma_c5"]=cp.ones(batch_c5_param["input_dim"])
            self.params["beta_c5"]= cp.zeros(batch_c5_param["input_dim"])

            self.params['W_a1'] = std *  cp.random.randn(cp.prod(cp.array(affin1_param["input_dim"])), hidden_size)
            self.params['b_a1'] = cp.zeros(hidden_size)
            self.params["gamma_a1"]=cp.ones(batch_a1_param["input_dim"])
            self.params["beta_a1"]= cp.zeros(batch_a1_param["input_dim"])

            self.params['W_a2'] = std *  cp.random.randn(affin2_param["input_dim"], output_size)
            self.params['b_a2'] = cp.zeros(output_size)

        else:
            self.params=param


        self.layers = OrderedDict()

        #conv1
        self.layers['Conv1'] = Convolution(self.params['W_c1'], self.params['b_c1'],
                                           conv1_param['stride'], conv1_param['pad']) 
        #batchnorm1
        self.layers["Batch_c1"] = BatchNormalization(self.params["gamma_c1"],self.params["beta_c1"],
                                                    moving_mean=const["Batch_c1"][0],moving_var=const["Batch_c1"][1])
        #Relu1
        self.layers['ReLU1'] = ReLU()

        # #conv2
        # self.layers['Conv2'] = Convolution(self.params['W_c2'], self.params['b_c2'],
        #                                    conv2_param['stride'], conv2_param['pad']) 
        # #batchnorm2
        # self.layers["Batch_c2"] = BatchNormalization(self.params["gamma_c2"],self.params["beta_c2"],
        #                                             moving_mean=const["Batch_c2"][0],moving_var=const["Batch_c2"][1])
        # #Relu2
        # self.layers['ReLU2'] = ReLU()
        #Maxpooling1
        self.layers['Pool1'] = MaxPooling(pool_h=pool1_param["pool_size"], pool_w=pool1_param["pool_size"], stride=pool1_param["stride"], pad=pool1_param["pad"])


        #conv3
        self.layers['Conv3'] = Convolution(self.params['W_c3'], self.params['b_c3'],
                                           conv3_param['stride'], conv3_param['pad']) 
        #batchnorm3
        self.layers["Batch_c3"] = BatchNormalization(self.params["gamma_c3"],self.params["beta_c3"],
                                                    moving_mean=const["Batch_c3"][0],moving_var=const["Batch_c3"][1])
        #Relu3
        self.layers['ReLU3'] = ReLU()

        # #conv4
        # self.layers['Conv4'] = Convolution(self.params['W_c4'], self.params['b_c4'],
        #                                    conv4_param['stride'], conv4_param['pad']) 
        # #batchnorm4
        # self.layers["Batch_c4"] = BatchNormalization(self.params["gamma_c4"],self.params["beta_c4"],
        #                                             moving_mean=const["Batch_c4"][0],moving_var=const["Batch_c4"][1])
        # #Relu4
        # self.layers['ReLU4'] = ReLU()
        #Maxpooling2
        self.layers['Pool2'] = MaxPooling(pool_h=pool2_param["pool_size"], pool_w=pool2_param["pool_size"], stride=pool2_param["stride"], pad=pool2_param["pad"])


        #conv5
        self.layers['Conv5'] = Convolution(self.params['W_c5'], self.params['b_c5'],
                                           conv5_param['stride'], conv5_param['pad']) 
        #batchnorm5
        self.layers["Batch_c5"] = BatchNormalization(self.params["gamma_c5"],self.params["beta_c5"],
                                                    moving_mean=const["Batch_c5"][0],moving_var=const["Batch_c5"][1])
        #Relu5
        self.layers['ReLU5'] = ReLU()


        #affin1
        self.layers['Affine1'] = Affine(self.params['W_a1'], self.params['b_a1'])
        #batchnorm5
        self.layers["Batch_a1"] = BatchNormalization(self.params["gamma_a1"],self.params["beta_a1"],
                                                    moving_mean=const["Batch_a1"][0],moving_var=const["Batch_a1"][1])
        #Relu5
        self.layers['ReLU5'] = ReLU()

        #affin2
        self.layers['Affine2'] = Affine(self.params['W_a2'], self.params['b_a2'])

        #softmax 
        self.last_layer = SoftmaxWithLoss()


    def predict(self, x,train_flg):
        for layer in self.layers.values():
            x = layer.forward(x,train_flg)

        return x

    def loss(self, x, t,train_flg):
        """
        損失関数
        x : 入力データ
        t : 教師データ
        """
        y = self.predict(x,train_flg)
        return self.last_layer.forward(y, t)

    def accuracy(self, x, t, batch_size=100):
        if t.ndim != 1 : t = cp.argmax(t, axis=1)
        
        y = self.predict(x,train_flg=False)
        y = cp.argmax(y, axis=1)
        acc = cp.sum(y == t)
        return acc / x.shape[0]


    def gradient(self, x, t):
        """勾配を求める（誤差逆伝播法）
        Parameters
        ----------
        x : 入力データ
        t : 教師データ
        Returns
        -------
        各層の勾配を持ったディクショナリ変数
            grads['W1']、grads['W2']、...は各層の重み
            grads['b1']、grads['b2']、...は各層のバイアス
        """
        # forward
        self.loss(x, t,train_flg=True)

        # backward
        dout = 1
        dout = self.last_layer.backward(dout)

        layers = list(self.layers.values())
        layers.reverse()
        for layer in layers:
            dout = layer.backward(dout)

        # 設定
        grads = {}
        grads['W_c1'], grads['b_c1'] = self.layers['Conv1'].dW, self.layers['Conv1'].db
        # grads['W_c2'], grads['b_c2'] = self.layers['Conv2'].dW, self.layers['Conv2'].db
        grads['W_c3'], grads['b_c3'] = self.layers['Conv3'].dW, self.layers['Conv3'].db
        # grads['W_c4'], grads['b_c4'] = self.layers['Conv4'].dW, self.layers['Conv4'].db
        grads['W_c5'], grads['b_c5'] = self.layers['Conv5'].dW, self.layers['Conv5'].db

        grads['W_a1'], grads['b_a1'] = self.layers['Affine1'].dW, self.layers['Affine1'].db
        grads['W_a2'], grads['b_a2'] = self.layers['Affine2'].dW, self.layers['Affine2'].db
        grads["gamma_c1"],grads["beta_c1"] = self.layers["Batch_c1"].dgamma,self.layers["Batch_c1"].dbeta
        # grads["gamma_c2"],grads["beta_c2"] = self.layers["Batch_c2"].dgamma,self.layers["Batch_c2"].dbeta
        grads["gamma_c3"],grads["beta_c3"] = self.layers["Batch_c3"].dgamma,self.layers["Batch_c3"].dbeta
        # grads["gamma_c4"],grads["beta_c4"] = self.layers["Batch_c4"].dgamma,self.layers["Batch_c4"].dbeta
        grads["gamma_c5"],grads["beta_c5"] = self.layers["Batch_c5"].dgamma,self.layers["Batch_c5"].dbeta
        grads["gamma_a1"],grads["beta_a1"] = self.layers["Batch_a1"].dgamma,self.layers["Batch_a1"].dbeta

        return grads





class DeepConvNet:
    def __init__(self, input_dim=(1, 28, 28),             
                 hidden_size=512, output_size=15, weight_init_std=0.01,param=None,const={"Batch1":[None,None],"Batch2":[None,None],"Batch3":[None,None],"Batch4":[None,None],"Batch5":[None,None]}):
        """
        input_size : tuple, 入力の配列形状(チャンネル数、画像の高さ、画像の幅)
        conv_param : dict, 畳み込みの条件
        pool_param : dict, プーリングの条件
        hidden_size : int, 隠れ層のノード数
        output_size : int, 出力層のノード数
        weight_init_std ： float, 重みWを初期化する際に用いる標準偏差
        """
        self.params = {}
        std = weight_init_std

        conv1_param={"input_dim":input_dim[0],'filter_num':32, 'filter_size':3, 'pad':1, 'stride':1}
        batch1_param={"input_dim":conv1_param["filter_num"]}
        conv2_param={"input_dim":batch1_param["input_dim"],'filter_num':32, 'filter_size':3, 'pad':1, 'stride':1}
        batch2_param={"input_dim":conv2_param["filter_num"]}
        pool1_param={"input_dim":batch2_param["input_dim"],'pool_size':2, 'pad':0, 'stride':2} 

        conv3_param={"input_dim":pool1_param["input_dim"],'filter_num':64, 'filter_size':3, 'pad':1, 'stride':1}
        batch3_param={"input_dim":conv3_param["filter_num"]}
        conv4_param={"input_dim":batch3_param["input_dim"],'filter_num':64, 'filter_size':3, 'pad':1, 'stride':1}
        batch4_param={"input_dim":conv4_param["filter_num"]}
        pool2_param={"input_dim":batch4_param["input_dim"],'pool_size':2, 'pad':0, 'stride':2} 


        affin1_param={"input_dim":(64,7,7)}
        batch5_param={"input_dim":hidden_size}
        affin2_param={"input_dim":hidden_size}


        if param==None:
            self.params['W1'] = std * cp.random.randn(conv1_param['filter_num'], conv1_param["input_dim"], conv1_param['filter_size'], conv1_param['filter_size']) # W1は畳み込みフィルターの重みになる
            self.params['b1'] = cp.zeros(conv1_param['filter_num']) #b1は畳み込みフィルターのバイアスになる

            self.params["gamma1"]=cp.ones(batch1_param["input_dim"])
            self.params["beta1"]= cp.zeros(batch1_param["input_dim"])

            self.params['W2'] = std * cp.random.randn(conv2_param['filter_num'], conv2_param["input_dim"], conv2_param['filter_size'], conv2_param['filter_size']) # W1は畳み込みフィルターの重みになる
            self.params['b2'] = cp.zeros(conv2_param['filter_num']) #b1は畳み込みフィルターのバイアスになる

            self.params["gamma2"]=cp.ones(batch2_param["input_dim"])
            self.params["beta2"]= cp.zeros(batch2_param["input_dim"])

            self.params['W3'] = std * cp.random.randn(conv3_param['filter_num'], conv3_param["input_dim"], conv3_param['filter_size'], conv3_param['filter_size']) # W1は畳み込みフィルターの重みになる
            self.params['b3'] = cp.zeros(conv3_param['filter_num']) #b1は畳み込みフィルターのバイアスになる

            self.params["gamma3"]=cp.ones(batch3_param["input_dim"])
            self.params["beta3"]= cp.zeros(batch3_param["input_dim"])

            self.params['W4'] = std * cp.random.randn(conv4_param['filter_num'], conv4_param["input_dim"], conv4_param['filter_size'], conv4_param['filter_size']) # W1は畳み込みフィルターの重みになる
            self.params['b4'] = cp.zeros(conv4_param['filter_num']) #b1は畳み込みフィルターのバイアスになる

            self.params["gamma4"]=cp.ones(batch4_param["input_dim"])
            self.params["beta4"]= cp.zeros(batch4_param["input_dim"])



            self.params['W5'] = std *  cp.random.randn(cp.prod(affin1_param["input_dim"]), hidden_size)
            self.params['b5'] = cp.zeros(hidden_size)

            self.params["gamma5"]=cp.ones(batch5_param["input_dim"])
            self.params["beta5"]= cp.zeros(batch5_param["input_dim"])

            self.params['W6'] = std *  cp.random.randn(affin2_param["input_dim"], output_size)
            self.params['b6'] = cp.zeros(output_size)

        else:
            self.params=param


        self.layers = OrderedDict()
        #conv1
        self.layers['Conv1'] = Convolution(self.params['W1'], self.params['b1'],
                                           conv1_param['stride'], conv1_param['pad']) 

        #batchnorm1
        self.layers["Batch1"] = BatchNormalization(self.params["gamma1"],self.params["beta1"],
                                                    moving_mean=const["Batch1"][0],moving_var=const["Batch1"][1])

        #Relu1
        self.layers['ReLU1'] = ReLU()

        #conv2
        self.layers['Conv2'] = Convolution(self.params['W2'], self.params['b2'],
                                           conv2_param['stride'], conv2_param['pad']) 

        #batchnorm2
        self.layers["Batch2"] = BatchNormalization(self.params["gamma2"],self.params["beta2"],
                                                    moving_mean=const["Batch2"][0],moving_var=const["Batch2"][1])

        #Relu2
        self.layers['ReLU2'] = ReLU()
        
        #Maxpooling1
        self.layers['Pool1'] = MaxPooling(pool_h=pool1_param["pool_size"], pool_w=pool1_param["pool_size"], stride=pool1_param["stride"], pad=pool1_param["pad"])

        #conv3
        self.layers['Conv3'] = Convolution(self.params['W3'], self.params['b3'],
                                           conv3_param['stride'], conv3_param['pad']) 

        #batchnorm3
        self.layers["Batch3"] = BatchNormalization(self.params["gamma3"],self.params["beta3"],
                                                    moving_mean=const["Batch3"][0],moving_var=const["Batch3"][1])

        #Relu3
        self.layers['ReLU3'] = ReLU()

        #conv4
        self.layers['Conv4'] = Convolution(self.params['W4'], self.params['b4'],
                                           conv4_param['stride'], conv4_param['pad']) 

        #batchnorm4
        self.layers["Batch4"] = BatchNormalization(self.params["gamma4"],self.params["beta4"],
                                                    moving_mean=const["Batch4"][0],moving_var=const["Batch4"][1])

        #Relu4
        self.layers['ReLU4'] = ReLU()
        
        #Maxpooling2
        self.layers['Pool2'] = MaxPooling(pool_h=pool2_param["pool_size"], pool_w=pool2_param["pool_size"], stride=pool2_param["stride"], pad=pool2_param["pad"])


        #affin1

        self.layers['Affine1'] = Affine(self.params['W5'], self.params['b5'])

        #batchnorm5

        self.layers["Batch5"] = BatchNormalization(self.params["gamma5"],self.params["beta5"],
                                                    moving_mean=const["Batch5"][0],moving_var=const["Batch5"][1])

        #Relu5
        self.layers['ReLU5'] = ReLU()

        #affin2

        self.layers['Affine2'] = Affine(self.params['W6'], self.params['b6'])

        #softmax 
        self.last_layer = SoftmaxWithLoss()


    def predict(self, x,train_flg):
        for layer in self.layers.values():
            x = layer.forward(x,train_flg)

        return x

    def loss(self, x, t,train_flg):
        """
        損失関数
        x : 入力データ
        t : 教師データ
        """
        y = self.predict(x,train_flg)
        return self.last_layer.forward(y, t)

    def accuracy(self, x, t, batch_size=100):
        if t.ndim != 1 : t = cp.argmax(t, axis=1)
        
        y = self.predict(x,train_flg=False)
        y = cp.argmax(y, axis=1)
        acc = cp.sum(y == t)
        return acc / x.shape[0]


    def gradient(self, x, t):
        """勾配を求める（誤差逆伝播法）
        Parameters
        ----------
        x : 入力データ
        t : 教師データ
        Returns
        -------
        各層の勾配を持ったディクショナリ変数
            grads['W1']、grads['W2']、...は各層の重み
            grads['b1']、grads['b2']、...は各層のバイアス
        """
        # forward
        self.loss(x, t,train_flg=True)

        # backward
        dout = 1
        dout = self.last_layer.backward(dout)

        layers = list(self.layers.values())
        layers.reverse()
        for layer in layers:
            dout = layer.backward(dout)

        # 設定
        grads = {}
        grads['W1'], grads['b1'] = self.layers['Conv1'].dW, self.layers['Conv1'].db
        grads['W2'], grads['b2'] = self.layers['Conv2'].dW, self.layers['Conv2'].db
        grads['W3'], grads['b3'] = self.layers['Conv3'].dW, self.layers['Conv3'].db
        grads['W4'], grads['b4'] = self.layers['Conv4'].dW, self.layers['Conv4'].db
        grads['W5'], grads['b5'] = self.layers['Affine1'].dW, self.layers['Affine1'].db
        grads['W6'], grads['b6'] = self.layers['Affine2'].dW, self.layers['Affine2'].db
        grads["gamma1"],grads["beta1"] = self.layers["Batch1"].dgamma,self.layers["Batch1"].dbeta
        grads["gamma2"],grads["beta2"] = self.layers["Batch2"].dgamma,self.layers["Batch2"].dbeta
        grads["gamma3"],grads["beta3"] = self.layers["Batch3"].dgamma,self.layers["Batch3"].dbeta
        grads["gamma4"],grads["beta4"] = self.layers["Batch4"].dgamma,self.layers["Batch4"].dbeta
        grads["gamma5"],grads["beta5"] = self.layers["Batch5"].dgamma,self.layers["Batch5"].dbeta

        return grads
import numpy as np
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
            self.params['W1'] = std * np.random.randn(filter_num, input_dim[0], filter_size, filter_size) # W1は畳み込みフィルターの重みになる
            self.params['b1'] = np.zeros(filter_num) #b1は畳み込みフィルターのバイアスになる
            self.params['W2'] = std *  np.random.randn(pool_output_pixel, hidden_size)
            self.params['b2'] = np.zeros(hidden_size)
            self.params['W3'] = std *  np.random.randn(hidden_size, output_size)
            self.params['b3'] = np.zeros(output_size)
            self.params["gamma1"]=np.ones(filter_num)
            self.params["beta1"]= np.zeros(filter_num)
            self.params["gamma2"]=np.ones(hidden_size)
            self.params["beta2"]= np.zeros(hidden_size)
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
        if t.ndim != 1 : t = np.argmax(t, axis=1)
        
        y = self.predict(x,train_flg=False)
        y = np.argmax(y, axis=1)
        acc = np.sum(y == t)
        return acc / x.shape[0]

        # for i in range(int(x.shape[0] / batch_size)):
        #     tx = x[i*batch_size:(i+1)*batch_size]
        #     tt = t[i*batch_size:(i+1)*batch_size]
        #     y = self.predict(tx,train_flg=False)
        #     y = np.argmax(y, axis=1)
        #     acc += np.sum(y == tt) 
               
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
            self.params['W1'] = std * np.random.randn(conv1_param['filter_num'], conv1_param["input_dim"], conv1_param['filter_size'], conv1_param['filter_size']) # W1は畳み込みフィルターの重みになる
            self.params['b1'] = np.zeros(conv1_param['filter_num']) #b1は畳み込みフィルターのバイアスになる

            self.params["gamma1"]=np.ones(batch1_param["input_dim"])
            self.params["beta1"]= np.zeros(batch1_param["input_dim"])

            self.params['W2'] = std * np.random.randn(conv2_param['filter_num'], conv2_param["input_dim"], conv2_param['filter_size'], conv2_param['filter_size']) # W1は畳み込みフィルターの重みになる
            self.params['b2'] = np.zeros(conv2_param['filter_num']) #b1は畳み込みフィルターのバイアスになる

            self.params["gamma2"]=np.ones(batch2_param["input_dim"])
            self.params["beta2"]= np.zeros(batch2_param["input_dim"])

            self.params['W3'] = std *  np.random.randn(np.prod(affin1_param["input_dim"]), hidden_size)
            self.params['b3'] = np.zeros(hidden_size)

            self.params["gamma3"]=np.ones(batch3_param["input_dim"])
            self.params["beta3"]= np.zeros(batch3_param["input_dim"])

            self.params['W4'] = std *  np.random.randn(affin2_param["input_dim"], output_size)
            self.params['b4'] = np.zeros(output_size)

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
        if t.ndim != 1 : t = np.argmax(t, axis=1)
        
        y = self.predict(x,train_flg=False)
        y = np.argmax(y, axis=1)
        acc = np.sum(y == t)
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

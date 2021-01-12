# 環境構築手順
以下の方法に慣れていない方は、DAY1教材の2_notebook/0_preparation.ipynbに沿って環境を構築してください

## 1. pyenvのインストール
  ```
  https://github.com/pyenv/pyenv
  ```
## 2. pyenv-virtualenvのインストール
  ```
  git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
  echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
  ```
## 3. 仮想環境の構築
  ```
  pyenv virtualenv 3.7.3 DLvr6
  ```
## 4. 該当ディレクトリに仮想環境を設定
  ```
  pyenv local DLvr6
  ```
## 5. 必要ライブラリをインストール
  ```
  pip install --upgrade pip
  pip install -r pckg.list
  ```
## 6. Mecab環境を構築する
#### [Windowsの場合]
  * (1) Mecabのインストール    
      * http://oita.oika.me/2018/05/03/python3-mecab-on-windows/
  * (2) mecab-python-windowsのインストール    
  ```
  pip install mecab-python-windows
  ```


#### [Mac, Linuxの場合]
  * (1) swigのインストール
    * Macの場合
      ```
      brew install swig
      ```

    * Ubuntuの場合
      ```
      sudo apt-get install swig
      ```

  * (2) MeCabのインストール
    * MeCabの公式サイト  
    http://taku910.github.io/mecab/#install  
    * インストール方法  
    mecab-0.996.tar.gzをダウンロードし、端末にて以下を実行する。

      ```    
      tar zxfv mecab-0.996.tar.gz
      cd mecab-0.996
      ./configure
      make
      make check
      sudo make install
      ```

      次に、辞書のインストール。mecab-ipadic-2.7.0-20070801.tar.gzをダウンロードし、端末にて以下を実行する。

      ```
      tar zxfv mecab-ipadic-2.7.0-20070801.tar.gz
      cd mecab-ipadic-2.7.0-20070801
      ./configure --with-charset=utf8
      make
      sudo make install
      ```

  * (3) mecab-python3のインストール
      ```
      pip install mecab-python3==0.996.2
      ```

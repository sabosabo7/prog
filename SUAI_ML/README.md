# 環境構築手順(上級者向け)
以下の方法に慣れていない方は、0_preparation.ipynbに沿って環境を構築すること

## 1. pyenv-virtualenvのインストール
  ```
  git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
  echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
  ```
## 2. 仮想環境の構築
  ```
  pyenv virtualenv 3.7.3 MLvr3
  ```
## 3. 該当ディレクトリに仮想環境を設定
  ```
  pyenv local MLvr3
  ```
## 4. 必要ライブラリをインストール
  ```
  pip install --upgrade pip
  pip install -r pckg.list
  ```
## 5. graphviz本体をインストールする
  * https://www.graphviz.org/download/
  ```
  # [mac]
  brew install graphviz
  # windows
  http://ruby.kyoto-wu.ac.jp/info-com/Softwares/Graphviz/

  ```

# 在 Ubuntu 中安装 Python 3.10

1. sudo add-apt-repository ppa:deadsnakes/ppa
2. sudo apt update
3. sudo apt install python3.10

# 使用 update-alternatives 切换版本

先查看旧的 python 版本

python3 --version

sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python***  1

sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 2

选择 python 版本

sudo update-alternatives --config python3

# python 创建虚拟环境
python3 -m venv venv

报错的话可能是没有 venv 模块，安装一下即可 sudo apt install python3-venv -y

检查一下：python3 -m venv -h

# pip3 命令找不到
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10



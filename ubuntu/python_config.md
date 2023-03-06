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

报错的话可能是没有 venv 模块

```
错误的安装方式： sudo apt install python3-venv -y

https://discuss.python.org/t/cannot-create-venv-for-python-3-10/11784/5

Trying to create venv for Python 3.10 using "python3.10 -m venv venv get error message:

Error: Command ‘[’/home/shawn/dev/py/proj1/venv/bin/python3.10’, ‘-Im’, ‘ensurepip’, ‘–upgrade’, ‘–default-pip’]’ returned non-zero exit status 1.

directory venv is created but the activate files are not created…

What am I doing wrong.

Thank you - mistake was not installing python3.10-venv. I had python3-venv installed but not 3.10.
```
安装 venv 需要和自身的 python 版本相匹配

sudo apt install python3.10-venv -y

# pip3 命令找不到
```
错误示例：sudo apt install python3-pip

python3-pip is already the newest version (9.0.1-2.3~ubuntu1.18.04.8)
```
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10



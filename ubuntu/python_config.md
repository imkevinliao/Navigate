# 在 Ubuntu 中安装 Python 3.10

补充知识：Linux 中我们使用包管理工具安装软件（apt dnf yum）,这些包管理工具都是有源，我们下载软件时候会从指定网站去查找软件并下载，但是有些时候某些软件我们不能从Linux发行版本的默认源中找到，故而需要添加源，告诉包管理工具从这里面查找 `sudo add-apt-repository ppa:deadsnakes/ppa`

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

# update-alternatives
update-alternatives --help
```
用法：update-alternatives [<选项> ...] <命令>

命令：
  --install <链接> <名称> <路径> <优先级>
    [--slave <链接> <名称> <路径>] ...
                           在系统中加入一组候选项。
  --remove <名称> <路径>   从 <名称> 替换组中去除 <路径> 项。
  --remove-all <名称>      从替换系统中删除 <名称> 替换组。
  --auto <名称>            将 <名称> 的主链接切换到自动模式。
  --display <名称>         显示关于 <名称> 替换组的信息。
  --query <名称>           机器可读版的 --display <名称>.
  --list <名称>            列出 <名称> 替换组中所有的可用候选项。
  --get-selections         列出主要候选项名称以及它们的状态。
  --set-selections         从标准输入中读入候选项的状态。
  --config <名称>          列出 <名称> 替换组中的可选项，并就使用其中
                           哪一个，征询用户的意见。
  --set <名称> <路径>      将 <路径> 设置为 <名称> 的候选项。
  --all                    对所有可选项一一调用 --config 命令。

<链接> 是指向 /etc/alternatives/<名称> 的符号链接。
    (如 /usr/bin/pager)
<名称> 是该链接替换组的主控名。
    (如 pager)
<路径> 是候选项目标文件的位置。
    (如 /usr/bin/less)
<优先级> 是一个整数，在自动模式下，这个数字越高的选项，其优先级也就越高。

选项：
  --altdir <目录>          改变候选项目录。
  --admindir <目录>        设置 statoverride 文件的目录。
  --log <文件>             改变日志文件。
  --force                  就算没有通过自检，也强制执行操作。
  --skip-auto              在自动模式中跳过设置正确候选项的提示
                           (只与 --config 有关)
  --verbose                启用详细输出。
  --quiet                  安静模式，输出尽可能少的信息。不显示输出信息。
  --help                   显示本帮助信息。
  --version                显示版本信息。
```
```
update-alternatives  --get-selections | grep py
获取所有的可以配置的选项

update-alternatives --config editor
将ubuntu的默认编辑器从nano切换成vim
```
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

# 使用软链接（快捷方式）
```
sudo ln -s /usr/bin/python3 /usr/bin/py3

sudo ln -s /usr/bin/python2 /usr/bin/py2

删除软链接（注意，这里不是 sudo rm -rf /usr/bin/py3/)
sudo rm -rf /usr/bin/py2
sudo rm -rf /usr/bin/py3
```
# 配置虚拟环境
激活虚拟环境 source venv/bin/activate

关闭虚拟环境 deactivate

激活虚拟环境 source 后跟 activate 的绝对或者相对路径
# pip3 命令找不到
```
示例(可能存在错误)：sudo apt install python3-pip

python3-pip is already the newest version (9.0.1-2.3~ubuntu1.18.04.8)
```
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10



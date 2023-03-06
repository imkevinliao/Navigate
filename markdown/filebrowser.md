# filebrowser introduce
filebrowser定位应该算是一款轻量级云盘，全平台通用，当然我肯定是以Linux为主。

# filebrowser deploy
部署过程中如果遇到问题后面会详细解答，此处部署为正常流程没有以外的情况。

这个是官方提供的下载方式，会看到：Putting filemanager in /usr/loacl/bin，这表示filebrowser在该目录下（注意！后面在写filebrowser.service文件需要使用）
```
curl -fsSL https://raw.githubusercontent.com/filebrowser/get/master/get.sh | bash
```

基础配置：三条命令请一条条分别执行
```
sudo filebrowser -d /etc/filebrowser.db config init
sudo filebrowser -d /etc/filebrowser.db config set --address 0.0.0.0
sudo filebrowser -d /etc/filebrowser.db config set --port 8080
```

此时已经可以使用了：filebrowser -d /etc/filebrowser.db （但请先不要使用，所有对filebrowser.db的修改都需要先关闭服务，所以这里请不要启动服务!!!）

将filebrowser添加到守护进程中，随linux服务器自启：（我们不希望每次重启linux后，还要去重新手动启动filebrowser服务）
```
sudo vim /usr/lib/systemd/system/filebrowser.service

如果上面的路径不存在则选择下面的

sudo vim /etc/systemd/system/filebrowser.service
```

编写service文件，复制以下内容，简要说明ExecStart=/usr/local/bin/filebrowser -d /etc/filebrowser.db，这个根据你filebrowser的实际位置填写，就是之前提到的要注意。（另自行查找vim的基本使用，通常复制好下面的文本后按p即可复制，然后:wq退出vim即可，vim不展开说了，cat进去也是可以的）
```
[Unit]
Description=File browser
After=network.target

[Service]
ExecStart=/usr/local/bin/filebrowser -d /etc/filebrowser.db

[Install]
WantedBy=multi-user.target
```

此时我们可以启动filebrowser了吗？我的回答是暂时还不可以，我们还需要配置用户名和密码，这里有很多内容，我后面展开说。实际上一行命令就可以，但是我给了两条，是因为不清楚你在配置的时候是否会遇到问题，所以给通解。
```
sudo filebrowser users add [user_name] [user_password] --perm.admin -d /etc/filebrowser.db
sudo filebrowser users update [user_name] --password [user_password] -d /etc/filebrowser.db
```
请自己设置用户名密码，举例：
```
sudo filebrowser users add admin 123456 --perm.admin -d /etc/filebrowser.db
sudo filebrowser users update admin --password 123456 --perm.admin -d /etc/filebrowser.db
```

将filebrowser加入到开机启动中
```
sudo systemctl enable filebrowser.service
```

至此配置完成，然后我们启动filebrowser
```
sudo systemctl start filebrowser.service
```

附带查看filebrowser状态和停止命令
```
sudo systemctl status filebrowser.service
sudo systemctl stop filebrowser.service
```

最后登录界面：浏览器中，你服务器的ip地址加上端口即可，端口就是之前配置的8080

例如你的ip是127.0.0.1，访问则是：127.0.0.1:8080，就可以看到登录界面了，然后输入我们之前设置的用户名和密码就可以登陆了。

# 答疑解惑

filebrowser的部署其实是很简单的事情，但是一开始接触的时候花了不少时间理解，一度觉得很难用，第三方教程不多，而且有些地方没说清楚。

## 安装问题（网络）
例如死在第一步：curl -fsSL https://raw.githubusercontent.com/filebrowser/get/master/get.sh | bash

国内如果因为网络原因无法访问使用脚本的情况（我就遇到了，头疼），直接去下载源文件

源文件地址：https://github.com/filebrowser/filebrowser/releases/download/v2.22.3/linux-amd64-filebrowser.tar.gz

如果失效请自行搜索查找filebrowser.tar.gz压缩文件即可，然后拷贝到远程服务器（linux）

解压文件（命令）：tar -xzvf linux-amd64-filebrowser.tar.gz

解压出的文件只需要关心其中一个即可，就是把解压出来的filebrowser复制到/usr/local/bin/ 就好了(sudo cp filebrowser /usr/local/bin/)

## 权限问题
所有命令执行前，非root用户请使用sudo提权，root用户请无视，基本都需要root权限

# 用户问题
很多人安装filebrowser发现无法登录，用户名密码错误之类的，官方文档中说的是默认用户名密码都是:admin，第三方文档有说用户:admin，密码:admin123。

个人试了很多次，基本都是没有用，所以上面对用户名密码的设置，第一个命令是增加用户名:admin，密码是:123456，用户权限为管理员权限，第二个命令是更新用户名和密码，filebrowser在不停的更新中，所以不清楚。

# ip:port 无法访问
排查方式：
1. 先检查file browser是否开启，systemctl status查看
2. 排查端口是否开放（我的问题是服务器提供商有防火墙，导致端口未开放），telnet工具可以快速检测能否正常连接端口，通常无法访问肯定是连不上
3. 端口问题，可能是服务器提供商的防火墙，也可能是服务器自身的防火墙


# 补充1
所有对filebrowser.db的操作都需要先停止服务！！！

设置日志位置：filebrowser -d /etc/filebrowser.db config set –log /var/log/filebrowser.log

设置语言环境：filebrowser -d /etc/filebrowser.db config set –locale zh-cn

其实上面的都没必要，因为登录界面后全都可以在图形化界面去设置，包括增加用户，修改密码，设置路径（上述并没有指定文件路径通常会默认根路径，也就是登录filebrowser后你会看到linux的“/”路径下的文件，可以在设置中自行调整）。图形界面可以完成的事情，没必要命令行处理，对于大部分习惯界面用户的人来说。

# 补充2
一开始在网上查找教程的时候总是能看到下面这种，其实就是另外一种方式罢了，仅供参考。.json和.db都是filebrowser的配置文件，这个也在一开始时候让人很恼火，很多网上教程有json的有db的。
```
vi /etc/filebrowser/config.json
filebrowser -c config.json
{
　　"port": 8090,
　　"address": "0.0.0.0",
　　"noAuth": false,
　　"password":"12345678",
　　"root":"/data/fbroot",
　　"alternativeReCaptcha": false,
　　"reCaptchaKey": "",
　　"reCaptchaSecret": "",
　　"database":"/etc/filebrowser/filebrowser.db",
　　"log":"/var/log/filebrowser.log",
　　"plugin": "",
　　"baseURL": "/filebrowser",
　　"allowCommands": true,
　　"allowEdit": true,
　　"allowNew": true,
　　"commands": [
　　　　"ls",
　　　　"df"
　　]
}
```

# https 域名问题
这个问题涉及到另外的部分，ssl证书这块对于很多小白而言就很麻烦，还需要域名什么的，如果是完全不了解的人实在是太困难了，个人始终认为作为工具，做好该做的事情就足够了。对于爱折腾的人来说，这里不需要我介绍，对于不爱折腾的人来说，别折磨自己。

# 官方文档的问题
刚开始接触filebrowser的时候看不懂那些命令，因为尝试执行的时候报错，后面渐渐就明白了，参看添加用户的命令，应该有助于理解官方文档中的命令该怎么写。

<https://filebrowser.org/installation>

<https://filebrowser.org/cli/filebrowser-users-add>
# 脚本
有想过把这一系列操作写出bash脚本，拷贝脚本后直接执行就可以完成上述所有操作

但是，想来自己没有时间维护，不能维护的脚本实际意义并不大，不是批量部署，有能力的人会自己写，没能力的人也如果脚本遇到问题也很难用。


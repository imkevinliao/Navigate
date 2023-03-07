# ssh 远程登录
本地生成密钥（一路回车） ssh-keygen

拷贝公钥到远程服务器 ssh-copy-id -i ~/.ssh/id_rsa.pub ubuntu@xxx.xxx.xxx.xxx

免密登录 ssh ubuntu@xxx.xxx.xxx.xxx

在bashrc中配置别名 vim ~/.bashrc 

alias cn = 'ssh ubuntu@xxx.xxx.xxx.xxx'

生效配置 source ~/.bashrc

后续登录服务器就可以直接使用别名了 

cn 直接登录

退出 ssh 登录状态 logout 命令

# ssh 配置
<sshd_config 参考>[https://developer.aliyun.com/article/972993]

文件路径： /etc/ssh/sshd_config

禁止 root 用户远程密码登录 PermitRootLogin prohibit-password

对于 PermitRootLogin 有 yes 和 no 代表着允许和不允许 root 用户登录，而 prohibit-password 代表着不允许 root 用户密码登录，而可以密钥登录

禁用密码登录：PasswordAuthentication no

启用密钥验证：PubkeyAuthentication yes

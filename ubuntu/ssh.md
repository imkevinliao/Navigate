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
[sshd_config 参考](https://developer.aliyun.com/article/972993)


文件路径： /etc/ssh/sshd_config

禁止 root 用户远程密码登录 PermitRootLogin prohibit-password

对于 PermitRootLogin 有 yes 和 no 代表着允许和不允许 root 用户登录，而 prohibit-password 代表着不允许 root 用户密码登录，而可以密钥登录

禁用密码登录：PasswordAuthentication no

启用密钥验证：PubkeyAuthentication yes

禁止空密码：PermitEmptyPasswords no

修改配置后重启服务（使生效）：sudo systemctl restart sshd

# ssh 免密登录失败

https://blog.csdn.net/moakun/article/details/104095404

1. 检查服务器用户目录，例如用户为kevin，/home/kevin  目录权限必须是：755
2. 检查服务器用户目录下的.ssh目录，/home/kevin/.ssh 目录权限必须是：700
3. 检查authorized_keys文件权限，必须是600或者644，该文件位于/home/kevin/.ssh/authorized_keys

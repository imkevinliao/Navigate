本地生成密钥（一路回车） ssh-keygen

拷贝公钥到远程服务器 ssh-copy-id -i ~/.ssh/id_rsa.pub ubuntu@xxx.xxx.xxx.xxx

免密登录 ssh ubuntu@xxx.xxx.xxx.xxx

在bashrc中配置别名 vim ~/.bashrc 

alias cn = 'ssh ubuntu@xxx.xxx.xxx.xxx'

生效配置 source ~/.bashrc

后续登录服务器就可以直接使用别名了 

cn 直接登录

退出 ssh 登录状态 logout 命令

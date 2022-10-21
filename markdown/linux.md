列出所有由人创建的用户：
```
command1: cut -d: -f1,3 /etc/passwd | egrep ':[0-9]{4}$' | cut -d: -f1   
command2: awk -F: '$3 >= 1000 && $1 != "nobody" {print $1}' /etc/passwd   
```

删除最新的解压文件：[参考链接](https://www.commandlinefu.com/commands/view/2573/remove-all-files-previously-extracted-from-a-tar.gz-file)
```
tar -tf <file.tar.gz> | parallel rm
```

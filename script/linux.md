列出所有由人创建的用户：
```
command1: cut -d: -f1,3 /etc/passwd | egrep ':[0-9]{4}$' | cut -d: -f1   
command2: awk -F: '$3 >= 1000 && $1 != "nobody" {print $1}' /etc/passwd   
```

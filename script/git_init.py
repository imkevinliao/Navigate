import os

"""
配置说明：
请修改 cmd_user 为自己的用户名和邮箱地址
git在windows下，默认是CRLF作为换行符，git add 提交时，检查文本中有LF 换行符（linux系统里面的），则会告警。所以问题的解决很简单，让git忽略该检查即可 git config --global core.autocrlf false
git status不能显示中文的问题也需要对core进行配置，还需要在gitbash终端设置本地Local为zh_CN，字符集为UTF-8
"""

"""
个人更喜欢这个：git config --global alias.lg "log --no-merges --color --graph --date=format:'%Y-%m-%d %H:%M:%S' --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Cblue %s %Cgreen(%cd) %C(bold blue)<%an>%Creset' --abbrev-commit"
这个更详细一些：git config --global alias.lg "log --no-merges --color --stat --graph --date=format:'%Y-%m-%d %H:%M:%S' --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Cblue %s %Cgreen(%cd) %C(bold blue)<%an>%Creset' --abbrev-commit"
网上通常是这个：git config --global alias.lg --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cd) %C(bold blue)<%an>%Creset' --abbrev-commit --
"""

git_lg = """ git config --global alias.lg "log --no-merges --color --graph --date=format:'%Y-%m-%d %H:%M:%S' --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Cblue %s %Cgreen(%cd) %C(bold blue)<%an>%Creset' --abbrev-commit" """

def git_command():
    cmd = []
    cmd_user = ['git config --global user.name "imkevinliao"', 'git config --global user.email "imkevinliao@gmail.com"']
    cmd_encode = ['git config --global core.autocrlf false', 'git config --global core.safecrlf true']
    cmd_chinese = ['git config --global core.quotepath false']
    cmd_alias = ['git config --global alias.gp pull', 'git config --global alias.br branch',
                 'git config --global alias.co checkout', 'git config --global alias.ci commit',
                 'git config --global alias.st status', git_lg]
    cmd_editor = ['git config --global core.editor vim']
    cmd.extend(cmd_user)
    # cmd.extend(cmd_encode)
    # cmd.extend(cmd_chinese)
    cmd.extend(cmd_alias)
    cmd.extend(cmd_editor)
    return cmd


def exec_command(commands):
    for _ in commands:
        os.system(_)
    print(f'show git config you set:')
    os.system("cd ~ && cat .gitconfig")


if __name__ == '__main__':
    exec_command(git_command())
    ...

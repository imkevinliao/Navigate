import os

"""
有的时候会因为编码问题导致clone的代码在本地无法正常编译，需要对乱码问题进行处理
git status不能显示中文的问题也需要对core进行配置，还需要在gitbash终端设置本地Local为zh_CN，字符集为UTF-8
"""


def git_command():
    cmd = []
    cmd_user = ['git config --global user.name "imkevinliao"', 'git config --global user.email "imkevinliao@gmail.com"']
    cmd_encode = ['git config --global core.autocrlf true', 'git config --global core.safecrlf true']
    cmd_chinese = ['git config --global core.quotepath false']
    cmd_alias = ['git config --global alias.gp pull', 'git config --global alias.br branch',
                 'git config --global alias.co checkout', 'git config --global alias.ci commit',
                 'git config --global alias.st status',
                 "git config --global alias.lg --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cd) %C(bold blue)<%an>%Creset' --abbrev-commit --"]
    cmd_editor = ['git config --global core.editor vim']
    # cmd.extend(cmd_user)
    cmd.extend(cmd_user)
    cmd.extend(cmd_encode)
    cmd.extend(cmd_chinese)
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

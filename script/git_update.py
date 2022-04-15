import os


def find_git(path_dirs):
    my_list = []
    for _ in path_dirs:
        filepath, fullname = os.path.split(_)
        if '.git' == fullname:
            my_list.append(filepath)
    return my_list


def get_dirs():
    path_dirs = []
    num = 0
    for root, dirs, files in os.walk(main_path):
        for dir_name in dirs:
            path_dirs.append(os.path.join(root, dir_name))
    return path_dirs


def repo_update(git_dirs):
    for _ in git_dirs:
        os.chdir(_)
        print("current directory is:",end=' ')
        os.system("pwd")
        os.system("git pull")


if __name__ == '__main__':
    main_path = r'/root'
    repo_update(find_git(get_dirs()))
    ...

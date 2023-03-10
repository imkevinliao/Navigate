import re

from log import Log
from shell import Shell


def config_python(py_inst: Shell):
    """
    包括配置python源，下载python，切换python版本
    """
    commands_python = ["sudo add-apt-repository ppa:deadsnakes/ppa", "sudo apt update",
                       "sudo apt install python3.10 -y"]
    py_inst.popen()
    
    py_inst.set_commands(commands_python)
    
    commands_python = ["python3 --version"]
    py_inst.set_commands(commands_python)
    res = py_inst.run()[0][1].strip()
    regex = r"3.\d+"
    match_result = re.search(regex, res)
    if match_result:
        python_version = match_result.group()
    else:
        python_version = None
    
    commands_python = ["sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 0"]
    if python_version:
        commands_python.append(
            f"sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python{python_version} 1")
    else:
        log.info(f"没有获取到系统当前的python3版本")
    py_inst.set_commands(commands_python)
    py_inst.run()
    ...


if __name__ == '__main__':
    log = Log(log_filepath="./shell.log", logfile_mode="w+")
    inst = Shell()
    config_python(inst)

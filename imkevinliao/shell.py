import subprocess
from concurrent.futures import ThreadPoolExecutor

from util import decode


class Shell:
    """
    run，popen，popen_multi
    这三个函数返回 list[tuple(command,command_result)]；无论命令是否执行成功，都返回该命令以及该命令执行的结果
    
    call 只返回执行后的状态码: 0 表示成功执行，其他值则表示失败
    
    popen popen_multi 会在控制台实时显示结果
    run 不在控制台显示结果
    """
    
    def __init__(self, cmds: list = None):
        self.__LINUX_EXECUTE_OK = 0
        self.__commands = cmds
        if self.__commands:
            self.__check_commands(self.__commands)
    
    def set_commands(self, commands: list):
        self.__check_commands(commands)
        self.__commands = commands
    
    @staticmethod
    def __check_commands(commands):
        if not isinstance(commands, list):
            raise Exception("Commands must be list, please check your commands")
        for i in commands:
            if not isinstance(i, str):
                raise Exception("Command must be string, please check your commands")
    
    def call(self):
        for cmd in self.__commands:
            ret = subprocess.call(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE)
            return ret
    
    def run(self) -> list:
        run_results = []
        for cmd in self.__commands:
            completed = subprocess.run(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
            if self.__LINUX_EXECUTE_OK == completed.returncode:
                result = decode(completed.stdout)
                run_results.append((cmd, result))
            else:
                result = decode(completed.stderr)
                error_msg = "Executing Failed, Status Code: " + str(completed.returncode) + "error_info: " + result
                run_results.append((cmd, error_msg))
        return run_results
    
    @staticmethod
    def __popen_core(task):
        process = subprocess.Popen(task, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        
        for info in iter(process.stdout.readline()):
            print(info)
        output, err = process.communicate()
        if err:
            error_info = decode(process.stderr)
            error_msg = "Executing Failed, Status Code: " + str(process.returncode) + "error_info: " + error_info
            result = (task, error_msg)
        else:
            task_info = decode(process.stdout)
            result = (task, task_info)
        process.kill()
        return result
    
    def popen_multi(self, max_threads=10):
        results = []
        pool = ThreadPoolExecutor(max_workers=max_threads)
        tasks = self.__commands
        for task in tasks:
            result = pool.submit(self.__popen_core, task)
            results.append(result)
        pool.shutdown()
        return results
    
    def popen(self):
        results = []
        for cmd in self.__commands:
            result = self.__popen_core(cmd)
            results.append(result)
        return results

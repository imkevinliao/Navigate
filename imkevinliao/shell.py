import subprocess
from concurrent.futures import ThreadPoolExecutor

from util import decode


class Shell:
    """
    对于 subprocess：run popen call 的封装
    run 单个命令安全运行（逐个进行）无法实时查看控制台输出，只能在执行结束后查看
    popen 单个命令运行过程还需要查看控制台输出popen，多线程执行程序（可以但是不推荐）
    call 无需知道命令执行后的输出，仅仅判断命令是否执行正常（最安全）
    
    安全程度 call（最安全）  popen（最不安全）
    尽可能用 run 和 call 确保安全
    """
    
    def __init__(self, cmds: list = None):
        self.__LINUX_EXECUTE_OK = 0
        self.__LINUX_EXECUTE_FAILED = -1
        self.__commands = cmds
        if self.__commands:
            self.__check_commands(self.__commands)
    
    def set_commands(self, commands):
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
            if self.__LINUX_EXECUTE_OK == ret:
                return self.__LINUX_EXECUTE_OK
            else:
                return self.__LINUX_EXECUTE_FAILED
    
    def run(self) -> list:
        """
        返回 list[tuple(command,command_result)]
        """
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
        # 返回 list[tuple(command,command_result)]
        results = []
        pool = ThreadPoolExecutor(max_workers=max_threads)
        tasks = self.__commands
        for task in tasks:
            result = pool.submit(self.__popen_core, task)
            results.append(result)
        pool.shutdown()
        return results
    
    def popen(self):
        # 返回 list[tuple(command,command_result)]
        results = []
        for cmd in self.__commands:
            result = self.__popen_core(cmd)
            results.append(result)
        return results

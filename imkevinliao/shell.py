import subprocess
import warnings
from concurrent.futures import ThreadPoolExecutor

from util import decode


class Shell:
    """
    run, popen, popen_multi
    返回值都是list[tuple[int, str]] 即：执行状态码 和 执行结果
    注：状态码为 0 表示成功，其他表示失败
    """
    
    def __init__(self, cmds: list = None):
        self.__ExecutionStatus = None  # True or False
        self.__commands = cmds
        self.__record = False
        self.records = []
        if self.__commands:
            self.__check_commands(self.__commands)
    
    def enable_record(self):
        self.__record = True
    
    def close_record(self):
        self.records = []
    
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
        warnings.warn("该方法被废弃，请使用run", DeprecationWarning)
        for cmd in self.__commands:
            completed = subprocess.run(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
            ret = completed.returncode
            return ret
    
    @staticmethod
    def __msg(status_code, msg_cmd, msg_result) -> str:
        if status_code == 0:
            status = "True"
        else:
            status = "False"
        cmd_info = f"execute command:{msg_cmd}\nexecute status:{status}\n"
        cmd_result = f"execute result:\n {msg_result}\n"
        result = cmd_info + cmd_result
        return result
    
    def run(self) -> list[tuple[int, str]]:
        run_results = []
        for cmd in self.__commands:
            completed = subprocess.run(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
            ret = completed.returncode
            result = self.__msg(ret, cmd, decode(completed.stdout))
            run_results.append((ret, result))
        if self.__record:
            self.records.extend(run_results)
        return run_results
    
    def __popen_core(self, task):
        process = subprocess.Popen(task, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        
        for info in iter(process.stdout.readline()):
            print(info)
        stdout, stderr = process.communicate()
        print(decode(stderr))
        ret = process.returncode
        if ret == 0:
            result = self.__msg(ret, task, decode(stdout))
        else:
            result = self.__msg(ret, task, decode(stderr))
        run_result = (task, result)
        process.kill()
        return run_result
    
    def popen_multi(self, max_threads=10):
        results = []
        pool = ThreadPoolExecutor(max_workers=max_threads)
        tasks = self.__commands
        for task in tasks:
            result = pool.submit(self.__popen_core, task)
            results.append(result)
        pool.shutdown()
        if self.__record:
            self.records.extend(results)
        return results
    
    def popen(self):
        run_results = []
        for cmd in self.__commands:
            result = self.__popen_core(cmd)
            run_results.append(result)
        if self.__record:
            self.records.extend(run_results)
        return run_results

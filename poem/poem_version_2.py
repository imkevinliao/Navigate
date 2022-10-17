import json
import logging
import multiprocessing
import os
import sys
import time
from multiprocessing import Manager

import mariadb
import opencc

# global config
isDirectInsert = True  # check the value if exists, before insert,Recommend True.
isSimplifiedChinese = True  # origin data is Traditional Chinese,Recommend True.
isDropTable = False  # if true,table will be dropped,include data of table,Recommend False
INSERT_NUMBER = 500  # Recommend 500
isMultiProcess = True
shi_path = r"D:\chinese-poetry-master\json"
ci_path = r"D:\chinese-poetry-master\ci"

# config mariadb connect
pool = mariadb.ConnectionPool(
    pool_name='pools',
    pool_size=4,
    host='127.0.0.1',
    user='root',
    password='root',
    database='test2',
)

# config log encoding 参数需要 python3.9及以上版本，配置目的为了防止logging中文乱码
LOG_FORMAT = "%(asctime)s %(levelname)s [line:%(lineno)d] %(message)s"
LOG_DATE_FORMATE = "%Y-%m-%d %H:%M:%S(%p)"
LOG_FILENAME = "poem.log"
logging.basicConfig(format=LOG_FORMAT, datefmt=LOG_DATE_FORMATE, level=logging.DEBUG, filename=LOG_FILENAME,
                    encoding="utf-8")


class Table(object):
    def __init__(self, table_name: str, primary_key: str, column_name: list, column_desc: list,
                 column_info: dict = None):
        self.table_name = table_name
        self.primary_key = primary_key
        self.column_name = column_name
        self.column_desc = column_desc
        if column_info:
            self.column_info = column_info
        else:
            self.column_info = dict(zip(column_name, column_desc))

    def show(self):
        sql_str = ""
        for key, value in self.column_info.items():
            sql_str = sql_str + key + " " + value + ","
        table = f"""
            create table if not exists {self.table_name}(
                {sql_str}
                primary key ({self.primary_key})
            );
        """
        print(table)


def timeit(func):
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        # logging.debug(f'Function {func.__name__} args:{args} kwargs:{kwargs} Took {total_time:.4f} seconds')
        logging.debug(f'Function {func.__name__} Took {int(total_time) // 3600} hours '
                      f'{int(total_time // 60)} minutes {int(total_time % 60)} seconds')
        return result

    return timeit_wrapper


def create_table(table_name: str, primary_key: str, column_name: list, column_desc: list):
    column_info = dict(zip(column_name, column_desc))
    sql_str = ""
    for key, value in column_info.items():
        sql_str = sql_str + key + " " + value + ","
    create = f"""
        create table if not exists {table_name}(
            {sql_str}
            primary key ({primary_key})
        );
    """
    logging.debug(f"create info {create}")
    return create


def drop_table(table_name):
    drop = "drop table " + table_name
    return drop


def t2s(data):
    """
    Traditional to Simplified.
    Data type can be list, str, tuple.
    input data == return data
    """
    cc = opencc.OpenCC("t2s.json")
    if isinstance(data, list):
        result = []
        for i in data:
            result.append(cc.convert(i))
        return result
    elif isinstance(data, str):
        result = cc.convert(data)
        return result
    elif isinstance(data, tuple):
        result = []
        for i in data:
            result.append(cc.convert(i))
        result = tuple(result)
        return result
    else:
        logging.debug("args type out of range!!!")


def get_json_paths(root_path) -> list:
    """
    获取指定路径下符合条件的文件的绝对路径
    :param root_path:
    :return:
    """
    dirs = os.listdir(root_path)
    filter_paths = []
    for file in dirs:
        if '0' in file and 'json' in file:  # 唐诗&宋词
            filter_paths.append(os.path.join(root_path, file))
    if not filter_paths:
        logging.warning(f"No file that meets the rule exists in the directory :{root_path}")
    logging.debug(f"after filter path is {filter_paths}")
    return filter_paths


def get_json_data(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def set_table(table_name):
    table_name = table_name
    if table_name == 'shi':
        primary_key = 'id'
        column_name = ["id", "title", "author", "dynastic", "content", "self_id", "simple"]
        column_desc = ["int not null auto_increment", "varchar(255)", "varchar(255)", "varchar(255)", "text",
                       "varchar(255)", "varchar(255)"]
    elif table_name == 'ci':
        primary_key = 'id'
        column_name = ["id", "title", "author", "dynastic", "content"]
        column_desc = ["int not null auto_increment", "varchar(255)", "varchar(255)", "varchar(255)", "text"]
        ...
    else:
        sys.exit()
    tb = Table(table_name, primary_key, column_name, column_desc)
    return tb


def save_to_mariadb(tb: Table, paths: list):
    conn = pool.get_connection()
    cursor = conn.cursor()
    if isDropTable:
        cursor.execute(drop_table(tb.table_name))
    cursor.execute(create_table(tb.table_name, tb.primary_key, tb.column_name, tb.column_desc))
    for file_path in paths:
        logging.info(f"Processing file:{file_path}")
        data = get_json_data(file_path)
        mult_data = []
        for index, value in enumerate(data):
            if tb.table_name == "shi":
                column_names = (tb.column_name[1], tb.column_name[2], tb.column_name[4], tb.column_name[5])
                column_value = (value["title"], value["author"], ''.join(value["paragraphs"]), value["id"])
            elif tb.table_name == "ci":
                column_names = (tb.column_name[1], tb.column_name[2], tb.column_name[4])
                column_value = (value["rhythmic"], value["author"], ''.join(value["paragraphs"]))
            else:
                sys.exit()
            if isSimplifiedChinese:
                column_value = t2s(column_value)

            column_fills = f"({(len(column_names) - 1) * '?,' + '?'})"
            column_str = ''
            for i, j in enumerate(column_names):
                if i == len(column_names) - 1:
                    column_str = column_str + j
                else:
                    column_str = column_str + j + ","
            column_str = "(" + column_str + ")"
            if INSERT_NUMBER > 1:
                mult_data.append(column_value)
                if (len(mult_data) == INSERT_NUMBER) or (index == (len(data) - 1)):
                    cursor_new = conn.cursor()
                    cursor_new.executemany(f"insert into {tb.table_name} {column_str} values {column_fills}", mult_data)
                    cursor_new.close()
                    mult_data = []
            else:
                cursor.execute(f"insert into {tb.table_name} {column_str} values {column_fills}", column_value)
                logging.debug(f"""sql command is "insert into {tb.table_name} {column_str} values {column_fills}" """)

    conn.commit()
    conn.close()


def error(value):
    print(f'error:{value}')


def core_exec():
    if isMultiProcess:
        logging.info("now multiprocess:")
        multi_core = multiprocessing.Pool(processes=3)
        multi_core.apply_async(save_to_mariadb, args=(set_table("ci"), get_json_paths(ci_path)), error_callback=error)
        multi_core.apply_async(save_to_mariadb, args=(set_table("shi"), get_json_paths(shi_path)), error_callback=error)
        multi_core.close()
        multi_core.join()
    else:
        save_to_mariadb(set_table("ci"), get_json_paths(ci_path))
        save_to_mariadb(set_table("shi"), get_json_paths(shi_path))


def log_init():
    logging.info("Program start...")
    logging.info(f"params:\nisDirectInsert is:{isDirectInsert};isSimplifiedChinese is:{isSimplifiedChinese}\n"
                 f"isDropTable is:{isDropTable};INSERT_NUMBER is:{INSERT_NUMBER}\n"
                 f"shi_path is:{shi_path};ci_path is{ci_path}")


if __name__ == '__main__':
    log_init()
    core_exec()

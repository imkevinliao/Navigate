import csv
import logging
import sys
import time

from easydict import EasyDict
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

LOGIN_WAIT = 3
SELECT_PAGE_WAIT = 3
PAGE_DOWNLOAD_WAIT = 3
IMPLICITLY_WAIT = 10
PAGE_START = 90
PAGE_END = PAGE_START + 10

out_filepath = "../out/requests.csv"
is_write_header = False


def save_to_csv(data):
    with open(out_filepath, mode="a+", newline="") as csvfile:
        fieldnames = ["统一社会信用代码", "企业名称", "法定代表人", "注册资本", "实收资本", "注册号", "成立日期",
                      "纳税人识别号", "经营状态", "组织机构代码", "核准日期", "登记机关", "所属省份", "所在城市",
                      "所属行业", "社保缴纳人数", "电话", "邮箱", "曾用名", "营业期限", "企业类型", "国民经济行业名称",
                      "注销日期", "吊销日期", "企业住所", "经营业务范围", "许可经营项目"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        global is_write_header
        if is_write_header:
            writer.writeheader()
            is_write_header = False
        writer.writerows(data)
    print("save ok.")


def config():
    options = Options()
    options.add_argument("--headless")
    options.add_experimental_option("detach", True)  # 禁止自动关闭
    options.add_argument('--disable-gpu')
    options.add_argument("--start-maximized")
    service = Service(r'D:\msedgedriver.exe')
    return webdriver.Edge(service=service, options=options)


def login(edge):
    edge.get(r"https://www.riskbird.com/")
    log = edge.find_element(By.XPATH, '//*[@id="page-header-dom"]/div/div/div/div[3]/ul/li[2]/a')
    edge.execute_script("arguments[0].click();", log)
    # log.click()
    passwd_login = edge.find_element(By.XPATH, '//*[@id="loginPassTabBtn"]')
    passwd_login.click()
    user_name = edge.find_element(By.XPATH, '//*[@id="loginModalInputAccount"]')
    user_password = edge.find_element(By.XPATH, '//*[@id="loginModalInputPwd"]')
    
    user_name.send_keys("your_account_name")
    user_password.send_keys("your_account_password")
    
    login_click = edge.find_element(By.XPATH, '//*[@id="loginPassBtn"]')
    login_click.click()
    time.sleep(LOGIN_WAIT)


def page_info(edge):
    data = EasyDict()
    
    data.统一社会信用代码 = edge.find_element(By.XPATH, '//*[@id="dt_jbxx"]/tbody/tr[1]/td[1]').text
    data.企业名称 = edge.find_element(By.XPATH, '//*[@id="dt_jbxx"]/tbody/tr[1]/td[2]').text
    data.法定代表人 = edge.find_element(By.XPATH, '//*[@id="dt_jbxx"]/tbody/tr[2]/td[1]/a').text
    data.注册资本 = edge.find_element(By.XPATH, '//*[@id="dt_jbxx"]/tbody/tr[2]/td[2]').text
    data.实收资本 = edge.find_element(By.XPATH, '//*[@id="dt_jbxx"]/tbody/tr[2]/td[3]').text
    data.注册号 = edge.find_element(By.XPATH, '//*[@id="dt_jbxx"]/tbody/tr[3]/td[1]').text
    data.成立日期 = edge.find_element(By.XPATH, '//*[@id="dt_jbxx"]/tbody/tr[3]/td[2]').text
    data.纳税人识别号 = edge.find_element(By.XPATH, '//*[@id="dt_jbxx"]/tbody/tr[3]/td[3]').text
    data.经营状态 = edge.find_element(By.XPATH, '//*[@id="dt_jbxx"]/tbody/tr[4]/td[1]').text
    data.组织机构代码 = edge.find_element(By.XPATH, '//*[@id="dt_jbxx"]/tbody/tr[4]/td[2]').text
    data.核准日期 = edge.find_element(By.XPATH, '//*[@id="dt_jbxx"]/tbody/tr[4]/td[3]').text
    data.登记机关 = edge.find_element(By.XPATH, '//*[@id="dt_jbxx"]/tbody/tr[5]/td[1]').text
    data.所属省份 = edge.find_element(By.XPATH, '//*[@id="dt_jbxx"]/tbody/tr[5]/td[2]').text
    data.所在城市 = edge.find_element(By.XPATH, '//*[@id="dt_jbxx"]/tbody/tr[5]/td[3]').text
    data.所属行业 = edge.find_element(By.XPATH, '//*[@id="dt_jbxx"]/tbody/tr[6]/td[1]').text
    data.社保缴纳人数 = edge.find_element(By.XPATH, '//*[@id="dt_jbxx"]/tbody/tr[6]/td[2]').text
    data.电话 = edge.find_element(By.XPATH, '//*[@id="dt_jbxx"]/tbody/tr[6]/td[3]').text
    data.邮箱 = edge.find_element(By.XPATH, '//*[@id="dt_jbxx"]/tbody/tr[7]/td[1]').text
    data.曾用名 = edge.find_element(By.XPATH, '//*[@id="dt_jbxx"]/tbody/tr[7]/td[2]').text
    data.营业期限 = edge.find_element(By.XPATH, '//*[@id="dt_jbxx"]/tbody/tr[7]/td[3]').text
    data.企业类型 = edge.find_element(By.XPATH, '//*[@id="dt_jbxx"]/tbody/tr[8]/td[1]').text
    data.国民经济行业名称 = edge.find_element(By.XPATH, '//*[@id="dt_jbxx"]/tbody/tr[8]/td[2]').text
    data.注销日期 = edge.find_element(By.XPATH, '//*[@id="dt_jbxx"]/tbody/tr[8]/td[3]').text
    data.吊销日期 = edge.find_element(By.XPATH, '//*[@id="dt_jbxx"]/tbody/tr[9]/td[1]').text
    data.企业住所 = edge.find_element(By.XPATH, '//*[@id="dt_jbxx"]/tbody/tr[9]/td[2]').text
    data.经营业务范围 = edge.find_element(By.XPATH, '//*[@id="dt_jbxx"]/tbody/tr[10]/td').text
    data.许可经营项目 = edge.find_element(By.XPATH, '//*[@id="dt_jbxx"]/tbody/tr[11]/td').text
    return data


def core(edge):
    base_url = "https://www.riskbird.com/web/advance/toSearch?code=360800&type=regionid&txt=%E6%B1%9F%E8%A5%BF:%20%E5%90%89%E5%AE%89"
    edge.get(base_url)
    handle = edge.current_window_handle
    csv_data = []
    
    for page in range(PAGE_START, PAGE_END):
        logging.info(f"dealt page start:{page}")
        edge.switch_to.window(handle)
        page_form = edge.find_element(By.XPATH, '//*[@id="tbSearchResult_topage"]/input')
        page_form.clear()
        page_form.send_keys(page)
        page_form.send_keys(Keys.ENTER)
        time.sleep(SELECT_PAGE_WAIT)
        
        elements = edge.find_elements(By.XPATH, '//*[@id="tbSearchResult"]/tbody/tr//a')
        
        for ele in elements:
            edge.execute_script("arguments[0].click();", ele)
            time.sleep(PAGE_DOWNLOAD_WAIT)
            
            handles = edge.window_handles
            for _ in handles:
                if _ != handle:
                    edge.switch_to.window(_)
                    logging.info(f"get url info:{edge.current_url}")
                    try:
                        write_flag = True
                        data = page_info(edge)
                    except Exception as e:
                        write_flag = False
                        with open("../out/error_url.log", "a+", encoding='utf-8') as f:
                            f.write(f"{edge.current_url}\n")
                        logging.error(edge.current_url)
                        logging.error(e)
                    if write_flag:
                        csv_data.append(data)
                    edge.close()
            edge.switch_to.window(handle)
        logging.info(f"dealt page end:{page}")
    save_to_csv(csv_data)


class MyLog(object):
    """
    使用方式，复制class到需要用的地方
    MyLog() or MyLog(log_name = "./out.log")
    """
    
    def __init__(self, log_name=None):
        self.__filename = log_name
        self.my_init()
        ...
    
    @staticmethod
    def test():
        logging.debug("hello debug 中文")
        logging.info("hello info 中文")
        logging.warning("hello warning 中文")
        logging.error("hello error 中文")
    
    def my_init(self):
        logger = logging.getLogger()
        
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter(fmt="%(asctime)s %(levelname)s [line:%(lineno)d] %(message)s",
                                      datefmt="%Y-%m-%d %H:%M:%S(%p)")
        
        stdout_handler = logging.StreamHandler(sys.stdout)
        logger.addHandler(stdout_handler)
        stdout_handler.setFormatter(formatter)
        
        if self.__filename:
            file_handler = logging.FileHandler(filename=self.__filename, encoding='utf-8')
            logger.addHandler(file_handler)
            file_handler.setFormatter(formatter)


if __name__ == '__main__':
    MyLog("../out/requests.log")
    driver = config()
    driver.implicitly_wait(IMPLICITLY_WAIT)
    login(driver)
    core(driver)
    driver.close()

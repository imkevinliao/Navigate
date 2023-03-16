import datetime
import os
import re
from time import localtime

import akshare as ak
import pandas as pd
from matplotlib import pyplot as plt


class AnalyzeStock:
    def __init__(self, csvfile, stock_name=""):
        self.csvfile = csvfile
        self.stock_name = stock_name
        self.data = pd.read_csv(self.csvfile)
        self.__pretreatment()

    def __extract_stock_name(self):
        _, fullname = os.path.split(self.csvfile)
        regex = r"\d{3,8}"
        result = re.findall(regex, fullname)
        if result:
            self.stock_name = result[0]

    def __pretreatment(self):
        self.data["日期"] = pd.to_datetime(self.data["日期"])
        # 如果没有给定股票代号，那么就尝试从文件名中提取
        if not self.stock_name:
            self.__extract_stock_name()

    def stock_info(self):
        data = self.data
        print(f"下面展示文件 {self.csvfile} 的详细数据：{self.stock_name}")
        records = data.shape[0]
        high_price = data["收盘"].max()
        low_price = data["收盘"].min()
        high_price_records = data.loc[data["收盘"] == high_price]
        low_price_records = data.loc[data["收盘"] == low_price]
        print(f"最高价格一共有 {len(high_price_records)} 条，最高价详细数据：\n{high_price_records}")
        print(f"最低价格一共有 {len(low_price_records)} 条，最低价详细数据：\n{low_price_records}")
        print(f"一共有 {records} 条数据，最高：{high_price}, 最低：{low_price}")

    def query_compare(self, compare_price: float, start_time="19700101", end_time="22220101", plot=False):
        s_date = datetime.datetime.strptime(str(start_time), '%Y%m%d').date()
        e_date = datetime.datetime.strptime(str(end_time), '%Y%m%d').date()
        all_data = self.data[self.data["日期"].isin(pd.date_range(s_date, e_date))]
        all_records = all_data.shape[0]
        compare_results_high = all_data[all_data["收盘"] > compare_price]
        compare_records = compare_results_high.shape[0]
        print(f"在查询时间范围内有 {all_records} 条数据，价格高于 {compare_price} 的有 {compare_records} 条记录，"
              f"历史上有 {(compare_records / all_records) * 100:0.2f}% 的时间高于 {compare_price}")
        if plot is True:
            ax = plt.subplot(1, 1, 1)
            plt.title(f"stock {self.stock_name}", color="k")
            plt.plot(all_data["日期"], all_data["收盘"], color="b")
            plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
            plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题
            ax.text(0.8, 0.9, c="b", s="---历史走势", transform=ax.transAxes)
            ax.text(0.8, 0.8, c="r", s="---比较价格", transform=ax.transAxes)
            text = f"数据个数：{all_records}\n高于 {compare_price} 数据个数：{compare_records}"
            ax.text(0.05, 0.9, c="k", s=text, transform=ax.transAxes)
            plt.axhline(y=compare_price, c="r")
            plt.show()


def download(root="./", stock_code=513330):
    hs = ak.index_zh_a_hist(symbol=stock_code, start_date=start_date)
    filepath = "513330.csv"
    hs.to_csv(filepath, encoding='utf-8')
    ...


inst = AnalyzeStock(csvfile=r"513330.csv")
inst.stock_info()
inst.query_compare(compare_price=0.555, plot=True, start_time="20220316")

if __name__ == '__main__':
    # base_path = r"/home/ubuntu"
    # makedirs(base_path) if not exists(base_path) else ...
    time = localtime()
    today = f"{time.tm_year}{str(time.tm_mon).zfill(2)}{str(time.tm_mday).zfill(2)}"
    start_date = "19700101"
    end_data = "22220101"
    # hs = ak.index_zh_a_hist(symbol="513330", start_date=start_date)
    # filepath = "513330.csv"
    # hs.to_csv(filepath, encoding='utf-8')
    # stock_index = ak.stock_zh_index_spot()
    # stock_index_file = "A股指数_" + today + ".csv"
    # save(stock_index, _file=stock_index_file, root_path=base_path)
    #
    # hs300 = ak.index_zh_a_hist(symbol="000300")
    # hs300_file = "沪深300_" + today + ".csv"
    # save(hs300, _file=hs300_file, root_path=base_path)
    #
    # sz50 = ak.index_zh_a_hist(symbol="000016")
    # sz50_file = "上证50_" + today + ".csv"
    # save(sz50, _file=sz50_file, root_path=base_path)
    #
    # zz500 = ak.index_zh_a_hist(symbol="000905")
    # zz500_file = "中证500_" + today + ".csv"
    # save(zz500, _file=zz500_file, root_path=base_path)
    #
    # yh = ak.stock_zh_a_hist(symbol="000792")
    # yh_file = "盐湖股份" + ".csv"
    # save(yh, _file=yh_file, root_path=base_path)

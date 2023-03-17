from ak import AnalyzeStock

inst = AnalyzeStock(csvfile=r"D:\lwx1135395work\PycharmProjects\HISI\res\513330.csv")
inst.basic_info()
inst.query_compare(compare_price=0.407, plot=True, start_time="20220316")

import xlwings as xw
import re

sheet_name = "工作表1"
file_path = r'my.xlsx'

app = xw.App(visible=False)
wb = app.books.open(file_path)
sheet = wb.sheets[sheet_name]
# 将g列第1到第200的数据处理后写入f列
src_data = sheet.range("g1:g200").value

for index, value in enumerate(src_data):
    # 因为存在0~255和0-255两种情况，且-与负号同意义，需要正则判断前后数据
    if value and (('~' in value) or ('-' in value)):
        value = value.replace('~',', ')
        if(re.match(r'\d-\d', value)):
            value = value.replace('-', ', ')
        new_value = '[' + value + ']'
        dst_data = 'f' + str(index + 1) # sheet以1作为第一个数据，而python以0开始，所以需要加1
        sheet.range(dst_data).value = new_value
        wb.save()
wb.close()
app.quit()

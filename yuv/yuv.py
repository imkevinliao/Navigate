import os
import shutil
import struct
import time
import xml.etree.ElementTree as ET

# V350_R02
name = r'R02_PE420'


def modify_xml(file_path: "xml file path", file_formate: "FF_YUV422_PLANAR or FF_YUV420_PLANAR", file_bits: "10 or 8",
               file_bypass: "0 or 1"):
    tree = ET.parse(file_path)
    root = tree.getroot()

    width, height, cright = 64, 4, 63
    root.find('.//img_prop/width').text = str(width)
    root.findall('.//component/hw/cright')[0].text = str(cright)
    root.findall('.//component/hw/cright')[1].text = str(cright)
    root.find('.//img_prop/height').text = str(height)

    # format422, format420 = "FF_YUV422_PLANAR", "FF_YUV420_PLANAR"
    file_format_yuv_in, file_format_yuvfbcd = r'.//img_prop/file_format', r'.//component/write_pic/file_attrib/file_format'

    # file_bits8, file_bits10 = "8", "10"
    file_bits_per_sample_yuv_in, file_bits_per_sample_yuvfbcd = r'.//img_prop/file_bits_per_sample', r'.//component/write_pic/file_attrib/file_bits_per_sample'

    yuv10b = None
    yuv10b_fbcd = r'.//component/hw/yuv10b'

    root.find(file_format_yuv_in).text = str(file_formate)
    root.findall(file_format_yuvfbcd)[0].text = str(file_formate)
    root.findall(file_format_yuvfbcd)[1].text = str(file_formate)

    root.find(file_bits_per_sample_yuv_in).text = str(file_bits)
    # root.findall(file_bits_per_sample_yuvfbcd)[0].text = str(file_bits)
    root.findall(file_bits_per_sample_yuvfbcd)[1].text = str(file_bits)

    # write_pic 的bypass不需要处理
    root.findall(r'.//component/hw/bypass')[0].text = str(file_bypass)
    root.findall(r'.//component/hw/bypass')[1].text = str(file_bypass)

    if file_bits == "10":
        yuv10b = 1
    elif file_bits == "8":
        yuv10b = 0
    root.find(yuv10b_fbcd).text = str(yuv10b)
    root.findall(yuv10b_fbcd)[0].text = str(yuv10b)
    root.findall(yuv10b_fbcd)[1].text = str(yuv10b)

    tree.write(file_path)
    # print(f'文件修改完成：{file_path}\nYUV格式：{file_formate}\n比特位：{file_bits}\n')


def create_yuv_data(m_type='422', bits='8'):
    width, height = 64, 4
    file_name = 'test_in.yuv'
    base_size = width * height
    y_value, u_value, v_value = 2, 4, 8
    dividends_type, dividends_bits = 1, 1
    if m_type == '422':
        dividends_type = 2
    if m_type == '420':
        dividends_type = 4
    if bits == '10':
        dividends_bits = 1
    if bits == '8':
        # 关于8bits数据不对的问题 -> Test
        # base_size = base_size * 2
        dividends_bits = 1
    y_size, u_size, v_size = int(base_size / dividends_bits), int(base_size / dividends_type / dividends_bits), int(
        base_size / dividends_type / dividends_bits)
    y_data = [y_value] * y_size
    u_data = [u_value] * u_size
    v_data = [v_value] * v_size
    yuv_data = y_data + u_data + v_data
    with open(file_name, 'wb') as f:
        for x in yuv_data:
            if bits == '8':
                a = struct.pack('B', x)
            elif bits == '10':
                a = struct.pack('h', x)
            f.write(a)
    # print(f'File created：{file_name}\nType：{m_type}\nBits：{bits}\n')


def copy_yuv():
    src = 'test_in.yuv'
    dst = fr'D:\localrepo\{name}\cpipe_v350\test_image\test_in.yuv'
    shutil.copy2(src, dst)
    # print(f'已复制：{src} 到 {dst}\n')


def print_yuv(file_path, m_type=None, bits=None):
    m_time = time.localtime(os.path.getmtime(file_path))
    format_control = 16
    if m_type == 'in':
        print(f'input data:({format_control} data points per row)')
        print(f'the last modification time of the file：', end=' ')
        print(
            f'{m_time.tm_year}-{m_time.tm_mon:02}-{m_time.tm_mday:02} {m_time.tm_hour:02}:{m_time.tm_min:02}:{m_time.tm_sec:02}')
    elif m_type == 'out':
        print(f'output data：({format_control} data points per row)')
        print(f'the last modification time of the file：', end=' ')
        print(
            f'{m_time.tm_year}-{m_time.tm_mon:02}-{m_time.tm_mday:02} {m_time.tm_hour:02}:{m_time.tm_min:02}:{m_time.tm_sec:02}')
    else:
        print(f'数据：(每行{format_control}个数据)', end='')

    file = open(file_path, 'rb')
    index = 0
    while True:
        if bits == '8':
            context = file.read(1)
        elif bits == '10':
            context = file.read(2)
        try:
            if bits == '8':
                value = struct.unpack('B', context)[0]
            elif bits == '10':
                value = struct.unpack('h', context)[0]
            if index % int(format_control) == 0:
                print()
            index = index + 1
            print(f'{value:6}', end='')
        except Exception:
            ...
        context = file.read(2)
        if not context:
            break
    print(f"\nindex = {index}\n")


def copy_to_result(dst):
    input_yuv_path = fr'D:\localrepo\{name}\cpipe_v350\test_image\test_in.yuv'
    output_yuv_path = fr'D:\localrepo\{name}\cpipe_v350\out\test_out.00000.yuv'
    fbc_xml_path = fr'D:\localrepo\{name}\cpipe_v350\resources\config\test_fbcd.xml'
    if not os.path.exists(dst):
        os.makedirs(dst)
    shutil.copy2(input_yuv_path, dst)
    shutil.copy2(output_yuv_path, dst)
    shutil.copy2(fbc_xml_path, dst)


if __name__ == '__main__':
    # 修改输入bit和输入的格式即可： bit = 8 or 10 , formate = FF_YUV422_PLANAR or FF_YUV420_PLANAR
    input_bits = '10'
    input_formate = "FF_YUV420_PLANAR"
    bypass = 0
    output_date = True
    print(f'input_bits:{input_bits}\ninput_formate:{input_formate}\nbypass_status:{bypass}\n')

    xml_path = fr'D:\localrepo\{name}\cpipe_v350\resources\config\test_fbcd.xml'
    if input_formate == "FF_YUV422_PLANAR":
        input_type = '422'
    elif input_formate == "FF_YUV420_PLANAR":
        input_type = '420'
    modify_xml(file_path=xml_path, file_formate=input_formate, file_bits=input_bits, file_bypass=bypass)
    create_yuv_data(m_type=input_type, bits=input_bits)
    copy_yuv()

    print_yuv(r'test_in.yuv', 'in', bits=input_bits)
    input(f'wait......')
    print_yuv(fr'D:\localrepo\{name}\cpipe_v350\out\test_out.00000.yuv', 'out', bits=input_bits)
    print([f'2^{i}={2 ** i}' for i in range(16)])
    """参考数据 print([f'2^{i}={2 ** i}' for i in range(16)]) ['2^0=1', '2^1=2', '2^2=4', '2^3=8', '2^4=16', 
    '2^5=32', '2^6=64', '2^7=128', '2^8=256', '2^9=512', '2^10=1024', '2^11=2048', '2^12=4096', '2^13=8192', 
    '2^14=16384', '2^15=32768'] """

    # 复制测试的输入输出和xml文件到result中，注意每次使用完后记得修改dir_index的值
    dirs_index = 4
    if input_bits == '8':
        dst = r'D:\localrepo\V350_R02_TestResult\result_00' + str(dirs_index) + r'\8bits' + r'_bypass_' + str(bypass)
    elif input_bits == '10':
        dst = r'D:\localrepo\V350_R02_TestResult\result_00' + str(dirs_index) + r'\10bits' + r'_bypass_' + str(bypass)
    if output_date:
        copy_to_result(dst)
    ...

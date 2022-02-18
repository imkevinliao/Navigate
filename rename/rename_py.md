# 源码
src:[0]C701HIV_M030_f[73]_w[4096]_h[2304]_ISO_56.raw      
dst:C701HIV_M030_id(001)_FID_323331363030313533323035553030_EI_000100s_286_ISO_56_LV_87_ DGAIN_ 1796 _ WHBF_4096_2304_num. 001.raw     
```python3
import os
import re
import shutil
import struct
import xml.etree.ElementTree as ET


def get_dgain(dgain_path):
    dgain = []
    binfile = open(dgain_path, 'rb')
    size = os.path.getsize(dgain_path)
    unsigned_short = 2
    dgain_num = int(size / unsigned_short)
    if dgain_num > 1024:
        dgain_num = 1024
    for i in range(dgain_num):
        data = binfile.read(unsigned_short)
        num = struct.unpack('H', data)
        dgain.append(str(num[0]))
    return dgain


def get_lv(lv_path):
    lv = []
    f = open(lv_path, "r")
    line = f.readline()
    while line:
        lv.append(line.strip())
        line = f.readline()
    return lv


def readXML(file_dir_path):
    xml_name = os.path.join(file_dir_path, r'RawReadBackConfig.xml')
    name_list = []
    info_list = []
    tree = ET.parse(xml_name)
    root = tree.getroot()
    for filename in root.iter("filename"):
        name = filename.text
        if "M030" in name:
            name_list.append(name)
    for algoInfo in root.iter("algoInfo"):
        info_list.append(algoInfo.attrib)
    return name_list, info_list


def get_path():
    dir_paths = []
    cnt = 1
    for root, dirs, files in os.walk(work_path):
        # print(f'第{cnt}次遍历开始')
        # print(f'current root path is {root}')
        for dir_name in dirs:
            real_dir_path = os.path.join(work_path, dir_name)
            dir_paths.append(real_dir_path)
            # print(f'dir name is {dir_name},dir real path is {real_dir_path}')
        for file in files:
            filepath = os.path.join(root, file)
            # print(f'file name is {file},file real path is {filepath}')
        # print(f'第{cnt}次遍历结束')
        cnt += 1
    return dir_paths


def my_rename(name_list, info_list, lv_list, dgain_list, dir_path):
    for i in range(len(name_list)):
        order = str(i + 1).zfill(3)
        name = os.path.splitext(name_list[i])[0]  # 去掉.raw文件类型，取文件名
        name_element = name.split('_')
        name_num = re.findall(r'\d+', name)
        name_head = name_element[0].split(']')
        minExpo = info_list[i].get('minExpo')
        expo = info_list[i].get("expo")
        iso = info_list[i].get("iso")
        gain = str(int((int(iso) / 50) * 256))
        distance = info_list[i].get("distance")
        expo = str(int(1000000 / float(expo)))  # EI值转换，如有错误，本处验证
        expo = expo.rjust(6, '0')
        new_name = "C701HIV_M030" + "_id(" + order + ")" + "_FID_323331363030313533323035553030_EI_" + \
                   expo + "s_" + gain + "_ISO_" + iso + "_LV_" + lv_list[i] + "_DGAIN_" + \
                   dgain_list[i] + "_WHBF_4096_2304" + "_num." + order
        for root, dirs, files in os.walk(dir_path):
            for j in range(len(files)):
                file_name = os.path.splitext(files[j])
                if file_name[0] == name and file_name[1] == ".raw":
                    srcfile = os.path.join(dir_path, files[j])
                    newfile = os.path.join(dir_path, new_name + '.raw')
                    os.rename(srcfile, newfile)
                    # print(f'old file path is :{srcfile},\nnew file path is:{newfile}')


def just_do_it():
    """it's the core code,for rename file name"""
    print(f'The working directory you specified is {work_path}, prepare arguments for python program to rename...')
    paths = get_path()
    for path in paths:
        name, info = readXML(path)
        lv = get_lv(os.path.join(path, r'lv.txt'))
        dgain = get_dgain(os.path.join(path, r'drcgain.bin'))
        my_rename(name, info, lv, dgain, path)
    print('******have done it!******')


def cope_to_test(src_path, dst_path):
    """需要修改的文件路径->拷贝到指定文件路径后再进行操作，如不需要可直接操作源地址"""
    shutil.rmtree(dst_path, ignore_errors=True)
    shutil.copytree(src_path, dst_path)


def create_test_file(create=True):
    """if arguments is False,delete all files which the function created,default is True"""
    print('start create or delete test file,it will take some time,please wait...')
    paths = get_path()
    filepaths = []
    for path in paths:
        names, _ = readXML(path)
        for name in names:
            filepath = os.path.join(path, name)
            filepaths.append(filepath)
    if create:
        for filepath in filepaths:
            if os.path.exists(filepath):
                continue
            f = open(filepath, 'a+')
            f.close()
    else:
        for filepath in filepaths:
            if os.path.exists(filepath):
                os.remove(filepath)
    print('files are already created or deleted!')


def delete_raw_type_file():
    for root, dirs, files in os.walk(work_path):
        for file in files:
            if ".raw" in file:
                filepath = os.path.join(root, file)
                os.remove(filepath)
    print('files has been deleted.')


if __name__ == '__main__':
    work_path = r'D:\PycharmTest\raw'
    # create_test_file()
    # just_do_it()
    # delete_raw_type_file()
    ...
```

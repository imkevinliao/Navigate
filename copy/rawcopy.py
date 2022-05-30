import os
import shutil

src_path = r'D:\copyraw_test_in'
dst_path = r'D:\copyraw_test_out'


def get_dirs_name(dirs_path):
    my_dirs = os.listdir(src_path)
    return my_dirs


def create_dirs(dirs):
    for _ in dirs:
        for num in range(0, 3):
            folder = os.path.join(dst_path, _)
            folder = folder + '_' + str(num)
            if not os.path.exists(folder):
                os.makedirs(folder)
                print("folder is created:", folder)
            else:
                print("folder has created:", folder)


def dealt_files_index(files):
    index = 0
    for i in range(100):
        flag = False
        my_str = "num." + str(i) + ".raw"
        for file in files:
            if ("RGB" not in file) and (my_str in file):
                flag = True
                break
        if flag:
            index = i
            break
        else:
            index = ''
    if index:
        print("当前文件夹内raw图的开始索引值为：", index)
    else:
        print("未能确定当前文件夹内raw图的开始索引值!")
    return index


def dealt_files(root, files):
    raw_files = [file for file in files if '.raw' in file]
    rgb_files = [file for file in raw_files if '.raw' in file and 'RGB' in file]
    normal_files = [file for file in raw_files if '.raw' in file and 'RGB' not in file]
    if rgb_files:
        my_str = os.path.basename(root) + '_RGB'
        rgb_dir = [my_str]
        print('存在RGBfile, 准备创建对应的RGB文件夹')
        create_dirs(rgb_dir)
        for index, file in enumerate(rgb_files):
            src_base = root
            src = os.path.join(src_base, file)
            dst_base = dst_path + os.path.basename(root)
            dst = os.path.join(dst_base, file)
            new_dst = ''
            if 0 <= index < 60:
                new_dst = dst_path + '\\' + os.path.basename(root) + '_RGB' + '_0\\'
            elif 200 <= index < 260:
                new_dst = dst_path + '\\' + os.path.basename(root) + '_RGB' + '_1\\'
            elif 370 <= index < 430:
                new_dst = dst_path + '\\' + os.path.basename(root) + '_RGB' + '_2\\'
            try:
                if new_dst:
                    print('正在复制的文件：', src)
                    shutil.copy(src, new_dst)
                    print('文件已经复制到：', new_dst)
            except OSError as err:
                print('Error:')
                print('复制过程出现异常,异常文件:', src, '异常文件应该复制到：', new_dst, '复制错误, 代码中的index为：', index, '复制报错信息：', err)
        ...
    # index_start = dealt_files_index(files)
    my_str = os.path.basename(root)
    normal_dir = [my_str]
    create_dirs(normal_dir)
    for index, file in enumerate(normal_files):
        src_base = root
        src = os.path.join(src_base, file)
        dst_base = dst_path + os.path.basename(root)
        dst = os.path.join(dst_base, file)
        new_dst = ''
        if 0 <= index < 60:
            new_dst = dst_path + '\\' + os.path.basename(root) + '_0\\'
        elif 200 <= index < 260:
            new_dst = dst_path + '\\' + os.path.basename(root) + '_1\\'
        elif 370 <= index < 430:
            new_dst = dst_path + '\\' + os.path.basename(root) + '_2\\'
        try:
            if new_dst:
                print('正在复制的文件：', src)
                shutil.copy(src, new_dst)
                print('文件已经复制到：', new_dst)
        except OSError as err:
            print('Error:')
            print('复制过程出现异常,异常文件:', src, '异常文件应该复制到：', new_dst, '复制错误, 代码中的index为：', index, '复制报错信息：', err)

    ...


def copy_exec(task_dirs):
    for root, dirs, files in os.walk(src_path):
        if os.path.basename(root) in task_dirs:
            print('当前正在操作的文件夹:', root)
            # with open('files.txt', 'a+', encoding='utf8') as f:
            #     f.writelines([line + '\n' for line in files if '.raw' in line])
            dealt_files(root, files)
            print('当前已经操作完成的文件夹：', root)
    ...


def test001():
    aaa = r"D:\copyraw_test_in\M014_Indoor_00128\C701HIV_M030_20220426_1057387076_id(0)_FID_323330363037303133323131544131_EI_000100s_655_ISO_128_LV_78_WHBF_4096_2304_12_2_num.43.raw"
    bbb = r"D:\copyraw_test_out\M014_Indoor_00128_0\\"
    shutil.copy(aaa, bbb)


def test002():
    import sys
    print(sys.version)


def test003():
    words = ['afbef', 'caoffafe', 'fwaefofafwa', 'afafowejtgoaf', 'uuuufefeffsfsf']
    list1 = []
    # for word in words:
    #     if 'a' in word:
    #         list1.append(word)
    list1 = [word for word in words if 'u' in word]
    print(list1)


def run():
    dirs = get_dirs_name(src_path)
    copy_exec(dirs)


if __name__ == '__main__':
    run()
    ...

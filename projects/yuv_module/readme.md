# 使用场景
工作中需要生成一个64x4的yuv小图，然后在vs工程中配置参数跑图。

# 说明
yuv图片有多种格式，所以需要在xml中配置数据格式。工程支持8bits和10bits输入，相关的参数也需要修改。所以才会有xml模块的处理，xml模块中需要配置一些参数。
代码一点都不优雅，8bits和10bits一开始不清楚，以为输入都是两个bits位来的，所以后面这里修改的时候完全就是临时补上去的，没有系统的设计好。再有就是关于跑图的输出这一块，
一开始也是没有的，后面有了，就集成在里面的，这也让代码显得很割裂。在一个就是xml的修改，一开始的时候都是手动修改的，但是测试的时候反复调试，修改的太累的才加的xml模块。
人工修改xml有些地方可能没注意就忘记改或者什么的，还是直接代码里处理比较安全。

# 结语
当我对整个流程很清楚以后，就发现如果让我这个时候重新来设计一次，绝对不会是现在这个样子，目前维护起来相当麻烦，不过好消息就是不需要维护。

当我们对整个流程有了很清楚的概念后再去设计代码或者说编写代码，会优雅很多。但是当我们不了解完整的流程，有额外的新需求破坏了原有的代码结构的时候，只能先硬着头皮先写下去。
最尴尬的是，当我们有能力去重构代码的时候，却发现已经没有那个必要了，没有必要花时间去做了。

生活中的遗憾也大抵如此吧。

# 重构
实际上vs跑图命令也可以集成到脚本中，这样子的话就不需要去vs上处理了。但是因为偶尔还是可能需要使用到vs对代码调试，分析问题，所以这样的集成又显得不是那么明智。
也许不必追求过分地完美。

贴上后面追加的，修改xml跑图测试：只需要修改下参数就可以了，极其方便。事实上，有一些重复的代码还可以再精炼一下，但是正如先前所说的，已经没有必要了。
```Python3
import os
import shutil
import xml.etree.ElementTree as ET

xml_path = r'D:\localrepo\V350_R02\cpipe_v350\resources\config\test_fbcd.xml'
input_path = r'D:\localrepo\V350_R02\cpipe_v350\test_image\test_in.yuv'
output_path = r'D:\localrepo\V350_R02\cpipe_v350\out\test_out.00000.yuv'

width = 3968
cright = width - 1
height = 2976
bits = 8
bypass = 0
format = r'FF_YUV420_NV12'
result_path = fr'D:\localrepo\V350_R02_TestResult\{format}\bits_{bits}_bypass_{bypass}_{width}x{height}'


def modify():
    tree = ET.parse(xml_path)
    root = tree.getroot()
    root.find('.//img_prop/width').text = str(width)
    root.findall('.//component/hw/cright')[0].text = str(cright)
    root.findall('.//component/hw/cright')[1].text = str(cright)
    root.find('.//img_prop/height').text = str(height)

    root.find('.//img_prop/file_bits_per_sample').text = str(bits)
    root.findall('.//component/write_pic/file_attrib/file_bits_per_sample')[1].text = str(bits)

    # write_pic 的bypass不需要处理
    root.findall(r'.//component/hw/bypass')[0].text = str(bypass)
    root.findall(r'.//component/hw/bypass')[1].text = str(bypass)

    if bits == 10:
        yuv10b = 1
    elif bits == 8:
        yuv10b = 0
    root.find('.//component/hw/yuv10b').text = str(yuv10b)
    root.findall('.//component/hw/yuv10b')[0].text = str(yuv10b)
    root.findall('.//component/hw/yuv10b')[1].text = str(yuv10b)

    root.find('.//img_prop/file_format').text = str(format)
    root.findall('.//component/write_pic/file_attrib/file_format')[0].text = str(format)
    root.findall('.//component/write_pic/file_attrib/file_format')[1].text = str(format)

    tree.write(xml_path)


def prepare_file():
    if bits == 8:
        src = r'C:\Users\ReceiveFile\ut_3968x2976_nv12_8bits.yuv'
    elif bits == 10:
        src = r'C:\Users\ReceiveFile\ut_3968x2976_nv12_10bits.yuv'
    dst = r'D:\localrepo\V350_R02\cpipe_v350\test_image\test_in.yuv'
    shutil.copy2(src, dst)


def output_file():
    if not os.path.exists(result_path):
        os.makedirs(result_path)
    shutil.copy2(xml_path, result_path)
    shutil.copy2(input_path, result_path)
    shutil.copy2(output_path, result_path)
    pass


if __name__ == '__main__':
    modify()
    prepare_file()
    input('等待vs跑图')
    output_file()

```

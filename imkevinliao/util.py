import sys

r = b"'sudo' \xb2\xbb\xca\xc7\xc4\xda\xb2\xbf\xbb\xf2\xcd\xe2\xb2\xbf\xc3\xfc\xc1\xee\xa3\xac\xd2\xb2\xb2\xbb\xca\xc7" \
    b"\xbf\xc9\xd4\xcb\xd0\xd0\xb5\xc4\xb3\xcc\xd0\xf2\r\n\xbb\xf2\xc5\xfa\xb4\xa6\xc0\xed\xce\xc4\xbc\xfe\xa1\xa3\r\n "


def __decode(decoded_string: str, encoding_set=None):
    """
    decoded_string:待解码的字符串
    encoding_set:指定解码的字符集
    """
    if encoding_set is None:
        encoding_set = ["utf-8", "gbk2312", "utf-16", "gbk"]
    encoding_set_length = len(encoding_set)
    for index, value in enumerate(encoding_set):
        try:
            decode_string = decoded_string.decode(value)
            print(f"{value}解码成功,返回解码后的字符串.")
            return decode_string
        except UnicodeDecodeError as e:
            if index == (encoding_set_length - 1):
                print("解码失败，返回原字符串.")
        except LookupError as e:
            print(f"找不到{value}字符集")
    return decoded_string


def check_python_version(enable_hint=False):
    if sys.version_info > (3, 6):
        if enable_hint:
            print(f"Current python version is {sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}")
    else:
        print("Current python version lower than 3.6, f-string can't be used.")



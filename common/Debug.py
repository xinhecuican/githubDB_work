
# 输出红色字，
# 使用: Debug.error_message
def error_message(msg):
    return print("\033[0;31m" + msg + "\033[0m")


def info_message(msg):
    return print("\033[0;33m" + msg + "\033[0m")

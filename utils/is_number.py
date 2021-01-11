import re


# 判断是否数字
def isnumber(num):
    regex = re.compile(r"^(-?\d+)(\.\d*)?$")
    if re.match(regex, num):
        return True
    else:
        return False

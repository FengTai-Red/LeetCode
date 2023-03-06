# 0067. 二进制求和
# 给你两个二进制字符串，返回它们的和（用二进制表示）。
# 输入为 非空 字符串且只包含数字 1 和 0。
# 示例 1:
# 输入: a = "11", b = "1"
# 输出: "100"
# 示例 2:
# 输入: a = "1010", b = "1011"
# 输出: "10101"
# 提示：
# 每个字符串仅由字符 '0' 或 '1' 组成。
# 1 <= a.length, b.length <= 10^4
# 字符串如果不是 "0" ，就都不含前导零。

def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    len_a = len(a)
    len_b = len(b)
    c = ""
    len_long = len_a if (len_a>len_b) else len_b
    if (len_a < len_b):
        a = ("0" * (len_long - len_a)) + a
    else:
        b = ("0" * (len_long - len_b)) + b
    carry = 0
    print(a)
    print(b)
    for i in range(len_long -1, -1, -1):
        sum = (int(a[i]) + int(b[i]) + carry) % 2
        carry = (int(a[i]) + int(b[i]) + carry) // 2
        print(sum)
        c = str(sum) + c
    if (carry == 1):
        c = str(carry) + c
    return c

if __name__ == "__main__":
    a = "1"
    b = "1"
    print(addBinary(a, b))

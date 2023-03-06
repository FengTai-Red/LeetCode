# 7. 整数反转
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^(31−1)]。请根据这个假设，如果反转后整数溢出那么就返回 0。

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    a = x
    if x < 0:
        x = abs(x)
    lenght = 1
    mun_list = []
    mun_list.append(x % 10)
    while(True):
        if abs(x) >= 10:
            x = x // 10
            mun_list.append(x % 10)
            lenght += 1
        else:
            break
    num = 0
    for i in range(lenght):
        num += mun_list[i] * (10 ** (lenght -1))
        lenght -= 1
    if a < 0:
        if (-num < -2147483648):
            return 0
        else:
            return -num
    else:
        if (num > 2147483647):
            return 0
        else:
            return num


if __name__ == "__main__":
    x = 10
    print(reverse(x))

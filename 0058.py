# 0058.最后一个单词的长度
# 给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。
# 如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。
# 如果不存在最后一个单词，请返回 0 。
# 说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。
# 示例:
# 输入: "Hello World"
# 输出: 5
def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    i = len(s) - 1
    count = 0
    flag = True
    while i != -1:
        if (flag and s[i] == " "):
            i -= 1
        else:
            count += 1
            flag = False
            i -= 1
            if (s[i] == " "):
                break
    return count

if __name__ == "__main__":
    s = "ss    "
    print(lengthOfLastWord(s))
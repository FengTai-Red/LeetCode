# 14. 最长公共前缀
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。
# 示例 1:
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 说明:
# 所有输入只包含小写字母 a-z 。

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if strs == []:
        return ""
    lenght = len(strs)
    temp = strs[0]
    outstr = ""
    for i in range(lenght):
        if len(temp) > len(strs[i]):
            temp = strs[i]
    lenght = len(temp)
    is_same = False
    for i in range(lenght):
        for s in strs:
            if temp[i] == s[i]:
                is_same = True
            else:
                is_same = False
                break
        if not is_same:
            break
        else:
            outstr += temp[i]
    return outstr



if __name__ == "__main__":
    strs = []
    strs = ["asd", "asdewdfghw", "asbasdd"]
    strs = ["aca","cba"]
    print(longestCommonPrefix(strs))
    
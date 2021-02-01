class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        i = j = len(s) - 1
        ret = []
        while i >= 0:
            # 找到开头或单词前的空格
            while i >= 0 and s[i] != ' ':
                i -= 1
            ret.append(s[i + 1:j + 1])
            # 跳过空格
            while i >= 0 and s[i] == ' ':
                i -= 1
            j = i
        return " ".join(ret)

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        # result = []
        # for index, char in enumerate(s):
        #     if char == "#":
        #         stringLength = int(s[index-1])
        #         string = s[index + 1:index+1+stringLength]
        #         result.append(string)
        # return result
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j+1 : j+1+length]
            result.append(word)
            i = j + 1 + length
        return result

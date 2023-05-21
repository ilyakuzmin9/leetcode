class Solution:
    def romanToInt(self, s: str) -> int:
        matchingDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ellist=[]
        for element in range(0, len(s)):
            for key,value in matchingDict.items():
                if s[element] == key:
                    ellist.append(value)
        resultlist=[]
        for i in range(len(ellist)):
            try:
                if ellist[i]<ellist[i+1]:
                    resultlist.append(ellist[i+1]-ellist[i])
                    ellist.remove(ellist[i+1])
                else:
                    resultlist.append(ellist[i])
            except IndexError:
                try:
                    resultlist.append(ellist[i])
                except IndexError:
                    break
                break

        return sum(resultlist)



p1 = Solution()
print(p1.romanToInt('LXXXVIII'))
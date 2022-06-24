import re

class palindrome:

    def filterListByLength(item):
        if(len(item) < self.minLength):
            return False
        else:
            return True
    
    def findOrReturnNull(str):
        minLength = 3

        str = re.sub(r"[^A-Za-z0-9]", '', str)
        str = str.lower()

        strLength = len(str)
        palindromes = []

        for end in range(strLength, 0, -1):
            for start in range(0, strLength):
                subStr = str[start:end]
                if subStr == subStr[::-1]:
                    palindromes.append(subStr)

        
        palindromes.sort(key = len)        
        filteredList = list(filter(lambda str: len(str) >= minLength, palindromes))

        filteredList.sort(key = len)

        if len(filteredList) < 1:
            return None
        else:
            return filteredList[::-1][0]
    
    